# [haberpy](https://pypi.org/project/haberpy/)

Haber sitelerinden bildirimleri kolay sekilde alabilmeniz icin tasarlanmis bir Python API.

- Kar amaci gutmemektedir...

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -U haberpy
```

## Usage

```python
# Yerel haberler
from haberpy.sondakika import Local

city = "Ankara"
local = Local(city)

# Ankaraya ait yerel en güncel haber
local.current_news()

"""
{
    'img': 'https://i.sdacdn.com/haber/2023/06/20/baro-tarafindan-hazirlanan-karabag-hukuki-rap-16048190_300.jpg',
    'title': "Ankara Barosu, 'Karabağ Hukuki Raporu'nu takdim etti",
    'about': "Ankara 2 No'lu Barosu, Azerbaycan Milli Kurtuluş Günü dolayısıyla düzenlenen programda 'Karabağ Hukuki Raporu'nu takdim etti. Baro Başkanı Sabri Hafif, Türkiye'nin Azerbaycan'a verdiği desteğin 'Tek millet, iki devlet olunmasının göstergesi olduğunu' ifade ederek Cumhurbaşkanı Recep Tayyip Erdoğan ve Türk Silahlı Kuvvetlerine teşekkür etti. Türk Dünyası Hukuku İşbirliği Komisyonu Başkanı Faruk Keleştimur ise Ermenistan'ın Karabağ'a yaptığı işgalin insanlık suçu olduğunu belirtti."
}
"""

# Ankaraya ait yerel haberler

local.news(limit=2)

"""
{
    1: {
        'img': 'https://i.sdacdn.com/haber/2023/06/20/baro-tarafindan-hazirlanan-karabag-hukuki-rap-16048190_300.jpg',
        'title': "Ankara Barosu, 'Karabağ Hukuki Raporu'nu takdim etti",
        'about': "Ankara 2 No'lu Barosu, Azerbaycan Milli Kurtuluş Günü dolayısıyla düzenlenen programda 'Karabağ Hukuki Raporu'nu takdim etti. Baro Başkanı Sabri Hafif, Türkiye'nin Azerbaycan'a verdiği desteğin 'Tek millet, iki devlet olunmasının göstergesi olduğunu' ifade ederek Cumhurbaşkanı Recep Tayyip Erdoğan ve Türk Silahlı Kuvvetlerine teşekkür etti. Türk Dünyası Hukuku İşbirliği Komisyonu Başkanı Faruk Keleştimur ise Ermenistan'ın Karabağ'a yaptığı işgalin insanlık suçu olduğunu belirtti."
    },
    2: {
        'img': 'https://i.sdacdn.com/haber/2023/06/20/ehliyet-sinavi-kopya-sebekesine-duzenek-opera-16048084_300.jpg',
        'title': 'Ehliyet sınavında kopya çekmeye yönelik şebekeye operasyon',
        'about': 'Ankara merkezli 29 ilde gerçekleştirilen operasyonda, ehliyet sınavında kopya çekmeye yönelik kamera ve kulaklık düzeneği kullanan suç örgütüne yönelik çalışma yapıldı. Şüphelilerin yaklaşık 20 milyon TL haksız kazanç elde ettiği tespit edildi. 270 şüphelinin kimlik ve adres bilgileri tespit edilirken, çok sayıda kişi gözaltına alındı ve kamera-kulaklık düzenekleri ele geçirildi.'
        }
    }
"""

# Dünya haberleri
from haberpy.sondakika import World

world = World()

# Dünya haberlerinden en güncel haber
world.current_news()

"""
{
    'img': 'https://s.sdacdn.com/static/sondakikacom_haberi.jpg', 
    'title': "BM Genel Sekreteri İsrail'i Filistin Topraklarındaki Yerleşim Faaliyetlerini Durdurmaya Çağırdı", 
    'about': "BM Genel Sekreteri Antonio Guterres'in sözcü yardımcısı Farhan Haq, İsrail hükümetini işgal altındaki Filistin topraklarında yürüttüğü tüm yerleşim faaliyetlerini 'derhal ve tamamen' sona erdirmeye çağırdığını bildirdi. Guterres, İsrail'in yerleşim planlama prosedürlerini değiştirme kararından derin rahatsızlık duyduğunu belirtti. Yerleşimler, uygulanabilir iki devletli çözümün ve adil, kalıcı ve kapsamlı bir barışın gerçekleştirilmesinin önünde büyük bir engel teşkil ediyor."
}
"""

# Dünyadan haberler
world.news(limit=2)

