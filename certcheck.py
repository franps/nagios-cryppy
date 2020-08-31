from datetime import datetime
from OpenSSL import crypto as c

today = datetime.now()

def get_expiration_from_file(certName):
	with open(certName) as f:
		cert = c.load_certificate(c.FILETYPE_PEM, f.read())
		exp = datetime.strptime(cert.get_notAfter().decode('ascii'),"%Y%m%d%H%M%SZ")
	return exp

def is_expired(exp):
	days_to_exp = (exp-today).days
	if days_to_exp <= 0 :
		print ("Cert about to expire or already expired, run for your lives! : ",days_to_exp, "days to expiration")
	if days_to_exp < 30 :
		print ("Expiration in less than 30 days: ",days_to_exp, "days to expiration")
	elif days_to_exp < 60: 
		print ("Expiration in less than 60 days: ",days_to_exp, "days to expiration")

exp = get_expiration_from_file('testcert.pem')
print("Cert expiraton: ", exp)
is_expired(exp)