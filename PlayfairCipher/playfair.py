"""
untuk key = 'PERGI NGAMPUS'
jadiin per 2 huruf
    n = 2
    for index in range(0, len(enkriptxt), n):
        decchar.append(enkriptxt[index:index+n])
    
    for item in plainsplit:
    if len(item) > 2:
        splitchar(plainsplit)

"""

def splitchar(plaintxt):
    plaintxt = plaintxt.upper().replace('J', 'I')
    n = 2
    index = 0
    bigram = []
    newText = ""
    newText = plaintxt.replace(" ", "")
    
    while index < len(newText):
        if index + 1 < len(newText) and newText[index] == newText[index + 1]:
            bigram.append(newText[index] + 'Z')
            #bigram.append(newText[index+1:index+3])
            index = index+1
            #print('if: ',bigram)
        else:
            bigram.append(newText[index:index+n])
            index = index+2
            #print('else: ',bigram)

    if len(bigram[-1]) != 2:
        bigram[-1] = bigram[-1] + 'Z'
    
    newstring = "".join(bigram)
    #print(newstring)

    return bigram #return ini brarti kek dari fungsi ini yg diambil yang mana

def kunci():
    #i = row j = column
    matrix = []
    pfcipher = ['P','E','R','G','I','N','A','M','U','S','B','C','D','F','H','K','L','O','Q','T','V','W','X','Y','Z']

    for i in range(5):
        a = []
        for j in range(5):
            value = pfcipher.pop(0)
            a.append(value)
            #print(value)
        matrix.append(a)
        #print(a)
    print("Matriks Kunci :")
    for i in range(5):
        for j in range(5):
            #pfkey = matrix[i][j]
            #print(pfkey, end=" ")
            print(matrix[i][j], end=" ")
        print()
    return matrix

def findpos(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return (i, j)

def enkripsi(ciphertxt, key):
    enkriptxt = ""
    for pair in ciphertxt:
        char1 = pair[0]
        char2 = pair[1]
        
        char1pos = findpos(key, char1)
        char2pos = findpos(key, char2)

        if char1pos[0] == char2pos[0]:
            enkriptxt = enkriptxt + key[char1pos[0]][(char1pos[1] + 1) % 5]
            enkriptxt = enkriptxt + key[char2pos[0]][(char2pos[1] + 1) % 5]
        elif char1pos[1] == char2pos[1]:
            enkriptxt = enkriptxt + key[(char1pos[0] + 1) % 5][char1pos[1]]
            enkriptxt = enkriptxt + key[(char2pos[0] + 1) % 5][char2pos[1]]
        else:
            enkriptxt = enkriptxt + key[char1pos[0]][char2pos[1]]
            enkriptxt = enkriptxt + key[char2pos[0]][char1pos[1]]
    return enkriptxt

print("Playfair Cipher Enkripsi")
plain = input("Input Plaintext: ")
plainsplit = splitchar(plain)
print('Cipher Text  : ', plainsplit)
enkrips = enkripsi(plainsplit, kunci())
print('Enkripsi Text: ', enkrips)
