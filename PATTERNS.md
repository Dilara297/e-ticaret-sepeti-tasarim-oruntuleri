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
