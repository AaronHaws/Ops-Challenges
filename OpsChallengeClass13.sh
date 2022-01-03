#!/bin/bash

DOMAIN_LIST="Google.com"

for domain in $DOMAIN_LIST
do
  echo -n "$domain :: "
  whois $domain 
  dig $domain 
  host $domain
  nslookup $domain
    out-file ~/Desktop $ google.txt
done