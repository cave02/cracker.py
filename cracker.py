###########librerias necesarias###########
import hashlib #libreria para el hash
import argparse #libreria de las funciones args
import pyfiglet #libreria para el banner porque me da flojera lol
################args######################
parser = argparse.ArgumentParser()
parser.add_argument("-dic",help="diccionario")
parser.add_argument("-buscar",help="fila que contiene hashes")
parser.add_argument('-hash',help="hash")
args = parser.parse_args()
######################################
##### cosas pa que sea vea chido #####
info = "[" + "\033[36m" + "Info" + "\033[0m" + "]"
##########################
#blake2b
#blake2s
#recordatorio##############
#g = hashlib.md5(x.encode())
#z = g.hexdigest()
###########banner###########
banner = pyfiglet.figlet_format("CRACKER.py")
print("\033[31m"+banner+"\033[0m")
good = ""
file = args.buscar
password = args.hash
wordlist = args.dic
pro = "\033[0m"+"["+"\033[32m"+"+"+"\033[0m"+"]"

def crack(password,wordlist):
        if len (password) == 32 :
                print("\033[0m")
                with open(wordlist,"r") as infile: #aqui abre el diccionario
                        for line in infile:
                                line = line.strip() #cheka las contraseñas
                                linehash = hashlib.md5(line.encode()).hexdigest() #convierte las palabras en el diccionario en hash
                                if str(linehash) == str(password): #si el hash y la contraseña coincide
                                        print(good)
                                        print(info+" tipo : md5 ")
                                        print()
                                        print(line),exit() #escribe la contraseña

        elif len(password) == 40 :
                with open(wordlist,"r") elif len(password) == 56 :
                with open(wordlist,"r")as infile:
                        for line in infile:
                                line = line.strip()
                                linehash = hashlib.sha3_224(line.encode()).hexdigest()
                                if str(linehash) == str(password):
                                        print(good),print(info+" tipo : sha3_224")
                                        print()
                                        print(line)
                                        exit()

        elif len(password) == 64 :
                with open(wordlist,"r")as infile:
                        for line in infile:
                                line = line.strip()
                                linehash = hashlib.sha256(line.encode()).hexdigest()
                                linehash2 = hashlib.blake2s(line.encode()).hexdigest()
                                if str(linehash2) == str(password):
                                        print(good),print(info+" tipo : blake2s")
                                        print(line)
                                        exit()
                                if str(linehash) == str(password):
                                        print(good),print(info+" tipo : sha256"),print(line),exit()

        elif len(password) == 96 :
                with open(wordlist,"r")as infile:
                        for line in infile:
                                line = line.strip()
                                linehash = hashlib.sha384(line.encode()).hexdigest()
                                if str(linehash) == str(password):
                                        print(good),print(info+" tipo : sha384"),print(line),exit()
        elif len(password) == 128 :
                with open(wordlist,"r") as infile:
                        for line in infile:
                                line = line.strip()
                                linehash = hashlib.sha512(line.encode()).hexdigest()
                                linehash2 = hashlib.blake2b(line.encode()).hexdigest()
                                if str(linehash2) == str(password):
                                        print(good),print(info+" tipo : blake2b")
                                        print()
                                        print(line)
                                        exit()
                                if str(linehash) == str(password):
                                        print(good)
                                        print(info+" tipo : sha512")
                                        print()
                                        print(line)
                                        exit()

def filek(file,info):
        with open(file,"r")as infile:
                for line in infile:
                        line = line.strip()
                        if len(line) == 32 :
                                print()
                                print(info+" posible hash encontrado")
                                print()
                                print(line)
                        elif len(line) == 40 :
                                print()
                                print(info+"posible hash encontrado")
                                print()
                                print(line)
                        elif len(line) == 56 :
                                print()
                                print(info+"posible hash encontrado")
                                print()
                                print(line)
                        elif len(line) == 64 :
                                print()
                                print(info+"posible hash encontrado")
                                print()
                                print(line)
                        elif len(line) == 96 :
                                print()
                                print(info+"posible hash encontrado")
                                print()
                                print(line)
                        elif len(line) == 32 :
				print(info+"posible hash encontrado")
				print(line)
	exit()

if wordlist:
	crack(password,wordlist)
if file:
	filek(file,info)
if password:
	brute_p()
print("----------------------------------")
print("contraseña no desifrada!") #si la contraseña no se encuentra
print("intente con otro diccionario ")
exit()
