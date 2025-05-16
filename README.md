# 校园网自动认证工具

## 介绍

因校园网会不定时退出登录状态，导致无法访问网络。

本工具通过定时任务自动登录校园网，保持网络连接。

## 使用方法

### 1. 安装依赖

通过[requirements.txt](requirements.txt)安装依赖。

### 2. 修改配置

复制`config`目录下的[auth_config.example.yaml](config/auth_config.example.yaml)文件为`auth_config.yaml`，并根据需要修改配置。

### 3. 测试

尝试运行[test_encryption.py](scripts/test_encryption.py)脚本，检查是否代码是否正常运行。

### 4. 运行

使用[main.py](main.py)运行程序。

### 5. 定时任务

Windows平台可以手动添加定时任务，同时[scheduled_task.bat](scripts/scheduled_task.bat)可帮助创建（该脚本尚未进行测试）。
