from pegawai import Pegawai

class PegawaiTetap(Pegawai):
    def __init__(self, nama,  tipe, idPegawai, gaji, jabatan, status, noHp, masaKerja, jatahCuti, danaPensiun):
        super().__init__(nama, tipe, idPegawai, gaji, jabatan, status, noHp)

        self.__masaKerja = masaKerja
        self.__jatahCuti = jatahCuti
        self.__danaPensiun = danaPensiun

    def getMasaKerja(self):
        return self.__masaKerja
    def getCuti(self):
        return self.__jatahCuti
    def getDanaPensiun(self):
        return self.__danaPensiun