#  E-Ticaret Sepeti — Yazılım Tasarım Örüntüleri Ödevi

**Konu: D — E-Ticaret Sepeti**

İndirim hesaplama mantığı gerçek projelerde sıkça karmaşıklaşan
bir alandır. Bu projede başlangıçta kötü tasarlanmış bir sepet sistemi,
üç faz boyunca tasarım örüntüleri kullanılarak geliştirildi.

##  Kullanılan Tasarım Örüntüleri

| Faz   | Örüntü  |      Dosya       | Amaç      |
|-------|---------|------------------|-----------|
| Faz 1 |Factory  |`src/fabrika.py`  | Kullanıcı türüne göre doğru sepet nesnesini üretmek |
| Faz 2 |Decorator|`src/dekorator.py`| Mevcut kodu bozmadan kargo/hediye paketi eklemek |
| Faz 2 | Facade  | `src/facade.py`  | Karmaşık işlemleri tek arayüzden yönetmek |
| Faz 3 | Strategy|`src/strateji.py` | İndirim algoritmalarını değiştirilebilir yapmak |
| Faz 3 | Observer| `src/observer.py`| Sepet olaylarını ilgili sistemlere bildirmek |

##  Mimari Diyagram
Kullanici
↓
SiparisYoneticisi (Facade)
↓
SepetFabrikasi (Factory Method)
↓
GozlemlenebilirSepet (Observer)
↓
StratejiliSepet (Strategy)
↓
KargoDekorator → HediyePaketiDekorator (Decorator)

##  Nasıl Çalıştırılır?

```bash
# Faz 1 - Factory Method
python src/fabrika.py

# Faz 2 - Decorator
python src/dekorator.py

# Faz 2 - Facade
python src/facade.py

# Faz 3 - Strategy
python src/strateji.py

# Faz 3 - Observer
python src/observer.py
```