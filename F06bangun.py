from FungsiUtama import *

def Bangun(candilist : list, bahanlist : list, uname : str, role : str) -> tuple[list, list]:
    # verifikasi role (jin pembangun)
    if role == "jin_pembangun":

        # generate bahan yang dibutuhkan
        batuDibutuhkan = RNG(1, 5); pasirDibutuhkan = RNG(1, 5); airDibutuhkan = RNG(1, 5)
        # verifikasi apakah bahan mencukupi
        if bahanlist[0].jumlah >= pasirDibutuhkan and bahanlist[1].jumlah >= batuDibutuhkan and bahanlist[2].jumlah >= airDibutuhkan:
            bahanlist[0].jumlah -= pasirDibutuhkan
            bahanlist[1].jumlah -= batuDibutuhkan
            bahanlist[2].jumlah -= airDibutuhkan

            # mencari ID candi yang kosong
            # juga kasus ketika candi masih belum 100
            if LenSejati(candilist) != 100:
                i = 0
                while(i < NMax):
                    
                    # jika candi belum 100
                    # ternyata ID kosong di Mark
                    if candilist[i] == Mark:
                        AppendMark(candilist, candi(i, uname, pasirDibutuhkan, batuDibutuhkan, airDibutuhkan))
                        print(f"Sisa candi yang perlu dibangun : {100-LenSejati(candilist)}")
                        return candilist, bahanlist
                    
                    # ID kosong di tengah dan bukan di Mark
                    elif candilist[i] == None:
                        Append(candilist, candi(i+1, uname, pasirDibutuhkan, batuDibutuhkan, airDibutuhkan))
                        print(f"Sisa candi yang perlu dibangun : {100-LenSejati(candilist)}")
                        return candilist, bahanlist
                
                    i += 1
            else:
                print(f"Sisa candi yang perlu dibangun : 0")
        
        # apabila bahan tidak mencukupi
        else:
            print(f"""Bahan bangunan tidak mencukupi.
Candi tidak bisa dibangun!""")
            
    # yang mengakses bukan jin pembangun
    else:
        print(f"perintah hanya bisa diakses oleh akun jin pembangun")
    
    return candilist, bahanlist


