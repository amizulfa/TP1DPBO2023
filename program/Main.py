# Saya Amida Zulfa Laila NIM 2101147 mengerjakan Tugas Praktikum 1
# dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka
# saya tidak melakukan kecurangan seperti yang telah dispesifikasikan.
# Aamiin.

from Mahasiswa import Mahasiswa 
from Dosen import Dosen
from AnggotaBEM import AnggotaBEM
from DPM import DPM
from BEM import BEM
from AnggotaDPM import AnggotaDPM
from AsistenDosen import AsistenDosen
from Buku import Buku

# instantiation object
buku1 = Buku("Dasar - dasar Teknikk Informatika", "Novega Pratama Adiputra")
buku2 = Buku("Kecerdasan Buatan dengan Python", "Yulia W")
buku3 = Buku("Big Data", "Cahyono")
buku4 = Buku("Tutorial Flutter", "Yudi W")
buku5 = Buku("Cara cepat Lulus IT", "Amin Basalamah")

# instantiation object
asdos1 = AsistenDosen()
asdos1.setNik(12345678)
asdos1.setName("Bulan")
asdos1.setGender("Cowo")
asdos1.setNim(2209876)
asdos1.setTahun(2021)

# instantiation object
asdos2 = AsistenDosen()
asdos2.setNik(12345678)
asdos2.setName("Najma")
asdos2.setGender("Cewe")
asdos2.setNim(2209876)
asdos2.setTahun(2021)

# instantiation object
mhs1 = Mahasiswa( 123, "Anin", "Cewe", 2101114,"Lenovo Thinkpad",[buku4, buku2,buku5])
mhs2 = Mahasiswa( 5463, "Afri", "Cowo", 2301345,"Acer Sapu", [buku5])

# instantiation object
dsn1 = Dosen(12678,"Rose", "Cewe", 88776655,"Macbook",2,[asdos1,asdos2] )

# instantiation object
Adpm1 = AnggotaDPM()
Adpm1.setName("Alga")
Adpm1.setNim(2345678)
Adpm1.setDivision("Pengawasan")
Adpm1.setPosition("Anggota DPM")

# instantiation object
dpm = DPM("Kertarahaja", 2023,[Adpm1])

# instantiation object
Abem1 = AnggotaBEM()
Abem1.setName("April")
Abem1.setNim(765389)
Abem1.setDivision("Kominfo")
Abem1.setPosition("Ketua Divisi")

# instantiation object
Abem2 = AnggotaBEM()
Abem2.setName("Rapi")
Abem2.setNim(2122278)
Abem2.setDivision("Non - Divisi")
Abem2.setPosition("Ketua BEM")

# instantiation object
bem = BEM("Kertarahaja", 2023, "Nongki Bareng", "Mencerdaskan Mahasiswa",[Abem1, Abem2])

# membuat list Mahasiswa
listMhs = []
# masukan ke dalam list
listMhs.append(mhs1)
listMhs.append(mhs2)

# membuat list dosen
listDosen = []
# masukan ke dalam list
listDosen.append(dsn1)

# MENAMPILKAN LIST MAHASISWA
q=1
for i in listMhs:
    print("+==========================================================================+")
    print("|                               Mahasiswa "+str(q)+"                                |")
    print("+==========================================================================+")
    print("|NIK                  :", i.getNik())
    print("|Nama                 :", i.getName())
    print("|Jenis Kelamin        :", i.getGender())
    print("|NIM                  :", i.getNim())
    print("+==========================================================================+")
    print("|",i.getName(),"Punya Laptop yaitu  :",i.getLaptop())
    print("|",i.getName(),"Juga punya Buku yaitu   :")
    p = 1
    for j in i.getListBuku():
        print("|        "+str(p)+". Judulnya            :", j.getJudul())
        print("|           Penulisnya          :", j.getPenulis())
        p=p+1
    q=q+1
print("+==========================================================================+")
print('\n')

