class Pegawai:
    def __init__(self,nama,  tipe, idPegawai, gaji, jabatan, status, noHp):
        self.nama = nama
        self.tipe = tipe
        self.__idPegawai = idPegawai
        self.__gaji = gaji
        self.jabatan = jabatan
        self.status = status
        self.__noHp = noHp
        pass

    def getId(self): #Getter untuk id pegawai
        return self.__idPegawai
    def getGaji(self): #Getter untuk gaji
        return self.__gaji

    def showDetails(self):
        print('Nama: ', self.nama)
        print('Jenis: ', self.tipe)
        print('ID: ', self.__idPegawai)
        print('Gaji: ', self.__gaji)
        print('Jabatan: ', self.jabatan)
        print('Status: ', self.status)
        print('NO HP: ', self.__noHp)

    def checkStatus(self):
        if self.status == "Aktif":
            print("Pegawai masih aktif")
        else:
            print("Pegawai sudah tidak aktif")