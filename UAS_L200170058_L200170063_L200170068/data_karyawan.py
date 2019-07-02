class data_karyawan(object):
    
    """class data untuk karyawan"""
    
    def __init__(self, NIP, nama_karyawan, jabatan):
        self.nip = NIP
        self.pegawai = nama_karyawan
        self.Jabatan = jabatan

    def __repr__(self):
        info = self.NIP + ', ' + self.pegawai + ', ' + self.Jabatan
        return info

    def __str__(self):
        info = self.NIP + ', ' + self.pegawai + ', ' + self.Jabatan
        return info

class my_Array(object):
    
    """class untuk Array pada data Karyawan"""

    def __init__(self):
        self.index = 10 * [None]
        
    def __getitem__(self, item):
        getData = self.index[item]
        return getData
    
    def __setitem__(self, key, value):
        self.index[key] = value



karyawan_1 = data_karyawan('7005',
                   'Abizar Bima',
                   'OB')
karyawan_2 = data_karyawan('7001',
                   'Aladin Santoso',
                   'OB')
karyawan_3 = data_karyawan('7004',
                   'Bonjofi firdaus',
                   'Dokter')
karyawan_4 = data_karyawan('7003',
                   'Dani Cebalos',
                   'Dokter')
karyawan_5 = data_karyawan('7002',
                   'Fahri Antama',
                   'Dokter')
karyawan_6 = data_karyawan('7010',
                   'Kenny Galon',
                   'Suster')
karyawan_7 = data_karyawan('7006',
                   'Ardito Pranomo',
                   'Dokter')
karyawan_8 = data_karyawan('7008',
                   'Jayanto',
                   'Apoteker')
karyawan_9 = data_karyawan('7007',
                   'Kento Momota',
                   'Apoteker')
karyawan_10 = data_karyawan('7009',
                   'Lin Dan',
                   'Kasir')


akumulasi_data_final = my_Array()

akumulasi_data_final[0] = [karyawan_1.nip, karyawan_1.pegawai, karyawan_1.Jabatan]
akumulasi_data_final[1] = [karyawan_2.nip, karyawan_2.pegawai, karyawan_2.Jabatan]
akumulasi_data_final[2] = [karyawan_3.nip, karyawan_3.pegawai, karyawan_3.Jabatan]
akumulasi_data_final[3] = [karyawan_4.nip, karyawan_4.pegawai, karyawan_4.Jabatan]
akumulasi_data_final[4] = [karyawan_5.nip, karyawan_5.pegawai, karyawan_5.Jabatan]
akumulasi_data_final[5] = [karyawan_6.nip, karyawan_6.pegawai, karyawan_6.Jabatan]
akumulasi_data_final[6] = [karyawan_7.nip, karyawan_7.pegawai, karyawan_7.Jabatan]
akumulasi_data_final[7] = [karyawan_8.nip, karyawan_8.pegawai, karyawan_8.Jabatan]
akumulasi_data_final[8] = [karyawan_9.nip, karyawan_9.pegawai, karyawan_9.Jabatan]
akumulasi_data_final[9] = [karyawan_10.nip, karyawan_10.pegawai, karyawan_10.Jabatan]



data_final = [akumulasi_data_final[0], akumulasi_data_final[1],
              akumulasi_data_final[2], akumulasi_data_final[3],
              akumulasi_data_final[4], akumulasi_data_final[5],
              akumulasi_data_final[6], akumulasi_data_final[7],
              akumulasi_data_final[8], akumulasi_data_final[9]]
