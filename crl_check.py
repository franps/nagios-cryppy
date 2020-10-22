from datetime import datetime
from OpenSSL import crypto
import subprocess
import sys

today = datetime.now()

def get_expiration_from_file(crlName):
    with open(crlName) as crl:
        try:
            if "BEGIN X509 CRL" in crl.read():
                format = "PEM"
        except UnicodeDecodeError as e: # trying to read DER format will throw this error, not fancy but effective
            format = "DER"

    nextUpdate = subprocess.check_output(["/usr/bin/openssl", "crl", "-inform", format, "-noout", "-nextupdate", "-in", crlName], stderr=subprocess.STDOUT).decode('ascii')
    nextUpdate = nextUpdate.split("=")[1][:-1] # Data before splitting: 'nextUpdate=Oct 28 04:57:01 2020 GMT\n'
    exp = datetime.strptime(nextUpdate,"%b %d %H:%M:%S %Y %Z")

    return exp

def is_expired(exp):
    days_to_exp = (exp-today).days
    if days_to_exp <= 3 :
        print ("CRITICAL CRL about to expire or already expired, run for your lives! : ",days_to_exp, "days to expiration")
        exitcode = 2
    elif days_to_exp < 15 :
        print ("CRITICAL CRL expiration in less than 15 days: ",days_to_exp, "days to expiration")
        exitcode = 2 
    elif days_to_exp < 30: 
        print ("WARNING CRL expiration in less than 30 days: ",days_to_exp, "days to expiration")
        exitcode = 1 
    else:
        print ("OK CRL expires in :",days_to_exp," days to expiration")
        exitcode = 0

    sys.exit(exitcode)

#exp = get_expiration_from_file('testcrl.crl')
#print("Crl expiraton: ", exp)
#is_expired(exp)