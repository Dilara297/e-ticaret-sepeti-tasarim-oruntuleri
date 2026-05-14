from fabrika import SepetBase, SepetFabrikasi


class SepetDekorator(SepetBase):
    def __init__(self, sepet: SepetBase):
        self._sepet = sepet

    def urun_ekle(self, urun_adi, fiyat, adet):
        self._sepet.urun_ekle(urun_adi, fiyat, adet)

    def ara_toplam(self):
        return self._sepet.ara_toplam()

    def indirim_uygula(self, toplam):
        return self._sepet.indirim_uygula(toplam)

    def kullanici_turu(self):
        return self._sepet.kullanici_turu()

    def toplam_hesapla(self):
        return self._sepet.toplam_hesapla()

    def rapor_yazdir(self):
        self._sepet.rapor_yazdir()

class HediyePaketiDekorator(SepetDekorator):
    HEDIYE_UCRETI = 25.0

    def toplam_hesapla(self):
        return self._sepet.toplam_hesapla() + self.HEDIYE_UCRETI

    def rapor_yazdir(self):
        self._sepet.rapor_yazdir()
        print(f"Hediye paketi        : +{self.HEDIYE_UCRETI} TL")
        print(f"Genel Toplam         : {self.toplam_hesapla()} TL")

class KargoDekorator(SepetDekorator):
    UCRETSIZ_KARGO_LIMITI = 300.0
    KARGO_UCRETI = 29.90

    def toplam_hesapla(self):
        ara = self._sepet.toplam_hesapla()
        if ara >= self.UCRETSIZ_KARGO_LIMITI:
            return ara
        return ara + self.KARGO_UCRETI

    def rapor_yazdir(self):
        self._sepet.rapor_yazdir()
        ara = self._sepet.toplam_hesapla()
        if ara >= self.UCRETSIZ_KARGO_LIMITI:
            print("Kargo                : Ucretsiz")
        else:
            print(f"Kargo                : +{self.KARGO_UCRETI} TL")
        print(f"Genel Toplam         : {self.toplam_hesapla()} TL")

if __name__ == "__main__":
    print("=== Sadece kargo ===")
    sepet = SepetFabrikasi.sepet_olustur("uye")
    sepet.urun_ekle("Laptop", 800, 1)
    sepet = KargoDekorator(sepet)
    sepet.rapor_yazdir()

    print()
    print("=== Kargo + hediye paketi ===")
    sepet2 = SepetFabrikasi.sepet_olustur("premium")
    sepet2.urun_ekle("Kulaklık", 150, 1)
    sepet2 = KargoDekorator(sepet2)
    sepet2 = HediyePaketiDekorator(sepet2)
    sepet2.rapor_yazdir()