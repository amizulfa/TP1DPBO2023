# Saya Amida Zulfa Laila NIM 2101147 mengerjakan Tugas Praktikum 1
# dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka
# saya tidak melakukan kecurangan seperti yang telah dispesifikasikan.
# Aamiin.

# class declaration
class BEM:
    
    # Private attributes
    __namaKabinet=""
    __tahun=0
    __program=""
    __inovasi=""
    __listAnggotaBEM=[] # composite class AnggotaBEM

    # contructor 
    def __init__(self,namaKabinet="",tahun=0, program="", inovasi="",listAnggotaBEM=[]):
        self.__namaKabinet = namaKabinet
        self.__tahun = tahun
        self.__program = program
        self.__inovasi = inovasi
        self.__listAnggotaBEM=listAnggotaBEM

    # Getter dan Setter
    
    # Get namaKabinet
    def getNamaKabinet(self):
        return self.__namaKabinet
    
    # set namaKabinet
    def setNamaKabinet(self, namaKabinet):
        self.__namaKabinet = namaKabinet
        
    # Get tahun
    def getTahun(self):
        return self.__tahun
    
    # set tahun
    def setTahun(self, tahun):
        self.__tahun = tahun
    
    # Get program
    def getProgram(self):
        return self.__program
    
    # set program
    def setProgram(self, program):
        self.__program = program
    
    # Get inovasi
    def getInovasi(self):
        return self.__inovasi
    
    # set inovasi
    def setInovasi(self, inovasi):
        self.__inovasi = inovasi
   
    # Get listAnggotaBEM
    def getListAnggotaBEM(self):
        return self.__listAnggotaBEM
    
    # set listAnggotaBEM
    def setListAnggotaBEM(self, listAnggotaBEM):
        self.__listAnggotaBEM.append(listAnggotaBEM)
    
    def melaksanakanProgram(self):
        return "Sedang Melaksanakan Program"
