def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def overlap(A,B,err):
    kalimat1=A.split(' ')
    kalimat2=B.split(' ')
    up=len(intersection(kalimat1,kalimat2))
    do=min(len(kalimat1),len(kalimat2))
    hasil = (up/do)*100
    err_percent = 100-hasil
    if err == 0:
        return {
            "check_oc": hasil,
            "err_percent": err_percent 
        }
    else:
        err_correction = ((err-err_percent)/err)*100
        return {
            "check_oc": hasil,
            "err_percent": err_percent,
            "err_correction": err_correction 
        }
