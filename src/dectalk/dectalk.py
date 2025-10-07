from . import _ttsapi as ttsapi
from pathlib import Path
import os
import ctypes
import weakref
import contextlib

WAVE_MAPPER = -1

class MmSysErrBase(Exception):
    _registry = {}

    def __new__(cls, code, *args, **kwargs):
        subclass = cls._registry.get(code, cls)
        instance = super(MmSysErrBase, subclass).__new__(subclass)
        return instance

    def __init__(self, code, *args, **kwargs):
        self.code = code
        self.message = kwargs.get("message", self.__class__.__doc__ or "Unknown error")
        super().__init__(f"[{code}] {self.message}", *args)

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        error_code = getattr(cls, 'ERROR_CODE', None)
        if error_code is not None:
            MmSysErrBase._registry[error_code] = cls



class MmSysErrError(MmSysErrBase):
    ERROR_CODE = ttsapi.MMSYSERR_ERROR


class MmSysErrBadDeviceId(MmSysErrBase):
    ERROR_CODE = ttsapi.MMSYSERR_BADDEVICEID


class MmSysErrNotEnabled(MmSysErrBase):
    ERROR_CODE = ttsapi.MMSYSERR_NOTENABLED


class MmSysErrAllocated(MmSysErrBase):
    ERROR_CODE = ttsapi.MMSYSERR_ALLOCATED


class MmSysErrInvalidHandle(MmSysErrBase):
    ERROR_CODE = ttsapi.MMSYSERR_INVALHANDLE

class MmSysErrNoDriver(MmSysErrBase):
    ERROR_CODE = ttsapi.MMSYSERR_NODRIVER

class MmSysErrNoMem(MmSysErrBase):
    ERROR_CODE = ttsapi.MMSYSERR_NOMEM

class MmSysNotSupported(MmSysErrBase):
    ERROR_CODE = ttsapi.MMSYSERR_NOTSUPPORTED

class MmSysBadErrNum(MmSysErrBase):
    ERROR_CODE = ttsapi.MMSYSERR_BADERRNUM

class MmSysInvalidFlag(MmSysErrBase):
    ERROR_CODE = ttsapi.MMSYSERR_INVALFLAG

class MmSysInvalidParam(MmSysErrBase):
    "An invalid parameter or was passed."
    ERROR_CODE = ttsapi.MMSYSERR_INVALPARAM

class MmSysHandleBusy(MmSysErrBase):
    ERROR_CODE = ttsapi.MMSYSERR_HANDLEBUSY

class MmSysInvalidAlias(MmSysErrBase):
    ERROR_CODE = ttsapi.MMSYSERR_INVALIDALIAS

from enum import IntEnum

class WAVE_FORMAT(IntEnum):
    _1M08 = ttsapi.WAVE_FORMAT_1M08
    _1S08 = ttsapi.WAVE_FORMAT_1S08
    _2M08 = ttsapi.WAVE_FORMAT_2M08
    _2S08 = ttsapi.WAVE_FORMAT_2S08

    _1M16 = ttsapi.WAVE_FORMAT_1M16
    _1S16 = ttsapi.WAVE_FORMAT_1S16
    _2M16 = ttsapi.WAVE_FORMAT_2M16
    _2S16 = ttsapi.WAVE_FORMAT_2S16

    _4S16 = ttsapi.WAVE_FORMAT_4S16
    _4M16 = ttsapi.WAVE_FORMAT_4M16
    _4S08 = ttsapi.WAVE_FORMAT_4S08
    _4M08 = ttsapi.WAVE_FORMAT_4M08

    _08M08 = ttsapi.WAVE_FORMAT_08M08
    _08M16 = ttsapi.WAVE_FORMAT_08M16
    PCM = ttsapi.WAVE_FORMAT_PCM
    # MPEG = ttsapi.WAVE_FORMAT_M

