def tampilkan_menu_utama():
    print("---------- MENU UTAMA ----------")
    print("1. Biodata")
    print("2. SKS")
    print("3. Input Nilai")
    print("4. Lihat Nilai")
    print("5. Lihat IP")
    print("6. Keluar")
    print("-----------------------------------")

def header_seksi(judul):
    print(f"\n=== {judul} ===")

def jeda_dan_kembali():
    """Menahan program agar user bisa melihat hasil sebelum kembali ke menu"""
    input("\nKlik Enter untuk kembali ke menu...")