from abc import ABC, abstractmethod

class SepetBase(ABC):
    def __init__(self):
        self.urunler = []

    def urun_ekle(self, urun_adi, fiyat, adet):
        self.urunler.append({"ad": urun_adi, "fiyat": fiyat, "adet": adet})

    def ara_toplam(self):
        toplam = 0
        for urun in self.urunler:
            toplam += urun["fiyat"] * urun["adet"]
        return toplam

    @abstractmethod
    def indirim_uygula(self, toplam):
        pass

    @abstractmethod
    def kullanici_turu(self):
        pass

    def toplam_hesapla(self):
        ara = self.ara_toplam()
        return self.indirim_uygula(ara)

    def rapor_yazdir(self):
        print("===== SEPET RAPORU =====")
        for urun in self.urunler:
            print(f"{urun['ad']} x{urun['adet']} - {urun['fiyat']} TL")
        print(f"Ara Toplam : {self.ara_toplam()} TL")
        print(f"Genel Toplam: {self.toplam_hesapla()} TL")
        print(f"Kullanici Turu: {self.kullanici_turu()}")

class NormalSepet(SepetBase):
    def indirim_uygula(self, toplam):
        return toplam  

    def kullanici_turu(self):
        return "Normal Musteri"


class uyeSepet(SepetBase):
    def indirim_uygula(self, toplam):
        return toplam * 0.90  

    def kullanici_turu(self):
        return "Uye Musteri (%10 indirim)"


class PremiumSepet(SepetBase):
    def indirim_uygula(self, toplam):
        return toplam * 0.80  

    def kullanici_turu(self):
        return "Premium Musteri (%20 indirim)"

class SepetFabrikasi:
    @staticmethod
    def sepet_olustur(kullanici_turu):
        if kullanici_turu == "normal":
            return NormalSepet()
        elif kullanici_turu == "uye":
            return uyeSepet()
        elif kullanici_turu == "premium":
            return PremiumSepet()
        else:
            raise ValueError(f"Bilinmeyen kullanici turu: {kullanici_turu}")

if __name__ == "__main__":
    sepet1 = SepetFabrikasi.sepet_olustur("premium")
    sepet1.urun_ekle("Laptop", 800, 1)
    sepet1.urun_ekle("Mouse", 150, 2)
    sepet1.rapor_yazdir()

    print()

    sepet2 = SepetFabrikasi.sepet_olustur("uye")
    sepet2.urun_ekle("Klavye", 300, 1)
    sepet2.rapor_yazdir()