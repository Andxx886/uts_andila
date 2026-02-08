import sys
from utils import *
from cli import *

def main():
    while True:
        clear_screen()
        tampilkan_menu()
        pilihan = input("\nPilihan: ")

        if pilihan == '1':
            try:
                n = float(input("Nilai Mahasiswa: "))
                print(f"Label: {konversi_nilai_ke_label(n)}")
            except ValueError:
                print("Error: Masukkan angka yang valid!")
            jeda_dan_kembali()

        elif pilihan == '2':
            l = input("Label Nilai Mahasiswa: ")
            print(f"Bobot: {konversi_label_ke_bobot(l)}")
            jeda_dan_kembali()

        elif pilihan in ['3', '4', '5']:
            try:
                jml = int(input("Jumlah Data: "))
                print("--------- Input SKS ---------")
                list_sks = [int(input(f"SKS {i+1}: ")) for i in range(jml)]
                t_sks = hitung_total_sks(list_sks)
                
                if pilihan == '3':
                    print(f"\nTotal SKS: {t_sks}")
                else:
                    print("\n--------- Input Nilai Mahasiswa ---------")
                    list_nilai = [float(input(f"Nilai {i+1}: ")) for i in range(jml)]
                    t_nilai = hitung_total_nilai(list_sks, list_nilai)
                    
                    if pilihan == '4':
                        print(f"\nTotal Nilai: {t_nilai}")
                    elif pilihan == '5':
                        ips = hitung_ips(t_nilai, t_sks)
                        print(f"\nIPS: {ips:.2f}")
            except ValueError:
                print("Error: Input harus berupa angka!")
            jeda_dan_kembali()

        elif pilihan == '6':
            print("Keluar dari Proyek 1. Sampai jumpa!")
            sys.exit() # Hanya di sini program benar-benar berhenti
        
        else:
            print("\nPilihan tidak valid!")
            jeda_dan_kembali()

if __name__ == "__main__":
    main()