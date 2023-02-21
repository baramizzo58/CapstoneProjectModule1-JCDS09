# List Daftar Menu
daftar_menu = [
    '1. Menampilkan Data Yellow Pages',
    '2. Menambah Data Yellow Pages',
    '3. Mengupdate Data Yellow Pages',
    '4. Menghapus Data Yellow Pages',
    '5. Exit'
]

# List kontak dalam Yellow Pages
daftar_kontak = [
    {'indeks': 'a-001', 'nama' : 'Adisad', 'no_hp' : 6281234567890, 'kota' : 'Solo', 'zip_code' : 57144},
    {'indeks': 'a-002', 'nama' : 'Anik', 'no_hp' : 6281098765432, 'kota' : 'Sukoharjo', 'zip_code' : 57562},
    {'indeks': 'b-001', 'nama' : 'Budari', 'no_hp' : 6281325476980, 'kota' : 'Boyolali', 'zip_code' : 57384},
    {'indeks': 'b-002', 'nama' : 'Budi', 'no_hp' : 6281111111111, 'kota' : 'Karanganyar', 'zip_code' : 57762},
    {'indeks': 'b-003', 'nama' : 'Budimeister', 'no_hp' : 6282222222222, 'kota' : 'Klaten', 'zip_code' : 57464},
    {'indeks': 'c-001', 'nama' : 'Cacuk', 'no_hp' : 6283333333333, 'kota' : 'Wonogiri', 'zip_code' : 57695}
]

# Menu Utama
def menu_utama():
    while True:
        print('\n*************SELAMAT DATANG DI YELLOW PAGES PURWADHIKA*************')
        for i in daftar_menu:
            print(i)
        option = input ("\nSilahkan Pilih Menu (1-5):\n")
        if (option == '1'):
            read_data()
        elif (option == '2'):
            create_data()
        elif (option == '3'):
            update_data()
        elif (option == '4'):
            delete_data()
        elif (option == '5'):
            print('\nThank you and good bye!\n')
            quit()
        else:
            print('\nOpsi menu tidak tersedia, silahkan input angka 1-5\n')
            menu_utama()

# Menu Read Data
def read_data():
    while True:
        print('\n*************MENU 1: MENAMPILKAN DATA YELLOW PAGES*************')
        print('1. Menampilkan seluruh data')
        print('2. Menampilkan data tertentu')
        print('3. Kembali ke Menu Utama\n')
        option = input ("Silahkan pilih sub-menu (1-3):\n")
        if (option == '1'):
            if (len(daftar_kontak) != 0):
                print ('\nBerikut seluruh Data Kontak:')
                for i,j in enumerate(daftar_kontak):
                    print(f"{i+1}. Indeks: {j['indeks']}, Nama: {j['nama']}, No HP: {j['no_hp']}, Kota: {j['kota']}, ZIP Code: {j['zip_code']}")
            else: 
                print ('\nTidak ada data')
            read_data()
        elif (option == '2'):
            if (len(daftar_kontak) != 0):
                cari_indeks = input("\nSilakan input indeks yang dicari:\n").lower()
                checker = False
                for i,j in enumerate(daftar_kontak):
                    if (cari_indeks == daftar_kontak[i]['indeks']):
                        print ('\nBerikut hasil pencarian kontak:')
                        print(f"{i+1}. Indeks: {j['indeks']}, Nama: {j['nama']}, No HP: {j['no_hp']}, Kota: {j['kota']}, ZIP Code: {j['zip_code']}")
                        checker = True
                        break
                if (checker == False):
                    print ('\nTidak ada data')
            else:
                print ('\nTidak ada data')
            read_data()
        elif (option == '3'):
            menu_utama()
        else:
            read_data()

# Menu Create Data
def create_data():
    while True:
        print('\n*************MENU 2: MENAMBAHKAN DATA YELLOW PAGES*************')
        print('1. Menambahkan data kontak')
        print('2. Kembali ke Menu Utama\n')
        option = input ("Silahkan pilih sub-menu (1-2):\n")
        if (option == '1'):
            indeks_kontak = input ('\nSilahkan input indeks kontak: \n').lower()
            checker = False
            for i in range(len(daftar_kontak)):
                if (indeks_kontak == daftar_kontak[i]['indeks']):
                    print ('\nData sudah ada')
                    checker = True
                    break
            if (checker == False):
                tambah_nama = input ('\nSilahkan input Nama: \n').title()
                tambah_no_hp = input ('\nSilahkan input No HP: \n')
                tambah_kota = input ('\nSilahkan input Kota: \n').title()
                tambah_zip_code = input ('\nSilahkan input ZIP code: \n')
                while True:
                    simpan = input('\nApakah data akan disimpan? (yes/no): \n').lower()
                    if (simpan == 'yes'):
                        daftar_kontak.append(
                            {
                                'indeks': indeks_kontak,
                                'nama': tambah_nama,
                                'no_hp': tambah_no_hp,
                                'kota': tambah_kota,
                                'zip_code': tambah_zip_code
                            }
                        )
                        print ('\nData saved')
                        break
                    elif (simpan == 'no'):
                        print("\nData not saved")
                        break
            create_data()
        elif (option == '2'):
            menu_utama()
        else:
            create_data()

