# Сценарий template выполняет конвертацию заданного файла .ui в сценарий Python
$file = $args[0]
pyuic5 -x "../src/views/templates/$file.ui" -o "../src/views/$file.py"