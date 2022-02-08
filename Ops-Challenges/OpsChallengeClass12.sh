$env:PSModulePath

function ipconfigall() {
    
    ipconfig /all | select-string "IPv4"
    
}
echo ($ipconfigall) > Network_report.txt
