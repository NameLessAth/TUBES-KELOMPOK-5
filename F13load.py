from FungsiUtama import *

def Load():

    parser = argparse.ArgumentParser()
    parser.add_argument("folder", type=str, help="membuka folder tertentu dan meng-load di path tersebut")
    args = parser.parse_args().folder

    # ketika argparse argument nya kosong (ex: python main.py, tanpa argparse)
    if args == None:
        print("Tidak ada argument folder yang diberikan!")
        exit()

    # ketika tidak menemukan folder yang ditemukan
    if not os.path.isdir(args):
        print(f"tidak ada folder dengan nama {args}!")
        exit()

    # ketika ketemu
    else:
        userlist = convertuser(args+"/user.csv")
        candilist = convertcandi(args+"/candi.csv")
        bahanbangunanlist = convertbb(args+"/bahan_bangunan.csv")

        # kreativitas, kalau di notal gausah gpp, animasi loading
        listLoading = "|/-\\"
        i = 0
        while i != 20:
            print(listLoading[i % 4] + " Loading " + listLoading[i % 4], end="\r")
            i += 1
            time.sleep(0.1)
        print("selamat datang di permainan!")
        time.sleep(0.1)
