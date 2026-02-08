# main.py
from utils import QueueManager
import cli

def main():
    manager = QueueManager()

    while True:
        cli.bersihkan_layar()
        cli.tampilkan_menu()
        pilihan = cli.input_pilihan()

        if pilihan == '1':
            nama = cli.input_nama()
            manager.tambah_antrian(nama)
            # Opsional: Langsung kembali ke menu setelah input
        
        elif pilihan == '2':
            dipanggil = manager.panggil_antrian()
            if dipanggil:
                print(f"memanggil {dipanggil}")
            else:
                print("Tidak ada antrian")
            cli.jeda_enter() # Tahan layar untuk melihat siapa yang dipanggil
        
        elif pilihan == '3':
            # Menampilkan daftar antrian sesuai gambar Anda
            daftar = manager.dapatkan_semua_antrian()
            cli.tampilkan_daftar(daftar)
            cli.jeda_enter() # Tahan layar agar daftar tidak langsung hilang
        
        elif pilihan == '4':
            print("Keluar...")
            break
        
        else:
            print("Pilihan tidak tersedia!")
            cli.jeda_enter()

if __name__ == "__main__":
    main()