class TextToSpeechBuffer(ttsapi.TTS_BUFFER_T):
    BUFFER_SIZE = 4096
    MAX_PHONEMES = 128
    MAX_INDEX_MARKS = 128
    def __init__(self):
        self.lpData = (ttsapi.CHAR * self.BUFFER_SIZE)()
        self.dwMaximumBufferLength = self.BUFFER_SIZE

        self.lpPhonemeArray = (ttsapi.TTS_PHONEME_T * self.MAX_PHONEMES)()
        self.dwMaximumNumberOfPhonemeChanges = self.MAX_PHONEMES

        self.lpIndexArray = (ttsapi.TTS_INDEX_T * self.MAX_INDEX_MARKS)()
        self.dwMaximumNumberOfIndexMarks = self.MAX_INDEX_MARKS

    def process(self, parent):
        for i in range(self.dwNumberOfIndexMarks):
            print('index val: ', self.lpIndexArray[i].dwIndexValue)
            print('index sample: ', self.lpIndexArray[i].dwIndexSampleNumber)

        if self.dwBufferLength > 0:
            print(self.dwBufferLength)
            buf = self.lpData[:self.dwBufferLength]
            parent.process(buf)
            # print('got buffer data: ', len())

        ttsapi.TextToSpeechAddBuffer(parent, self)

        self.dwBufferLength = 0



class TTS_MSG(IntEnum):
    BUFFER = 9

@ttsapi.CFUNCTYPE(ttsapi.UNCHECKED(ttsapi.VOID), ttsapi.LONG, ttsapi.LONG, ttsapi.DWORD, ttsapi.UINT)
def callback2(param1, param2, user_defined, uiMsg):
    print(param1, param2, user_defined, uiMsg)
    obj = TextToSpeechHandle._objlookup[user_defined]
    match uiMsg:
        case TTS_MSG.BUFFER:
            a = TextToSpeechBuffer.from_address(param2)
            a.process(obj)
        case _:
            print('unknown!', uiMsg)


class TextToSpeechHandle(ttsapi.LPTTS_HANDLE_T):

    _objlookup = weakref.WeakValueDictionary()

    NUM_BUFFERS = 1
    def get_callback(self):
        @ttsapi.CFUNCTYPE(ttsapi.UNCHECKED(ttsapi.VOID), ttsapi.LONG, ttsapi.LONG, ttsapi.DWORD, ttsapi.UINT)
        def callback(param1, param2, user_defined, uiMsg):
            print(param1, param2, user_defined, uiMsg)
        return callback

    def __init__(self, afmt=WAVE_FORMAT.PCM):
        selfid = id(self) % 0x100000000

        with contextlib.chdir(Path(ttsapi.__file__).parent):  # This is so fucked up
            result = ttsapi.TextToSpeechStartup(
                self, # handle
                WAVE_MAPPER, # devnum
                ttsapi.DO_NOT_USE_AUDIO_DEVICE, # options
                callback2, # callback
                selfid, # instanceparameter (callback arg 3)
            )


        self.ret = b''

        if result != 0:
            raise MmSysErrBase(result)
        self.valid = True

        self._objlookup[selfid] = self

        result = ttsapi.TextToSpeechOpenInMemory(self, afmt)

        if result != 0:
            raise MmSysErrBase(result)

        self.buffers = [TextToSpeechBuffer() for _ in range(self.NUM_BUFFERS)]
        print(self.buffers)

        for buffer in self.buffers:
            result = ttsapi.TextToSpeechAddBuffer(self, buffer)
            if result != 0:
                raise MmSysErrBase(result)


        # result = TextToSpeechLoadUserDictionary(self, str)
        # handle result

    def speak(self, s: str, force: bool = False):
        if self.ret:
            print('wuhoh')
        self.ret = b''
        dwFlag = 1 if force else 0
        result = ttsapi.TextToSpeechSpeak(self, ctypes.create_string_buffer(s.encode()), dwFlag)
        if result != 0:
            raise MmSysErrBase(result)
        import time
        time.sleep(3)
        ret =  self.ret
        self.ret = b''
        return ret

    def __del__(self):
        self.shutdown()

    def shutdown(self):
        self.valid = False
        result = ttsapi.TextToSpeechShutdown(self)

    def reset(self):
        result = TextToSpeechReset(self, True)
        result

    def process(self, data: bytes):
        self.ret += data