# Menu Update Data
def update_data():
    while True:
        print('\n*************MENU 3: MENGUPDATE DATA YELLOW PAGES*************')
        print('1. Mengupdate data kontak')
        print('2. Kembali ke Menu Utama\n')
        option = input ("Silahkan pilih sub-menu (1-2):\n")
        if (option == '1'):
            indeks_kontak = input('\nSilahkan input indeks kontak yang akan diupdate:\n').lower()
            checker = False
            for i,j in enumerate(daftar_kontak):
                if (indeks_kontak == daftar_kontak[i]['indeks']):
                    print ('\nData kontak yang akan di update:')
                    print(f"{i+1}. Indeks: {j['indeks']}, Nama: {j['nama']}, No HP: {j['no_hp']}, Kota: {j['kota']}, ZIP Code: {j['zip_code']}")
                    while True:
                        option_update = input ("\nApakah data akan diupdate (yes/no):\n").lower()
                        if (option_update =='yes'):
                            while True:
                                option_update = input('\nSilahkan input kolom yang akan diupdate (nama/no_hp/kota/zip_code):\n')
                                if (option_update == 'nama'):
                                    nama_update = input('\nSilahkan input Nama yang baru:\n').capitalize()
                                    while True:
                                        option_nama = input('\nApakah data akan diupdate? (yes/no):\n').lower()
                                        if (option_nama == 'yes'):
                                            daftar_kontak[i][option_update] = nama_update
                                            print ("\nData updated\n")
                                            break
                                        elif (option_nama == 'no'):
                                            print("\nData not updated\n")
                                            break
                                    update_data()
                                elif (option_update == 'no_hp'):
                                    no_hp_update = input('\nSilahkan input Nomor HP yang baru:\n')
                                    while True:
                                        option_no_hp = input('\nApakah data akan diupdate? (yes/no):\n').lower()
                                        if (option_no_hp == 'yes'):
                                            daftar_kontak[i][option_update] = no_hp_update
                                            print ("\nData updated\n")
                                            break
                                        elif (option_no_hp == 'no'):
                                            print("\nData not updated\n")
                                            break
                                    update_data()
                                elif (option_update == 'kota'):
                                    kota_update = input ('\nSilahkan input Kota yang baru:\n').title()
                                    while True:
                                        option_kota = input('\nApakah data akan diupdate? (yes/no):\n').lower()
                                        if (option_kota == 'yes'):
                                            daftar_kontak[i][option_update] = kota_update
                                            print ("\nData updated\n")
                                            break
                                        elif (option_kota == 'no'):
                                            print("\nData not updated\n")
                                            break
                                    update_data()
                                elif (option_update == 'zip_code'):
                                    zip_code_update = input('\nSilahkan input ZIP Code yang baru:\n').lower()
                                    while True:
                                        option_zip_code = input('\nApakah data akan diupdate? (yes/no):\n').lower()
                                        if (option_zip_code == 'yes'):
                                            daftar_kontak[i][option_update] = zip_code_update
                                            print ("\nData updated\n")
                                            break
                                        elif (option_zip_code == 'no'):
                                            print("\nData not updated\n")
                                            break
                                    update_data()
                        elif(option_update =='no'):
                            update_data()
                            break
                    checker = True
            if (checker == False):
                print ('\nData yang anda cari tidak ada\n')
                update_data()
        elif option == '2':
            menu_utama()
        else:
            update_data()

# Menu Delete Data
def delete_data():
    while True:
        print('\n*************MENU 4: MENGHAPUS DATA YELLOW PAGES*************')
        print('1. Menghapus data kontak')
        print('2. Kembali ke Menu Utama\n')
        option = input ("Silahkan pilih sub-menu (1-2):\n")
        if (option == '1'):
            indeks_kontak = input ('\nSilahkan input indeks kontak yang akan dihapus:\n').lower()
            checker = False
            for i in range(len(daftar_kontak)):
                if (indeks_kontak == daftar_kontak[i]['indeks']):
                    while True:
                        cek = input ("\nApakah data akan dihapus (yes/no):\n").lower()
                        if (cek =='yes'):
                            del daftar_kontak[i]
                            print ("\nData deleted")
                            break
                        elif (cek == 'no'):
                            print ("\nData not deleted")
                            break
                    checker = True
                    break
            if (checker == False):
                print ("\nData yang anda cari tidak ada")
            delete_data()
        elif (option == '2'):
            menu_utama()
        else:
            delete_data()

# Memanggil Fungsi
menu_utama()