import os
import yaml
from pathlib import Path
from typing import Dict, Any

from .base import *

def load_auth_config() -> Dict[str, Any]:
    """Load authentication configuration from YAML file."""
    config_path = Path(__file__).parent / "auth_config.yaml"
    if not config_path.exists():
        raise FileNotFoundError(
            f"认证配置文件不存在: {config_path}\n"
            "请复制 auth_config.example.yaml 为 auth_config.yaml 并填入实际配置"
        )
    
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def load_config() -> Dict[str, Any]:
    """Load all configuration settings."""
    auth_config = load_auth_config()
    
    return {
        # Base configuration
        "SCRIPT_DIR": SCRIPT_DIR,
        "LOG_DIR": LOG_DIR,
        "LOG_FILE": LOG_FILE,
        "PING_HOST": PING_HOST,
        "CHECK_HOST": CHECK_HOST,
        "LOGIN_GATEWAY": LOGIN_GATEWAY,
        "LOGIN_URL": LOGIN_URL,
        "PAGE_INFO": PAGE_INFO,
        "HEADERS": HEADERS,
        
        # Authentication configuration
        "AUTH_CONFIG": auth_config
    }

# Create a global config object
config = load_config() 