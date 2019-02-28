#!/usr/bin/env python3

import subprocess
import argparse 

def criar(args):
    """Cria o diretorio desejado"""
    diretorio = args.nome
    print(diretorio)
    subprocess.call(['mkdir', args.nome])
    for i in range(1,40):
        subprocess.call(['touch', str(i)], cwd=args.nome)

def listar(args):
    """Lista o diretorio desejado"""
    subprocess.call(['ls', args.nome])

def deletar(args):
    """Deleta o diretorio desejado"""
    subprocess.call(['rm', '-rf', args.nome])

def desligar_reiniciar(args):
    """Desliga ou Reinicia a maquina"""
    if args.comando == 'desligar':
        subprocess.call(['poweroff'])
    elif args.comando == 'reiniciar':
        subprocess.call(['reboot'])
    else:
        print('Comando não reconhecido, favor digitar desligar ou reiniciar.')

def listar_rede(args):
    """Lista a interface de rede desejada"""
    subprocess.call(['ifconfig', args.interface])

parser = argparse.ArgumentParser(description="Comando para criar e listar diretorios durante a aula.")

subparser = parser.add_subparsers()

criar_dir = subparser.add_parser('criar')
criar_dir.add_argument('--nome', required=True)
criar_dir.set_defaults(func=criar)

listar_dir = subparser.add_parser('listar')
listar_dir.add_argument('--nome', required=True)
listar_dir.set_defaults(func=listar)

deletar_dir = subparser.add_parser('deletar')
deletar_dir.add_argument('--nome', required=True)
deletar_dir.set_defaults(func=deletar)

desligar_reiniciar_maquina = subparser.add_parser('desligar_reiniciar')
desligar_reiniciar_maquina.add_argument('--comando', required=True)
desligar_reiniciar_maquina.set_defaults(func=desligar_reiniciar)

listar_interface_rede =  subparser.add_parser('listar_rede')
listar_interface_rede.add_argument('--interface', required=True)
listar_interface_rede.set_defaults(func=listar_rede)

cmd = parser.parse_args()
cmd.func(cmd)
