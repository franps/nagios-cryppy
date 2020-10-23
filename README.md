# certcheck

This script tries to make more accesible and help automate several certificate related issues such as checking expiration and alerting if close to date.

requirements:
`pyOpenSSL`

## check_crl
crl_check is a nagios friendly script to check the expiration date of crls and alert when 30, 15, and 3 days are left.
you can try it on a terminal running 
`./check_crl.py path/to/crl.crl`