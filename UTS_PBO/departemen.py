class Departemen:
    def __init__(self, nama, lokasi, leader):
        self.__nama = nama
        self.lokasi = lokasi
        self.__leader = leader
        self.__daftarPegawai = []

    def tambahPegawai(self, pegawai):
        for p in self.__daftarPegawai:
            if p.getId() == pegawai.getId():
                print("Id pegawai sudah terdaftar")
                return
            
        self.__daftarPegawai.append(pegawai)
        print("Berhasil ditambahkan")

    def tampilPegawai(self):
        if not self.__daftarPegawai:
            print("Pegawai tidak ditemukan")
            return
        
        for p in self.__daftarPegawai:
            p.showDetails()
            print('\n')

    def findPegawai(self, searchId):
        for s in self.__daftarPegawai:
            if s.getId() == searchId:
                s.showDetails()
                return
            print("Pegawai tidak ditemukan")

    def delPegawai(self, Hapus):
        for h in self.__daftarPegawai:
            if h.getId() == Hapus:
                self.__daftarPegawai.remove(h)
                print("Pegawai berhasil dihapus")
                return  
        print("Pegawai tidak ditemukan")