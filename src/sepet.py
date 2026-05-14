class Sepet:
    def __init__(self, kullanici_turu):
        self.urunler = []
        self.kullanici_turu = kullanici_turu  

    def urun_ekle(self, urun_adi, fiyat, adet):
        self.urunler.append({"ad": urun_adi, "fiyat": fiyat, "adet": adet})

    def toplam_hesapla(self):
        toplam = 0
        for urun in self.urunler:
            toplam += urun["fiyat"] * urun["adet"]

        if self.kullanici_turu == "uye":
            toplam = toplam * 0.90 
        elif self.kullanici_turu == "premium":
            toplam = toplam * 0.80 
        else:
            pass 

        if toplam > 500:
            toplam = toplam - 50  
        
        if toplam > 1000:
            toplam = toplam * 0.95  

        return toplam

    def bildirim_gonder(self, iletisim):
        if "@" in iletisim:
            print(f"Email gonderildi: {iletisim} -> Siparisıniz alindi! Toplam: {self.toplam_hesapla()} TL")
        elif iletisim.startswith("05"):
            print(f"SMS gonderildi: {iletisim} -> Siparisıniz alindi!")
        else:
            print("Gecersiz iletisim bilgisi")

    def rapor_yazdir(self):
        print("===== SEPET RAPORU =====")
        for urun in self.urunler:
            print(f"{urun['ad']} x{urun['adet']} - {urun['fiyat']} TL")
        print(f"TOPLAM: {self.toplam_hesapla()} TL")
        if self.kullanici_turu == "premium":
            print("Uygulanan indirim: %20")
        elif self.kullanici_turu == "uye":
            print("Uygulanan indirim: %10")
        else:
            print("Indirim uygulanmadi")

sepet1 = Sepet("premium")
sepet1.urun_ekle("Laptop", 800, 1)
sepet1.urun_ekle("Mouse", 150, 2)
sepet1.bildirim_gonder("dilara@gmail.com")
sepet1.rapor_yazdir()

sepet2 = Sepet("normal")
sepet2.urun_ekle("Klavye", 300, 1)
sepet2.rapor_yazdir()