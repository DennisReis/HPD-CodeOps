#!/usr/bin/env python3

import subprocess

def cria_dir():
    global opa
    opa = input("Digite o nome do dir desejado: ")
    subprocess.call(['mkdir', opa])
    for i in range(1,40):
        subprocess.call(['touch', str(i)], cwd=opa)

def list_dir():
    subprocess.call(['ls', opa])

def del_dir():
    subprocess.call(['rm', '-rf', opa])

cria_dir()
list_dir()
del_dir()
