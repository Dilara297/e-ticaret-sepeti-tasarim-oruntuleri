 # Kullanılan Tasarım Örüntüleri

---

## Faz 1 — Factory Method

### Nerede Uygulandı?
`src/fabrika.py` — `SepetFabrikasi` sınıfı

### Neden Bu Örüntü?
Başlangıç kodunda kullanıcı türü string olarak geçiliyordu ve Sepet sınıfı
if-else ile hangi indirimi uygulayacağına kendisi karar veriyordu. Yeni bir
kullanıcı türü eklemek için doğrudan Sepet sınıfını değiştirmek gerekiyordu.
Factory Method ile nesne yaratma sorumluluğu ayrı bir sınıfa taşındı.

### Ne Kazandık?
- Yeni kullanıcı türü eklemek için mevcut kodu değiştirmemize gerek yok
- Her kullanıcı türünün indirim mantığı kendi sınıfında izole edildi
- String ile tip kontrolü ortadan kalktı, hata riski azaldı

### Önce / Sonra

**Önce:**
```python
if self.kullanici_turu == "uye":
    toplam = toplam * 0.90
elif self.kullanici_turu == "premium":
    toplam = toplam * 0.80
```

**Sonra:**
```python
sepet = SepetFabrikasi.sepet_olustur("premium")
```

---

## Faz 2 — Decorator

### Nerede Uygulandı?
`src/dekorator.py` — `HediyePaketiDekorator`, `KargoDekorator`

### Neden Bu Örüntü?
Sepete hediye paketi ve kargo ücreti eklemek için mevcut sınıfları
değiştirmek istemedik. Decorator ile sepet nesnesini sarmalayarak
yeni davranış ekledik. Dekoratörler zincirlenebilir olduğu için
ikisi aynı anda uygulanabiliyor.

### Ne Kazandık?
- Mevcut sepet kodu hiç değişmedi
- Yeni özellik eklemek için sadece yeni bir dekoratör sınıfı yazılıyor
- Özellikler isteğe bağlı ve birleştirilebilir

### Önce / Sonra
**Önce:** Hediye paketi eklemek için Sepet sınıfını değiştirmek gerekiyordu

**Sonra:**
```python
sepet = KargoDekorator(sepet)
sepet = HediyePaketiDekorator(sepet)
```

---

## Faz 2 — Facade

### Nerede Uygulandı?
`src/facade.py` — `SiparisYoneticisi`

### Neden Bu Örüntü?
Fabrika, dekoratör gibi birden fazla sınıfla ayrı ayrı çalışmak
karmaşıktı. Facade ile tüm bu işlemler tek bir sınıftan yönetiliyor.

### Ne Kazandık?
- Kullanıcı sadece SiparisYoneticisi ile konuşuyor
- Arka planda hangi sınıfların çalıştığını bilmesi gerekmiyor
- Yeni bir özellik eklendiğinde sadece Facade güncelleniyor

### Önce / Sonra
**Önce:** Her sınıfı ayrı ayrı oluşturup bağlamak gerekiyordu

**Sonra:**
```python
yonetici = SiparisYoneticisi()
yonetici.siparis_ozeti("premium", urunler, hediye_paketi=True)
```

---

## Faz 3 — Strategy

### Nerede Uygulandı?
`src/strateji.py` — `IndirimStratejisi` ve alt sınıfları

### Neden Bu Örüntü?
İndirim algoritmaları if/else ile Sepet sınıfına gömülüydü.
Strategy ile her algoritma kendi sınıfında izole edildi ve
runtime'da değiştirilebilir hale geldi.

### OCP Örneği
Yeni indirim kuralı eklemek için sadece yeni bir strateji sınıfı
yazılıyor, mevcut hiçbir kod değişmiyor.

### Ne Kazandık?
- İndirimler birleştirilebilir (KampanyaStratejisi)
- Runtime'da strateji değiştirilebilir
- Mevcut kod değişmeden yeni kural eklenebilir

---

## Faz 3 — Observer

### Nerede Uygulandı?
`src/observer.py` — `GozlemlenebilirSepet`, `SepetGozlemcisi`

### Neden Bu Örüntü?
Sepette değişiklik olduğunda log, bildirim, stok gibi sistemlerin
haberdar olması gerekiyordu. Observer ile bu bağımlılık gevşek
hale getirildi.

### Ne Kazandık?
- Sepet sınıfı gözlemcileri tanımıyor, sadece haber veriyor
- Yeni gözlemci eklemek için mevcut kodu değiştirmek gerekmiyor
- Gözlemciler runtime'da eklenip çıkarılabiliyor