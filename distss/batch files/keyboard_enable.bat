 @echo off
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\i8042prt" /v Start /t REG_DWORD /d 3 /f
shutdown /r /t 0