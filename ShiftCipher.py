"""
Nama    : Bandana Irmal Abdillah
NPM     : 140810180025
Kelas   : A
Kriptografi - Shift Cipher
"""

def listToString(s): 
    str1 = ""
    for element in s:
        str1 += element

    return str1

def Encrypt(kata, k):
    plain_text = []
    encrypted_number = []
    encrypted_text = []

    for i in kata:
        huruf = ord(i) - 97
        plain_text.append(huruf)
        
    for i in range(0,len(plain_text)):
        x = plain_text[i]
        y = (x + k) % 26
        encrypted_number.append(y)
        # print(encrypted_number)
        
    for i in range(0,len(encrypted_number)):
        huruf2 = chr(encrypted_number[i]+97) 
        encrypted_text.append(huruf2)
        # print(encrypted_text)
    
    # print(encrypted_text)
    kata = listToString(encrypted_text)
    #print("encrypted : " + listToString(encrypted_text))
    return kata
    
    

def Decrypt(kata, k):
    plain_text = []
    decrypted_number = []
    encrypted_text = []
    
    print("ciper text : " + kata)
    for i in kata:
        huruf = ord(i) - 97
        encrypted_text.append(huruf)
        
    for i in range(0,len(encrypted_text)):
        x = encrypted_text[i]
        y = (x - k) % 26
        decrypted_number.append(y)
        # print(decrypted_number)
        
    for i in range(0,len(decrypted_number)):
        huruf2 = chr(decrypted_number[i]+97) 
        plain_text.append(huruf2)
        # print(plain_text)
    
    # print(plain_text)
    #print("decrypted : " + listToString(plain_text))
    kata = listToString(plain_text)
    return kata

print("Shift Cipher")
text = input("Input Kata :")
k = int(input("Input K :"))
print("plain text : " + text)

#Encrypt(text, k)
text = Encrypt(text, k)
print("Setelah proses enkripsi : "+ text)
text = Decrypt(text, k)  
print("Setelah proses dekripsi : " + text)


