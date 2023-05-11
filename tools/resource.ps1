# Сценарий resource выполняет конвертацию заданного файла .qrc в сценарий Python
$file = $args[0]
$outputFile = $file + "_rc"
pyrcc5 "../resources/$file.qrc" -o "../resources/$outputFile.py"