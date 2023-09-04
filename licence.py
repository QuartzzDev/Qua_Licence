# QuartzzDev <3


import string
import random
import quaLib

quaLib.RedPrint("Qua Licence")
choice = int(input("""
[1] - Anahtar Oluştur 
[2] - Anahtar Sorgula """))

def CheckKey(key_to_check):
    with open('key.txt', 'r') as f:
        existing_keys = f.read().splitlines()

    if key_to_check in existing_keys:
        quaLib.CyanPrint("Anahtar Kabul Edildi . . .")
    else:
        quaLib.RedPrint("Anahtar Kabul Edilmedi . . .")

def CreateRandomKey():
    key = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(25))

    with open('key.txt', 'a') as f:
        if f.tell() != 0:
            f.write('\n')
        f.write(key)


if choice == 1:
    reqKey = int(input("Kaç tane anahtar eklensin : "))
    for i in range(reqKey):
        CreateRandomKey()
    quaLib.BluePrint("Anahtarlar Eklendi . . .")
elif choice == 2:
    userKey = input("Anahtarı Giriniz : ")
    CheckKey(userKey)
else:
    quaLib.RedPrint("Yanlış Giriş Yaptınız .")

    
    

