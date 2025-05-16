import logging
import pytest
import os
import sys

# 添加项目根目录到 Python 路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from utils.encryption import encrypted_password_js_compatible

# 测试数据
TEST_CASES = [
    {
        "name": "测试用例",
        "password": "123456",
        "mac_value": "88d2704ccfb75dcc7ad798252c3ac5e2",
        "public_key_exponent": "10001",
        "public_key_modulus": "94dd2a8675fb779e6b9f7103698634cd400f27a154afa67af6166a43fc26417222a79506d34cacc7641946abda1785b7acf9910ad6a0978c91ec84d40b71d2891379af19ffb333e7517e390bd26ac312fe940c340466b4a5d4af1d65c3b5944078f96a1a51a5a53e4bc302818b7c9f63c4a1b07bd7d874cef1c3d4b2f5eb7871"
    },
    {
        "name": "空密码测试",
        "password": "",
        "mac_value": "88d2704ccfb75dcc7ad798252c3ac5e2",
        "public_key_exponent": "10001",
        "public_key_modulus": "94dd2a8675fb779e6b9f7103698634cd400f27a154afa67af6166a43fc26417222a79506d34cacc7641946abda1785b7acf9910ad6a0978c91ec84d40b71d2891379af19ffb333e7517e390bd26ac312fe940c340466b4a5d4af1d65c3b5944078f96a1a51a5a53e4bc302818b7c9f63c4a1b07bd7d874cef1c3d4b2f5eb7871"
    }
]

def setup_logging():
    """设置日志配置"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

def test_encryption(test_case):
    """测试密码加密过程"""
    setup_logging()
    
    # 构造密码字符串
    password_with_mac = f"{test_case['password']}>{test_case['mac_value']}"
    logging.info(f"测试用例: {test_case['name']}")
    logging.info(f"原始密码: {test_case['password']}")
    logging.info(f"MAC值: {test_case['mac_value']}")
    logging.info(f"组合后的密码: {password_with_mac}")
    
    # 加密过程
    logging.info("开始加密...")
    logging.info(f"公钥指数: {test_case['public_key_exponent']}")
    logging.info(f"公钥模数: {test_case['public_key_modulus']}")
    
    # 执行加密
    encrypted_password = encrypted_password_js_compatible(
        password_with_mac,
        test_case['public_key_exponent'],
        test_case['public_key_modulus']
    )
    
    # 验证结果
    assert encrypted_password is not None, "加密结果不应为空"
    assert isinstance(encrypted_password, str), "加密结果应为字符串"
    assert len(encrypted_password) > 0, "加密结果长度应大于0"
    
    # 输出结果
    logging.info("加密完成")
    logging.info(f"加密后的密码: {encrypted_password}")
    
    return encrypted_password

def test_encryption_error_handling():
    """测试加密错误处理"""
    setup_logging()
    
    # 测试无效的公钥指数
    with pytest.raises(Exception):
        encrypted_password_js_compatible(
            "test>mac",
            "invalid_exponent",
            TEST_CASES[0]['public_key_modulus']
        )
    
    # 测试无效的公钥模数
    with pytest.raises(Exception):
        encrypted_password_js_compatible(
            "test>mac",
            TEST_CASES[0]['public_key_exponent'],
            "invalid_modulus"
        )

if __name__ == "__main__":
    # 运行所有测试用例
    for test_case in TEST_CASES:
        test_encryption(test_case)
    
    # 运行错误处理测试
    test_encryption_error_handling() 