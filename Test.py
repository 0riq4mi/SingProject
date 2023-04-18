from SarkiProjesi import *


print("""================================
      
    Şarkı kütüphasnesine hoşgeldiniz...
    İşlemler;
    
    1- Şarkıları Göster  
      
    2- Şarkı Bul  
      
    3- Şarkı Ekle  
      
    4- Şarkı Sil  
    
    5- Sanatçının Şarkıları
    
    6- Prodüksiyonun Şarkıları
      
    7- Süre Listele  
       
================================""")

sarkilar = Sarkilar()

while True:
    islem = input("Yapacığınız İşlem : ")
    if islem == "q":
        print("Program Sonlandırılıyor...")
        print("Yine Bekleriz...")
        break
    elif islem == "1":
        sarkilar.sarkilari_göster()
    elif islem == "2":
        isim = input("Bulmak istedğiniz Şarkı İsmini Giriniz : ")
        print("Şarkı Aranıyor...")
        time.sleep(2)
        sarkilar.sarki_bul(isim)
    elif islem == "3":
        isim = input("Şarkı İsmi : ")
        sanatci = input("Sanatçı İsmi : ")
        albüm = input("Albüm İsmi : ")
        prodüksiyon = input("Prodüksiyon İsmi : ")
        süresi = input("Şarkı Süresi ('00:00' şeklinde giriniz.) : ")
        
        yeni_sarki = Sarki(isim, sanatci, albüm, prodüksiyon, süresi)
        print("Yeni Şarkı Ekleniyor...")
        time.sleep(2)
        sarkilar.sarki_ekle(yeni_sarki)
        print("Şarki Eklendi...")
    elif islem == "4":
        isim = input("Hangi Şarkıyı silmek istiyorsunuz ? :")
        cevap = input("Emin misiniz ? (E/H)")
        if cevap == "E" or cevap == "e":
            time.sleep(2)
            sarkilar.sarki_sil(isim)
    elif islem == "5":
        sanatci = input("Şarkılarını aradığınız sanatçinin ismini giriniz : ")
        print("Aranıyor...")
        time.sleep(2)
        sarkilar.sanatcinin_sarkilari(sanatci)
    elif islem == "6":
        prodüksiyon = input("Şarkılarını aradğınız prodüksiyonun ismini giriniz : ")
        print("Aranıyor...")
        time.sleep(2)
        sarkilar.prodüksiyon_sarkilari(prodüksiyon)
    elif islem == "7":
        print("Toplam Süre Hesaplanıyor...")
        time.sleep(2)
        sarkilar.sarki_listele()
    elif islem == "8":
        sarkilar.hata_bul()
    else:
        print("Hatalı Giriş!!!")
