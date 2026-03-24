import requests

# Telegram Bilgilerin
TOKEN = "8699472322:AAEa0MCSs1xBI9LpGOM-Q5Z0KtSDq6t89Y4"
CHAT_ID = "7302555608"

def mesaj_gonder(metin):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID, 
        "text": metin,
        "parse_mode": "Markdown" # Mesajın daha güzel görünmesini sağlar
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("✅ Mesaj Telegram'a uçtu!")
        else:
            print(f"❌ Hata: {response.text}")
    except Exception as e:
        print(f"⚠️ Bağlantı hatası: {e}")

def dolar_kuru_al():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
        res = requests.get(url).json()
        kur = res['rates']['TRY']
        # Şık bir mesaj formatı
        return (
            "🔔 *Sistem Bildirimi*\n\n"
            f"💰 Güncel Dolar Kuru: *{kur} TL*\n"
            "🚀 GitHub Actions üzerinden gönderildi."
        )
    except:
        return "⚠️ Sistem çalışıyor ama kur verisi çekilemedi!"

if __name__ == "__main__":
    bilgi = dolar_kuru_al()
    mesaj_gonder(bilgi)
