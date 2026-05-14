from abc import ABC, abstractmethod

class IndirimStratejisi(ABC):
    @abstractmethod
    def indirim_uygula(self, toplam: float) -> float:
        pass

    @abstractmethod
    def aciklama(self) -> str:
        pass

class IndirimsizStrateji(IndirimStratejisi):
    def indirim_uygula(self, toplam: float) -> float:
        return toplam

    def aciklama(self) -> str:
        return "Indirim uygulanmadi"


class YuzdeIndirimStratejisi(IndirimStratejisi):
    def __init__(self, oran: float):
        self._oran = oran

    def indirim_uygula(self, toplam: float) -> float:
        return toplam * (1 - self._oran)

    def aciklama(self) -> str:
        return f"%{int(self._oran * 100)} indirim uygulandı"


class SabitIndirimStratejisi(IndirimStratejisi):
    def __init__(self, miktar: float, limit: float):
        self._miktar = miktar
        self._limit = limit

    def indirim_uygula(self, toplam: float) -> float:
        if toplam >= self._limit:
            return toplam - self._miktar
        return toplam

    def aciklama(self) -> str:
        return f"{self._limit} TL uzeri {self._miktar} TL indirim"


class KampanyaStratejisi(IndirimStratejisi):
    
    def __init__(self, stratejiler: list):
        self._stratejiler = stratejiler

    def indirim_uygula(self, toplam: float) -> float:
        for strateji in self._stratejiler:
            toplam = strateji.indirim_uygula(toplam)
        return toplam

    def aciklama(self) -> str:
        return " + ".join(s.aciklama() for s in self._stratejiler)

class StratejiliSepet:
    def __init__(self, strateji: IndirimStratejisi):
        self._urunler = []
        self._strateji = strateji

    def strateji_degistir(self, strateji: IndirimStratejisi):
        """Runtime'da strateji degistirilebilir — OCP"""
        self._strateji = strateji

    def urun_ekle(self, ad, fiyat, adet):
        self._urunler.append({"ad": ad, "fiyat": fiyat, "adet": adet})

    def ara_toplam(self):
        return sum(u["fiyat"] * u["adet"] for u in self._urunler)

    def toplam_hesapla(self):
        return self._strateji.indirim_uygula(self.ara_toplam())

    def rapor_yazdir(self):
        print("===== SEPET RAPORU =====")
        for u in self._urunler:
            print(f"{u['ad']} x{u['adet']} - {u['fiyat']} TL")
        print(f"Ara Toplam  : {self.ara_toplam()} TL")
        print(f"Toplam      : {self.toplam_hesapla():.2f} TL")
        print(f"Aciklama    : {self._strateji.aciklama()}")

if __name__ == "__main__":
    print("=== Yuzde indirim ===")
    sepet = StratejiliSepet(YuzdeIndirimStratejisi(0.20))
    sepet.urun_ekle("Laptop", 800, 1)
    sepet.rapor_yazdir()

    print()
    print("=== Runtime'da strateji degisti (OCP) ===")
    sepet.strateji_degistir(SabitIndirimStratejisi(100, 500))
    sepet.rapor_yazdir()

    print()
    print("=== Kampanya: yuzde + sabit birlikte ===")
    kampanya = KampanyaStratejisi([
        YuzdeIndirimStratejisi(0.10),
        SabitIndirimStratejisi(50, 400)
    ])
    sepet2 = StratejiliSepet(kampanya)
    sepet2.urun_ekle("Telefon", 500, 1)
    sepet2.urun_ekle("Kilif", 50, 2)
    sepet2.rapor_yazdir()