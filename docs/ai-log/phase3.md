 # Faz 3 — AI Kullanım Günlüğü

## Pair Programming Oturumu (30+ dakika)

### Ne Tartıştık?
Observer ve Strategy pattern'lerini birlikte nasıl kullanacağımızı
tartıştık. AI önce ikisini ayrı ayrı açıkladı, sonra birleştirme
konusunda yardımcı oldu.

### Sorduğum Promptlar
1. "Strategy pattern ile indirim algoritmalarını nasıl birbirinden
   ayırabilirim? Runtime'da değiştirilebilir olsun."

2. "Observer pattern'de sepet değişikliklerini nasıl takip ederim?
   Somut observer örnekleri ver."

3. "KampanyaStratejisi birden fazla stratejiyi birleştiriyor.
   Bu OCP'yi nasıl sağlıyor?"

### AI'ın Yanıtları (Özet)
AI, Strategy için soyut bir arayüz oluşturmamı ve her algoritmanın
bunu implement etmesini önerdi. Observer için ise publish-subscribe
mantığını açıkladı. KampanyaStratejisi için Composite pattern ile
karıştırdım, AI farkı açıkladı — Composite nesneleri ağaç yapısında
birleştirir, biz sadece algoritmaları zincirledik.

### AI Beni Nerede Yanılttı?
AI başta Observer'da sepeti doğrudan gözlemcilere geçirmek yerine
sadece veri geçirmemi önerdi. Ancak ben tüm sepet nesnesini geçirmeyi
tercih ettim çünkü gözlemciler farklı bilgilere ihtiyaç duyabilir.
Bu kararı kendim verdim.

### AI Olmadan Ne Kadar Sürerdi?
Strategy'yi muhtemelen 2-3 saatte çözerdim ama Observer'ı doğru
yapılandırmak çok daha uzun sürerdi. AI sayesinde toplam süre
yaklaşık 1.5 saate indi.