# MENAMPILKAN LIST DOSEN
q=1
for i in listDosen:
    print("+==========================================================================+")
    print("|                                  Dosen "+str(q)+"                                 |")
    print("+==========================================================================+")
    print("|NIK                  :", i.getNik())
    print("|Nama                 :", i.getName())
    print("|Jenis Kelamin        :", i.getGender())
    print("|NIP                  :", i.getNip())
    print("+==========================================================================+")
    print("|",i.getName(),"Punya Laptop yaitu  :", i.getLaptop())
    print("|",i.getName(),"Punya spidol sebanyak  :",i.getSpidol())
    print("|",i.getName(),"Juga punya Asisten yaitu     :")
    p = 1
    for j in i.getAsdos():
        print("|        "+str(p)+". Namanya             :", j.getName())
        print("|           Angkatan            :", j.getTahun())
        p=p+1
    q=q+1
print("+==========================================================================+")
print('\n')

# MENAMPILKAN DPM
print("+==========================================================================+")
print("|                                    DPM                                   |")
print("+==========================================================================+")
print("|Kabinet                  :", dpm.getNamaKabinet())
print("|Tahun                    :", dpm.getTahun())
print("+==========================================================================+")
print("| DPM", dpm.memberiRekomendasi())
print("| DPM punya Anggota, yaitu :")
p = 1
for j in dpm.getListAnggotaDPM():
    print("|        "+str(p)+". Nama             :", j.getName())
    print("|           NIM              :", j.getNim())
    print("|           Divisi           :", j.getDivision())
    print("|           Posisi           :", j.getPosition())
    p=p+1
print("+==========================================================================+")
print('\n')

# MENAMPILKAN BEM
print("+==========================================================================+")
print("|                                    BEM                                   |")
print("+==========================================================================+")
print("|Kabinet                  :", bem.getNamaKabinet())
print("|Tahun                    :", bem.getTahun())
print("+==========================================================================+")
print("| BEM punya Program, yaitu    :", bem.getProgram())
print("| BEM punya Inovasi, yaitu    :", bem.getInovasi())
print("| BEM punya Anggota, yaitu :")
p = 1
for j in bem.getListAnggotaBEM():
    print("|        "+str(p)+". Nama             :", j.getName())
    print("|           NIM              :", j.getNim())
    print("|           Divisi           :", j.getDivision())
    print("|           Posisi           :", j.getPosition())
    p=p+1
print("+==========================================================================+")

# CONTOH PENGGUNAAN METHOD DALAM CLASS
print('\n')
print("+===============================================================================================================+")
print("|                                         Contoh Penggunaan Method                                              |")
print("+===============================================================================================================+")
print("|",Abem2.getName(),"Sebagai",Abem2.getPosition(),"mempunyai Program",bem.getProgram())
print("| BEM",bem.melaksanakanProgram(),bem.getProgram())        
print("+---------------------------------------------------------------------------------------------------------------+")
print("|",Adpm1.getName(),dpm.memberiRekomendasi(),"Sebagai",Adpm1.getPosition(),"pada bidang",Adpm1.getDivision(),"Kepada BEM")
print("+---------------------------------------------------------------------------------------------------------------+")
print("|",asdos2.getName(),asdos2.mengajarAsdos(),"lalu",asdos2.memberiTugasAsdos())
print("+---------------------------------------------------------------------------------------------------------------+")
print("|",dsn1.getName(),dsn1.mengajar(),"lalu",dsn1.memberiTugas(),"dan",dsn1.memberiNilai())
print("+---------------------------------------------------------------------------------------------------------------+")
print("| Sebagai Manusia", mhs1.getName(), mhs1.makan(),",",mhs1.minum(),", dan",mhs1.tidur())
print("| Sebagai Mahasiswa", mhs1.getName(), mhs1.hadirKelas(),", dan sekarang",mhs1.belajar(),", dan sekarang",mhs1.mengerjakanTugas())
print("+===============================================================================================================+")
