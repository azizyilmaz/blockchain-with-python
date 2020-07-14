# Blockchain application with Python

**Blockchain Nedir?**

Sistemde oluşan her bir ekonomik hareket/transaction bloklara yazılır. Ağdaki her blokta transaction bilgileri saklanır. Bloklar zincir gibi birbirine bağlı olarak sistemde bulunur. Bu bağlı bloklar listesine blockchain denir. Transactionların tutulduğu hesap defterleridir diyebiliriz.   

Her bloğun tekil bir değeri vardır. Bu tekil değer kriptolama fonksiyonları tarafından random oluşturulan hash değeri ile sağlanır.  

Zincirdeki her yeni blokta, kendisinden önce gelen son bloğun hash değeri saklanır. Bu şekilde blok zinciri oluşturulur. 

Oluşturulan blokların kopyaları ağdaki tüm bilgisayarlara açık bir şekilde dağıtılır ve değişiklik olduğunda bilgi tüm bilgisayarlarda güncellenir. Böylece bilgisayar transaction geçmişine erişebilir ve transactionı doğrulayabilir. Bu yüzden blockchain, merkezi olmayan dağıtık bir ağ yapısında çalışır. Sistemdeki tüm bilgiler güvenli garanti altına alınmış ve aynı zamanda şeffaf bir şekilde herkesle paylaşıldığı için tercih edilir. Herhangi bir merkez yoktur. Hackerların merkezi sistemlerde veriye ulaşması için tek bir merkeze erişim sağlamaları yeterlidir. Hackerların blockchain sisteminde veriye ulaşmaları için ağdaki milyonlarca bilgisayara erişmesi gerekir.  

**Kriptopara/Cryptocurrency**

Dijital değişim aracıdır. Döviz kurlarının dijital vasıtasına kripto para denir. Her kripto paranın kendi blockchain sistemi vardır. Kripto para 3 kavram bulunur: Güvenli blockchain sistemi, cüzdan/wallet, mining.    

**Kriptografi/Cryptography**

Blockchainler herkesin erişebileceği halka açık veritabanlarında tutulur. Kötü niyetli kişiler verileri manipüle edip değiştirmek ve daha fazla kripto paraya sahip olmak isteyebilir. Bu durumu engellemek için kriptografi kullanılır. Cryptography (şifreleme algoritmaları) veriyi güvenle şifreleyerek kötü niyetli davranışları önlemiş olur, blockchain’i korur. Şifrelemenin kripto paradaki ana mantığı bireylere tekil dijital imza oluşturmasıdır. Bireyler transactionlarını blockchain’e kendi dijital imzası ile kaydeder. İmza, biri public biri private (private kişiye özel ve taklit edilemez) olan şifrelenmiş anahtar çiftlerinden oluşur. 

**Cüzdan/Wallet**

İşlem yapabilmek için hesabınızın olması gerekir. Buna dijital cüzdan denir. Bu cüzdanın güvenliği şifreleme ile sağlanır. Her cüzdanın iki anahtarı vardır. Biri özel biri genel anahtar. Bireylerin public ve private keyleri cüzdanı muhafaza eder. Fiziksel cüzdan gibi, ne kadar kripto paranın olduğu takip edilir. Cüzdanların tekil adresi vardır. Başka bireylere kripto para göndermek için kullanılır. Özel anahtar transactionın oluşması için cüzdanın imza üretmesine yardım eder. Özel anahtar kişiye özel olduğundan gizli kalması önemlidir. Aksi halde başkaları işlem oluşturabilir ve yetkilendirme sağlanmamış olur. Genel anahtar ise başkalarının doğrulayabilmesi için imza ve veri ile birlikte paylaşılır.  

**Mining**

Madenciler blockchain ağında bireylerin oluşturdukları transactionları saklayabilecekleri yeni blokların ağa eklenmesini sağlar. Bireyler transaction oluşturdukça bunlar havuzda/transaction poolda geçici olarak doğrulanmamış bir biçimde bekletilir. Madenci proof of work denilen hesaplama bulmacasını çözerek doğrulanmamış transaction grubunu almaya ve zincirde oluşturduğu yeni bloklara official veri olarak kaydetmeye hakkı kazanır. Bu algoritmayı çözmek zor ve düşük olasılığa sahip bir iştir. Madenci algoritmayı çözdüğünde kripto para ödülü kazanır. Madenci oluşturduğu yeni bloğu -içine transactionları da ekleyerek- blockchain ağında paylaşır. Diğer minerlar algoritmanın çözümünü kolay şekilde doğrulayarak onaylar. 

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