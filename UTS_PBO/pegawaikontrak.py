from pegawai import Pegawai

class PegawaiKontrak(Pegawai):
    def __init__(self, nama, tipe, idPegawai, gaji, jabatan, status, noHp, durasiKontrak, proyek, endTanggal):
        super().__init__(nama, tipe, idPegawai, gaji, jabatan, status, noHp)

        self.__durasiKontrak = durasiKontrak
        self.__proyek = proyek
        self.__endTanggal = endTanggal

    def getDurasiKontrak(self):
        return self.__durasiKontrak
    def getProyek(self):
        return self.__proyek
    def getBerakhir(self):
        return self.__endTanggal
        