NMax = 120
Mark = False
# recursive function : Len, Append, Remove, 
def Tail(arrayLama):
    arrayBaru = [None for i in range(NMax)]
    for i in range(1, NMax):
        if arrayLama[i] != None:
            arrayBaru[i-1] = arrayLama[i]
        else:
            break
    return arrayBaru

def Len(arr):
    if arr[0] == Mark:
        return 0
    return Len(Tail(arr)) if (arr[0] == None) else 1+Len(Tail(arr))

# per array an
def Append(arr, elm, i=0):
    if arr[i] == Mark:
        arr[i] = elm; arr[i+1] = Mark; return arr
    elif arr[i] == None:
        arr[i] = elm; return arr
    return Append(arr, elm, i+1)

class user:
    def __init__(self, username : str, password : str, role : str):
        self.username = username
        self.password = password
        self.role = role
class candi:
    def __init__(self, id : int, pembuat : str, pasir : int, batu : int, air : int):
        self.id = id
        self.pembuat = pembuat
        self.pasir = pasir
        self.batu = batu
        self.air = air
class bahan_bangunan:
    def __init__(self, nama : str, deskripsi : str, jumlah : int):
        self.nama = nama
        self.deskripsi = deskripsi
        self.jumlah = jumlah

def convertuser(csv = "user.csv"):
    arrayBaru = [None for i in range(NMax)]; arrayBaru[0] = Mark
    a = None; b = None; c = None
    fileYangDibaca = open(csv); k=0; l=0; count = 0
    for line in fileYangDibaca:
        if count == 0:
            count += 1
        else:
            stringYangDiappend = ""
            for i in range(len(line)):
                if i != len(line)-1:
                    if line[i+1] == "\n" or line[i+1] == ";":
                        stringYangDiappend += line[i]
                        if k == 0:
                            a = stringYangDiappend
                            k+=1
                        elif k == 1:
                            b = stringYangDiappend
                            k+=1
                        else:
                            c = stringYangDiappend
                            Append(arrayBaru, user(a,b,c))
                            k = 0
                        stringYangDiappend = ""
                    elif line[i] != ";": 
                        stringYangDiappend += line[i]
    return arrayBaru

def convertbb(csv = "bahan_bangunan.csv"):
    arrayBaru = [None for i in range(NMax)]; arrayBaru[0] = Mark
    a = None; b = None; c = None; d = True
    fileYangDibaca = open(csv); k=0; count=0
    for line in fileYangDibaca:
        if count == 0:
            count += 1
        else:
            stringYangDiappend = ""
            for i in range(len(line)):
                if i != len(line)-1:
                    if line[i+1] == "\n" or line[i+1] == ";":
                        stringYangDiappend += line[i]
                        if k == 0:
                            a = stringYangDiappend
                            k+=1
                        elif k == 1:
                            b = stringYangDiappend
                            k+=1
                        else:
                            c = int(stringYangDiappend)
                            Append(arrayBaru, bahan_bangunan(a, b, c))
                            k = 0
                        stringYangDiappend = ""
                    elif line[i] != ";": 
                        stringYangDiappend += line[i]
    return arrayBaru

def convertcandi(csv = "candi.csv"):
    arrayBaru = [None for i in range(NMax)]; arrayBaru[0] = Mark
    a = None; b = None; c = None; d = None; e = None
    fileYangDibaca = open(csv); k=0; m=0
    for line in fileYangDibaca:
        if m == 0:
            m += 1
        else:
            stringYangDiappend = ""
            for i in range(len(line)):
                if i != len(line)-1:
                    if line[i+1] == "\n" or line[i+1] == ";":
                        stringYangDiappend += line[i]
                        if k == 0:
                            a = int(stringYangDiappend)
                            k+=1
                        elif k == 1:
                            b = stringYangDiappend
                            k+=1
                        elif k == 2:
                            c = int(stringYangDiappend)
                            k += 1
                        elif k == 3:
                            d = int(stringYangDiappend)
                            k += 1
                        else:
                            e = int(stringYangDiappend)
                            Append(arrayBaru, candi(a, b, c, d, e))
                            k = 0
                        stringYangDiappend = ""
                    elif line[i] != ";": 
                        stringYangDiappend += line[i]
    return arrayBaru
