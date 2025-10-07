r"""Wrapper for ttsapi.h

Generated with:
/home/m/proj/mine/dectalk.py/venv/bin/ctypesgen -llibdectalk -L src/dectalk/_libdectalk/ -I dectalk/src/dapi/src/api/ -I dectalk/src/dapi/src/osf/ dectalk/src/dapi/src/api/ttsapi.h dectalk/src/dapi/src/osf/dtmmedefs.h -o src/dectalk/_ttsapi.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types



class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):

    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = ['src/dectalk/_libdectalk/']

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HP-UX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs(['src/dectalk/_libdectalk/'])

# Begin libraries
_libs["libdectalk"] = load_library("libdectalk")

# 1 libraries
# End libraries

# No modules

Int8 = c_char# dectalk/src/dapi/src/osf/dtmmedefs.h: 127

Int16 = c_short# dectalk/src/dapi/src/osf/dtmmedefs.h: 128

Int32 = c_int# dectalk/src/dapi/src/osf/dtmmedefs.h: 129

Int64 = c_longlong# dectalk/src/dapi/src/osf/dtmmedefs.h: 131

Uint8 = c_ubyte# dectalk/src/dapi/src/osf/dtmmedefs.h: 135

Uint16 = c_ushort# dectalk/src/dapi/src/osf/dtmmedefs.h: 136

Uint32 = c_uint# dectalk/src/dapi/src/osf/dtmmedefs.h: 137

Uint64 = c_ulonglong# dectalk/src/dapi/src/osf/dtmmedefs.h: 139

Char8 = c_char# dectalk/src/dapi/src/osf/dtmmedefs.h: 144

Char16 = c_short# dectalk/src/dapi/src/osf/dtmmedefs.h: 145

DWORD = Uint32# dectalk/src/dapi/src/osf/dtmmedefs.h: 152

BOOL = c_ubyte# dectalk/src/dapi/src/osf/dtmmedefs.h: 168

BYTE = Uint8# dectalk/src/dapi/src/osf/dtmmedefs.h: 185

WORD = Uint16# dectalk/src/dapi/src/osf/dtmmedefs.h: 189

INT = Int32# dectalk/src/dapi/src/osf/dtmmedefs.h: 192

LONG = c_long# dectalk/src/dapi/src/osf/dtmmedefs.h: 194

FLOAT = c_float# dectalk/src/dapi/src/osf/dtmmedefs.h: 199

UINT = Uint32# dectalk/src/dapi/src/osf/dtmmedefs.h: 205

CHAR = Char8# dectalk/src/dapi/src/osf/dtmmedefs.h: 209

SHORT = Int16# dectalk/src/dapi/src/osf/dtmmedefs.h: 210

PUINT = POINTER(Uint32)# dectalk/src/dapi/src/osf/dtmmedefs.h: 212

PFLOAT = POINTER(FLOAT)# dectalk/src/dapi/src/osf/dtmmedefs.h: 213

PBOOL = POINTER(BOOL)# dectalk/src/dapi/src/osf/dtmmedefs.h: 214

LPBOOL = POINTER(BOOL)# dectalk/src/dapi/src/osf/dtmmedefs.h: 215

PBYTE = POINTER(BYTE)# dectalk/src/dapi/src/osf/dtmmedefs.h: 216

LPBYTE = POINTER(BYTE)# dectalk/src/dapi/src/osf/dtmmedefs.h: 217

PINT = POINTER(INT)# dectalk/src/dapi/src/osf/dtmmedefs.h: 218

LPINT = POINTER(INT)# dectalk/src/dapi/src/osf/dtmmedefs.h: 219

PWORD = POINTER(WORD)# dectalk/src/dapi/src/osf/dtmmedefs.h: 220

LPWORD = POINTER(WORD)# dectalk/src/dapi/src/osf/dtmmedefs.h: 221

LPLONG = POINTER(LONG)# dectalk/src/dapi/src/osf/dtmmedefs.h: 222

PDWORD = POINTER(DWORD)# dectalk/src/dapi/src/osf/dtmmedefs.h: 223

LPDWORD = POINTER(DWORD)# dectalk/src/dapi/src/osf/dtmmedefs.h: 224

VOID = None# dectalk/src/dapi/src/osf/dtmmedefs.h: 226

LPVOID = POINTER(None)# dectalk/src/dapi/src/osf/dtmmedefs.h: 228

SIZE = LONG# dectalk/src/dapi/src/osf/dtmmedefs.h: 230

WPARAM = UINT# dectalk/src/dapi/src/osf/dtmmedefs.h: 233

LPARAM = LONG# dectalk/src/dapi/src/osf/dtmmedefs.h: 234

MMRESULT = UINT# dectalk/src/dapi/src/osf/dtmmedefs.h: 235

DT_HANDLE = POINTER(LONG)# dectalk/src/dapi/src/osf/dtmmedefs.h: 241

HANDLE = DT_HANDLE# dectalk/src/dapi/src/osf/dtmmedefs.h: 242

WCHAR = Char16# dectalk/src/dapi/src/osf/dtmmedefs.h: 245

PWCHAR = POINTER(WCHAR)# dectalk/src/dapi/src/osf/dtmmedefs.h: 247

LPWCH = POINTER(WCHAR)# dectalk/src/dapi/src/osf/dtmmedefs.h: 248

PWCH = POINTER(WCHAR)# dectalk/src/dapi/src/osf/dtmmedefs.h: 248

LPCWCH = POINTER(WCHAR)# dectalk/src/dapi/src/osf/dtmmedefs.h: 249

PCWCH = POINTER(WCHAR)# dectalk/src/dapi/src/osf/dtmmedefs.h: 249

NWPSTR = POINTER(WCHAR)# dectalk/src/dapi/src/osf/dtmmedefs.h: 250

LPWSTR = POINTER(WCHAR)# dectalk/src/dapi/src/osf/dtmmedefs.h: 251

PWSTR = POINTER(WCHAR)# dectalk/src/dapi/src/osf/dtmmedefs.h: 251

LPCWSTR = POINTER(WCHAR)# dectalk/src/dapi/src/osf/dtmmedefs.h: 253

PCWSTR = POINTER(WCHAR)# dectalk/src/dapi/src/osf/dtmmedefs.h: 253

LPSTR = POINTER(CHAR)# dectalk/src/dapi/src/osf/dtmmedefs.h: 254

PSTR = POINTER(CHAR)# dectalk/src/dapi/src/osf/dtmmedefs.h: 254

LPCSTR = POINTER(CHAR)# dectalk/src/dapi/src/osf/dtmmedefs.h: 255

# dectalk/src/dapi/src/osf/dtmmedefs.h: 344
class struct_tWAVEFORMATEX(Structure):
    pass

struct_tWAVEFORMATEX.__slots__ = [
    'wFormatTag',
    'nChannels',
    'nSamplesPerSec',
    'nAvgBytesPerSec',
    'nBlockAlign',
    'wBitsPerSample',
    'cbSize',
]
struct_tWAVEFORMATEX._fields_ = [
    ('wFormatTag', WORD),
    ('nChannels', WORD),
    ('nSamplesPerSec', DWORD),
    ('nAvgBytesPerSec', DWORD),
    ('nBlockAlign', WORD),
    ('wBitsPerSample', WORD),
    ('cbSize', WORD),
]

WAVEFORMATEX = struct_tWAVEFORMATEX# dectalk/src/dapi/src/osf/dtmmedefs.h: 344

PWAVEFORMATEX = POINTER(WAVEFORMATEX)# dectalk/src/dapi/src/osf/dtmmedefs.h: 345

NPWAVEFORMATEX = POINTER(WAVEFORMATEX)# dectalk/src/dapi/src/osf/dtmmedefs.h: 346

LPWAVEFORMATEX = POINTER(WAVEFORMATEX)# dectalk/src/dapi/src/osf/dtmmedefs.h: 347

SPEAKER_T = DWORD# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 352

LPSPEAKER_T = POINTER(SPEAKER_T)# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 353

LANGUAGE_T = DWORD# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 355

LPLANGUAGE_T = POINTER(LANGUAGE_T)# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 356

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 370
class struct_LANGUAGE_PARAMS_TAG(Structure):
    pass

struct_LANGUAGE_PARAMS_TAG.__slots__ = [
    'dwLanguage',
    'dwLanguageAttributes',
]
struct_LANGUAGE_PARAMS_TAG._fields_ = [
    ('dwLanguage', LANGUAGE_T),
    ('dwLanguageAttributes', DWORD),
]

LANGUAGE_PARAMS_T = struct_LANGUAGE_PARAMS_TAG# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 370

LPLANGUAGE_PARAMS_T = POINTER(LANGUAGE_PARAMS_T)# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 372

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 384
class struct_TTS_CAPS_TAG(Structure):
    pass

struct_TTS_CAPS_TAG.__slots__ = [
    'dwNumberOfLanguages',
    'lpLanguageParamsArray',
    'dwSampleRate',
    'dwMinimumSpeakingRate',
    'dwMaximumSpeakingRate',
    'dwNumberOfPredefinedSpeakers',
    'dwCharacterSet',
    'Version',
]
struct_TTS_CAPS_TAG._fields_ = [
    ('dwNumberOfLanguages', DWORD),
    ('lpLanguageParamsArray', LPLANGUAGE_PARAMS_T),
    ('dwSampleRate', DWORD),
    ('dwMinimumSpeakingRate', DWORD),
    ('dwMaximumSpeakingRate', DWORD),
    ('dwNumberOfPredefinedSpeakers', DWORD),
    ('dwCharacterSet', DWORD),
    ('Version', DWORD),
]

TTS_CAPS_T = struct_TTS_CAPS_TAG# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 384

LPTTS_CAPS_T = POINTER(TTS_CAPS_T)# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 386

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 399
class struct_TTS_PHONEME_TAG(Structure):
    pass

struct_TTS_PHONEME_TAG.__slots__ = [
    'dwPhoneme',
    'dwPhonemeSampleNumber',
    'dwPhonemeDuration',
    'dwReserved',
]
struct_TTS_PHONEME_TAG._fields_ = [
    ('dwPhoneme', DWORD),
    ('dwPhonemeSampleNumber', DWORD),
    ('dwPhonemeDuration', DWORD),
    ('dwReserved', DWORD),
]

TTS_PHONEME_T = struct_TTS_PHONEME_TAG# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 399

LPTTS_PHONEME_T = POINTER(TTS_PHONEME_T)# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 401

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 409
class struct_TTS_INDEX_TAG(Structure):
    pass

struct_TTS_INDEX_TAG.__slots__ = [
    'dwIndexValue',
    'dwIndexSampleNumber',
    'dwReserved',
]
struct_TTS_INDEX_TAG._fields_ = [
    ('dwIndexValue', DWORD),
    ('dwIndexSampleNumber', DWORD),
    ('dwReserved', DWORD),
]

TTS_INDEX_T = struct_TTS_INDEX_TAG# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 409

LPTTS_INDEX_T = POINTER(TTS_INDEX_T)# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 411

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 426
class struct_TTS_BUFFER_TAG(Structure):
    pass

struct_TTS_BUFFER_TAG.__slots__ = [
    'lpData',
    'lpPhonemeArray',
    'lpIndexArray',
    'dwMaximumBufferLength',
    'dwMaximumNumberOfPhonemeChanges',
    'dwMaximumNumberOfIndexMarks',
    'dwBufferLength',
    'dwNumberOfPhonemeChanges',
    'dwNumberOfIndexMarks',
    'dwReserved',
]
struct_TTS_BUFFER_TAG._fields_ = [
    ('lpData', LPSTR),
    ('lpPhonemeArray', LPTTS_PHONEME_T),
    ('lpIndexArray', LPTTS_INDEX_T),
    ('dwMaximumBufferLength', DWORD),
    ('dwMaximumNumberOfPhonemeChanges', DWORD),
    ('dwMaximumNumberOfIndexMarks', DWORD),
    ('dwBufferLength', DWORD),
    ('dwNumberOfPhonemeChanges', DWORD),
    ('dwNumberOfIndexMarks', DWORD),
    ('dwReserved', DWORD),
]

TTS_BUFFER_T = struct_TTS_BUFFER_TAG# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 426

LPTTS_BUFFER_T = POINTER(TTS_BUFFER_T)# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 428

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 450
class struct_anon_1(Structure):
    pass

struct_anon_1._pack_ = 1
struct_anon_1.__slots__ = [
    'cThisPhoneme',
    'cNextPhoneme',
    'wDuration',
]
struct_anon_1._fields_ = [
    ('cThisPhoneme', c_ubyte),
    ('cNextPhoneme', c_ubyte),
    ('wDuration', WORD),
]

PHONEME_MARK = struct_anon_1# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 450

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 465
class struct_anon_2(Structure):
    pass

struct_anon_2._pack_ = 1
struct_anon_2.__slots__ = [
    'cThisPhoneme',
    'cNextPhoneme',
    'wDuration',
]
struct_anon_2._fields_ = [
    ('cThisPhoneme', c_ushort),
    ('cNextPhoneme', c_ushort),
    ('wDuration', WORD),
]

PHONEME_MARK2 = struct_anon_2# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 465

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 472
class union_anon_3(Union):
    pass

union_anon_3._pack_ = 1
union_anon_3.__slots__ = [
    'pmData',
    'dwData',
    'pmData2',
]
union_anon_3._fields_ = [
    ('pmData', PHONEME_MARK),
    ('dwData', DWORD),
    ('pmData2', PHONEME_MARK2),
]

PHONEME_TAG = union_anon_3# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 472

LPTTS_HANDLE_T = POINTER(None)# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 488

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 541
for _lib in _libs.values():
    if not _lib.has("TextToSpeechStartupEx", "cdecl"):
        continue
    TextToSpeechStartupEx = _lib.get("TextToSpeechStartupEx", "cdecl")
    TextToSpeechStartupEx.argtypes = [POINTER(LPTTS_HANDLE_T), UINT, DWORD, CFUNCTYPE(UNCHECKED(VOID), LONG, LONG, DWORD, UINT), LONG]
    TextToSpeechStartupEx.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 550
for _lib in _libs.values():
    if not _lib.has("TextToSpeechStartupExFonix", "cdecl"):
        continue
    TextToSpeechStartupExFonix = _lib.get("TextToSpeechStartupExFonix", "cdecl")
    TextToSpeechStartupExFonix.argtypes = [POINTER(LPTTS_HANDLE_T), UINT, DWORD, CFUNCTYPE(UNCHECKED(VOID), LONG, LONG, DWORD, UINT), LONG, String]
    TextToSpeechStartupExFonix.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 566
for _lib in _libs.values():
    if not _lib.has("TextToSpeechStartup", "cdecl"):
        continue
    TextToSpeechStartup = _lib.get("TextToSpeechStartup", "cdecl")
    TextToSpeechStartup.argtypes = [POINTER(LPTTS_HANDLE_T), UINT, DWORD, CFUNCTYPE(UNCHECKED(VOID), LONG, LONG, DWORD, UINT), LONG]
    TextToSpeechStartup.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 580
for _lib in _libs.values():
    if not _lib.has("TextToSpeechShutdown", "cdecl"):
        continue
    TextToSpeechShutdown = _lib.get("TextToSpeechShutdown", "cdecl")
    TextToSpeechShutdown.argtypes = [LPTTS_HANDLE_T]
    TextToSpeechShutdown.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 585
for _lib in _libs.values():
    if not _lib.has("TextToSpeechSpeak", "cdecl"):
        continue
    TextToSpeechSpeak = _lib.get("TextToSpeechSpeak", "cdecl")
    TextToSpeechSpeak.argtypes = [LPTTS_HANDLE_T, LPSTR, DWORD]
    TextToSpeechSpeak.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 588
for _lib in _libs.values():
    if not _lib.has("TextToSpeechPause", "cdecl"):
        continue
    TextToSpeechPause = _lib.get("TextToSpeechPause", "cdecl")
    TextToSpeechPause.argtypes = [LPTTS_HANDLE_T]
    TextToSpeechPause.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 590
for _lib in _libs.values():
    if not _lib.has("TextToSpeechResume", "cdecl"):
        continue
    TextToSpeechResume = _lib.get("TextToSpeechResume", "cdecl")
    TextToSpeechResume.argtypes = [LPTTS_HANDLE_T]
    TextToSpeechResume.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 595
for _lib in _libs.values():
    if not _lib.has("TextToSpeechOpenWaveOutFile", "cdecl"):
        continue
    TextToSpeechOpenWaveOutFile = _lib.get("TextToSpeechOpenWaveOutFile", "cdecl")
    TextToSpeechOpenWaveOutFile.argtypes = [LPTTS_HANDLE_T, String, DWORD]
    TextToSpeechOpenWaveOutFile.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 598
for _lib in _libs.values():
    if not _lib.has("TextToSpeechCloseWaveOutFile", "cdecl"):
        continue
    TextToSpeechCloseWaveOutFile = _lib.get("TextToSpeechCloseWaveOutFile", "cdecl")
    TextToSpeechCloseWaveOutFile.argtypes = [LPTTS_HANDLE_T]
    TextToSpeechCloseWaveOutFile.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 600
for _lib in _libs.values():
    if not _lib.has("TextToSpeechGetStatus", "cdecl"):
        continue
    TextToSpeechGetStatus = _lib.get("TextToSpeechGetStatus", "cdecl")
    TextToSpeechGetStatus.argtypes = [LPTTS_HANDLE_T, LPDWORD, LPDWORD, DWORD]
    TextToSpeechGetStatus.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 602
for _lib in _libs.values():
    if not _lib.has("TextToSpeechReset", "cdecl"):
        continue
    TextToSpeechReset = _lib.get("TextToSpeechReset", "cdecl")
    TextToSpeechReset.argtypes = [LPTTS_HANDLE_T, BOOL]
    TextToSpeechReset.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 604
for _lib in _libs.values():
    if not _lib.has("TextToSpeechSync", "cdecl"):
        continue
    TextToSpeechSync = _lib.get("TextToSpeechSync", "cdecl")
    TextToSpeechSync.argtypes = [LPTTS_HANDLE_T]
    TextToSpeechSync.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 606
for _lib in _libs.values():
    if not _lib.has("TextToSpeechGetRate", "cdecl"):
        continue
    TextToSpeechGetRate = _lib.get("TextToSpeechGetRate", "cdecl")
    TextToSpeechGetRate.argtypes = [LPTTS_HANDLE_T, LPDWORD]
    TextToSpeechGetRate.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 608
for _lib in _libs.values():
    if not _lib.has("TextToSpeechSetRate", "cdecl"):
        continue
    TextToSpeechSetRate = _lib.get("TextToSpeechSetRate", "cdecl")
    TextToSpeechSetRate.argtypes = [LPTTS_HANDLE_T, DWORD]
    TextToSpeechSetRate.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 610
for _lib in _libs.values():
    if not _lib.has("TextToSpeechGetSpeaker", "cdecl"):
        continue
    TextToSpeechGetSpeaker = _lib.get("TextToSpeechGetSpeaker", "cdecl")
    TextToSpeechGetSpeaker.argtypes = [LPTTS_HANDLE_T, LPSPEAKER_T]
    TextToSpeechGetSpeaker.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 612
for _lib in _libs.values():
    if not _lib.has("TextToSpeechSetSpeaker", "cdecl"):
        continue
    TextToSpeechSetSpeaker = _lib.get("TextToSpeechSetSpeaker", "cdecl")
    TextToSpeechSetSpeaker.argtypes = [LPTTS_HANDLE_T, SPEAKER_T]
    TextToSpeechSetSpeaker.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 614
for _lib in _libs.values():
    if not _lib.has("TextToSpeechGetLanguage", "cdecl"):
        continue
    TextToSpeechGetLanguage = _lib.get("TextToSpeechGetLanguage", "cdecl")
    TextToSpeechGetLanguage.argtypes = [LPTTS_HANDLE_T, LPLANGUAGE_T]
    TextToSpeechGetLanguage.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 616
for _lib in _libs.values():
    if not _lib.has("TextToSpeechSetLanguage", "cdecl"):
        continue
    TextToSpeechSetLanguage = _lib.get("TextToSpeechSetLanguage", "cdecl")
    TextToSpeechSetLanguage.argtypes = [LPTTS_HANDLE_T, LANGUAGE_T]
    TextToSpeechSetLanguage.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 618
for _lib in _libs.values():
    if not _lib.has("TextToSpeechGetCaps", "cdecl"):
        continue
    TextToSpeechGetCaps = _lib.get("TextToSpeechGetCaps", "cdecl")
    TextToSpeechGetCaps.argtypes = [LPTTS_CAPS_T]
    TextToSpeechGetCaps.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 623
for _lib in _libs.values():
    if not _lib.has("TextToSpeechLoadUserDictionary", "cdecl"):
        continue
    TextToSpeechLoadUserDictionary = _lib.get("TextToSpeechLoadUserDictionary", "cdecl")
    TextToSpeechLoadUserDictionary.argtypes = [LPTTS_HANDLE_T, LPSTR]
    TextToSpeechLoadUserDictionary.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 626
for _lib in _libs.values():
    if not _lib.has("TextToSpeechUnloadUserDictionary", "cdecl"):
        continue
    TextToSpeechUnloadUserDictionary = _lib.get("TextToSpeechUnloadUserDictionary", "cdecl")
    TextToSpeechUnloadUserDictionary.argtypes = [LPTTS_HANDLE_T]
    TextToSpeechUnloadUserDictionary.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 628
for _lib in _libs.values():
    if not _lib.has("TextToSpeechOpenInMemory", "cdecl"):
        continue
    TextToSpeechOpenInMemory = _lib.get("TextToSpeechOpenInMemory", "cdecl")
    TextToSpeechOpenInMemory.argtypes = [LPTTS_HANDLE_T, DWORD]
    TextToSpeechOpenInMemory.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 630
for _lib in _libs.values():
    if not _lib.has("TextToSpeechCloseInMemory", "cdecl"):
        continue
    TextToSpeechCloseInMemory = _lib.get("TextToSpeechCloseInMemory", "cdecl")
    TextToSpeechCloseInMemory.argtypes = [LPTTS_HANDLE_T]
    TextToSpeechCloseInMemory.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 632
for _lib in _libs.values():
    if not _lib.has("TextToSpeechAddBuffer", "cdecl"):
        continue
    TextToSpeechAddBuffer = _lib.get("TextToSpeechAddBuffer", "cdecl")
    TextToSpeechAddBuffer.argtypes = [LPTTS_HANDLE_T, LPTTS_BUFFER_T]
    TextToSpeechAddBuffer.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 634
for _lib in _libs.values():
    if not _lib.has("TextToSpeechReturnBuffer", "cdecl"):
        continue
    TextToSpeechReturnBuffer = _lib.get("TextToSpeechReturnBuffer", "cdecl")
    TextToSpeechReturnBuffer.argtypes = [LPTTS_HANDLE_T, POINTER(LPTTS_BUFFER_T)]
    TextToSpeechReturnBuffer.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 638
for _lib in _libs.values():
    if not _lib.has("TextToSpeechOpenLogFile", "cdecl"):
        continue
    TextToSpeechOpenLogFile = _lib.get("TextToSpeechOpenLogFile", "cdecl")
    TextToSpeechOpenLogFile.argtypes = [LPTTS_HANDLE_T, LPSTR, DWORD]
    TextToSpeechOpenLogFile.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 640
for _lib in _libs.values():
    if not _lib.has("TextToSpeechCloseLogFile", "cdecl"):
        continue
    TextToSpeechCloseLogFile = _lib.get("TextToSpeechCloseLogFile", "cdecl")
    TextToSpeechCloseLogFile.argtypes = [LPTTS_HANDLE_T]
    TextToSpeechCloseLogFile.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 654
for _lib in _libs.values():
    if not _lib.has("TextToSpeechTyping", "cdecl"):
        continue
    TextToSpeechTyping = _lib.get("TextToSpeechTyping", "cdecl")
    TextToSpeechTyping.argtypes = [LPTTS_HANDLE_T, c_ubyte]
    TextToSpeechTyping.restype = None
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 657
for _lib in _libs.values():
    if not _lib.has("TextToSpeechOpenSapi5Output", "cdecl"):
        continue
    TextToSpeechOpenSapi5Output = _lib.get("TextToSpeechOpenSapi5Output", "cdecl")
    TextToSpeechOpenSapi5Output.argtypes = [LPTTS_HANDLE_T, POINTER(None), DWORD]
    TextToSpeechOpenSapi5Output.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 661
for _lib in _libs.values():
    if not _lib.has("TextToSpeechCloseSapi5Output", "cdecl"):
        continue
    TextToSpeechCloseSapi5Output = _lib.get("TextToSpeechCloseSapi5Output", "cdecl")
    TextToSpeechCloseSapi5Output.argtypes = [LPTTS_HANDLE_T]
    TextToSpeechCloseSapi5Output.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 663
for _lib in _libs.values():
    if not _lib.has("TextToSpeechSetVolume", "cdecl"):
        continue
    TextToSpeechSetVolume = _lib.get("TextToSpeechSetVolume", "cdecl")
    TextToSpeechSetVolume.argtypes = [LPTTS_HANDLE_T, c_int, c_int]
    TextToSpeechSetVolume.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 664
for _lib in _libs.values():
    if not _lib.has("TextToSpeechGetVolume", "cdecl"):
        continue
    TextToSpeechGetVolume = _lib.get("TextToSpeechGetVolume", "cdecl")
    TextToSpeechGetVolume.argtypes = [LPTTS_HANDLE_T, c_int, POINTER(c_int)]
    TextToSpeechGetVolume.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 675
for _lib in _libs.values():
    if not _lib.has("TextToSpeechVersion", "cdecl"):
        continue
    TextToSpeechVersion = _lib.get("TextToSpeechVersion", "cdecl")
    TextToSpeechVersion.argtypes = [POINTER(LPSTR)]
    TextToSpeechVersion.restype = DWORD
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 682
for _lib in _libs.values():
    if not _lib.has("TextToSpeechStartLang", "cdecl"):
        continue
    TextToSpeechStartLang = _lib.get("TextToSpeechStartLang", "cdecl")
    TextToSpeechStartLang.argtypes = [String]
    TextToSpeechStartLang.restype = c_uint
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 683
for _lib in _libs.values():
    if not _lib.has("TextToSpeechCloseLang", "cdecl"):
        continue
    TextToSpeechCloseLang = _lib.get("TextToSpeechCloseLang", "cdecl")
    TextToSpeechCloseLang.argtypes = [String]
    TextToSpeechCloseLang.restype = BOOL
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 686
for _lib in _libs.values():
    if not _lib.has("TextToSpeechSelectLang", "cdecl"):
        continue
    TextToSpeechSelectLang = _lib.get("TextToSpeechSelectLang", "cdecl")
    TextToSpeechSelectLang.argtypes = [LPTTS_HANDLE_T, c_uint]
    TextToSpeechSelectLang.restype = BOOL
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 687
for _lib in _libs.values():
    if not _lib.has("TextToSpeechGetFeatures", "cdecl"):
        continue
    TextToSpeechGetFeatures = _lib.get("TextToSpeechGetFeatures", "cdecl")
    TextToSpeechGetFeatures.argtypes = []
    TextToSpeechGetFeatures.restype = DWORD
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 710
class struct_anon_4(Structure):
    pass

struct_anon_4.__slots__ = [
    'StructSize',
    'StructVersion',
    'DLLVersion',
    'DTalkVersion',
    'VerString',
    'Language',
    'Features',
]
struct_anon_4._fields_ = [
    ('StructSize', DWORD),
    ('StructVersion', DWORD),
    ('DLLVersion', WORD),
    ('DTalkVersion', WORD),
    ('VerString', LPSTR),
    ('Language', LPSTR),
    ('Features', DWORD),
]

VERSION_INFO = struct_anon_4# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 710

LPVERSION_INFO = POINTER(VERSION_INFO)# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 712

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 714
for _lib in _libs.values():
    if not _lib.has("TextToSpeechVersionEx", "cdecl"):
        continue
    TextToSpeechVersionEx = _lib.get("TextToSpeechVersionEx", "cdecl")
    TextToSpeechVersionEx.argtypes = [POINTER(LPVERSION_INFO)]
    TextToSpeechVersionEx.restype = DWORD
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 726
class struct_anon_5(Structure):
    pass

struct_anon_5.__slots__ = [
    'lang_code',
    'lang_name',
]
struct_anon_5._fields_ = [
    ('lang_code', c_char * int(3)),
    ('lang_name', c_char * int(40)),
]

LANG_ENTRY = struct_anon_5# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 726

LPLANG_ENTRY = POINTER(LANG_ENTRY)# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 728

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 734
class struct_anon_6(Structure):
    pass

struct_anon_6.__slots__ = [
    'Languages',
    'MultiLang',
    'Entries',
]
struct_anon_6._fields_ = [
    ('Languages', DWORD),
    ('MultiLang', BOOL),
    ('Entries', LPLANG_ENTRY),
]

LANG_ENUM = struct_anon_6# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 734

LPLANG_ENUM = POINTER(LANG_ENUM)# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 735

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 737
for _lib in _libs.values():
    if not _lib.has("TextToSpeechEnumLangs", "cdecl"):
        continue
    TextToSpeechEnumLangs = _lib.get("TextToSpeechEnumLangs", "cdecl")
    TextToSpeechEnumLangs.argtypes = [POINTER(LPLANG_ENUM)]
    TextToSpeechEnumLangs.restype = DWORD
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 779
class struct_SPDEFS_TAG(Structure):
    pass

struct_SPDEFS_TAG.__slots__ = [
    'sex',
    'smoothness',
    'assertiveness',
    'average_pitch',
    'pitch_range',
    'breathiness',
    'richness',
    'num_fixed_samp_og',
    'laryngealization',
    'head_size',
    'formant4_res_freq',
    'formant4_bandwidth',
    'formant5_res_freq',
    'formant5_bandwidth',
    'parallel4_freq',
    'parallel5_freq',
    'gain_frication',
    'gain_aspiration',
    'gain_voicing',
    'gain_nasalization',
    'gain_cfr1',
    'gain_cfr2',
    'gain_cfr3',
    'gain_cfr4',
    'loudness',
    'spectral_tilt',
    'baseline_fall',
    'lax_breathiness',
    'quickness',
    'hat_rise',
    'stress_rise',
    'avg_glot_open',
    'avg_glot_voicd_open',
    'avg_glot_unv_open',
    'area_chink',
    'open_quo',
    'output_gain_mult',
    'junk',
    'junk1',
]
struct_SPDEFS_TAG._fields_ = [
    ('sex', c_short),
    ('smoothness', c_short),
    ('assertiveness', c_short),
    ('average_pitch', c_short),
    ('pitch_range', c_short),
    ('breathiness', c_short),
    ('richness', c_short),
    ('num_fixed_samp_og', c_short),
    ('laryngealization', c_short),
    ('head_size', c_short),
    ('formant4_res_freq', c_short),
    ('formant4_bandwidth', c_short),
    ('formant5_res_freq', c_short),
    ('formant5_bandwidth', c_short),
    ('parallel4_freq', c_short),
    ('parallel5_freq', c_short),
    ('gain_frication', c_short),
    ('gain_aspiration', c_short),
    ('gain_voicing', c_short),
    ('gain_nasalization', c_short),
    ('gain_cfr1', c_short),
    ('gain_cfr2', c_short),
    ('gain_cfr3', c_short),
    ('gain_cfr4', c_short),
    ('loudness', c_short),
    ('spectral_tilt', c_short),
    ('baseline_fall', c_short),
    ('lax_breathiness', c_short),
    ('quickness', c_short),
    ('hat_rise', c_short),
    ('stress_rise', c_short),
    ('avg_glot_open', c_short),
    ('avg_glot_voicd_open', c_short),
    ('avg_glot_unv_open', c_short),
    ('area_chink', c_short),
    ('open_quo', c_short),
    ('output_gain_mult', c_short),
    ('junk', c_short),
    ('junk1', c_short),
]

SPDEFS = struct_SPDEFS_TAG# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 779

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 782
for _lib in _libs.values():
    if not _lib.has("TextToSpeechGetPhVdefParams", "cdecl"):
        continue
    TextToSpeechGetPhVdefParams = _lib.get("TextToSpeechGetPhVdefParams", "cdecl")
    TextToSpeechGetPhVdefParams.argtypes = [LPTTS_HANDLE_T, UINT]
    TextToSpeechGetPhVdefParams.restype = POINTER(c_short)
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 785
for _lib in _libs.values():
    if not _lib.has("TextToSpeechGetSpeakerParams", "cdecl"):
        continue
    TextToSpeechGetSpeakerParams = _lib.get("TextToSpeechGetSpeakerParams", "cdecl")
    TextToSpeechGetSpeakerParams.argtypes = [LPTTS_HANDLE_T, UINT, POINTER(POINTER(SPDEFS)), POINTER(POINTER(SPDEFS)), POINTER(POINTER(SPDEFS)), POINTER(POINTER(SPDEFS))]
    TextToSpeechGetSpeakerParams.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 789
for _lib in _libs.values():
    if not _lib.has("TextToSpeechSetSpeakerParams", "cdecl"):
        continue
    TextToSpeechSetSpeakerParams = _lib.get("TextToSpeechSetSpeakerParams", "cdecl")
    TextToSpeechSetSpeakerParams.argtypes = [LPTTS_HANDLE_T, POINTER(SPDEFS)]
    TextToSpeechSetSpeakerParams.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 793
class struct_dic_entry(Structure):
    pass

struct_dic_entry.__slots__ = [
    'fc',
    'text',
]
struct_dic_entry._fields_ = [
    ('fc', c_uint * int(1)),
    ('text', c_ubyte * int(128)),
]

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 808
for _lib in _libs.values():
    if not _lib.has("TextToSpeechDictionaryHit", "cdecl"):
        continue
    TextToSpeechDictionaryHit = _lib.get("TextToSpeechDictionaryHit", "cdecl")
    TextToSpeechDictionaryHit.argtypes = [LPTTS_HANDLE_T, POINTER(struct_dic_entry)]
    TextToSpeechDictionaryHit.restype = c_int
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 810
for _lib in _libs.values():
    if not _lib.has("TextToSpeechDumpDictionary", "cdecl"):
        continue
    TextToSpeechDumpDictionary = _lib.get("TextToSpeechDumpDictionary", "cdecl")
    TextToSpeechDumpDictionary.argtypes = [LPTTS_HANDLE_T, String]
    TextToSpeechDumpDictionary.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 812
for _lib in _libs.values():
    if not _lib.has("TextToSpeechUserDictionaryHit", "cdecl"):
        continue
    TextToSpeechUserDictionaryHit = _lib.get("TextToSpeechUserDictionaryHit", "cdecl")
    TextToSpeechUserDictionaryHit.argtypes = [LPTTS_HANDLE_T, POINTER(struct_dic_entry)]
    TextToSpeechUserDictionaryHit.restype = c_int
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 814
for _lib in _libs.values():
    if not _lib.has("TextToSpeechDumpUserDictionary", "cdecl"):
        continue
    TextToSpeechDumpUserDictionary = _lib.get("TextToSpeechDumpUserDictionary", "cdecl")
    TextToSpeechDumpUserDictionary.argtypes = [LPTTS_HANDLE_T, String]
    TextToSpeechDumpUserDictionary.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 816
for _lib in _libs.values():
    if not _lib.has("TextToSpeechAddUserEntry", "cdecl"):
        continue
    TextToSpeechAddUserEntry = _lib.get("TextToSpeechAddUserEntry", "cdecl")
    TextToSpeechAddUserEntry.argtypes = [LPTTS_HANDLE_T, POINTER(struct_dic_entry)]
    TextToSpeechAddUserEntry.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 818
for _lib in _libs.values():
    if not _lib.has("TextToSpeechDeleteUserEntry", "cdecl"):
        continue
    TextToSpeechDeleteUserEntry = _lib.get("TextToSpeechDeleteUserEntry", "cdecl")
    TextToSpeechDeleteUserEntry.argtypes = [LPTTS_HANDLE_T, POINTER(struct_dic_entry)]
    TextToSpeechDeleteUserEntry.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 820
for _lib in _libs.values():
    if not _lib.has("TextToSpeechChangeUserPhoneme", "cdecl"):
        continue
    TextToSpeechChangeUserPhoneme = _lib.get("TextToSpeechChangeUserPhoneme", "cdecl")
    TextToSpeechChangeUserPhoneme.argtypes = [LPTTS_HANDLE_T, POINTER(struct_dic_entry), POINTER(c_ubyte)]
    TextToSpeechChangeUserPhoneme.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 823
for _lib in _libs.values():
    if not _lib.has("TextToSpeechSaveUserDictionary", "cdecl"):
        continue
    TextToSpeechSaveUserDictionary = _lib.get("TextToSpeechSaveUserDictionary", "cdecl")
    TextToSpeechSaveUserDictionary.argtypes = [LPTTS_HANDLE_T, String]
    TextToSpeechSaveUserDictionary.restype = MMRESULT
    break

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 825
for _lib in _libs.values():
    if not _lib.has("TextToSpeechConvertToPhonemes", "cdecl"):
        continue
    TextToSpeechConvertToPhonemes = _lib.get("TextToSpeechConvertToPhonemes", "cdecl")
    TextToSpeechConvertToPhonemes.argtypes = [LPTTS_HANDLE_T, POINTER(c_ubyte), POINTER(DWORD), DWORD, POINTER(c_ubyte), DWORD, DWORD]
    TextToSpeechConvertToPhonemes.restype = MMRESULT
    break

# dectalk/src/dapi/src/osf/dtmmedefs.h: 96
try:
    H_MMBASIC = 1
except:
    pass

CONST = c_int# dectalk/src/dapi/src/osf/dtmmedefs.h: 115

# dectalk/src/dapi/src/osf/dtmmedefs.h: 172
try:
    TRUE = 1
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 176
try:
    FALSE = 0
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 278
try:
    MMSYSERR_BASE = 0
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 279
try:
    MMSYSERR_NOERROR = 0
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 280
try:
    MMSYSERR_ERROR = (MMSYSERR_BASE + 1)
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 281
try:
    MMSYSERR_BADDEVICEID = (MMSYSERR_BASE + 2)
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 282
try:
    MMSYSERR_NOTENABLED = (MMSYSERR_BASE + 3)
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 283
try:
    MMSYSERR_ALLOCATED = (MMSYSERR_BASE + 4)
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 284
try:
    MMSYSERR_INVALHANDLE = (MMSYSERR_BASE + 5)
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 285
try:
    MMSYSERR_NODRIVER = (MMSYSERR_BASE + 6)
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 286
try:
    MMSYSERR_NOMEM = (MMSYSERR_BASE + 7)
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 287
try:
    MMSYSERR_NOTSUPPORTED = (MMSYSERR_BASE + 8)
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 288
try:
    MMSYSERR_BADERRNUM = (MMSYSERR_BASE + 9)
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 289
try:
    MMSYSERR_INVALFLAG = (MMSYSERR_BASE + 10)
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 290
try:
    MMSYSERR_INVALPARAM = (MMSYSERR_BASE + 11)
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 291
try:
    MMSYSERR_HANDLEBUSY = (MMSYSERR_BASE + 12)
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 294
try:
    MMSYSERR_INVALIDALIAS = (MMSYSERR_BASE + 13)
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 295
try:
    MMSYSERR_LASTERROR = (MMSYSERR_BASE + 13)
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 298
try:
    WAVE_INVALIDFORMAT = 0x00000000
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 299
try:
    WAVE_FORMAT_1M08 = 0x00000001
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 300
try:
    WAVE_FORMAT_1S08 = 0x00000002
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 301
try:
    WAVE_FORMAT_1M16 = 0x00000004
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 302
try:
    WAVE_FORMAT_1S16 = 0x00000008
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 303
try:
    WAVE_FORMAT_2M08 = 0x00000010
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 304
try:
    WAVE_FORMAT_2S08 = 0x00000020
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 305
try:
    WAVE_FORMAT_2M16 = 0x00000040
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 306
try:
    WAVE_FORMAT_2S16 = 0x00000080
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 307
try:
    WAVE_FORMAT_4M08 = 0x00000100
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 308
try:
    WAVE_FORMAT_4S08 = 0x00000200
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 309
try:
    WAVE_FORMAT_4M16 = 0x00000400
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 310
try:
    WAVE_FORMAT_4S16 = 0x00000800
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 311
try:
    WAVE_FORMAT_08M08 = 0x00001000
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 312
try:
    WAVE_FORMAT_08M16 = 0x00002000
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 313
try:
    WAVE_FORMAT_MULAW = 0x00000007
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 315
try:
    WAVE_MAPPER = (DWORD (ord_if_char((-1)))).value
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 316
try:
    WAVE_OPEN_SHAREABLE = 0x00000004
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 317
try:
    CALLBACK_FUNCTION = 0x00030000
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 318
try:
    WAVE_FORMAT_PCM = 1
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 321
try:
    SUN_ULAW = 1
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 322
try:
    SUN_LIN_8 = 2
except:
    pass

# dectalk/src/dapi/src/osf/dtmmedefs.h: 323
try:
    SUN_LIN_16 = 3
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 228
try:
    ERROR_IN_AUDIO_WRITE = 1
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 229
try:
    ERROR_OPENING_WAVE_OUTPUT_DEVICE = 2
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 230
try:
    ERROR_GETTING_DEVICE_CAPABILITIES = 3
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 231
try:
    ERROR_READING_DICTIONARY = 4
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 232
try:
    ERROR_WRITING_FILE = 5
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 233
try:
    ERROR_ALLOCATING_INDEX_MARK_MEMORY = 6
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 234
try:
    ERROR_OPENING_WAVE_FILE = 7
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 235
try:
    ERROR_BAD_WAVE_FILE_FORMAT = 8
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 236
try:
    ERROR_UNSUPPORTED_WAVE_FILE_FORMAT = 9
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 237
try:
    ERROR_UNSUPPORTED_WAVE_AUDIO_FORMAT = 10
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 238
try:
    ERROR_READING_WAVE_FILE = 11
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 239
try:
    TTS_AUDIO_PLAY_START = 12
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 240
try:
    TTS_AUDIO_PLAY_STOP = 13
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 241
try:
    TTS_INDEX_MARK = 14
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 242
try:
    TTS_INDEX_BOOKMARK = 15
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 243
try:
    TTS_INDEX_WORDPOS = 16
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 244
try:
    TTS_INDEX_START = 17
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 245
try:
    TTS_INDEX_STOP = 18
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 253
try:
    OWN_AUDIO_DEVICE = 0x00000001
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 254
try:
    REPORT_OPEN_ERROR = 0x00000002
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 255
try:
    USE_SAPI5_AUDIO_DEVICE = 0x40000000
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 256
try:
    DO_NOT_USE_AUDIO_DEVICE = 0x80000000
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 258
try:
    TTSSTARTUP_USING_DEFAULT_CALLBACK = 0x08000000
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 260
try:
    WAVE_FORMAT_NULL = 0xC4000000
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 267
try:
    PAUL = 0
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 268
try:
    BETTY = 1
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 269
try:
    HARRY = 2
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 270
try:
    FRANK = 3
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 271
try:
    DENNIS = 4
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 272
try:
    KIT = 5
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 273
try:
    URSULA = 6
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 274
try:
    RITA = 7
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 275
try:
    WENDY = 8
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 283
try:
    TTS_NORMAL = 0
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 284
try:
    TTS_FORCE = 1
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 291
try:
    TTS_MSG_BUFFER = 9
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 292
try:
    TTS_MSG_INDEX_MARK = 1
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 293
try:
    TTS_MSG_STATUS = 2
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 294
try:
    TTS_MSG_VISUAL = 3
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 307
try:
    TTS_SILENT = 0x2
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 313
try:
    INPUT_CHARACTER_COUNT = 0
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 314
try:
    STATUS_SPEAKING = 1
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 315
try:
    WAVE_OUT_DEVICE_ID = 2
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 321
try:
    LOG_TEXT = 0x0001
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 322
try:
    LOG_PHONEMES = 0x0002
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 323
try:
    LOG_SYLLABLES = 0x0010
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 331
try:
    TTS_AMERICAN_ENGLISH = 1
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 337
try:
    PROPER_NAME_PRONUNCIATION = 0x00000001
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 344
try:
    DTALK_HELP_FILE_NAME = 'dectalk.hlp'
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 345
try:
    COPYRIGHT_COMPANY = 'Fonix Corporation'
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 346
try:
    COPYRIGHT_DATE = '2001-2002'
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 363
try:
    TTS_ASCII = 0
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 364
try:
    TTS_UNICODE = 1
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 452
try:
    FULL_RANGE_MARKS = 0xF011
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 666
try:
    VOLUME_MAIN = 1
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 667
try:
    VOLUME_ATTENUATION = 2
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 688
try:
    TTS_NOT_SUPPORTED = 0x7FFF
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 689
try:
    TTS_NOT_AVAILABLE = 0x7FFE
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 690
try:
    TTS_LANG_ERROR = 0x4000
except:
    pass

# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 695
try:
    VERSION_STRUCT_VER = 0x0001
except:
    pass

tWAVEFORMATEX = struct_tWAVEFORMATEX# dectalk/src/dapi/src/osf/dtmmedefs.h: 344

LANGUAGE_PARAMS_TAG = struct_LANGUAGE_PARAMS_TAG# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 370

TTS_CAPS_TAG = struct_TTS_CAPS_TAG# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 384

TTS_PHONEME_TAG = struct_TTS_PHONEME_TAG# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 399

TTS_INDEX_TAG = struct_TTS_INDEX_TAG# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 409

TTS_BUFFER_TAG = struct_TTS_BUFFER_TAG# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 426

SPDEFS_TAG = struct_SPDEFS_TAG# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 779

dic_entry = struct_dic_entry# /home/m/proj/mine/dectalk.py/dectalk/src/dapi/src/api/ttsapi.h: 793

# No inserted files

# No prefix-stripping

