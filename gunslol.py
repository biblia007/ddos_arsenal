#!/usr/bin/env python3
# ================================================================
# GUNS.LOL PROFILE VIEWS BOOSTER – HYBRID EDITION v6.1 TEST EDITION
# Author: @biblia007
# Description: Автоматический обход защиты (requests + Selenium fallback)
# ================================================================

import os
import sys
import subprocess
import random
import time
import threading
import queue
import json
import re
import socket
import ssl
from datetime import datetime
from collections import defaultdict

# ================================================================
# АВТОУСТАНОВКА БИБЛИОТЕК (без webdriver-manager)
# ================================================================

REQUIRED = [
    'requests',
    'colorama',
    'tqdm',
    'pysocks',
    'selenium',
    'undetected-chromedriver'
]

def install_packages():
    to_install = []
    for pkg in REQUIRED:
        try:
            if pkg == 'pysocks':
                __import__('socks')
            elif pkg == 'undetected-chromedriver':
                __import__('undetected_chromedriver')
            else:
                __import__(pkg)
            print(f"[✓] {pkg}")
        except ImportError:
            to_install.append(pkg)
            print(f"[✗] {pkg} - устанавливаю...")
    if to_install:
        for pkg in to_install:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', pkg, '--quiet'])
        print("[*] Перезапуск...")
        os.execv(sys.executable, [sys.executable] + sys.argv)

install_packages()

# ================================================================
# ИМПОРТЫ
# ================================================================

import requests
import colorama
from colorama import init, Fore, Back, Style
import tqdm
from tqdm import tqdm
import socks
import socket
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

init(autoreset=True)

# ================================================================
# КОНФИГУРАЦИЯ
# ================================================================

VERSION = "6.1"
AUTHOR = "@biblia007"

# 30+ источников прокси (сокращённый список)
PROXY_SOURCES = [
    {'name': 'ProxyScrape HTTP', 'url': 'https://cdn.jsdelivr.net/gh/proxyscrape/free-proxy-list@main/proxies/http/data.txt', 'type': 'http'},
    {'name': 'ProxyScrape HTTPS', 'url': 'https://cdn.jsdelivr.net/gh/proxyscrape/free-proxy-list@main/proxies/https/data.txt', 'type': 'https'},
    {'name': 'ProxyScrape SOCKS5', 'url': 'https://cdn.jsdelivr.net/gh/proxyscrape/free-proxy-list@main/proxies/socks5/data.txt', 'type': 'socks5'},
    {'name': 'TheSpeedX HTTP', 'url': 'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt', 'type': 'http'},
    {'name': 'TheSpeedX SOCKS5', 'url': 'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt', 'type': 'socks5'},
    # Добавьте остальные 30+ источников из предыдущих версий
]

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
]

REFERERS = [
    "https://www.google.com/",
    "https://www.bing.com/",
    "https://www.yahoo.com/",
    "https://www.duckduckgo.com/",
    "https://twitter.com/",
]

# ================================================================
# КЛАСС PROXY MANAGER (без изменений)
# ================================================================

