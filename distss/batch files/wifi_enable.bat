@echo off 
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Wifi\AllowWiFi" /v value /t REG_DWORD /d 1 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Wifi\AllowManualWiFiConfiguration" /v value /t REG_DWORD /d 1 /f
shutdown /r /t 0