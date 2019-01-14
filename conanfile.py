from conans import ConanFile, CMake, tools
from conans.tools import patch, replace_in_file


class CImgConan(ConanFile):
    name = "cimg"
    version = "2.4.5"
    description = "The CImg Library is a small and open-source C++ toolkit for image processing"
    url = "https://framagit.org/dtschump/CImg"
    license = "CeCILL V2"
    no_copy_source = True

    def source(self):
        self.run("git clone --depth 1 --branch v.%s https://framagit.org/dtschump/CImg.git" % self.version)
        
    def package(self):
        self.copy("CImg.h", dst="include", src="CImg")
