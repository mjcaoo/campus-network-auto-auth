import sys
import logging
from logging.handlers import TimedRotatingFileHandler
from config import config


def setup_logging():
    """Configure logging for the application."""
    config["LOG_DIR"].mkdir(parents=True, exist_ok=True)

    # 创建基于时间的日志处理器，每48小时轮转一次
    file_handler = TimedRotatingFileHandler(
        config["LOG_FILE"],
        when="H",  # 按小时轮转
        interval=48,  # 每48小时
        backupCount=1,  # 只保留一个备份文件
        encoding="utf-8",
    )

    # 设置日志格式
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)

    # 设置日志级别
    file_handler.setLevel(logging.INFO)  # 文件只记录INFO及以上级别

    # 控制台输出使用更详细的格式
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d %(message)s"
        )
    )
    console_handler.setLevel(logging.DEBUG)  # 控制台显示所有级别

    logging.basicConfig(
        level=logging.DEBUG,  # 根日志器设置为DEBUG级别
        handlers=[file_handler, console_handler],
    )
