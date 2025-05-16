import zipfile
import re
import sys
import requests
import time
import os

FIREBASE_RE = re.compile(r'https?://[a-zA-Z0-9\-\_\.]+firebaseio\.com')

def ascii_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
\033[91m
░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓███████▓▒░▒▓████████▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░     
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░     
   ░▒▓█▓▒░   ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░   ░▒▓█▓▒░     
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░     
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░     
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░   ░▒▓█▓▒░     
                                                                   
                                                                   

\033[91m----------- Zaafiyet Analiz Otomasyonu -----------
\033[1m          Siber Güvenlikte Güven'in imzasi
\033[0m""")
    time.sleep(1)

def firebase_url_bul(apk_yolu):
    url_listesi = set()
    with zipfile.ZipFile(apk_yolu, 'r') as apk:
        for dosya in apk.namelist():
            if dosya.endswith(('.xml', '.json', '.txt', '.html', '.dex', '.arsc', '.smali')):
                try:
                    veri = apk.read(dosya).decode('utf-8', errors='ignore')
                    bulunan = FIREBASE_RE.findall(veri)
                    if bulunan:
                        url_listesi.update(bulunan)
                except:
                    continue
    return url_listesi

def firebase_test_et(url):
    test_url = url.rstrip('/') + '/.json'
    try:
        yanit = requests.get(test_url, timeout=5)
        if yanit.status_code == 200:
            return True, yanit.json()
    except:
        pass
    return False, None

def main(apk_yolu):
    ascii_banner()
    print(f"[*] APK taraniyor: {apk_yolu}\n")

    url_listesi = firebase_url_bul(apk_yolu)
    if not url_listesi:
        print("[-] APK icinde hicbir Firebase URL bulunamadi.")
        return

    for url in url_listesi:
        print(f"[+] Firebase URL'si bulundu: {url}")
        cevap = input("[?] Bu veritabanını test etmek ister misiniz? (e/h): ").strip().lower()
        if cevap == "e":
            acik_mi, veri = firebase_test_et(url)
            if acik_mi:
                print(f"[!] Acik database bulundu: {url}")
                print(f"🔍 Örnek veri: {str(veri)[:300]}...\n")
            else:
                print("[-] Databaseye erisim kapali veya kisitli.\n")
        else:
            print("[*] Test atlaniyor.\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Kullanım: python TRUST.py <apk_dosyası>")
    else:
        main(sys.argv[1])
