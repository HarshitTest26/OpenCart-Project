@echo off
pip install --upgrade pytest-html-reporter
pytest -v -s testCases\test_AccountRegistration_01.py
pause
