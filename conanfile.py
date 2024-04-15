from conan import ConanFile
from conan.tools.cmake import cmake_layout

import subprocess
import os
import re


class exampleGtest(ConanFile):
    ###### TODO: CHANGE NAME, VERSION, DESCRIPTION AND AUTHOR ######
    name = "gtest_example"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def configure_cmake(self):
        cmake = CMake(self)

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()

    def requirements(self):
        self.requires("gtest/1.14.0")