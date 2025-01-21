rmdir /s /q .\dist
rmdir /s /q .\build
python setup.py sdist bdist_wheel
python -m twine upload dist\*