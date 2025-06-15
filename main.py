import logging
import time
from utils.logger import setup_logging
from utils.network_utils import is_network_available
from utils.auth import authenticate


def check_and_auth():
    """检查网络状态并在需要时进行认证"""
    if is_network_available():
        logging.debug("网络正常，无需认证")
    else:
        logging.info("检测到需要认证，开始认证流程...")
        try:
            authenticate()
            logging.info("认证完成")
        except Exception as e:
            logging.error(f"认证过程发生错误: {e}")


def main():
    """Main application entry point."""
    setup_logging()
    logging.info("-----------------------------")
    logging.info("开始执行认证脚本")

    # 设置检查间隔时间（秒）
    check_interval = 60  # 60秒检查一次

    try:
        while True:
            # 检查网络状态和认证
            check_and_auth()
            logging.debug(f"等待 {check_interval} 秒后进行下一次检查...")
            time.sleep(check_interval)

    except KeyboardInterrupt:
        logging.info("用户终止程序")
    except Exception as e:
        logging.error(f"程序运行出错: {e}")
    finally:
        logging.info("脚本执行完毕")


if __name__ == "__main__":
    main()
