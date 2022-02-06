try:
	import hashlib
	import argparse
	import os
except ImportError:
	print("\033[33m [!] instalando herramientas\033[0m")
	os.system("pip install argparse && pip install hashlib")

parser = argparse.ArgumentParser()
parser.add_argument("-H",help="hash a romper")
parser.add_argument("-d",help="diccionario a utilizar")
parser.add_argument("-f",help="fila que contiene hashes")

a = parser.parse_args()
print("\033[34m [*] creador : cave02")
print("\033[32;1m [*] github : https://github.com/cave02 \033[0m")

passwd = a.H
wordlist = a.d
file = a.f
def crack(passwd,wordlist):
	print("\033[32m")

	if len(passwd) == 32 :
		print("\033[33m[!] tipo md5 \033[0m")
		h = hashlib.md5
	elif len(passwd) == 40 :
		print("\033[33m[!] tipo sha1 \033[0m")
		h = hashlib.sha1
	elif len(passwd) == 56 :
		print("\033[33m[!] tipo sha224 \033[0m")
		h = hashlib.sha224
	elif len(passwd) == 64 :
		print("\033[33m[!] tipo sha256 \033[0m")
		h = hashlib.sha256
	elif len(passwd) == 96 :
		print("\033[33m[!] tipo sha384 \033[0m")
		h = hashlib.sha384
	elif len(passwd) == 128 :
		print("\033[33m[!] tipo sha512 \033[0m")
		h = hashlib.sha512
	else :
		print("\033[31m[×] hash no combatible\033[0m")
		exit()
	with open(wordlist,"r") as infile:
		print("\033[34m[+] rompiendo...")
		for line in infile:
			line = line.strip()
			linehash = h(line.encode()).hexdigest()
			if linehash == passwd :
				print("\033[32;1m diccionario : "+wordlist)
				print("  \033[33m"+passwd+"\033[34m >>> \033[32m"+line)
				print("\033[0m")
				exit()
def files(file,wordlist):
	with open(file,"r")as l:
		for line in l:
			line = line.strip()
			if len(line) == 32 :
				print()
				print("hash encontrado :"+line)
				with open(wordlist,"r") as word:
					for words in word:
						lol = words.strip()
						hashdic = hashlib.md5(lol.encode()).hexdigest()
						if hashdic == line :
							print()
							print("fila : "+file)
							print("diccionario : "+wordlist)
							print("\033[33m"+line+"\033[0m >>> \033[32m"+lol)
							print("\033[0m")
	exit()

if passwd:
	crack(passwd,wordlist)
if file:
	files(file,wordlist)
print("\033[0m")
print("\033[31m [×] hash no desifrado")
print("         no se encontro la contraseña en "+wordlist)
print("         intente con otros diccionarios")
print("\033[0m")
