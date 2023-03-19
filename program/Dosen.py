# Saya Amida Zulfa Laila NIM 2101147 mengerjakan Tugas Praktikum 1
# dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka
# saya tidak melakukan kecurangan seperti yang telah dispesifikasikan.
# Aamiin.

from Human import Human

# class declaration, class Dosen sebagai anak dari class Human 
class Dosen(Human):
    
    # Private attributes
    __nip=0
    __laptops=""
    __spidol=int
    __asdos=[]

    # contructor 
    def __init__(self,nik=0,name="",gender="",nip=0,laptops="", spidol=0, asdos=[]):
        super().__init__(nik,name,gender)
        self.__nip = nip
        self.__laptops=laptops
        self.__spidol=spidol
        self.__asdos= asdos

    #Getter dan Setter

    # Get nip
    def getNip(self):
        return self.__nip
    
    # set nip
    def setNip(self, nip):
        self.__nip = nip
    
    # get laptop
    def getLaptop(self):
        return self.__laptops
    
    # set laptop
    def setLaptop(self, laptops):
        self.__laptops=laptops
        
    # get pendidikan terakhir
    def getSpidol(self):
        return self.__spidol
    
    # set pendidikan terakhir
    def setSpidol(self, spidol):
        self.__spidol=spidol
    
    def setAsdos(self, asdos):
        self.__asdos.append(asdos)
        
    def getAsdos(self):
        return self.__asdos

    def mengajar(self):
        return "Sedang Mengajar"
    
    def memberiTugas(self):
        return "Memberi Tugas"
        
    def memberiNilai(self):
        return "Telah Memberi nilai"