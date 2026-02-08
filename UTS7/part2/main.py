import utils
import cli

def main():
    while True:
        cli.bersihkan_layar()
        cli.tampilkan_menu()
        pilih = cli.input_pilihan()

        if pilih == '1':
            plat, jenis, merk = cli.input_data_masuk()
            # Panggil fungsi dan simpan hasilnya (True/False)
            sukses = utils.kendaraan_masuk(plat, jenis, merk)
            
            if sukses:
                cli.pesan("berhasil menambahkan kendaraan")
            else:
                cli.pesan("plat sdh ada") # Notif sesuai permintaan Anda
            
            cli.jeda_enter()

        elif pilih == '2':
            plat = cli.input_plat_keluar()
            data = utils.kendaraan_keluar(plat)
            if data:
                cli.pesan(f"{data['plat']} {data['jenis']} {data['merk']}")
            else:
                cli.pesan("Kendaraan tidak ditemukan!")
            cli.jeda_enter()

        elif pilih == '3':
            data_parkir = utils.lihat_parkir()
            cli.tampilkan_daftar(data_parkir)
            cli.jeda_enter()

        elif pilih == '4':
            cli.pesan("Keluar dari program...")
            break

if __name__ == "__main__":
    main()