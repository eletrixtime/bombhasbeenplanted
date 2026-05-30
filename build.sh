rm build 
rm dist
pyinstaller --onefile --noconsole --add-data "planted.wav;." app.py