"""
{
    1: {
        'img': 'https://s.sdacdn.com/static/sondakikacom_haberi.jpg', 
        'title': "Tayvan'da Anaokulunda Çocuklara Bağımlılık Yapan İlaç İçirildiği Ortaya Çıktı", 
        'about': "Tayvan'ın Taipei kentinde bulunan bir anaokulunda öğretmenlerin, öğrencileri yatıştırmak için bağımlılık yapan fenobarbital ve benzodiazepin içeren şurup içirdiği ortaya çıktı. Soruşturma sonucunda 8 çocuğun vücudunda eser miktarda ilaç tespit edildi. Anaokulu 12 Haziran'da kapatılırken, okul yöneticileri 5 bin dolar ceza ödemek zorunda kaldı. Olaya dahil olan müdür ve 5 öğretmen tutuklandı ancak kefaletle serbest bırakıldı. Çocukları olaydan etkilenen aileler, devlet binalarının önünde protestolar düzenledi."
    }, 
    2: {
        'img': 'https://s.sdacdn.com/static/sondakikacom_haberi.jpg', 
        'title': 'Tunus Cumhurbaşkanı, Fransa ve Almanya İçişleri Bakanları ile İşbirliği ve Göç Konularını Görüştü', 
        'about': "Tunus Cumhurbaşkanı Kays Said, Fransa ve Almanya'nın konuk içişleri bakanları ile ikili işbirliği ve yasadışı göç konularını ele aldı. Toplantıda Tunus ile Avrupa Birliği arasındaki stratejik işbirliği ve ortaklık ilişkileri de ele alındı. Tunus, yasadışı göçün önlenmesinde Avrupa sınırlarının bekçiliğini yapmayacağını, sadece kendi sınırlarını koruyacağını vurguladı. Fransa İçişleri Bakanı, Tunus'a yasadışı göçmenlerin Avrupa kıyılarına ulaşmasını engellemesi için 25,8 milyon euro teklif etti."
    }
}
"""

# Spor haberleri
from haberpy.sondakika.sport import Sport

sport = Sport()

# Spor haberlerinden en güncel haber
sport.current_news()

"""
{
    'img': 'https://i.sdacdn.com/haber/2023/06/20/altay-da-kutay-dan-ihtarname-16048386_300.jpg', 
    'title': "Altay'da Kutay Yokuşlu alacaklarını tahsil etmek için ihtarname gönderdi", 
    'about': "Altay'ın altyapısından yetişen stoper Kutay Yokuşlu, alacaklarını tahsil etmek için kulübe ihtarname gönderdi. Eğer ödeme yapılmazsa serbest kalma hakkı kazanacak olan Kutay'ın transfer yasağı bulunan İzmir temsilcisi tarafından alacağı ödenmeye çalışılıyor. Altay'da ödemeleri yapılmayan diğer oyuncular Paixao, Naderi ve Björkander de serbest kalma hakkı kazanmıştı."
}
"""
sport.news(limit=2)

"""
{
    1: {
        'img': 'https://i.sdacdn.com/haber/2023/06/20/altay-da-kutay-dan-ihtarname-16048386_300.jpg', 
        'title': "Altay'da Kutay Yokuşlu alacaklarını tahsil etmek için ihtarname gönderdi", 
        'about': "Altay'ın altyapısından yetişen stoper Kutay Yokuşlu, alacaklarını tahsil etmek için kulübe ihtarname gönderdi. Eğer ödeme yapılmazsa serbest kalma hakkı kazanacak olan Kutay'ın transfer yasağı bulunan İzmir temsilcisi tarafından alacağı ödenmeye çalışılıyor. Altay'da ödemeleri yapılmayan diğer oyuncular Paixao, Naderi ve Björkander de serbest kalma hakkı kazanmıştı."
        }, 
    2: {
        'img': 'https://i.sdacdn.com/haber/2023/06/20/panathinaikos-ergin-ataman-ile-2-yillik-sozle-16048355_300.jpg', 
        'title': "Ergin Ataman, Yunanistan ekibi Panathinaikos'un başantrenörü oldu", 
        'about': "Anadolu Efes'ten ayrılan başantrenör Ergin Ataman, Yunanistan ekibi Panathinaikos'un başantrenörü olarak 2 yıllık anlaşma imzaladı. Ataman, yeni görevi için büyük hedeflere hazır olduklarını belirtti ve takımın güçlü bir kadro oluşturmak için çalıştığını söyledi."
    }
}
"""

# Ekonomi haberleri
from haberpy.sondakika.economy import Economy

economy = Economy()

