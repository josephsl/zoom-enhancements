# NVDA için Zoom Erişilebilirlik İyileştirmeleri eklentisi

* Yazarlar: Mohamad Suliman, Eilana Benish

Bu eklenti, Zoom programının erişilebilirliğini arttıran özellikler içermektedir. Toplantılar sırasında farklı olaylardan gelen uyarıları daha kolay takip edebilmek için klavye kısayolları sağlar. Ayrıca, uzaktan kontrol işlevinin daha erişilebilir hale getirilmesi gibi birçok farklı iyileştirme içerir.

Notlar:

* Ekran okuyucu uyarılarını Zoom'un kendisinden (Zoom 5.2.1 ve üzeri) yapılandırabilirsiniz. Bir uyarı Zoom'un kendisinden devre dışı bırakılırsa, uyarı raporlaması eklentiden etkinleştirilse bile NVDA bunları duyurmayacaktır. Ekran okuyucu uyarılarını yapılandırma hakkında daha fazla bilgiyi burada bulabilirsiniz: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0066934.
* Özel uyarı bildirim modu aracılığıyla yapılandırılan uyarı bildirimleri, İngilizce Zoom arayüzü için optimize edilmiştir.

## Keyboard shortcuts for controlling alerts in meetingsToplantı sırasında uyarıları kontrol etmek için klavye kısayolları

* NVDA + CTRL + Shift + A: farklı bildirim uyarı modları arasında geçiş yapar. Aşağıdaki modlar kullanılabilir:
	* Tüm uyarıları bildir, tüm uyarıları bildirir
	* Uyarıları bip sesiyle bildir: NVDA, Zoom’da görüntülenen her uyarı için kısa bir bip sesi çalar
	* Uyarıları bildirme,  NVDA hiçbir uyarıyı bildirmez
	* Özel, sadece seçilen uyarılar bildirilir. Bu, eklentinin ayarlar iletişim kutusu kullanılarak veya bu işlev için atanmış klavye kısayolu kullanılarak yapılabilir.

Her bir uyarı türünün bildirimini açıp kapatmak için aşağıdaki kısayollar kullanılabilir. Not: bu ayar, sadece özel mod seçiliyken etkilidir:

* NVDA + Ctrl + 1: Katılımcı Toplantıya Katıldı/Toplantıdan Ayrıldı (Yalnızca Toplantı Sahibi)
* NVDA + Ctrl + 2: Katılımcı Katıldı/Bekleme Odasından Ayrıldı (Yalnızca Toplantı Sahibi)
* NVDA + Ctrl + 3: Ses toplantı sahibi tarafından kapatıldı
* NVDA + Ctrl + 4: Video toplantı sahibi Tarafından Durduruldu
* NVDA + Ctrl + 5: Bir katılımcı tarafından ekran Paylaşımı Başlatıldı/Durduruldu
* NVDA + Ctrl + 6: Kayıt İzni Verildi/İptal Edildi
* NVDA + Ctrl + 7: Herkese Açık Toplantı İçi Sohbet mesajı Alındı
* NVDA + Ctrl + 8: Özel Toplantı İçi Sohbet mesajı Alındı
* NVDA + Ctrl + 9: Toplantı İçi Dosya Yüklemesi Tamamlandı
* NVDA + Ctrl + 0: Sunum izni Verildi/İptal Edildi
* NVDA + Shift + Ctrl + 1: Katılımcı Elini Kaldırdı/İndirdi (Yalnızca Toplantı Sahibi)
* NVDA + Shift + Ctrl + 2: Uzaktan Kontrol İzni Verildi/İptal Edildi
* NVDA + Shift + Ctrl + 3: IM sohbet mesajı alındı

Eklentinin istenen şekilde çalışması için Zoom erişilebilirlik iyileştirmeleri ayarlarında tüm uyarı türlerini Bildir seçeneğinin işaretli olduğuna emin olun.

## Eklenti İletişim Kutusunu açmak için klavye kısayolu

NVDA + Z Eklenti iletişim kutusunu açar:

* Bildirilen ve bildirilmeyen uyarıları görme
* Bildirilmesini istediğiniz uyarı türlerini eçme
* Uyarı bildirim modunu seçme
* Save custom changes

## Uzaktan Kontrol

Zoom’un artık uzaktan kumandayı erişilebilir bir şekilde kullanmak için özel klavye kısayolları sunduğu ortaya çıktı. Aşağıdaki klavye kısayollarını şu amaçlarla kullanabilirsiniz:

* Alt+Shift+r: Uzaktan kumandayı başlatmak için. İşlemi gerçekleştirebilmek için uzaktan kumanda edilecek bilgisayarın kullanıcısından izin almanız gerektiğini unutmayın
* Alt + Shift + g: Uzaktan kumandayı devretmek veya iptal etmek için

## Sohbet geçmişi iletişim kutusu

Eklentinin, eklenti çalışırken toplantı sırasında gönderilen tüm sohbet mesajlarını görebileceğiniz özel bir iletişim kutusu vardır. Bu iletişim kutusunu açmak için NVDA+Ctrl+h tuşlarını kullanın. İletişim kutusu, gönderilen sohbet mesajlarının bir listesini zaman damgalarıyla birlikte gösterir (bu, bir toplantıya iki veya daha fazla kişi katılıyorsa işe yarar).
