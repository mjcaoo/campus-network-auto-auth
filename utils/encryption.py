"""
加密工具模块，提供密码加密相关的功能。
"""

def encrypted_password_js_compatible(password: str, public_key_exponent: str, public_key_modulus: str) -> str:
    """
    使用RSA公钥加密密码，生成与JavaScript兼容的加密结果。
    
    Args:
        password: 需要加密的密码
        public_key_exponent: RSA公钥指数
        public_key_modulus: RSA公钥模数
        
    Returns:
        str: 加密后的密码字符串
    """
    # 将公钥参数转换为整数
    e = int(public_key_exponent, 16)
    n = int(public_key_modulus, 16)
    
    # 将密码转换为字节
    password_bytes = password.encode('utf-8')
    
    # 将字节转换为整数
    m = int.from_bytes(password_bytes, 'big')
    
    # 使用RSA加密: c = m^e mod n
    c = pow(m, e, n)
    
    # 将加密结果转换为十六进制字符串
    return hex(c)[2:] 