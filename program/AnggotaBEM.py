# Saya Amida Zulfa Laila NIM 2101147 mengerjakan Tugas Praktikum 1
# dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka
# saya tidak melakukan kecurangan seperti yang telah dispesifikasikan.
# Aamiin.

from Mahasiswa import Mahasiswa

# class declaration
# inheritance dari class Mahasiswa
# anak dari class Mahasiswa
class AnggotaBEM(Mahasiswa):
    
    # Private attributes
    __position=""
    __division=""

    # contructor 
    def __init__(self,nik=0,name="",gender="",nim=0,position="",division=""):
        super().__init__(nik,name,gender,nim)
        self.__position = position
        self.__division = division

    # Getter dan Setter

    # Get position
    def getPosition(self):
        return self.__position
    
    # set position
    def setPosition(self, position):
        self.__position = position
    
    # get division
    def getDivision(self):
        return self.__division
    
    # set division
    def setDivision(self, division):
        self.__division = division
    
