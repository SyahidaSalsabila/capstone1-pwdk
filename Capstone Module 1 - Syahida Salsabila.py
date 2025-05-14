#### Capstone Module 1 Syahida Lulu Salsabila ####

# Penyimpanan Data Pasien
DataPasien = [
     {
        "nama": "Rina",
        "umur": 25,
        "jenis_kelamin": "P",
        "diagnosa": "Demam",
        "no_rekam_medis": "RM001"
    },
    {
        "nama": "Dian",
        "umur": 30,
        "jenis_kelamin": "L",
        "diagnosa": "Asma",
        "no_rekam_medis": "RM002"
    },
    {
        "nama": "Dyren",
        "umur": 25,
        "jenis_kelamin": "L",
        "diagnosa": "Gerd",
        "no_rekam_medis": "RM003"
    },
    {
        "nama": "Sutsujin",
        "umur": 24,
        "jenis_kelamin": "L",
        "diagnosa": "Patah Tulang Kaki",
        "no_rekam_medis": "RM004"   
    },
    {
        "nama": "Vior",
        "umur": 26,
        "jenis_kelamin": "P",
        "diagnosa": "Gerd",
        "no_rekam_medis": "RM005"
    }
]

# Fungsi Create - Tambah Data Pasien
def generate_no_rekam_medis():
    nomor = len(DataPasien) + 1
    return f"RM{nomor:03d}"

def create_pasien():
    print("\n=== Tambah Pasien Baru ===")
    nama = input("Masukkan Nama Pasien: ")
    
    while True:
        umur = input("Masukkan Umur Pasien: ")
        if umur.isdigit():
            umur = int(umur)
            break
        else:
            print("Umur harus berupa angka. Coba lagi.")

    while True:
        jenis_kelamin = input("Masukkan Jenis Kelamin (L/P): ").upper()
        if jenis_kelamin in ["L", "P"]:
            break
        else:
            print("Jenis kelamin harus 'L' atau 'P'.")

    diagnosa = input("Masukkan Diagnosa Penyakit: ")
    no_rekam_medis = generate_no_rekam_medis()  # Dibuat otomatis

    pasien = {
        "nama": nama,
        "umur": umur,
        "jenis_kelamin": jenis_kelamin,
        "diagnosa": diagnosa,
        "no_rekam_medis": no_rekam_medis
    }
    DataPasien.append(pasien)
    print(f"Pasien {nama} berhasil ditambahkan dengan No. Rekam Medis: {no_rekam_medis}")

# Fungsi Read - Tampilkan Semua Data Pasien
def read_pasien():
    print("\n=== Daftar Data Pasien ===")
    if DataPasien: 
        for i, pasien in enumerate(DataPasien, start=1):
            print(f"\nPasien {i}:")
            print(f"Nama: {pasien['nama']}")
            print(f"Umur: {pasien['umur']}")
            print(f"Jenis Kelamin: {pasien['jenis_kelamin']}")
            print(f"Diagnosa: {pasien['diagnosa']}")
            print(f"No Rekam Medis: {pasien['no_rekam_medis']}")
    else:  
        print("Belum ada data pasien.")

