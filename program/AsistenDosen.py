# Saya Amida Zulfa Laila NIM 2101147 mengerjakan Tugas Praktikum 1
# dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka
# saya tidak melakukan kecurangan seperti yang telah dispesifikasikan.
# Aamiin.

from Mahasiswa import Mahasiswa

# class declaration
# inheritance dari class Mahasiswa
# anak dari class Mahasiswa
class AsistenDosen(Mahasiswa):
    
    # Private attributes
    __tahun=0
    

    # contructor 
    def __init__(self,nik=0,name="",gender="", nim=0, tahun=0):
        super().__init__(nik,name,gender,nim,)
        self.__tahun = tahun

    # Getter dan Setter
    
    # Get tahun
    def getTahun(self):
        return self.__tahun
    
    # set tahun
    def setTahun(self, tahun):
        self.__tahun = tahun
    
    def mengajarAsdos(self):
        return "Sedang Mengajar Mahasiswa"
    
    def memberiTugasAsdos(self):
        return "Memberi Tugas latihan praktikum"
