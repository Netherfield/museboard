@echo off
start cmd /k "call scripts/flask_run.bat"
timeout /t 1
call scripts/open.bat