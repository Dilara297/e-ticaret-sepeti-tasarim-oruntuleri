from fabrika import SepetFabrikasi
from dekorator import KargoDekorator, HediyePaketiDekorator


class SiparisYoneticisi:
 
    def siparis_olustur(self, kullanici_turu, urunler,
                        hediye_paketi=False, kargo=True):
        
        sepet = SepetFabrikasi.sepet_olustur(kullanici_turu)

        for urun in urunler:
            sepet.urun_ekle(urun["ad"], urun["fiyat"], urun["adet"])

        if kargo:
            sepet = KargoDekorator(sepet)
        if hediye_paketi:
            sepet = HediyePaketiDekorator(sepet)

        return sepet

    def siparis_ozeti(self, kullanici_turu, urunler,
                      hediye_paketi=False, kargo=True):
        sepet = self.siparis_olustur(
            kullanici_turu, urunler, hediye_paketi, kargo
        )
        sepet.rapor_yazdir()

if __name__ == "__main__":
    yonetici = SiparisYoneticisi()

    print("=== Normal siparis ===")
    yonetici.siparis_ozeti(
        kullanici_turu="premium",
        urunler=[
            {"ad": "Telefon", "fiyat": 500, "adet": 1},
            {"ad": "Kilif",   "fiyat": 50,  "adet": 2},
        ],
        hediye_paketi=True,
        kargo=True
    )

    print()
    print("=== Ucretsiz kargo siniri asiliyor ===")
    yonetici.siparis_ozeti(
        kullanici_turu="uye",
        urunler=[
            {"ad": "Monitor", "fiyat": 400, "adet": 1},
        ],
        kargo=True
    )