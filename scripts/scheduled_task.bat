@echo off
set TASK_NAME=校园网定时认证
set SCRIPT_PATH=%~dp0..\main.py
set PYTHON_PATH=%~dp0..\.venv\Scripts\python.exe

REM 删除同名任务（如果已存在）
schtasks /delete /tn "%TASK_NAME%" /f

REM 创建定时任务，每 30 分钟运行一次
schtasks /create /tn "%TASK_NAME%" /tr "\"%PYTHON_PATH%\" \"%SCRIPT_PATH%\"" /sc minute /mo 30 /f

echo 定时任务 "%TASK_NAME%" 创建成功！
pause