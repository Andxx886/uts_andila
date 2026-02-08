# List untuk menyimpan data kendaraan
daftar_kendaraan = []

def kendaraan_masuk(plat, jenis, merk):
    # CEK APAKAH PLAT SUDAH ADA
    for k in daftar_kendaraan:
        if k['plat'] == plat:
            return False # Kembalikan False jika ditemukan plat yang sama
    
    # Jika tidak ada yang sama, baru tambahkan
    kendaraan = {"plat": plat, "jenis": jenis, "merk": merk}
    daftar_kendaraan.append(kendaraan)
    return True # Kembalikan True jika berhasil

def kendaraan_keluar(plat):
    for i, kendaraan in enumerate(daftar_kendaraan):
        if kendaraan['plat'] == plat:
            return daftar_kendaraan.pop(i)
    return None

def lihat_parkir():
    return daftar_kendaraan