# Başlangıç Kodunun Sorunları

## Tespit Ettiğim Sorunlar

### 1. Sepet sınıfı çok fazla iş yapıyor (God Class)
`Sepet` sınıfı hem ürün yönetiyor, hem indirim hesaplıyor, hem bildirim gönderiyor,
hem de rapor yazıyor. Bir sınıfın bu kadar farklı sorumluluğu olmamalı.
Bu yüzden değiştirilmesi gerektiğinde her şeyi bozmak zorunda kalıyoruz.

### 2. İndirim kuralları sınıfın içine gömülmüş
Yeni bir indirim eklemek istediğimizde (örn. "öğrenci indirimi") doğrudan
`toplam_hesapla` metodunu değiştirmek zorundayız. Bu hem hata riskini artırıyor
hem de mevcut indirimleri bozabilir.

### 3. if-else zincirleri ile tip kontrolü
Kullanıcı türü ve indirim kontrolü if-else blokları ile yapılıyor. Yeni bir
kullanıcı türü eklendiğinde bu if-else zincirleri daha da büyüyecek ve
okunması zorlaşacak.

### 4. Bildirim gönderme mantığı sepete ait değil
Email mi SMS mi gönderileceğine `Sepet` sınıfı karar veriyor. Bu sorumluluk
ayrı bir yapıda olmalı. Şu an push notification eklemek istesek yine
`Sepet` sınıfını değiştirmek zorundayız.

### 5. İndirimler sırayla uygulanıyor, çakışma kontrolü yok
500 TL üstü indirim ve 1000 TL üstü indirim aynı sepete ikisi birden
uygulanabiliyor. Hangi indirimin önce uygulanacağı belli değil,
bu yüzden sonuç tutarsız olabilir.

---

## AI Karşılaştırması

### AI'a Sorduğum Prompt
> "Bu kodda hangi tasarım sorunlarını görüyorsun?
> Hangi tasarım örüntüleri bu sorunları çözebilir?
> Her sorun için kısa bir açıklama yaz."

### AI'ın Verdiği Yanıt (Özet)
AI de benzer sorunları tespit etti:
- `Sepet` sınıfının çok fazla sorumluluk taşıdığını (SRP ihlali) belirtti
- İndirim mantığı için **Strategy Pattern** önerdi
- Bildirim sistemi için **Observer** veya **Strategy Pattern** önerdi
- Nesne yaratımını merkeze almak için **Factory Method** önerdi

### Farklar
AI, indirim çakışması sorununu (sorun 5) ayrıca vurgulamadı — ben bunu
kendi incelememde fark ettim. Bunun dışında tespitler büyük ölçüde örtüştü.
AI'ın örüntü önerileri mantıklıydı ancak hangisini neden seçeceğimi
henüz tam anlayamadığımdan sonraki fazlarda daha dikkatli inceleyeceğim.