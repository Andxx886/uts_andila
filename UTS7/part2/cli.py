import os

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_menu():
    print("1. Kendaraan Masuk")
    print("2. Kendaraan Keluar")
    print("3. Lihat Parkir")
    print("4. Keluar")

def input_pilihan():
    return input("Pilihan : ")

def input_data_masuk():
    plat = input("Plat  : ")
    jenis = input("Jenis : ")
    merk = input("Merk  : ")
    return plat, jenis, merk

def input_plat_keluar():
    return input("Plat Kendaraan : ")

def tampilkan_daftar(daftar):
    if not daftar:
        print("Parkiran Kosong")
    else:
        print("Daftar Parkir")
        for i, k in enumerate(daftar, 1):
            print(f"{i}. {k['plat']}")

def pesan(teks):
    print(teks)

def jeda_enter():
    input("\n")