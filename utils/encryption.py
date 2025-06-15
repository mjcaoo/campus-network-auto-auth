"""
加密工具模块，提供密码加密相关的功能。
"""


def encrypted_password_js_compatible(
    password: str, public_key_exponent: str, public_key_modulus: str
) -> str:
    """
    使用RSA公钥加密密码，生成与JavaScript兼容的加密结果。

    Args:
        password: 需要加密的密码
        public_key_exponent: RSA公钥指数（十六进制字符串）
        public_key_modulus: RSA公钥模数（十六进制字符串）

    Returns:
        str: 加密后的密码字符串（十六进制，带前导零）
    """
    e = int(public_key_exponent, 16)
    n = int(public_key_modulus, 16)

    password_bytes = password.encode("utf-8")
    m = int.from_bytes(password_bytes, "big")

    c = pow(m, e, n)

    # 获取模数的十六进制长度，补全前导零
    modulus_hex_len = len(public_key_modulus)
    encrypted_hex = hex(c)[2:].zfill(modulus_hex_len)

    return encrypted_hex
