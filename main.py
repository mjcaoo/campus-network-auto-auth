import logging
from utils.logger import setup_logging
from utils.network_utils import is_network_available
from utils.auth import authenticate

def main():
    """Main application entry point."""
    setup_logging()
    logging.info("-----------------------------")
    logging.info("开始执行认证脚本")

    if is_network_available():
        logging.info("网络正常，无需认证")
    else:
        logging.info("网络异常，尝试进行认证...")
        try:
            authenticate()
        except Exception as e:
            logging.error(f"认证过程发生错误: {e}")

    logging.info("脚本执行完毕")

if __name__ == "__main__":
    main()
