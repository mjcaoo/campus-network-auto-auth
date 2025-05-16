import subprocess
import requests
import logging
from config import config

def is_network_available():
    """Check if the network is available by pinging a host."""
    try:
        result = subprocess.run(
            ["ping", "-n", "2", config["PING_HOST"]],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except Exception:
        return False

def get_query_string():
    """Get the query string from the login gateway."""
    try:
        text = requests.get(config["LOGIN_GATEWAY"]).text
        href = text.split("top.self.location.href='")[-1].split("'")[0].split("?")[-1]
        return href
    except requests.RequestException as e:
        logging.error(f"获取 queryString 失败: {e}")
        raise

def get_page_info(query_string):
    """Get page information from the authentication server."""
    try:
        payload = "queryString=" + query_string
        result = requests.request("POST", config["PAGE_INFO"], headers=config["HEADERS"], data=payload)
        return result.json()
    except requests.RequestException as e:
        logging.error(f"获取页面信息失败: {e}")
        raise 