#!/usr/bin/env python3
# or usr/bin/env python depending on the version you have

from datetime import datetime
from OpenSSL import crypto as c
import sys

today = datetime.now()

def get_expiration_from_file(certName):
	with open(certName) as f:
		cert = c.load_certificate(c.FILETYPE_PEM, f.read())
		exp_date = datetime.strptime(cert.get_notAfter().decode('ascii'),"%Y%m%d%H%M%SZ")
	return is_expired(exp_date)

def is_expired(exp):
    days_to_exp = (exp-today).days
    if days_to_exp <= 15 :
        print ("CRITICAL Cert about to expire or already expired, run for your lives! : ",days_to_exp, "days to expiration")
        exitcode = 2
    elif days_to_exp < 30 :
        print ("CRITICAL Cert expiration in less than 30 days: ",days_to_exp, "days to expiration")
        exitcode = 2 
    elif days_to_exp < 60: 
        print ("WARNING Cert expiration in less than 60 days: ",days_to_exp, "days to expiration")
        exitcode = 1 
    else:
        print ("OK Cert expires in :",days_to_exp," days to expiration")
        exitcode = 0

    sys.exit(exitcode)

if len(sys.argv)==2:
    get_expiration_from_file(sys.argv[1])
else: 
    print("UNKNOWN Plugin was not called correctly")
    sys.exit(3)

#exp = get_expiration_from_file('testcert.cer')
#print("Cert expiraton: ", exp)
#is_expired(exp)