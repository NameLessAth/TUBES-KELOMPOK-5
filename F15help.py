from FungsiUtama import *

def Help(Uname : str, Role : str):
    # jika user sudah login sebelumnya
    if Role != None:
        # fungsi help ketika bandung bondowoso yang mengakses
        if Role == "bandung_bondowoso":
            print(f"""=========== HELP ===========
1. logout
    Perintah ini berguna untuk keluar dari akun
2. summonjin
    Perintah ini berfungsi untuk memanggil jin, dan akan dimasukkan ke list dari user
3. hapusjin
    Perintah ini berfungsi untuk menghapus jin yang telah ada dari list user, dan juga menghapus seluruh candi yang telah dibuat oleh jin tersebut jika jin tersebut mempunyai role jin_pembangun.
4. ubahjin
    Perintah ini berfungsi untuk mengubah tipe jin dari tipe pembangun ke pengumpul, dan berlaku sebaliknya.
5. batchkumpul
    Perintah ini berfungsi untuk memanggil seluruh jin pengumpul, kemudian menyuruh mereka untuk mengumpulkan bahan bersamaan.
6. batchbangun
    Perintah ini berfungsi untuk memanggil seluruh jin pembangun, kemudian menyuruh mereka membangun bersamaan, bila bahan tidak mencukupi, semua pembangunan akan dibatalkan.
7. laporanjin
    Perintah ini berfungsi untuk mendapatkan laporan tentang jumlah jin (baik masing-masing jenis maupun total), jin termalas (jin yang membangun candi paling sedikit), jin terajin (jin yang membangun candi paling banyak), dan juga jumlah bahan saat ini yang dipunyai.
8. laporancandi
    Perintah ini berfungsi untuk mendapatkan laporan tentang jumlah candi, total bahan yang digunakan masing-masing, candi termahal, dan candi termurah.
9. save
    Perintah ini berfungsi untuk menyimpan progress sekarang di folder yang diinput
10. help
    Perintah ini berfungsi untuk mengeluarkan help, yang sedang anda akses sekarang.
11. exit
    Perintah ini berfungsi untuk keluar dari program, sebelum keluar, perintah akan mengverifikasi apakah hendak disave terlebih dahulu progressnya?.
=========== SELAMAT BERMAIN, BANG BANDUNG! ===========""")
            
        # fungsi help ketika Roro Jonggrang mengakses
        elif Role == "roro_jonggrang":
            print(f"""=========== HELP ===========
1. logout
    Perintah ini berguna untuk keluar dari akun
2. hancurkancandi
    Perintah ini berfungsi untuk menghancurkan candi dengan ID yang akan diinput.
3. ayamberkokok
    Perintah ini berfungsi untuk menyelesaikan game, bila candi yang telah dibuat Bandung dan para Jin mencapai 100, maka Bandung menang dan anda akan menikah dengan Bandung. Akan tetapi jika candi yang dibuat Bandung dan para Jin belum mencapai 100, maka anda memenangkan game dan anda tidak jadi menikahi Bandung.
4. save
    Perintah ini berfungsi untuk menyimpan progress sekarang di folder yang diinput
5. help
    Perintah ini berfungsi untuk mengeluarkan help, yang sedang anda akses sekarang.
6. exit
    Perintah ini berfungsi untuk keluar dari program, sebelum keluar, perintah akan mengverifikasi apakah hendak disave terlebih dahulu progressnya?.
=========== SELAMAT BERMAIN, TEH RORO JONGGRANG! ===========""")
        
        # fungsi help ketika Jin Pembangun mengakses
        elif Role == "jin_pembangun":
            print(f"""=========== HELP ===========
1. logout
    Perintah ini berguna untuk keluar dari akun
2. bangun
    Perintah ini berfungsi untuk membangun candi dengan ID terkecil yang kosong, dan juga akan memakan bahan sesuai RNG yang didapat. SEMANGAT MENGULI BANG JIN PEMBANGUN!!
3. save
    Perintah ini berfungsi untuk menyimpan progress sekarang di folder yang diinput
4. help
    Perintah ini berfungsi untuk mengeluarkan help, yang sedang anda akses sekarang.
5. exit
    Perintah ini berfungsi untuk keluar dari program, sebelum keluar, perintah akan mengverifikasi apakah hendak disave terlebih dahulu progressnya?.
=========== SELAMAT MENGULI, {Uname}! ===========""")
        
        # fungsi help ketika Jin Pengumpul mengakses
        else:
            print(f"""=========== HELP ===========
1. logout
    Perintah ini berguna untuk keluar dari akun
2. kumpul
    Perintah ini berfungsi untuk mengumpulkan bahan2 bangunan dengan RNG 0-5. Yok bisa menguli yok.
3. save
    Perintah ini berfungsi untuk menyimpan progress sekarang di folder yang diinput
4. help
    Perintah ini berfungsi untuk mengeluarkan help, yang sedang anda akses sekarang.
5. exit
    Perintah ini berfungsi untuk keluar dari program, sebelum keluar, perintah akan mengverifikasi apakah hendak disave terlebih dahulu progressnya?.
=========== SELAMAT MENGULI, {Uname}! ===========""")
    
    else:
        # minimal login boyyy
        print(f"""=========== HELP ===========
1. login
    Perintah ini berguna untuk masuk ke akun tertentu dengan username dan password yang cocok dan tersedia.
2. help
    Perintah ini berfungsi untuk mengeluarkan help, yang sedang anda akses sekarang.
3. exit
    Perintah ini berfungsi untuk keluar dari program, sebelum keluar, perintah akan mengverifikasi apakah hendak disave terlebih dahulu progressnya?.
=========== SELAMAT BERMAIN- , EH LOGIN DULU BANG! ===========""")
