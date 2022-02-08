
#!/usr/bin/env powershell

function logon() {
  $logon = Get-WinEvent -MaxEvents 100 -LogName Security | Where-Object {$_.ID -eq 4624 -or $_.ID -eq 4672}
  echo $logon > userslog.txt
}