class ProxyManager:
    def __init__(self):
        self.proxies = []
        self.working_proxies = []
        self.lock = threading.Lock()

    def load_from_sources(self, sources=None, max_per_source=500):
        if sources is None:
            sources = PROXY_SOURCES
        print(Fore.CYAN + f"[*] Загрузка прокси из {len(sources)} источников...")
        all_proxies = []
        session = requests.Session()
        session.headers.update({'User-Agent': random.choice(USER_AGENTS)})
        for source in sources:
            try:
                name = source.get('name', 'Unknown')
                url = source['url']
                ptype = source.get('type', 'mixed')
                resp = session.get(url, timeout=15)
                if resp.status_code == 200:
                    lines = resp.text.splitlines()
                    count = 0
                    for line in lines:
                        line = line.strip()
                        if line and ':' in line:
                            parts = line.split(':')
                            if len(parts) >= 2 and parts[1].isdigit():
                                port = int(parts[1])
                                if 1 <= port <= 65535:
                                    proxy = f"{parts[0]}:{port}"
                                    all_proxies.append((proxy, ptype))
                                    count += 1
                                    if count >= max_per_source:
                                        break
                    print(Fore.GREEN + f"  [+] {name}: {count} прокси")
                else:
                    print(Fore.YELLOW + f"  [-] {name}: HTTP {resp.status_code}")
                time.sleep(0.2)
            except Exception as e:
                print(Fore.RED + f"  [!] Ошибка {source.get('name', 'Unknown')}: {e}")
        seen = set()
        unique = []
        for proxy, ptype in all_proxies:
            if proxy not in seen:
                seen.add(proxy)
                unique.append((proxy, ptype))
        self.proxies = unique
        random.shuffle(self.proxies)
        print(Fore.GREEN + f"\n[+] Всего загружено: {len(self.proxies)} уникальных прокси.")
        return self.proxies

    def load_from_file(self, filepath, ptype='http'):
        if not os.path.exists(filepath):
            print(Fore.RED + f"[-] Файл {filepath} не найден.")
            return []
        with open(filepath, 'r') as f:
            lines = [line.strip() for line in f if line.strip() and ':' in line]
        proxies = []
        for line in lines:
            parts = line.split(':')
            if len(parts) >= 2 and parts[1].isdigit():
                proxies.append((f"{parts[0]}:{parts[1]}", ptype))
        self.proxies.extend(proxies)
        self.proxies = list(set(self.proxies))
        print(Fore.GREEN + f"[+] Добавлено {len(proxies)} прокси из файла.")
        return proxies

    def test_proxy(self, proxy, ptype='http', timeout=8):
        try:
            if ptype.startswith('socks'):
                ip, port = proxy.split(':')
                socks_type = socks.SOCKS5 if 'socks5' in ptype else socks.SOCKS4
                s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
                s.set_proxy(socks_type, ip, int(port))
                s.settimeout(timeout)
                s.connect(('www.google.com', 80))
                s.send(b'HEAD / HTTP/1.1\r\nHost: www.google.com\r\n\r\n')
                resp = s.recv(1024)
                s.close()
                return b'200' in resp or b'301' in resp
            else:
                proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
                r = requests.get('http://www.google.com', proxies=proxies, timeout=timeout,
                                  headers={'User-Agent': random.choice(USER_AGENTS)})
                return r.status_code in [200, 301, 302]
        except:
            return False

    def validate_proxies(self, count=300, max_workers=50):
        print(Fore.CYAN + f"[*] Проверка {min(count, len(self.proxies))} прокси...")
        test_proxies = self.proxies[:count]
        working = []
        lock = threading.Lock()
        q = queue.Queue()
        for proxy, ptype in test_proxies:
            q.put((proxy, ptype))
        def worker():
            while not q.empty():
                proxy, ptype = q.get()
                if self.test_proxy(proxy, ptype):
                    with lock:
                        working.append((proxy, ptype))
                    print(Fore.GREEN + f"[✓] {proxy} работает")
                else:
                    print(Fore.RED + f"[✗] {proxy} не работает")
                q.task_done()
                time.sleep(0.05)
        threads = []
        for _ in range(min(max_workers, q.qsize())):
            t = threading.Thread(target=worker)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        self.working_proxies = working
        print(Fore.GREEN + f"[+] Рабочих прокси: {len(working)}/{len(test_proxies)}")
        return working

    def get_working(self):
        return self.working_proxies

    def save_working(self, filename="working_proxies.txt"):
        if not self.working_proxies:
            print(Fore.YELLOW + "[-] Нет рабочих прокси для сохранения.")
            return
        with open(filename, 'w') as f:
            for proxy, ptype in self.working_proxies:
                f.write(f"{proxy}  # {ptype}\n")
        print(Fore.GREEN + f"[+] Рабочие прокси сохранены в {filename}")

# ================================================================
# КЛАСС GUNS BOOSTER (ГИБРИДНЫЙ ОБХОД)
# ================================================================

