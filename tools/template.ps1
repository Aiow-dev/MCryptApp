# Сценарий template выполняет конвертацию заданного файла .ui в сценарий Python
$file = $args[0]
pyuic5 -x "../views/templates/$file.ui" -o "../views/$file.py"