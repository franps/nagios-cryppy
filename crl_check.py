from datetime import datetime
from OpenSSL import crypto
import subprocess

today = datetime.now()

def get_expiration_from_file(crlName):
    nextUpdate = subprocess.check_output(["/usr/bin/openssl", "crl", "-inform", "PEM", "-noout", "-nextupdate", "-in", "testcrl.crl"], stderr=subprocess.STDOUT).decode('ascii')
    nextUpdate = nextUpdate.split("=")[1][:-1]
    exp = datetime.strptime(nextUpdate,"%b %d %H:%M:%S %Y %Z")

    return exp

def is_expired(exp):
	days_to_exp = (exp-today).days
	if days_to_exp <= 0 :
		print ("Crl about to expire or already expired, run for your lives! : ",days_to_exp, "days to expiration")
	if days_to_exp < 15 :
		print ("Expiration in less than 15 days: ",days_to_exp, "days to expiration")
	elif days_to_exp < 30: 
		print ("Expiration in less than 30 days: ",days_to_exp, "days to expiration")

exp = get_expiration_from_file('testcrl.crl')
print("Crl expiraton: ", exp)
is_expired(exp)