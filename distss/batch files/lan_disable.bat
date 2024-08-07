@echo off
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\ADMX_NetworkConnections\NC_LanProperties" /v policytype /t REG_DWORD /d 0 /f 
reg add "Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\ADMX_NetworkConnections\NC_LanConnect" /v policytype /t RED_DWORD /d 0 /f