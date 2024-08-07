@echo off
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\PrecisionTouchPad\Status" /v Enabled /t REG_DWORD /d 0 /f 
shutdown /r /t 0