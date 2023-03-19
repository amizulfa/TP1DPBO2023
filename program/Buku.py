# class declaration
class Buku:
    
    # Private attributes
    __judul=""
    __penulis=""

    # contructor 
    def __init__(self,judul="", penulis=""):
        self.__judul = judul
        self.__penulis = penulis

    # Getter dan Setter
    # Get judul
    def getJudul(self):
        return self.__judul
    
    # set judul
    def setJudul(self, judul):
        self.__judul = judul
   
    # Get penulis
    def getPenulis(self):
        return self.__penulis
    
    # set penulis
    def setPenulis(self, penulis):
        self.__penulis = penulis
    