from FungsiUtama import *

def Save(userlist : list, candilist : list, bahanlist : list):

    # meminta tujuan folder 
    folderTujuan = input("Masukkan nama folder: ")
    directory = "save/"+folderTujuan

    # printing format
    print("\nsaving...\n")

    # mengecek apakah parent folder save/ sudah ada atau belum
    if not os.path.isdir("save"):
        os.mkdir("save")
        print(f"Membuat parent folder save...")

    # mengecek apakah folder yang diinginkan sudah ada atau belum
    if not os.path.isdir(directory):
        os.mkdir(directory)
        print(f"Membuat folder {directory}...\n")
    
    # user
    # formatting menjadi seperti csv sebelumnya
    stringuser = "username;password;role\n"; i = 0
    while (i < NMax):
        if userlist[i] != None:
            stringuser += f"{userlist[i].username};{userlist[i].password};{userlist[i].role}"
        if userlist[i+1] != Mark:
            stringuser += "\n"
        else:
            break
        i += 1
    # save ke csv
    userfile = open(directory+"/user.csv", "w")
    userfile.write(stringuser)

    # candi
    # formatting menjadi seperti csv sebelumnya
    stringcandi = "id;pembuat;pasir;batu;air\n"; i = 0
    while (i < NMax):
        if candilist[i] != None:
                stringcandi += f"{candilist[i].id};{candilist[i].pembuat};{candilist[i].pasir};{candilist[i].batu};{candilist[i].air}"
        if candilist[i+1] != Mark:
            stringcandi += "\n"
        else:
            break
        i += 1
    # save ke csv
    candifile = open(directory+"/candi.csv", "w")
    candifile.write(stringcandi)

    # bahan bangunan
    # formatting menjadi seperti csv sebelumnya
    stringbahan = "nama;deskripsi;jumlah\n"; i = 0
    while (i < NMax):
        if bahanlist[i] != None:
            stringbahan += f"{bahanlist[i].nama};{bahanlist[i].deskripsi};{bahanlist[i].jumlah}"
        if bahanlist[i+1] != Mark:
            stringbahan += "\n"
        else:
            break
        i += 1
    # save ke csv
    bahanfile = open(directory+"/bahan_bangunan.csv", "w")
    bahanfile.write(stringbahan)

    # close semua file
    userfile.close; candifile.close; bahanfile.close
    print(f"save berhasil dilakukan di folder {directory}")    
