import sys
from utils import clear_screen, konversi_nilai_ke_label, konversi_label_ke_bobot
from cli import *

# Variabel global untuk menyimpan data selama program berjalan
data_mahasiswa = {
    "nama": "",
    "nim": "",
    "list_sks": [],
    "list_nilai": [],
    "list_matkul": []
}

def main():
    while True:
        clear_screen()
        tampilkan_menu_utama()
        pilihan = input("Pilihan: ")

        if pilihan == '1':
            header_seksi("INPUT BIODATA")
            data_mahasiswa["nama"] = input("Masukkan Nama: ")
            data_mahasiswa["nim"] = input("Masukkan NIM : ")
            print("\nBiodata berhasil disimpan!")
            jeda_dan_kembali()

        elif pilihan == '2':
            header_seksi("INPUT SKS")
            try:
                jumlah = int(input("Jumlah Mata Kuliah: "))
                data_mahasiswa["list_sks"] = []
                for i in range(jumlah):
                    sks = int(input(f"SKS Mata Kuliah {i+1}: "))
                    data_mahasiswa["list_sks"].append(sks)
                print("\nData SKS berhasil disimpan!")
            except ValueError:
                print("\nError: Masukkan angka yang valid untuk jumlah/sks!")
            jeda_dan_kembali()

        elif pilihan == '3':
            header_seksi("INPUT NILAI & MATKUL")
            if not data_mahasiswa["list_sks"]:
                print("Error: Isi data SKS (Menu 2) terlebih dahulu!")
            else:
                data_mahasiswa["list_nilai"] = []
                data_mahasiswa["list_matkul"] = []
                for i in range(len(data_mahasiswa["list_sks"])):
                    matkul = input(f"Nama Mata Kuliah {i+1}: ")
                    try:
                        nilai = float(input(f"Nilai Angka untuk {matkul}: "))
                        data_mahasiswa["list_matkul"].append(matkul)
                        data_mahasiswa["list_nilai"].append(nilai)
                    except ValueError:
                        print("Error: Nilai harus angka. Data matkul ini dilewati.")
                print("\ninput nilai selesai!")
            jeda_dan_kembali()

        elif pilihan == '4':
            header_seksi("DAFTAR NILAI")
            if not data_mahasiswa["list_matkul"]:
                print("Data masih kosong! Silakan isi biodata dan nilai dulu.")
            else:
                print(f"Nama: {data_mahasiswa['nama']} ({data_mahasiswa['nim']})")
                print("-" * 40)
                print(f"{'Mata Kuliah':<20} | {'Nilai':<6} | {'Label'}")
                print("-" * 40)
                for i in range(len(data_mahasiswa["list_matkul"])):
                    nilai_angka = data_mahasiswa["list_nilai"][i]
                    label = konversi_nilai_ke_label(nilai_angka)
                    print(f"{data_mahasiswa['list_matkul'][i]:<20} | {nilai_angka:<6} | {label}")
            jeda_dan_kembali()

        elif pilihan == '5':
            header_seksi("HASIL IP")
            total_sks = sum(data_mahasiswa["list_sks"])
            total_poin = 0
            if total_sks == 0 or not data_mahasiswa["list_nilai"]:
                print("Data SKS atau Nilai belum diisi!")
            else:
                for i in range(len(data_mahasiswa["list_sks"])):
                    label = konversi_nilai_ke_label(data_mahasiswa["list_nilai"][i])
                    bobot = konversi_label_ke_bobot(label)
                    total_poin += (bobot * data_mahasiswa["list_sks"][i])
                
                ip = total_poin / total_sks
                print(f"Nama      : {data_mahasiswa['nama']}")
                print(f"Total SKS : {total_sks}")
                print(f"IP Anda   : {ip:.2f}")
            jeda_dan_kembali()

        elif pilihan == '6':
            print("\nKeluar dari Program. Terima kasih!")
            sys.exit()
        
        else:
            print("\nPilihan tidak valid!")
            jeda_dan_kembali()

if __name__ == "__main__":
    main()