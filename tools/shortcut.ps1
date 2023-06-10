# Сценарий shortcut создает ярлык приложения на рабочем столе
$ShellFoldersDir = Get-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
$DesktopDir = $ShellFoldersDir.Desktop
$CurrentDir = Get-Location
$AppFile = "$CurrentDir/main.exe"
$LinkFile = "$DesktopDir\MCrypt.lnk"
$shell = New-Object -comObject Wscript.Shell
$shortcut = $shell.CreateShortcut($LinkFile)
$shortcut.TargetPath = $AppFile
$shortcut.WorkingDirectory = "$CurrentDir\"
$shortcut.Save()