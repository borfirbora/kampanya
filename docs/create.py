import os
from premailer import Premailer

# --- AYARLAR ---
html_dosyasi = "index.html"      # Senin tasarladığın dosya
css_dosyasi = "output.css"       # Tailwind çıktısı
cikti_dosyasi = "gonderilecek_mail.html" # Gmail'e yapıştıracağın sonuç

def mail_donustur():
    print("⏳ İşlem başlıyor: HTML ve CSS birleştiriliyor...")

    # 1. HTML Dosyasını Oku
    if not os.path.exists(html_dosyasi):
        print(f"HATA: {html_dosyasi} bulunamadı!")
        return

    with open(html_dosyasi, "r", encoding="utf-8") as f:
        html_icerik = f.read()

    # 2. CSS Dosyasını Oku
    css_icerik = ""
    if os.path.exists(css_dosyasi):
        with open(css_dosyasi, "r", encoding="utf-8") as f:
            css_icerik = f.read()
    else:
        print(f"UYARI: {css_dosyasi} bulunamadı, stilsiz devam ediliyor.")

    # 3. BÜYÜLÜ AN: Premailer ile Inline Hale Getir
    # keep_style_tags=True : Bazı medya sorgularını (mobil uyum) header'da tutar.
    # remove_classes=False : Class isimlerini silmez (bazen lazım olur).
    p = Premailer(html_icerik, 
                  css_text=css_icerik, 
                  keep_style_tags=True, 
                  remove_classes=False,
                  strip_important=False)
    
    sonuc_html = p.transform()

    # 4. Sonucu Kaydet
    with open(cikti_dosyasi, "w", encoding="utf-8") as f:
        f.write(sonuc_html)

    print(f"✅ BAŞARILI! '{cikti_dosyasi}' oluşturuldu.")
    print("👉 Şimdi bu dosyayı Chrome ile aç, Kopyala ve Gmail'e Yapıştır.")

if __name__ == "__main__":
    mail_donustur()