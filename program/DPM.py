# Saya Amida Zulfa Laila NIM 2101147 mengerjakan Tugas Praktikum 1
# dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka
# saya tidak melakukan kecurangan seperti yang telah dispesifikasikan.
# Aamiin.

# class declaration
class DPM:
    
    # Private attributes
    __namaKabinet=""
    __tahun=0
    __listAnggotaDPM=[] # composite class AnggotaDPM

    # contructor 
    def __init__(self,namaKabinet="",tahun=0,listAnggotaDPM=[]):
        self.__namaKabinet = namaKabinet
        self.__tahun = tahun
        self.__listAnggotaDPM=listAnggotaDPM

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
   
    # Get listAnggotaDPM
    def getListAnggotaDPM(self):
        return self.__listAnggotaDPM
    
    # set listAnggotaDPM
    def setListAnggotaDPM(self, listAnggotaDPM):
        self.__listAnggotaDPM.append(listAnggotaDPM)
    
    def memberiRekomendasi(self):
        return "Sedang Memberikan Evaluasi"
