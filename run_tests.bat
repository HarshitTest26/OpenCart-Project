@echo off
rem Uninstall the old, incompatible plugin
pip uninstall pytest-html-reporter -y

rem Install the correct and compatible plugin
pip install pytest-html

rem Run the tests and generate the report
pytest -v -s --html="reports\report.html" testCases\test_AccountRegistration_01.py

pause
