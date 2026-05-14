from abc import ABC, abstractmethod
from strateji import StratejiliSepet, YuzdeIndirimStratejisi

class SepetGozlemcisi(ABC):
    @abstractmethod
    def guncelle(self, olay: str, sepet):
        pass

class LogGozlemcisi(SepetGozlemcisi):
    def guncelle(self, olay: str, sepet):
        print(f"[LOG] {olay} | "
              f"Urun sayisi: {len(sepet.urunler())} | "
              f"Toplam: {sepet.toplam_hesapla():.2f} TL")

class BildirimGozlemcisi(SepetGozlemcisi):
    def guncelle(self, olay: str, sepet):
        if olay == "SIPARIS_VERILDI":
            print(f"[BILDIRIM] Siparisıniz alindi! "
                  f"Toplam: {sepet.toplam_hesapla():.2f} TL")


class StokGozlemcisi(SepetGozlemcisi):
    def guncelle(self, olay: str, sepet):
        if olay == "URUN_EKLENDI":
            print(f"[STOK] Stok guncelleme tetiklendi")

class GozlemlenebilirSepet(StratejiliSepet):
    def __init__(self, strateji):
        super().__init__(strateji)
        self._gozlemciler = []

    def gozlemci_ekle(self, gozlemci: SepetGozlemcisi):
        self._gozlemciler.append(gozlemci)

    def gozlemci_cikar(self, gozlemci: SepetGozlemcisi):
        self._gozlemciler.remove(gozlemci)

    def _bildir(self, olay: str):
        for g in self._gozlemciler:
            g.guncelle(olay, self)

    def urunler(self):
        return self._urunler

    def urun_ekle(self, ad, fiyat, adet):
        super().urun_ekle(ad, fiyat, adet)
        self._bildir("URUN_EKLENDI")

    def siparis_ver(self):
        self._bildir("SIPARIS_VERILDI")

if __name__ == "__main__":
    sepet = GozlemlenebilirSepet(YuzdeIndirimStratejisi(0.10))

    sepet.gozlemci_ekle(LogGozlemcisi())
    sepet.gozlemci_ekle(BildirimGozlemcisi())
    sepet.gozlemci_ekle(StokGozlemcisi())

    print("--- Urun ekleniyor ---")
    sepet.urun_ekle("Monitor", 400, 1)
    sepet.urun_ekle("Klavye", 150, 1)

    print()
    print("--- Siparis veriliyor ---")
    sepet.siparis_ver()

    print()
    sepet.rapor_yazdir()