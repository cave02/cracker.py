try:
	import hashlib
	import argparse
	import os
	import datetime
	import time
except ImportError:
	print("\033[33m [!] instalando herramientas\033[0m")
	os.system("pip install argparse && pip install hashlib")

parser = argparse.ArgumentParser()
parser.add_argument("-H",help="hash a romper")
parser.add_argument("-d",help="diccionario a utilizar")
parser.add_argument("-f",help="fila que contiene hashes")

a = parser.parse_args()
print("\033[32;1m[*] creador      : cave02")
print("[*] github       : \033[36;1mhttps://github.com/cave02 \033[0m")
print("[*] version      : 2.0")
passwd = a.H
wordlist = a.d
file = a.f
now = datetime.datetime.now()
final = time.time()
empiezo = time.time()
time_actual = now.strftime('%H:%M:%S %Y/%m/%d')
def crack(passwd,wordlist,now,final,empiezo):
	print("\033[32;1m")

	if len(passwd) == 32 :
		print("[*] tipo         :\033[33m md5 \033[0m")
		h = hashlib.md5
	elif len(passwd) == 40 :
		print("[*] tipo         : \033[33msha1 \033[0m")
		h = hashlib.sha1
	elif len(passwd) == 56 :
		print("[*] tipo         : \033[33msha224 \033[0m")
		h = hashlib.sha224
	elif len(passwd) == 64 :
		print("[*] tipo         : \033[33msha256 \033[0m")
		h = hashlib.sha256
	elif len(passwd) == 96 :
		print("[*] tipo         : \033[33msha384 \033[0m")
		h = hashlib.sha384
	elif len(passwd) == 128 :
		print("[*] tipo         : \033[33msha512 \033[0m")
		h = hashlib.sha512
	else :
		print("\033[31m[×] hash no combatible\033[0m")
		exit()
	with open(wordlist,"r") as infile:
		for line in infile:
			line = line.strip()
			linehash = h(line.encode()).hexdigest()
			if linehash == passwd :
				time.sleep(5)
				print("\033[32;1m[*] tiempo local : \033[33m"+str(time_actual)+"\033[32m")
				print("[*] crackeado en : "+str(final - final))
				print("[*] diccionario  : \033[33m"+wordlist+"\033[32m")
				print("[*] hash         : \033[33m"+linehash+"\033[32m")
				print("[\033[93;1m+\033[32;1m] contraseña   : \033[103m"+line+"\033[0m")
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
							print("[*] fila        : "+file)
							print("[*] diccionario : "+wordlist)
							print("[*] hash        : "+line)
							print("[\033[32;1m+\033[0m] contraseña  : "+lol)
							print()
	exit()

if passwd:
	crack(passwd,wordlist,now,empiezo,final)
if file:
	files(file,wordlist)
print("\033[0m")
print("\033[31m [×] hash no desifrado")
print("         no se encontro la contraseña en "+wordlist)
print("         intente con otros diccionarios")
print("\033[0m")
