NMax = 120
Mark = "MARK"
# recursive function : Len, Append, AppendMark


# per array an
def Tail(arrayLama):
    arrayBaru = [None for i in range(NMax)]
    for i in range(1, NMax):
        if arrayLama[i] != Mark:
            arrayBaru[i-1] = arrayLama[i]
        else:
            arrayBaru[i-1] = Mark
            break
    return arrayBaru

def Len(arr):
    if arr[0] == Mark:
        return 0
    return 1+Len(Tail(arr))

def Append(arr : list, elm : any, i=0) -> list:
    if arr[i] == Mark:
        arr[i] = elm; arr[i+1] = Mark; return arr
    elif arr[i] == None:
        arr[i] = elm; return arr
    return Append(arr, elm, i+1)

def AppendMark(arr : list, elm : any, i=0) -> list:
    if arr[i] == Mark:
        arr[i] = elm; arr[i+1] = Mark; return arr
    return AppendMark(arr, elm, i+1)

def Max(arr):
    maks = arr[0]
    for i in range(1, Len(arr)):
        if arr[i] > maks:
            maks = arr[i]
    return maks

def Min(arr):
    mini = arr[0]
    for i in range(1, Len(arr)):
        if arr[i] < mini:
            mini = arr[i]
    return mini
        

# compare string
def OrdChar(char):
    charlist = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in range(1, len(charlist)+1):
        if char == charlist[i-1]:
            return i

def CompareString(string1 : str, string2 : str) -> str :
    shorterstring = (lambda x, y : x if (len(x) <= len(y)) else y)(string1, string2)
    i = 0
    while i != len(shorterstring)-1 and string1[i] == string2[i]:
        i += 1
    if i == len(shorterstring)-1 and string1[i] == string2[i]:
        return shorterstring
    elif OrdChar(string1[i]) >= OrdChar(string2[i]):
        return string2
    else:
        return string1

# csv parser
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

def convertuser(csv : str = "user.csv") -> list :
    arrayBaru = [None for i in range(NMax)]; arrayBaru[0] = Mark
    a = None; b = None; c = None
    fileYangDibaca = open(csv); k=0; l=0; count = 0
    for line in fileYangDibaca:
        if count == 0:
            count += 1
        else:
            if line is not None and line != "\n" and line != "":
                stringYangDiappend = ""
                for i in range(len(line)):
                    if line[i] == "\n" or line[i] == ";" or i == len(line)-1:
                        if i == len(line)-1 and line[i] != "\n":
                            stringYangDiappend += line[i]
                        if k == 0:
                            a = stringYangDiappend
                            k+=1
                        elif k == 1:
                            b = stringYangDiappend
                            k+=1
                        else:
                            c = stringYangDiappend
                            AppendMark(arrayBaru, user(a,b,c))
                            k = 0
                        stringYangDiappend = ""
                    else: 
                        stringYangDiappend += line[i]
            else:
                AppendMark(arrayBaru, None)
    return arrayBaru

def convertbb(csv : str = "bahan_bangunan.csv") -> list :
    arrayBaru = [None for i in range(NMax)]; arrayBaru[0] = Mark
    a = None; b = None; c = None; d = True
    fileYangDibaca = open(csv); k=0; count=0
    for line in fileYangDibaca:
        if count == 0:
            count += 1
        else:
            if line is not None and line != "\n" and line != "":
                stringYangDiappend = ""
                for i in range(len(line)):
                    if line[i] == "\n" or line[i] == ";" or i == len(line)-1:
                        if i == len(line)-1 and line[i] != "\n":
                            stringYangDiappend += line[i]
                        if k == 0:
                            a = stringYangDiappend
                            k+=1
                        elif k == 1:
                            b = stringYangDiappend
                            k+=1
                        else:
                            c = int(stringYangDiappend)
                            AppendMark(arrayBaru, bahan_bangunan(a, b, c))
                            k = 0
                        stringYangDiappend = ""
                    else: 
                        stringYangDiappend += line[i]
            else:
                AppendMark(arrayBaru, None)
    return arrayBaru

def convertcandi(csv : str = "candi.csv") -> list :
    arrayBaru = [None for i in range(NMax)]; arrayBaru[0] = Mark
    a = None; b = None; c = None; d = None; e = None
    fileYangDibaca = open(csv); k=0; m=0
    for line in fileYangDibaca:
        if m == 0:
            m += 1
        else:
            if line is not None and line != "\n" and line != "":
                stringYangDiappend = ""
                for i in range(len(line)):
                    if line[i] == "\n" or line[i] == ";" or i == len(line)-1:
                        if i == len(line)-1 and line[i] != "\n":
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
                            AppendMark(arrayBaru, candi(a, b, c, d, e))
                            k = 0
                        stringYangDiappend = ""
                    else: 
                        stringYangDiappend += line[i]
            else:
                AppendMark(arrayBaru, None)
    return arrayBaru
