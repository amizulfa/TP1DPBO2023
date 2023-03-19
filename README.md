# TP1DPBO2023
> Saya Amida Zulfa Laila NIM 2101147 mengerjakan Tugas Praktikum 1
dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka
saya tidak melakukan kecurangan seperti yang telah dispesifikasikan.
Aamiin.

## Bahasa Pemrograman yang digunakan
> Python

## Desain Class Diagram
![image](https://user-images.githubusercontent.com/100895165/226159429-b7caac88-f7c3-428b-a588-a4afb0fd25ac.png)

## Penjelasan Desain
1. Terdapat 9 kelas, yaitu :
  - Human
    - Method :
      - get : mengembalikan nilai dari suatu atribut
      - set : memberikan nilai pada suatu atribut
      - makan : Manusia bisa makan
      - minum : Manusia bisa minum
      - tidur : Manusia bisa tidur
  - Mahasiswa
    - Method :
      - get : mengembalikan nilai dari suatu atribut
      - set : memberikan nilai pada suatu atribut
      - belajar : seorang mahasiswa sedang belajar
      - hadirKelas : seorang mahasiswa menghadiri kelas
      - mengerjakanTugas : seorang mahasiswa mengerjakan tugas
  - Dosen
    - Method :
      - get : mengembalikan nilai dari suatu atribut
      - set : memberikan nilai pada suatu atribut
      - mengajar : seorang dosen sedang mengajar mahasiswa
      - memberiTugas : seorang dosen memberi tugas kepada mahasiswa
      - memberiNilai : seorang dosen memberi nilai kepada mahasiswa
  - AsistenDosen
    - Method :
      - get : mengembalikan nilai dari suatu atribut
      - set : memberikan nilai pada suatu atribut
      - mengajar : asisten dosen mengajar mahasiswa
      - memberiTugas : asisten dosen memberi tugas praktikum kepada mahasiswa
  - AnggotaBEM
    - Method :
      - get : mengembalikan nilai dari suatu atribut
      - set : memberikan nilai pada suatu atribut 
  - AnggotaDPM
    - Method :
      - get : mengembalikan nilai dari suatu atribut
      - set : memberikan nilai pada suatu atribut
  - DPM
    - Method :
      - get : mengembalikan nilai dari suatu atribut
      - set : memberikan nilai pada suatu atribut
  - BEM
    - Method :
      - get : mengembalikan nilai dari suatu atribut
      - set : memberikan nilai pada suatu atribut
  - Buku
    - Method :
      - get : mengembalikan nilai dari suatu atribut
      - set : memberikan nilai pada suatu atribut
      
2. Relasi antar kelas :
    1. Mahasiswa dan Dosen is a Human karena objek nya Manusia
    2. AnggotaBEM, AnggotaDPM, dan AsistenDosen is a Mahasiswa karena ketiga            class tersebut pasti seorang Mahasiswa
    3. Mahasiswa composite class Buku, karena Mahasiswa punya buku
    4. BEM composite class AnggotaBEM, karena BEM pasti punya Anggota
    5. DPM composite class AnggotaDPM, karena DPM pasti punya Anggota
    6. Dosen composite class AsistenDosen, karena Dosen punya Asisten

## Alur Program
  - Program ini memakai hardcode sebagai input nya.
  - instansiasi objek dan memasukan ke dalam list
  - output yang dikeluarkan :
    - list mahasiswa
    - list dosen
      - list asistenDosen
    - DPM
    - BEM
    - contoh penggunaan method
    
## Dokumetasi Program
- List Mahasiswa dan Dosen
  ![image](https://user-images.githubusercontent.com/100895165/226160528-79323ecc-0bad-453a-aae0-c01cd1f03b1a.png)

- DPM dan BEM
  ![image](https://user-images.githubusercontent.com/100895165/226160545-9e36a64f-edf7-4aa5-bd66-935acbffd0a7.png)

- Contoh Method
  ![image](https://user-images.githubusercontent.com/100895165/226160562-d742863e-4ab0-4f2c-8407-ed5c0d835657.png)

    
