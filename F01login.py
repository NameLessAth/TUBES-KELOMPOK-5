import FungsiUtama

def login():
    
    userlist = FungsiUtama.convertuser()
    userInArr = False
    notLogin = True
    
    perintah = input("Masukkan command yang akan dijalankan! : ")
    
    while(perintah != "login"):
        print(f"{perintah} gagal!")
        print("Anda belum login, silakan login terlebih dahulu dengan menginput 'login'!")
        perintah = input("Masukkan command yang akan dijalankan! : ")
        
    while(notLogin):
        uname = input("Username: ")
        passw = input("Password: ")
        
        userInArr = False
        
        i = 0
        while (i < FungsiUtama.NMax):
            role = []
            if (userlist[i] == FungsiUtama.Mark):
                break
            else:
                if (uname == userlist[i].username):
                    if (passw == userlist[i].password):
                        print(f"Selamat datang, {uname}!")
                        print("Masukkan command 'help' untuk daftar command yang dapat kamu panggil.")
                        userInArr = True
                        notLogin = False
                        role = userlist[i].role
                        break
                    else:
                        print("Password salah! ")
                        userInArr = True
                        role = userlist[i].role
                        break
            i += 1       
            
        if (userInArr == False):
            print("Username tidak terdaftar! ")
            notLogin = True
            role = []
    
    if (notLogin == False):
        perintah2 = input("Masukkan command yang akan dijalankan! : ")
        if (perintah2 == "login"):
            print("Login gagal!")
            print(f"Anda telah login dengan username {uname}, silakan lakukan 'logout' sebelum melakukan login kembali!")

login()