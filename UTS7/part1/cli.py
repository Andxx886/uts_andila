# cli.py
import os

def bersihkan_layar():
    # Perintah menghapus teks di terminal Windows (cls) atau Mac/Linux (clear)
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_menu():
    print("1. Tambah Antrian")
    print("2. Panggil Antrian")
    print("3. Lihat Antrian")
    print("4. Keluar")

def input_pilihan():
    return input("Pilihan : ")

def input_nama():
    return input("Nama : ")

def tampilkan_daftar(daftar):
    if not daftar:
        print("Tidak ada antrian")
    else:
        print("Daftar antrian")
        for i, nama in enumerate(daftar, 1):
            print(f"{i}. {nama}")

def jeda_enter():
    # Menahan layar agar user bisa melihat output (seperti daftar antrian)
    input("\n")