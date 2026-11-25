from pegawai import Pegawai
from departemen import Departemen
from pegawaitetap import PegawaiTetap
from pegawaikontrak import PegawaiKontrak

departemenKreatif = Departemen("Departemen Kreatif", "Gedung Utara", "Pak Sonny")
P1 = PegawaiTetap("Jhon", "Tetap", "KT01", "Rp.4,500,000", "Senior Artist", "Aktif", "11111", "10 Tahun", "3", "Ada")
departemenKreatif.tambahPegawai(P1)

#************** Tampilan menu dan program utama supaya bisa dijalankan *************************************
while True:
    print('\n')
    print("==== Menu ====")
    print(" 1.) tambah data \n 2.) Tampilkan Pegawai \n 3.) Cari Data \n 4.) Hapus Data \n 5.) Keluar")
    uInput = int(input(">_ "))

############## Tambah Data Pegawai #####################
    if uInput == 1:
        print("Masukkan data")
        nama = input("Nama: ")
        tipe = input("Tipe: ")
        idP = input("ID: ")
        gaji = input("Gaji: ")
        jbn = input("Jabatan: ")
        stat = "Aktif"
        phone = input("No. HP: ")

        jenis = int(input("1.) Pekerja tetap \n2.) Pekerja kontrak? \n>_"))
        if jenis == 1:
            duration = input("Masa kerja: ")
            cuti = input("Cuti")
            danaPensiun = input("Dana Pensiun: ")
            tetap = PegawaiTetap(nama, tipe, idP, gaji, jbn, stat, phone, duration, cuti, danaPensiun)
            departemenKreatif.tambahPegawai(tetap)
        elif jenis == 2:
             durationK = input("Durasi kontrak: ")
             project = input("Proeject: ")
             endDate = input("Tangal Berakhir: ")
             kontrak = PegawaiKontrak(nama, tipe, idP, gaji, jbn, stat, phone, durationK, project, endDate)
             departemenKreatif.tambahPegawai(kontrak)
        else:
            print("Input tidak valid")

############### tampil semua pegawai di departemen ##################
    elif uInput == 2:
        departemenKreatif.tampilPegawai()

############### Search Pegawai ######################################
    elif uInput == 3:
        search = input("Masukkan ID: ")
        departemenKreatif.findPegawai(search)

############## Menghapus Pegawai ####################################
    elif uInput == 4:
        delete = input("Masukkan ID: ")
        departemenKreatif.delPegawai(delete)

############# Keluar Program ########################################
    elif uInput == 5:
        break