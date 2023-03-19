# Saya Amida Zulfa Laila NIM 2101147 mengerjakan Tugas Praktikum 1
# dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka
# saya tidak melakukan kecurangan seperti yang telah dispesifikasikan.
# Aamiin.

from Human import Human
# inheritance dari class Human
# anak dari class Human
class Mahasiswa(Human):
    
    # Private attributes
    __nim=0
    __laptops=""
    __listBuku=[]

    # contructor 
    def __init__(self, nik=0,name="",gender="",nim=0,laptops="",listBuku=[]):
        super().__init__(nik,name,gender)
        self.__nim = nim
        self.__laptops=laptops
        self.__listBuku=listBuku

    #Getter dan Setter

    # Get nim
    def getNim(self):
        return self.__nim
    
    # set nim
    def setNim(self, nim):
        self.__nim = nim
    
    # get laptop
    def getLaptop(self):
        return self.__laptops
    
    # set laptop
    def setLaptop(self, laptops):
        self.__laptops= laptops
    
    # get listBuku
    def getListBuku(self):
        return self.__listBuku
    
    # set listBuku
    def setListBuku(self, listBuku):
        self.__listBuku.append(listBuku)
    
    def belajar(self):
        return "Sedang Belajar"
    
    def hadirKelas(self):
        return "Menghadiri Kelas"
    
    def mengerjakanTugas(self):
        return "Sedang Mengerjakan Tugas"