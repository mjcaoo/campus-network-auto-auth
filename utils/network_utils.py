import subprocess
import requests
import logging
import re
import random
import time
from config import config


# 探测网址列表
PROBE_URLS = [
    "https://detectportal.firefox.com/success.txt",
    "https://www.baidu.com",
    "https://www.163.com",
    "https://www.taobao.com",
    "https://www.jd.com",
    "https://www.aliyun.com",
    "https://www.tencent.com",
    "https://www.bilibili.com",
    "https://www.zhihu.com",
    "https://www.weibo.com",
    "https://www.douban.com",
    "https://www.xiaomi.com",
    "https://www.meituan.com",
]

# 随机User-Agent列表
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0",
]


def get_random_headers():
    """生成随机的请求头"""
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "max-age=0",
        "DNT": "1",  # Do Not Track
    }


def is_network_available():
    """通过检测重定向来判断认证状态"""
    try:
        # 随机选择一个探测网址
        probe_url = random.choice(PROBE_URLS)
        logging.debug(f"使用探测网址: {probe_url}")

        # 添加随机延迟（3-8秒）
        delay = random.uniform(3, 8)
        logging.debug(f"等待 {delay:.1f} 秒后发送请求")
        time.sleep(delay)

        # 使用requests发送请求并获取重定向信息
        response = requests.get(
            probe_url,
            allow_redirects=False,  # 不自动跟随重定向
            timeout=10,  # 增加超时时间
            headers=get_random_headers(),
        )

        # 检查是否重定向到认证网关
        if response.status_code in [301, 302, 307, 308]:
            location = response.headers.get("Location", "").lower()
            if "172.208.2.102" in location:
                logging.info("检测到重定向到认证网关，需要认证")
                return False
        return True
    except requests.RequestException as e:
        logging.error(f"网络检测失败: {e}")
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
        result = requests.request(
            "POST", config["PAGE_INFO"], headers=config["HEADERS"], data=payload
        )
        return result.json()
    except requests.RequestException as e:
        logging.error(f"获取页面信息失败: {e}")
        raise
