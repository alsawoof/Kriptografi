import random

hmcipher = {'A':(['BU','CP','AV','AH','BT','BS','CQ']),
'B':(['AT']),
'C':(['DL','BK','AU']),
'D':(['BV','DY','DM','AI']),
'E':(['DK','CO','AW','BL','AA','CR','BM','CS','AF','AG','BO','BN','BE']),
'F':(['BW','CM','CN']),
'G':(['DN','BJ']),
'H':(['AS','CL','CK']),
'I':(['DJ','BI','AX','CJ','AB','BP','CU','CT']),
'J':(['BX']),
'K':(['DI']),
'L':(['AR','BH','CI','AJ']),
'M':(['DH','BG','AY']),
'N':(['BY','DG','DF','CH','AC','BR','DU','DT']),
'O':(['DZ','BF','DX','AK','CG','BQ','DR']),
'P':(['BZ','DE','AZ']),
'Q':(['DD']),
'R':(['AQ','DC','DQ','AL','CE','CF','CV','DS']),
'S':(['AP','AN','AO','CD','DW','DV']),
'T':(['CB','DB','DP','CC','AD','CY','CW','CX','AE']),
'U':(['CA','AM','BA']),
'V':(['BB']),
'W':(['CZ']),
'X':(['BD']),
'Y':(['DO','DA']),
'Z':(['BC']),
' ':(['SD'])}

def enkripsitxt(plaintxt):
    enkripsi = ''
    for char in plaintxt:
        if char in hmcipher:
            hmvar = hmcipher[char]
            #print(hmvar)
            encrypt = random.choice(hmvar)
            enkripsi = enkripsi + encrypt
        else:
            enkripsi = enkripsi + char
    return enkripsi

def dekripsitxt(enkriptxt):
    dekripsi = ''
    decchar = []
    n = 2
    for index in range(0, len(enkriptxt), n):
        decchar.append(enkriptxt[index:index+n])
    for value in decchar:
        for key, values in hmcipher.items():
            if value in values:
                dekripsi = dekripsi + key
                break
    return dekripsi

#plain = 'HELLO WORLD'
plain = input('Input kalimat: ')
plainup = plain.upper()

enkripsi = enkripsitxt(plainup)
print('Plaintext     : ',plainup)
print('Hasil Enkripsi: ',enkripsi)

dekripsi = dekripsitxt(enkripsi)
print('Hasil Dekripsi: ',dekripsi)
