# nagios crypto plugins in python (nagios-cryppy)

This scripts try to make more accesible and help automate several certificate related issues such as checking expiration and alerting if close to date.

## check_cert
crl_check is a nagios friendly script to check the expiration date of certs and alert when 60, 30, and 15 days are left. It supports both DER and PEM format, you can try it on a terminal running 

`./check_cert.py path/to/cert.cer`

## check_crl
crl_check is a nagios friendly script to check the expiration date of crls and alert when 30, 15, and 3 days are left.
It supports both DER and PEM format, you can try it on a terminal running 

`./check_crl.py path/to/crl.crl`