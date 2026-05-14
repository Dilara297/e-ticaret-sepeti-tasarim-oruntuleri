 # Faz 1 — AI Kullanım Günlüğü

## Sorduğum Prompt
"Elimde bir e-ticaret sepeti kodu var. Sepet sınıfı kullanıcı türüne göre
if-else ile indirim uyguluyor. Bu nesne yaratma sorununu hangi tasarım
örüntüsü çözer? Factory Method mu doğru seçim?"

## AI'ın Yanıtı (Özet)
AI, Factory Method'un bu durum için uygun olduğunu söyledi. Her kullanıcı
türü için ayrı bir sınıf oluşturmamı ve bir fabrika sınıfının doğru nesneyi
döndürmesini önerdi. Ayrıca soyut bir temel sınıf (ABC) kullanmamı tavsiye etti.

## Ben Ne Uyguladım?
AI'ın önerisini doğrudan kopyalamadım. Önce Factory Method'u Refactoring.Guru
üzerinden okudum, sonra kendi projeme uyarladım. AI temel sınıfa `indirim_orani`
adında sabit bir alan önerdi, ben bunun yerine `indirim_uygula` adında soyut
bir metot kullandım — bu daha esnek çünkü ileride karmaşık indirim mantığı
eklenebilir.

## AI'ın Önerdiğinden Farklı Yaptığım
AI doğrudan `discount_rate = 0.10` gibi sabit bir oran tutmamı önerdi.
Ben bunun yerine her sınıfın kendi `indirim_uygula` metodunu implement
etmesini tercih ettim. Böylece ileride "ilk 3 üründe indirim" gibi
karmaşık kurallar eklemek daha kolay olacak.
