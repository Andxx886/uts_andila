# utils.py

class QueueManager:
    def __init__(self):
        # Menyimpan data antrian dalam list
        self.antrian = []

    def tambah_antrian(self, nama):
        # Menambah data ke urutan paling belakang
        self.antrian.append(nama)

    def panggil_antrian(self):
        # Mengambil data dari urutan paling depan (index 0)
        if not self.antrian:
            return None
        return self.antrian.pop(0)

    def dapatkan_semua_antrian(self):
        # Mengembalikan list antrian saat ini
        return self.antrian