class GunsBooster:
    def __init__(self, proxy_manager):
        self.proxy_manager = proxy_manager
        self.success = 0
        self.fail = 0
        self.lock = threading.Lock()
        self.base_cookies = None
        self.cookie_lock = threading.Lock()
        self.use_selenium = False

    def _get_cookies_selenium(self):
        """Получает куки через undetected-chromedriver (автоустановка драйвера)."""
        try:
            print(Fore.YELLOW + "[*] Запуск браузера для обхода защиты...")
            options = Options()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920x1080")
            driver = uc.Chrome(options=options, version_main=120)  # version_main можно указать или оставить None
            driver.get('https://guns.lol/')
            time.sleep(3)
            try:
                click_btn = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'click to enter')]"))
                )
                click_btn.click()
                time.sleep(2)
            except:
                pass
            cookies = driver.get_cookies()
            driver.quit()
            cookie_dict = {c['name']: c['value'] for c in cookies}
            print(Fore.GREEN + "[+] Куки получены через Selenium.")
            return cookie_dict
        except Exception as e:
            print(Fore.RED + f"[-] Ошибка Selenium: {e}")
            return None

    def _get_base_cookies(self):
        with self.cookie_lock:
            if self.base_cookies is not None:
                return self.base_cookies

            # 1. Пробуем через requests
            sess = requests.Session()
            sess.headers.update({
                'User-Agent': random.choice(USER_AGENTS),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
            })
            try:
                resp = sess.get('https://guns.lol/', timeout=10)
                if 'click to enter' not in resp.text.lower():
                    self.base_cookies = sess.cookies.get_dict()
                    print(Fore.GREEN + "[+] Куки получены через requests.")
                    return self.base_cookies
                else:
                    print(Fore.YELLOW + "[!] requests не прошёл защиту, пробую Selenium...")
                    self.use_selenium = True
            except Exception as e:
                print(Fore.YELLOW + f"[!] Ошибка requests: {e}, пробую Selenium...")
                self.use_selenium = True

            if self.use_selenium:
                cookies = self._get_cookies_selenium()
                if cookies:
                    self.base_cookies = cookies
                    return self.base_cookies
                else:
                    print(Fore.RED + "[-] Не удалось получить куки.")
                    return None

    def send_view(self, username, proxy, ptype='http'):
        url = f"https://guns.lol/{username}"
        ts = int(time.time() * 1000)
        rand_param = random.randint(100000, 999999)
        url += f"?_={ts}{rand_param}"

        headers = {
            'User-Agent': random.choice(USER_AGENTS),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': random.choice(['en-US,en;q=0.9', 'ru-RU,ru;q=0.9']),
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Referer': random.choice(REFERERS),
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin' if random.random() > 0.5 else 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
            'DNT': '1' if random.random() > 0.3 else '0',
        }

        cookies = self._get_base_cookies()
        if not cookies:
            return False

        sess = requests.Session()
        sess.cookies.update(cookies)
        sess.headers.update(headers)

        if ptype.startswith('socks'):
            try:
                ip, port = proxy.split(':')
                socks_type = socks.SOCKS5 if 'socks5' in ptype else socks.SOCKS4
                s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
                s.set_proxy(socks_type, ip, int(port))
                s.settimeout(10)
                context = ssl.create_default_context()
                s = context.wrap_socket(s, server_hostname='guns.lol')
                s.connect(('guns.lol', 443))
                cookie_str = '; '.join([f'{k}={v}' for k, v in sess.cookies.items()])
                request = f"GET {url} HTTP/1.1\r\n"
                for k, v in headers.items():
                    request += f"{k}: {v}\r\n"
                request += "Host: guns.lol\r\n"
                if cookie_str:
                    request += f"Cookie: {cookie_str}\r\n"
                request += "\r\n"
                s.send(request.encode())
                resp = s.recv(4096)
                s.close()
                return b'200 OK' in resp or b'301' in resp or b'302' in resp
            except:
                return False
        else:
            proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
            try:
                sess.proxies = proxies
                resp = sess.get(url, timeout=10, allow_redirects=True)
                return resp.status_code in [200, 301, 302]
            except:
                return False

    def worker(self, username, proxy_queue):
        while not proxy_queue.empty():
            proxy, ptype = proxy_queue.get()
            if self.send_view(username, proxy, ptype):
                with self.lock:
                    self.success += 1
            else:
                with self.lock:
                    self.fail += 1
            proxy_queue.task_done()
            time.sleep(random.uniform(0.5, 2.0))

    def boost(self, username, views, threads=50, validate=True):
        if not self.proxy_manager.proxies:
            print(Fore.RED + "[-] Нет прокси. Загрузите сначала.")
            return

        if validate:
            self.proxy_manager.validate_proxies(count=min(500, len(self.proxy_manager.proxies)))

        working = self.proxy_manager.get_working()
        if not working:
            print(Fore.RED + "[-] Нет рабочих прокси.")
            return

        proxy_list = working * ((views // len(working)) + 1)
        proxy_list = proxy_list[:views]

        q = queue.Queue()
        for proxy, ptype in proxy_list:
            q.put((proxy, ptype))

        print(Fore.CYAN + f"[*] Запуск {views} просмотров для {username} через {len(proxy_list)} прокси...")
        start = time.time()

        thread_pool = []
        for _ in range(min(threads, q.qsize())):
            t = threading.Thread(target=self.worker, args=(username, q))
            t.start()
            thread_pool.append(t)

        for t in thread_pool:
            t.join()

        elapsed = time.time() - start
        print(Fore.GREEN + f"\n[+] РЕЗУЛЬТАТ:")
        print(Fore.GREEN + f"    Успешно: {self.success}")
        print(Fore.RED + f"    Ошибок: {self.fail}")
        print(Fore.GREEN + f"    Всего: {self.success + self.fail}")
        print(Fore.GREEN + f"    Время: {elapsed:.2f} сек.")
        if elapsed > 0:
            print(Fore.GREEN + f"    Скорость: {(self.success / elapsed):.2f} запросов/сек.")

# ================================================================
# ГЛАВНАЯ ФУНКЦИЯ
# ================================================================

def main():
    print(Fore.MAGENTA + "=" * 70)
    print(Fore.CYAN + f"   GUNS.LOL PROFILE VIEWS BOOSTER – HYBRID v{VERSION}")
    print(Fore.CYAN + f"   Author: {AUTHOR}")
    print(Fore.CYAN + f"   Автоматический обход защиты (requests + Selenium fallback)")
    print(Fore.MAGENTA + "=" * 70)
    print()

    proxy_manager = ProxyManager()
    booster = GunsBooster(proxy_manager)

    while True:
        print(Fore.YELLOW + "\n[Меню]")
        print("1. Загрузить прокси из интернета (30+ источников)")
        print("2. Загрузить прокси из файла")
        print("3. Запустить накрутку")
        print("4. Сохранить рабочие прокси")
        print("5. Показать статистику")
        print("6. Выход")
        choice = input(Fore.CYAN + "Выбор: ").strip()

        if choice == '1':
            proxy_manager.load_from_sources()
        elif choice == '2':
            filepath = input("Путь к файлу: ").strip()
            ptype = input("Тип (http/https/socks4/socks5, по умолчанию http): ").strip() or 'http'
            proxy_manager.load_from_file(filepath, ptype)
        elif choice == '3':
            username = input("Имя пользователя на guns.lol: ").strip()
            if not username:
                print(Fore.RED + "[-] Имя не может быть пустым.")
                continue
            try:
                views = int(input("Количество просмотров (по умолчанию 100): ") or "100")
            except:
                views = 100
            try:
                threads = int(input("Количество потоков (по умолчанию 50): ") or "50")
            except:
                threads = 50
            validate = input("Проверять прокси? (y/n, по умолчанию y): ").strip().lower()
            validate = validate != 'n'
            booster.boost(username, views, threads, validate)
            booster.success = 0
            booster.fail = 0
        elif choice == '4':
            proxy_manager.save_working()
        elif choice == '5':
            print(Fore.CYAN + f"\n[Статистика]")
            print(f"  Всего прокси загружено: {len(proxy_manager.proxies)}")
            print(f"  Рабочих прокси: {len(proxy_manager.working_proxies)}")
        elif choice == '6':
            print(Fore.GREEN + "Выход...")
            break
        else:
            print(Fore.RED + "Неверный выбор.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[!] Прервано пользователем.")
        sys.exit(0)
    except Exception as e:
        print(Fore.RED + f"\n[!] Критическая ошибка: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
