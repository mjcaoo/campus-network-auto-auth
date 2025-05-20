import pathlib

# Script configuration
SCRIPT_DIR = pathlib.Path(r"D:\Repositories\autoauth").resolve()
LOG_DIR = SCRIPT_DIR / "logs"
LOG_FILE = LOG_DIR / "check_auth.log"

# Network configuration
PING_HOST = "223.5.5.5"
CHECK_HOST = "https://www.baidu.com"
LOGIN_GATEWAY = "http://172.208.2.102/"
LOGIN_URL = "http://172.208.2.102/eportal/InterFace.do?method=login"
PAGE_INFO = "http://172.208.2.102/eportal/InterFace.do?method=pageInfo"

# HTTP Headers
HEADERS = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/135.0.0.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': '172.208.2.102'
} 