# Ekonomi haberlerinden en güncel haber
economy.current_news()

"""
{
    'img': 'https://i.sdacdn.com/haber/2023/06/20/kinik-ta-tarim-ihtisas-osb-hayata-geciyor-16048407_300.jpg', 
    'title': "Kınık Tarıma Dayalı İhtisas Bitkisel Üretim Organize Sanayi Bölgesi'nin projesi onaylandı", 
    'about': "İzmir Kınık Tarıma Dayalı İhtisas Bitkisel Üretim Organize Sanayi Bölgesi'nin (TDİOSB), Genel Yerleşim Planı ve Üst Yapı Modül Projeleri onaylandı. Projenin dünyada ilk olma özelliğine sahip olduğunu belirten Kınık Belediye Başkanı ve Kınık TDİOSB Yönetim Kurulu Üyesi Dr. Sadık Doğruer, projenin bölge ekonomisine katkısı olacağını belirtti. TDİOSB'de, tohum ve fide üretimi ile tıbbi ve aromatik bitkilerin yetiştirilmesine yönelik işletmeler ile üretilen ürünlerin işleneceği sanayi tesislerinin yer alması planlanıyor. Tam kapasiteyle faaliyete geçtiğinde doğrudan 3 bin kişiye istihdam sağlanması hedefleniyor."
}
"""

economy.news(limit=2)

"""
{
    1: {
        'img': 'https://i.sdacdn.com/haber/2023/06/20/kinik-ta-tarim-ihtisas-osb-hayata-geciyor-16048407_300.jpg', ,
        'title': "Kınık Tarıma Dayalı İhtisas Bitkisel Üretim Organize Sanayi Bölgesi'nin projesi onaylandı", 
        'about': "İzmir Kınık Tarıma Dayalı İhtisas Bitkisel Üretim Organize Sanayi Bölgesi'nin (TDİOSB), Genel Yerleşim Planı ve Üst Yapı Modül Projeleri onaylandı. Projenin dünyada ilk olma özelliğine sahip olduğunu belirten Kınık Belediye Başkanı ve Kınık TDİOSB Yönetim Kurulu Üyesi Dr. Sadık Doğruer, projenin bölge ekonomisine katkısı olacağını belirtti. TDİOSB'de, tohum ve fide üretimi ile tıbbi ve aromatik bitkilerin yetiştirilmesine yönelik işletmeler ile üretilen ürünlerin işleneceği sanayi tesislerinin yer alması planlanıyor. Tam kapasiteyle faaliyete geçtiğinde doğrudan 3 bin kişiye istihdam sağlanması hedefleniyor."
        }, 
    2: {
        'img': 'https://i.sdacdn.com/haber/2023/06/20/asgari-ucret-11-bin-402-lira-oldu-16048404_300.jpg', 
        'title': 'Yeni Asgari Ücret Temmuz Ayından İtibaren 11 Bin 402 Lira Olacak', 
        'about': "Çalışma ve Sosyal Güvenlik Bakanı Vedat Işıkhan, Asgari Ücret Tespit Komisyonu'nun üçüncü toplantısının ardından yeni asgari ücretin temmuz ayı itibarıyla 11 bin 402 lira olacağını duyurdu. Türk-İş Genel Başkanı Ergün Atalay, zamma ilişkin 'Bu sene 34 civarında bir ara zam oldu. Enflasyon durmadığı müddetçe zammın bir anlamı yok. Şu anda 486 dolar, asgari ücret tarihinin dolar üzerinden baktığınız zaman en yüksek rakamı. Bu mükemmel bir şey mi, değil. Ama bugünü şartlarında yapılması gereken buydu, bunu yaptık' dedi."
    }
}
"""

# Politika haberleri
from haberpy.sondakika.policy import Policy

policy = Policy()

# Politika haberlerinden en güncel haber
policy.current_news()

"""
{
    'img': 'https://i.sdacdn.com/haber/2023/06/20/mhp-genel-baskani-bahceli-turkiye-nin-ekonomi-16048375_300.jpg', 
    'title': 'MHP Genel Başkanı Bahçeli: "Türkiye\'nin ekonomik istikrarı elde etmesi için alınması gereken kısa dönemli tedbirler vardır"', 
    'about': 'MHP Genel Başkanı Bahçeli: "Türkiye\'nin ekonomik istikrarı elde etmesi için alınması gereken kısa dönemli tedbirler vardır. Uygur Türklerine terörist demek haksızlıktır, bühtandır, günahtır, cinayettir, rezalettir, melanettir" Milliyetçi Hareket Partisi Genel Başkanı Devlet Bahçeli...'
}
"""

