import math
#Definisi Fungsi Cosine Similarity
def cosine_sim(vec1, vec2):
    vec1 = list(vec1)
    vec2 = list(vec2)
    dot_prod = 0
    for i, v in enumerate(vec1):
        dot_prod += v * vec2[i]
    mag_1 = math.sqrt(sum([x**2 for x in vec1]))
    mag_2 = math.sqrt(sum([x**2 for x in vec2]))
    return dot_prod / (mag_1 * mag_2)
#Pembentukan Vektor Bag Of Word
def check_CS(kalimat1, kalimat2, error_percent):
    cosineBoW=[]
    bagOfWordsA = kalimat1.split(' ')
    bagOfWordsB = kalimat2.split(' ')
    uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB))
    numOfWordsA = dict.fromkeys(uniqueWords, 0)
    for word in bagOfWordsA:
        numOfWordsA[word] += 1
    numOfWordsB = dict.fromkeys(uniqueWords, 0)
    for word in bagOfWordsB:
        numOfWordsB[word] += 1
    #Perhitungan Cosine Similarity
    hasil = cosine_sim(numOfWordsA.values(),numOfWordsB.values())
    hasil = hasil*100
    err_percent = 100-hasil
    if error_percent == 0:
        return {
            "check_cs":hasil,
            "err_percent":err_percent,
        }
    else:
        err_correction = ((error_percent-err_percent)/error_percent)*100
        return{
            "check_cs":hasil,
            "err_percent":err_percent,
            "err_correction":err_correction
        }
    
# print(check_CS(text1,text2,0))
