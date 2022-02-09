#! Bin/Bash


dir /var/log/syslog /AD unicode > FoldersList.txt
dir /var/log/wtmp /AD unicode > FoldersList.txt
find /var/log/syslog -mtime +N_DAYS -exec rm {} \
find /var/log/wtmp -mtime +N_DAYS -exec rm {} \
dir /var/log/syslog /AD unicode > FoldersList.txt
dir /var/log/wtmp /AD unicode > FoldersList.txt