policy.news(limit=2)

"""
{
    1: {
        'img': 'https://i.sdacdn.com/haber/2023/06/20/mhp-genel-baskani-bahceli-turkiye-nin-ekonomi-16048375_300.jpg', 
        'title': 'MHP Genel Başkanı Bahçeli: "Türkiye\'nin ekonomik istikrarı elde etmesi için alınması gereken kısa dönemli tedbirler vardır"', 
        'about': 'MHP Genel Başkanı Bahçeli: "Türkiye\'nin ekonomik istikrarı elde etmesi için alınması gereken kısa dönemli tedbirler vardır. Uygur Türklerine terörist demek haksızlıktır, bühtandır, günahtır, cinayettir, rezalettir, melanettir" Milliyetçi Hareket Partisi Genel Başkanı Devlet Bahçeli.'
        },
    2: {
        'img': 'https://i.sdacdn.com/haber/2023/06/20/bahceli-yeni-bir-anayasa-hazirlanmali-ve-anay-16048303_300.jpg', 
        'title': "Bahçeli, Anayasa Mahkemesi'nin HDP'ye bloke kararına tepki gösterdi", 
        'about': "MHP Genel Başkanı Devlet Bahçeli, Anayasa Mahkemesi'nin HDP'ye ödenen Hazine yardımına bloke konulması talebinde karar verilmesine yer olmadığına hükmetmesine tepki gösterdi. Bahçeli, 'Yeni bir anayasa hazırlanmalı ve Anayasa Mahkemesi'ne şekil verilmeli… Onları şiddetle kınıyorum. Şu Kandil kuyruğundan ayrılmaları lazım' dedi."
    }
}
"""


# Magazin haberleri
from haberpy.sondakika.magazine import Magazine


magazine = Magazine()

# Magazin haberlerinden en güncel haber
magazine.current_news()

"""
{
    'img': 'https://i.sdacdn.com/haber/2023/06/20/oyuncu-pinar-deniz-sahnede-sarki-soyledi-16048416_2214_300.jpg', 
    'title': "Yargı'nın Pınar Deniz'i sevgilisi Kaan Yıldırım ile tatilde", 
    'about': "Kanal D'de yayınlanan Yargı dizisinin başrol oyuncusu Pınar Deniz, sezon finali sonrası sevgilisi Kaan Yıldırım ile tatile çıktı. Deniz, şarkıcı Aybüke Albere'nin konserinde sahneye çıkarak şarkı söylerken, Yıldırım da sevgilisini hayranlıkla izledi. İkilinin romantik anları sosyal medyada paylaşılırken, güzel yorumlar da yapıldı."
}
"""

magazine.news(limit=2)

"""
{
    1: {
        'img': 'https://i.sdacdn.com/haber/2023/06/20/oyuncu-pinar-deniz-sahnede-sarki-soyledi-16048416_2214_300.jpg', 
        'title': "Yargı'nın Pınar Deniz'i sevgilisi Kaan Yıldırım ile tatilde", 
        'about': "Kanal D'de yayınlanan Yargı dizisinin başrol oyuncusu Pınar Deniz, sezon finali sonrası sevgilisi Kaan Yıldırım ile tatile çıktı. Deniz, şarkıcı Aybüke Albere'nin konserinde sahneye çıkarak şarkı söylerken, Yıldırım da sevgilisini hayranlıkla izledi. İkilinin romantik anları sosyal medyada paylaşılırken, güzel yorumlar da yapıldı."
        },
    2: {
        'img': 'https://i.sdacdn.com/haber/2023/06/20/evden-kacan-18-yasindaki-kiz-38-yas-buyuk-16047894_6161_300.jpg',
        'title': "Manisa'da kaybolan öğrenci, öğretmeniyle evlenmiş",
        'about': "Manisa'da kaybolan Ticaret Meslek Lisesi öğrencisi Begüm Altınkıran, ailesiyle beraber yaşadığı evden karne almak üzere ayrıldı ve geri dönmedi. Ailesi, Müge Anlı ile Tatlı Sert programına başvurarak yardım istedi. Ancak canlı yayına bağlanan Begüm, kendisinden 32 yaş büyük öğretmeniyle gizlice evlendiğini ve mutlu olduğunu söyledi. Öğretmen ise hakkındaki iddialardan dolayı şikayetçi olacağını belirtti."
        }
}
"""
```



## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contact

[Telegram](https://t.me/ReWoxi) - [Github](https://github.com/Meinos10) - Discord: ```rewoxi```
