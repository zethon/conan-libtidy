# tidy-html5 conan recipe 
# as used by https://github.com/zethon/Owl

# NOTE: The tidy-html5 library will turn on debug logging for Windows DEBUG builds
# even if you set `ENABLE_DEBUG_LOG=Off` in the CMake file. This is because there
# is code to EXPLICITLY turn it on if it's Windows and Debug mode. However, you
# can use the preprocessor definition `DISABLE_DEBUG_LOG` to turn it off in Windows.
# But amazingly enough, there's no easy way to pass a preprocessor definition
# on the command-line to MSBuild. The best way I've found to do this is to set the
# 'CL' env var, which MSBuild checks for additional command line arguments.
#
# See: https://docs.conan.io/en/latest/reference/build_helpers/cmake.html#configure
#      https://github.com/htacg/tidy-html5/issues/852
#      https://stackoverflow.com/questions/8564337/how-to-define-a-c-preprocessor-macro-through-the-command-line-with-cmake

import os
from conans import ConanFile, CMake, tools

class LibtidyConan(ConanFile):
    name = "tidy-html5"
    version = "5.7.28"
    url = "https://github.com/htacg/tidy-html5"
    license = "permissive license"
    description = "The granddaddy of HTML tools, with support for modern standards"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    scm = {"revision": "d1b906991a7587688d384b648c55731f9be52506",
           "type": "git",
           "url": "https://github.com/htacg/tidy-html5.git",
           "subfolder": "source"}

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIB"] = False
        cmake.configure(source_folder="source")
        if self.settings.os == "Windows":
            os.environ["CL"] = "/DDISABLE_DEBUG_LOG=1"
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*.h", dst="include", src="source/include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)