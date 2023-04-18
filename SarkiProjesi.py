import sqlite3
import time
from datetime import datetime
from datetime import datetime, timedelta



class Sarki():
    
    def __init__(self, isim, sanatci, albüm, prodüksiyon, süresi):
        self.isim = isim
        self.sanatci = sanatci
        self.albüm = albüm
        self.prodüksiyon = prodüksiyon
        self.süresi = süresi
        
    def __str__(self):
        return "Şarkı ismi : {}\nSanatçı : {}\nAlbüm : {}\nProdüksiyon : {}\nSüresi : {}".format(self.isim, self.sanatci, self.albüm,self.prodüksiyon, self.süresi)
    
    
    
    
class Sarkilar():
    
    def __init__(self):
        self.baglanti_olustur()
    
    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect(r"C:\Users\oktay\Desktop\SQLite Veri Tabanı\Şarkı Projesi\Şarkı Projesi.db")
        self.cursor = self.baglanti.cursor()
        
        sorgu = "CREATE TABLE IF NOT EXISTS sarki_listesi (isim TEXT, sanatci TEXT, albüm TEXT, prodüksiyon TEXT, süresi TEXT)"
        
        self.cursor.execute(sorgu)
        self.baglanti.commit()
    
    def baglanti_kes(self):
        self.baglanti.close()
    
    def sarkilari_göster(self):
        sorgu = "SELECT * FROM sarki_listesi"
        self.cursor.execute(sorgu)
        sarkilar = self.cursor.fetchall()
        
        if len(sarkilar) == 0:
            print("Şarkı Listesi Boş...")
        else:
            for i in sarkilar:
                print("--------------------------------------")
                sarki = Sarki(i[0],i[1],i[2],i[3],i[4])
                print(sarki)
                print("--------------------------------------")
    
    def sarki_bul(self,isim):
        sorgu = "SELECT * FROM sarki_listesi WHERE isim = ?"
        self.cursor.execute(sorgu,(isim,))
        sarkilar = self.cursor.fetchall()
        if len(sarkilar) == 0:
            print("Böyle Bir Şarkı Bulunmuyor...")
        else:
            sarki = Sarki(sarkilar[0][0],sarkilar[0][1],sarkilar[0][2],sarkilar[0][3],sarkilar[0][4])
            print(sarki)
    
    def sarki_ekle(self,sarki):
        sorgu = "INSERT INTO sarki_listesi VALUES (?,?,?,?,?)"
        self.cursor.execute(sorgu,(sarki.isim,sarki.sanatci,sarki.albüm,sarki.prodüksiyon,sarki.süresi,))
        self.baglanti.commit()
        
    def sarki_sil(self, isim):
        sorgu = "SELECT * FROM sarki_listesi WHERE isim = ?"
        self.cursor.execute(sorgu, (isim,))
        sarkilar = self.cursor.fetchall()
        if len(sarkilar) == 0:
            print("Böyle bir şarkı bulunamadı.")
        else:
            sorgu = "DELETE FROM sarki_listesi WHERE isim = ?"
            self.cursor.execute(sorgu, (isim,))
            self.baglanti.commit()
            print("{} isimli şarkı başarıyla silindi.".format(isim))

    def toplam_sure(self):
        sorgu = "SELECT SUM(strftime('%s', süresi)) FROM sarki_listesi"
        self.cursor.execute(sorgu)
        toplam_sure = self.cursor.fetchone()[0]
        if toplam_sure is not None:
            toplam_sure = int(toplam_sure)
            dakika = toplam_sure // 60
            saniye = toplam_sure % 60
            saat = dakika // 60
            dakika = dakika % 60
            if saat > 0:
                print("Toplam Şarkı Süresi : {} saat {} dakika {} saniye".format(saat, dakika, saniye))
            else:
                print("Toplam Şarkı Süresi : {} dakika {} saniye".format(dakika, saniye))
        else:
            print("Şarkı Listesi Boş...")

    def sanatcinin_sarkilari(self,sanatci):
        sorgu = "SELECT * FROM sarki_listesi Where sanatci = ?"
        self.cursor.execute(sorgu,(sanatci,))
        liste = self.cursor.fetchall()
        if len(liste) == 0:
            print("Böyle Bir Sanatçı Bulunmuyor...")
        else:
            for i in liste:
                print(i)
    
    def prodüksiyon_sarkilari(self,prodüksiyon):
        sorgu = "SELECT * FROM sarki_listesi Where prodüksiyon = ?"
        self.cursor.execute(sorgu,(prodüksiyon,))
        liste = self.cursor.fetchall()
        if len(liste) == 0:
            print("Böyle Bir Prodüksiyon Bulunmuyor...")
        else:
            for i in liste:
                print(i)
    def sarki_listele(self):
        sorgu = "SELECT * FROM sarki_listesi"
        self.cursor.execute(sorgu)
        sarkilar = self.cursor.fetchall()

        print("Şarkılar Listesi:")
        print("{:<25} {:<20} {:<35} {:<35} {:<10}".format("Şarkı Adı", "Sanatçı", "Albüm", "Prodüksiyon", "Süre"))
        print("{:-<25} {:-<20} {:-<35} {:-<35} {:-<10}".format("", "", "", "", ""))

        toplam_sure = timedelta()

        for sarki in sarkilar:
            sarki_adi = sarki[0]
            sanatci = sarki[1]
            albüm = sarki[2]
            prodüksiyon = sarki[3]
            sarki_suresi = timedelta(minutes=int(sarki[4].split(':')[0]), seconds=int(sarki[4].split(':')[1]))

            print("{:<25} {:<20} {:<35} {:<35} {:<10}".format(sarki_adi, sanatci, albüm, prodüksiyon, str(sarki_suresi)))

            toplam_sure += sarki_suresi

        print("{:*<25} {:*<20} {:*<35} {:*<35} {:*<10}".format("", "", "", "", ""))
        print("{:<25} {:<20} {:<35} {:<35} {:<10}".format("Toplam süre:", "", "", "", str(toplam_sure)))




    def hata_bul(self):
        for sarki in self.cursor.execute("SELECT * FROM sarki_listesi"):
            print(type(sarki[0]))
            print(type(sarki[1]))
            print(type(sarki[2]))
            print(type(sarki[3]))
            print(type(sarki[4]))
            try:
                datetime.strptime(sarki[4], '%M:%S').strftime('%-M:%S')
            except ValueError:
                print(f"Invalid format for sarki_suresi in song '{sarki[1]}'")
       
    
    
    
    
