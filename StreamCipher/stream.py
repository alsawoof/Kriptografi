import binascii
#untuk ubah teks ke biner ascii
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

def xor(bin1, bin2, n):
    enkrip = ""
    for i in range(n):
        if(bin1[i]==bin2[i]):
            enkrip = enkrip+"0"
        else:
            enkrip = enkrip+"1"
    return enkrip

print("MENU")
print("1. Enkripsi Stream Cipher")
print("2. Dekripsi Stream Cipher")
print("3. Enkripsi ECB")
print("4. Dekripsi ECB")
print("5. Enkripsi CBC")
#print("5. Enkripsi CFB")
#print("6. Dekripsi CBC")
#print("8. Dekripsi CFB")
menu = input("Input nomor menu yang dipilih: ")
if menu == "1":
    txt = input('Input Plaintext: ')
    bittxt = text_to_bits(txt)

    lst = list()
    for i in range(0, len(bittxt), 8): #untuk slicing plaintext binary per 8 char 
        binchar = bittxt[i:i+8]
        #print(binchar)
        lst.append(binchar)
    print("Biner Plaintext: ", " ". join(lst))

    key = input('Input Kunci dalam biner: ')
    #print('Kunci: ',key)

    n = len(bittxt)
    keybin = key * (n // len(key)) + key[:n % len(key)] #untuk perulangan kunci sesuai dengan panjang biner
    #print(keybin)
    stream = xor(bittxt, keybin, n)
    print("Hasil Enkripsi Stream Cipher: ",stream)

elif menu == "2":
    dekrip = input("Input Ciphertext dalam biner: ")
    kunci = input("Input kunci: ")

    p = len(dekrip)
    kunbin = kunci * (p // len(kunci)) + kunci[:p % len(kunci)]

    streamdekrip = xor(dekrip, kunbin, p)
    print("Hasil Dekripsi Stream Cipher: ", streamdekrip)
    plaindekrip = text_from_bits(streamdekrip)
    print("Plain Text: ",plaindekrip)

elif menu == "3":
    txt = input('Input Plaintext: ')
    bittxt = text_to_bits(txt)
    #print(bittxt)

    lst = list()
    for i in range(0, len(bittxt), 8): #untuk slicing plaintext binary per 8 char 
        binchar = bittxt[i:i+8]
        #print(binchar)
        lst.append(binchar)
    print("Biner Plaintext: ", " ". join(lst))

    key = input('Input Kunci dalam biner: ')
    #print('Kunci: ',key)

    n = len(bittxt)
    keybin = key * (n // len(key)) + key[:n % len(key)] #untuk perulangan kunci sesuai dengan panjang biner
    #print(keybin)
    stream = xor(bittxt, keybin, n)
    print("Hasil XOR: ", stream)
    #print("\nLoop wrapping: ")

    lstecb = list()
    for i in range(0, len(stream), 4): #untuk slicing hasil xor binary per 4 char 
        binchar4 = stream[i:i+4]
        #print(binchar4)
        ecb = binchar4[1:]+binchar4[:1]
        #print("Hasil wrap: ", ecb)
        lstecb.append(ecb)
    print("\nHasil ECB:")
    print(" ". join(lstecb))

elif menu == "4":
    txt = input('Input Ciphertext dalam biner: ')
    key = input('Input Kunci dalam biner: ')
    
    #print('\nLoop Unwrap: ')
    lstecb = list()
    for i in range(0, len(txt), 4): #untuk slicing hasil xor binary per 4 char 
        binchar4 = txt[i:i+4]
        #print(binchar4)
        ecb = binchar4[-1]+binchar4[:-1]
        #print("Unwrap: ", ecb)
        lstecb.append(ecb)
    
    unw = "".join(lstecb)
    print("\nHasil Unwrap      : ", unw)
    
    n = len(unw)
    keybin = key * (n // len(key)) + key[:n % len(key)] #untuk perulangan kunci sesuai dengan panjang biner
    #print(keybin)
    stream = xor(unw, keybin, n)
    print("Hasil Dekripsi ECB: ", stream)
    
    text = text_from_bits(stream)
    print("Plaintext         : ", text)

elif menu == "5":
    txt = input('Input Plaintext: ')
    bittxt = text_to_bits(txt)

    lst = list()
    for i in range(0, len(bittxt), 4): #untuk slicing plaintext binary per 4 char 
        binchar4 = bittxt[i:i+4]
        #print(binchar4)
        lst.append(binchar4)
    print("Biner Plaintext: ", " ". join(lst))
    print()

    key = input('Input Kunci dalam biner: ')
    #print('Kunci: ',key)
    iv = input('Input IV: ')
    print()

    #print("Loop wrapping: ")
    wraplist = list()
    for i in range(len(lst)):
        xorc1 = xor(lst[i], iv, 4)
        #print("Hasil C1: ", xorc1)
        xorkey = xor(xorc1, key, 4)
        #print("Hasil XOR dengan Key: ", xorkey)
        wrap = xorkey[1:]+xorkey[:1]
        #print("Hasil Wrap: ", wrap)
        iv = wrap
        wraplist.append(wrap)
    
    #print()
    print("Hasil cipher: ", " ".join(wraplist))

else:
    print("Nomor tidak ada pada opsi")