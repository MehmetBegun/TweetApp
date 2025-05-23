# Django Tweet App

Django Tweet App, kullanıcıların kayıt olup giriş yapabildiği, tweet paylaşabildiği ve kendi tweetlerini silebildiği basit bir sosyal medya uygulamasıdır. Proje, Django framework’ü ve Bootstrap ile geliştirilmiştir.

## Özellikler

- Kullanıcı kaydı (signup), giriş (login) ve çıkış (logout)
- Tweet ekleme, listeleme ve silme
- Sadece tweet sahibi tarafından silme işlemleri
- Bootstrap ile modern ve responsive arayüz
- Kullanıcıya özel tweet yönetimi
- Tweetlerin otomatik olarak kullanıcıya atanması

## Kurulum

1. **Projeyi klonlayın:**
   ```bash
   git clone <repo-link>
   cd DjangoTweetApp
   ```

2. **Sanal ortam oluşturun ve aktif edin:**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate
   ```

3. **Gerekli paketleri yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Veritabanını oluşturun:**
   ```bash
   python manage.py migrate
   ```

5. **Sunucuyu başlatın:**
   ```bash
   python manage.py runserver
   ```

6. **Uygulamayı tarayıcıda açın:**
   ```
   http://127.0.0.1:8000/
   ```

## Kullanım

- **Kayıt Ol:** Sağ üstteki Signup linki ile yeni kullanıcı oluşturabilirsiniz.
- **Giriş Yap:** Login linki ile giriş yapabilirsiniz.
- **Tweet Paylaş:** Giriş yaptıktan sonra tweet ekleyebilir, kendi tweetlerinizi silebilirsiniz.
- **Çıkış:** Logout linki ile güvenli şekilde çıkış yapabilirsiniz.

## Dosya Yapısı

- `tweetApp/` : Django projesi ana dizini
- `tweet/` : Tweet uygulaması
  - `models.py` : Tweet ve kullanıcı modelleri
  - `views.py` : Tüm view fonksiyonları
  - `templates/tweet/` : HTML şablonları
  - `forms.py` : Tweet ekleme/güncelleme formları

## Katkı

Katkıda bulunmak için fork’layıp pull request gönderebilirsiniz.

## Lisans

Bu proje MIT lisansı ile lisanslanmıştır.

---

**Not:** Proje eğitim ve deneme amaçlıdır. Gerçek bir sosyal medya uygulaması için ek güvenlik ve özellikler gereklidir.
