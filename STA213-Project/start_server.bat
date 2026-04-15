@echo off
echo 正在启动本地服务器...
echo 请在浏览器中打开：
echo http://localhost:8000/bangumi_dashboard.html
echo.
server.exe file-server --listen :8000
pause
