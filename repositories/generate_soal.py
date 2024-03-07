import random
from repositories.modclass import pakai
text = []
modulstr = ["capital","uppercase","lowercase","csfold","swap"]
modulstrvalue = ["center()",]
modullist = ["append()","copy()","extend()","pop()","insert()","remove()"]

def splitlinefile(text):
    classes = text.rstrip('\n').rsplit('\n')
    return classes

def splitspace(textsplitline):
    split = []
    for i in range(len(textsplitline)):
        x = textsplitline[i]
        x = x.rsplit(' ')
        split.append(x)
    return split

def restoretext(x):
    hasil=[]
    for i in range(len(x)):
        rmline = (' '.join(e for e in x[i]))
        hasil.append(rmline+"\n")
    return ''.join(hasil)

def randomvaluex(list):
    randomx=[]
    i=0
    while i < len(list):
        x=random.randint(0,len(list)-1)
        if x not in randomx:
            randomx.append(x)
            i += 1
    return randomx

def randomvaluey(list,rdmx):
    randomy = []
    index = []
    i=0
    j=0
    while i < len(list):
        while j < len(list[rdmx[i]]):
            z = len(list[rdmx[i]])
            y=random.randint(0,z-1)
            if y not in index:
                index.append(y)
                j += 1
        randomy.append(index)
        index = []
        j=0
        i += 1
    return randomy


def mkerr(list,idx,rdmx,rdmy):
    j=0
    k=0
    index = 0
    while j > -1:
        for k in range(len(rdmx)):
            if index < idx:
                if j > len(rdmy[k])-1:
                    #print("continue")
                    continue
                else:
                    a=rdmx[k]
                    b=rdmy[k][j]
                    if list[a][b] == "":
                        continue
                    else:
                        list[a][b] = pakai(modulstr[random.randint(0,4)])(list[a][b])
                        #print(list[a][b])
                        index += 1
                        #print("index = ",index)
            else:
                j = -2
        j += 1
        k=0




def run(textsoal,err_idx):
    text = splitlinefile(textsoal)
    hasil = splitspace(text)
    valx = randomvaluex(hasil)
    valy = randomvaluey(hasil,valx)
    mkerr(hasil,err_idx,valx,valy)
    #writefile(hasil)
    generate = restoretext(hasil)
    return generate
