_kartSifre=1234
_bakiye=500
sifre_sayac=3
login=False
while True:
    if login==False:
        sifre=int(input("Şifrenizi Giriniz: "))
    if sifre==_kartSifre:
        login=True
        print("""
1. Para Çek
2. Para Yatır
3. Bakiye Sorgulama
4. Kart İade          
          """)
        secim=int(input("Yapacağınız işlemi seçiniz: "))
        if secim==1:
            miktar=int(input("Çekilecek tutarı giriniz: "))
            if _bakiye<miktar:
                print("Yetersiz bakiye!")
                continue       
            _bakiye-=miktar
        elif secim==2:
            miktar=int(input("Yatırılacak miktarı belirleyiniz: "))
            _bakiye+=miktar
        elif secim==3:
            print("Bakiyeniz {} TL ".format(_bakiye))
        elif secim==4:
            print("İyi günler.")
            break
        else:
                  print("Yapacağınız işlemi seçiniz: ")
    else:
        sifre_sayac-=1
        if sifre_sayac <=0:
            print("Şifrenizi yanlış girdiniz.")
            break