# Blockchain application with Python

**Block Chain**

**Blockchain Nedir?**

İnsanların sistemde yaptıkları her bir finansal hareket (transaction) bloklara yazılır. Bu finansal hareketin detayları bloklarda saklanır. Bloklar zincir gibi birbirine bağlı olarak sistemde bulunur. Bu bağlı bloklar listesine blockchain denir. Bir bakıma finansal hareketlerin tutulduğu hesap defterleridir diyebilirim.  

**Blok Nedir?**

Her bloğun tekil bir değeri (unique id) vardır. Bu tekil değer, kriptolama fonksiyonları tarafından rastgele (random) oluşturulan imzalama (hash) değeri ile sağlanır. Zincirdeki her yeni blokta, kendisinden önce gelen son bloğun hash değeri saklanır. Bu şekilde blok zinciri oluşturulur.

**Bloklara Erişim ve Güvenlik**

Oluşturulan blokların kopyaları ağdaki tüm bilgisayarlara açık bir şekilde dağıtılır ve bloklarda değişiklik olduğunda bilgi tüm bilgisayarlarda güncellenir. Böylece bilgisayarlar finansal hareketlerin geçmişine (history) erişebilir ve hareketi doğrulayabilir. Bu yüzden blockchain, merkezi olmayan dağıtık bir ağ yapısında çalışır. Sistemdeki tüm bilgiler, güvenliği garanti altına alınmış ve şeffaf bir şekilde herkesle paylaşılır. Herhangi bir merkez yoktur. Hackerların merkezi sistemlerde veriye ulaşması için tek bir merkeze erişim sağlamaları yeterlidir. Hackerların blockchain sisteminde veriye ulaşmaları için ağdaki milyonlarca bilgisayara erişmesi gerekir.

**Kriptopara (Cryptocurrency)**

Dijital değiş tokuş aracıdır. Döviz kurlarının dijital vasıtasına kripto para denir. Her kripto paranın kendi blockchain sistemi vardır. Kripto parada 3 kavram bulunur: Güvenli blockchain sistemi, cüzdan (wallet), mining.   

**Kriptografi (Cryptography)**

Blockchainler herkesin erişebileceği halka açık veritabanlarında tutulur. Kötü niyetli kişiler verileri manipüle edip değiştirmek ve daha fazla kripto paraya sahip olmak isteyebilir. Bu durumu engellemek için şifreleme algoritmaları kullanılır. Bu algoritmalar veriyi güvenle şifreleyerek kötü niyetli davranışları önlemiş olur, blockchain’i korur. Şifrelemenin kripto paradaki ana mantığı kullanıcıya unique dijital imza oluşturmasıdır. Kullanıcılar transactionlarını blockchain’e kendi dijital imzası ile kaydeder. İmza, biri public biri private (private kişiye özel ve taklit edilemez) olan şifrelenmiş anahtar çiftlerinden oluşur. Özel anahtar kişiye özel olduğundan gizli kalması önemlidir. Aksi halde başkaları işlem oluşturabilir ve yetkilendirme sağlanmamış olur. Genel anahtar ise başkalarının doğrulayabilmesi için imza ve veri ile birlikte paylaşılır.  

**Cüzdan (Wallet)**

İşlem yapabilmek için hesabınızın olması gerekir. Buna dijital cüzdan denir. Bu cüzdanın güvenliği şifreleme ile sağlanır. Her cüzdanın iki anahtarı vardır. Biri özel biri genel anahtar. Bireylerin public ve private keyleri, cüzdanı muhafaza eder. Fiziksel cüzdanda olduğu gibi, ne kadar kripto paranın olduğu takip edilir. Cüzdanların unique adresi vardır. Başka bireylere kripto para göndermek için kullanılır.   

**Mining**

Madenciler, blockchain ağında, kullanıcıların oluşturdukları transactionları saklayabilecekleri yeni blokların ağa eklenmesini sağlar. Kullanıcılar transaction oluşturdukça bunlar havuzda/transaction poolda geçici olarak doğrulanmamış bir biçimde bekletilir. Madenci, proof of work denilen hesaplama bulmacasını çözerek doğrulanmamış transaction grubunu, zincirde oluşturduğu yeni bloğa official veri olarak kaydetme hakkı kazanır. Bu algoritmayı çözmek zor ve düşük olasılığa sahip bir iştir. Madenci algoritmayı çözdüğünde kripto para ödülü kazanır. Madenci oluşturduğu yeni bloğu -içine transactionları da ekleyerek- blockchain ağında paylaşır. Diğer madenciler algoritmanın çözümünü kolay şekilde doğrulayarak onaylar.

**Hashing ve SHA-256**

Verileri şifrelemek için SHA-256 algoritması kullanılır. Secure Hash Algorithm, 256 bit uzunluğunda unique değer üretir (64 karakter uzunluğunda hexadecimal değer (256bit/4=64karakter)).  

Her blok için unique bir hash değerin üretilmesi gerekir. Bloğun hash değeri; veri, timestamp ve zincirdeki bir önceki bloğun hash değerinden üretilir.   

**UTF-8 ile Encoding ve Decoding**

String bir değer UTF-8 standardı ile 0 ve 1ler’den oluşan 8 bitlik değere dönüştürülerek encode edilmiş olur.  

Encode edilmiş değer, orijinal formata dönüştürülerek decode edilmiş olur.  

**Cryptographic Hash Function**

Bu fonksiyon herhangi bir uzunluktaki girdiyi alır ve sabit olan bir özet üretir. En önemli özelliği, verilen bir girdinin özetini üretmek çok kolay yapılabilirken, oluşan özetin girdisini bulmak imkânsızdır ve girdileri tek tek denemekten başka yol yoktur. Bunun da sebebi; özetin sonucunun tamamen rastgele olmasındandır. Girdideki en küçük değişiklik, tamamen farklı bir özet üretmeye sebep olacaktır. En önemli örneklerden biri SHA256’dir ve özetin uzunluğu, isminden de anlaşılacağı gibi, 256 bittir. İnternette bunu hesaplamasını online yapabilen birçok web sitesi mevcuttur. Mesela bir örnek yapalım [1]: 

merhaba –> SHA256 –> 4c6bcdd55f3153e1939669ab1ec039e4059174dc25abdfcb2f58868849b4d61b 

merhabb –> SHA256 –> 8775b90bf257388326699cc40f608b3f49cf5d09288ea8f7b1f6acf2f30c0dfb 

Yukarda gördüğünüz örnekte, tek bir karakter değişikliği tamamen alakasız başka bir özet üretmektedir. Bu da özeti tamamen tahmin edilemez ve rastgele yapar.

# How to run application?
Blockchain application with Python

**Run the application and API**

Make sure to activate the virtual environment.

```
py -m backend.app
```

**Run a peer instance**

Make sure to activate the virtual environment.

```
set PEER=True && py -m backend.app
```

**Run the frontend**

```
npm run start
```

**Seed the backend with data**

Make sure to activate the virtual environment.

```
set SEED_DATA=True && py -m backend.app
```