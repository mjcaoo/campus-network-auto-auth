import os
import sys

# 添加项目根目录到 Python 路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from utils.network_utils import is_network_available_by_requests

if __name__ == "__main__":
    print("Checking network availability")
    network = is_network_available_by_requests()
    if network:
        print("Network is available")
    else:
        print("Network is not available")
