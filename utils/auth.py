import re
import logging
import requests
from config import config
from utils import encrypted_password_js_compatible

def construct_auth_data(username, password_encrypted, service, query_string):
    """Construct authentication data for the login request."""
    return {
        "userId": username,
        "password": password_encrypted,
        "service": service,
        "queryString": query_string,
        "operatorUserId": "",
        "passwordEncrypt": "true"
    }

def auth_request(data):
    """Send authentication request to the server."""
    try:
        response = requests.post(config["LOGIN_URL"], headers=config["HEADERS"], data=data, verify=False, timeout=10)
        logging.info(f"认证响应状态码: {response.text}")
        logging.info("认证完成")
    except requests.RequestException as e:
        logging.error(f"认证失败: {e}")
        raise

def authenticate():
    """Main authentication process."""
    from utils.network_utils import get_query_string, get_page_info
    
    try:
        # Get query string and MAC value
        query_string = get_query_string()
        m = re.search(r"mac=([^&]+)", query_string)
        mac_value = m.group(1) if m else None
        logging.info(f"query_string: {query_string}")
        logging.info(f"mac_value: {mac_value}")

        # Get page info and encryption parameters
        pageinfo = get_page_info(query_string)
        public_key_exponent = pageinfo['publicKeyExponent']
        public_key_modulus = pageinfo["publicKeyModulus"]
        logging.info(f"publicKeyExponent: {public_key_exponent}")
        logging.info(f"publicKeyModulus: {public_key_modulus}")

        # Encrypt password and send authentication request
        password_encrypted = encrypted_password_js_compatible(
            config["AUTH_CONFIG"]["password"] + ">" + mac_value,
            public_key_exponent,
            public_key_modulus
        )
        logging.info(f"Encrypted password: {password_encrypted}")

        data = construct_auth_data(
            config["AUTH_CONFIG"]["username"],
            password_encrypted,
            config["AUTH_CONFIG"]["service"],
            query_string
        )
        auth_request(data)

    except requests.RequestException as e:
        logging.error(f"请求失败: {e}")
        raise 