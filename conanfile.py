from conans import ConanFile, CMake, tools


class LibtidyConan(ConanFile):
    name = "tidy-html5"
    version = "5.6"
    url = "https://github.com/htacg/tidy-html5"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    scm = {"revision": "3a30f6a4300417674026f6dddea5973debc6b808",
           "type": "git",
           "url": "https://github.com/htacg/tidy-html5.git",
           "subfolder": "source"}

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="source")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="hello")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]