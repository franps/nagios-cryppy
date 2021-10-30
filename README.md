# nagios crypto plugins in python (nagios-cryppy)

This scripts try to make more accesible and help automate several certificate related issues such as checking expiration and alerting if close to date.

## check_cert
check_cert is a nagios friendly script to check the expiration date of certs and alert when 60, 30, and 15 days are left. It supports both DER and PEM format, you can try it on a terminal running 

`./check_cert.py path/to/cert.cer`

## check_certs_folder
check_certs_folder is a nagios friendly script to check the expiration date of all certs in a folder and alert when 60, 30, and 15 days are left. It supports both DER and PEM format, you can try it on a terminal running 

`./check_certs_folder.py path/to/folder/`

## check_crl
check_crl is a nagios friendly script to check the expiration date of crls and alert when 30, 15, and 3 days are left.
It supports both DER and PEM format, you can try it on a terminal running 

`./check_crl.py path/to/crl.crl`

## check_ssl
check_ssl is a nagios friendly script to check the expiration date of ssl certs.
It supports PEM format, you can try it on a terminal running 

`./check_ssl.py www.example.com`

## check_jks
check_jks is a nagios friendly script to check the expiration date of certs inside a JKS.
It supports JKS with one or more certs inside, you can try it on a terminal running 

`./check_jks.py example.jks passphrase`