# Fungsi Filter
def filter_pasien():
    print("\n=== Filter Data Pasien ===")
    print("1. Cari berdasarkan Nama")
    print("2. Cari berdasarkan Nomor Rekam Medis")
    print("3. Cari berdasarkan Jenis Kelamin")
    print("4. Cari berdasarkan Diagnosa")

    pilihan = input("Pilih filter (1/2/3/4): ")

    hasil = [] 

    if pilihan == "1":
        keyword = input("Masukkan Nama: ").lower() 
        for pasien in DataPasien:
            if keyword in pasien['nama'].lower():  
                hasil.append(pasien)  
    elif pilihan == "2":
        keyword = input("Masukkan Nomor Rekam Medis: ").upper()  
        for pasien in DataPasien:
            if keyword == pasien['no_rekam_medis']: 
                hasil.append(pasien) 
    elif pilihan == "3":
        keyword = input("Masukkan Jenis Kelamin (L/P): ").upper()
        for pasien in DataPasien:
            if keyword == pasien['jenis_kelamin']:  
                hasil.append(pasien)
    elif pilihan == "4":  
        keyword = input("Masukkan Diagnosa: ").lower()  
        for pasien in DataPasien:
            if keyword in pasien['diagnosa'].lower(): 
                hasil.append(pasien)  
    else:
        print("Pilihan tidak valid.")
        return

    if hasil:
        print(f"\nDitemukan {len(hasil)} pasien:")
        for i, pasien in enumerate(hasil, start=1):
            print(f"\nPasien ke-{i}")
            print(f"  Nama           : {pasien['nama']}")
            print(f"  Umur           : {pasien['umur']} tahun")
            print(f"  Jenis Kelamin  : {'Laki-laki' if pasien['jenis_kelamin'] == 'L' else 'Perempuan'}")
            print(f"  Diagnosa       : {pasien['diagnosa']}")
            print(f"  No Rekam Medis : {pasien['no_rekam_medis']}")
    else:
        print("Tidak ditemukan data pasien sesuai filter.")

# Fungsi Update - Ubah Data Pasien
def update_pasien():
    read_pasien()
    if not DataPasien:
        return

    index_input = input("\nMasukkan nomor pasien yang ingin diubah: ")
    
    if index_input.isdigit():
        index = int(index_input) - 1
        
        if 0 <= index < len(DataPasien):
            print(f"Data pasien saat ini: {DataPasien[index]}")
            
            nama = input("Masukkan Nama Baru (kosongkan jika tidak diubah): ")
            umur = input("Masukkan Umur Baru (kosongkan jika tidak diubah): ")
            jenis_kelamin = input("Masukkan Jenis Kelamin Baru (kosongkan jika tidak diubah): ")
            diagnosa = input("Masukkan Diagnosa Baru (kosongkan jika tidak diubah): ")
            no_rekam_medis = input("Masukkan No Rekam Medis Baru (kosongkan jika tidak diubah): ")
            
            if nama:
                DataPasien[index]['nama'] = nama
            if umur:
                if umur.isdigit():
                    DataPasien[index]['umur'] = int(umur)
                else:
                    print("Umur harus berupa angka.")
            if jenis_kelamin:
                if jenis_kelamin in ["L", "P"]:
                    DataPasien[index]['jenis_kelamin'] = jenis_kelamin
                else:
                    print("Jenis kelamin harus 'L' atau 'P'.")
            if diagnosa:
                DataPasien[index]['diagnosa'] = diagnosa
            if no_rekam_medis:
                DataPasien[index]['no_rekam_medis'] = no_rekam_medis

            print("Data pasien berhasil diperbarui.")
        else:
            print("Nomor pasien tidak valid.")
    else:
        print("Masukkan angka yang valid untuk nomor pasien.")

# Fungsi Delete - Hapus Data Pasien
def delete_pasien():
    read_pasien()
    if not DataPasien:
        return
    
    index_input = input("\nMasukkan nomor pasien yang ingin dihapus: ")
    
    if index_input.isdigit():
        index = int(index_input) - 1
        if 0 <= index < len(DataPasien):
            pasien_terhapus = DataPasien.pop(index)
            print(f"Data pasien {pasien_terhapus['nama']} berhasil dihapus.")
        else:
            print("Nomor pasien tidak valid.")
    else:
        print("Masukkan angka yang valid.")

# Menu Utama
def main():
    while True:
        print("\n=== Data Pasien Rumah Sakit Bandung ===")
        print("1. Tambah Pasien Baru")
        print("2. Lihat Data Pasien")
        print("3. Filter Data Pasien")
        print("4. Ubah Data Pasien")
        print("5. Hapus Data Pasien")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            create_pasien()
        elif pilihan == "2":
            read_pasien()
        elif pilihan == "3":
            filter_pasien()
        elif pilihan == "4":
            update_pasien()
        elif pilihan == "5":
            delete_pasien()
        elif pilihan == "6":
            print("Terima Kasih, Semoga sehat selalu!")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka 1-6.")

if __name__ == "__main__":
    main()
