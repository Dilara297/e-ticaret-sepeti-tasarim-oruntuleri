 # Faz 2 — AI Kullanım Günlüğü

## Sorduğum Prompt
"Sepetime hediye paketi ve kargo ücreti gibi özellikler eklemek istiyorum
ama mevcut Sepet sınıfını değiştirmek istemiyorum. Adapter mı yoksa
Decorator mı kullanmalıyım? Farkını açıkla."

## AI'ın Yanıtı (Özet)
AI, Adapter'ın farklı arayüzleri uyumlu hale getirmek için kullanıldığını,
Decorator'ın ise mevcut nesneye yeni davranış eklemek için kullanıldığını
açıkladı. Bizim durumumuzda arayüz uyumsuzluğu değil, özellik ekleme
ihtiyacı olduğu için Decorator'ın doğru seçim olduğunu söyledi.
Facade için ise karmaşık alt sistemi tek noktadan yönetmek amacıyla
kullanmamı önerdi.

## AI'ın Yanlış veya Eksik Önerdiği Şey
AI başlangıçta dekoratörü doğrudan Sepet sınıfından türetmemi önerdi.
Ancak bu yaklaşımda fabrika ile entegrasyon zorlaşıyordu. Ben SepetBase
üzerinden türeterek fabrika ile uyumlu hale getirdim. AI bu detayı
başta atlayarak daha basit bir yapı önerdi — benim çözümüm daha
entegre bir yapı sağladı.

## Ben Ne Uyguladım?
Decorator için SepetDekorator temel sınıfı oluşturdum, üzerine
HediyePaketiDekorator ve KargoDekorator ekledim. Facade için
SiparisYoneticisi sınıfı tüm bu karmaşıklığı gizleyerek
kullanıcıya tek bir arayüz sunuyor. Dekoratörleri zincirleyerek
hem kargo hem hediye paketi aynı anda uygulanabiliyor.
