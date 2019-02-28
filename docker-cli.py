#!/usr/bin/env python3

import docker
import argparse

def listar(self):
    """Listando os containers e suas respectivas imagens"""
    client = docker.from_env()
    get_all = client.containers.list()
    for cada_container in get_all:
        conectando = client.containers.get(cada_container.id)
        print("O container %s utiliza a imagem %s e esta rodando o comando %s" %(conectando.short_id, conectando.attrs['Config']['Image'], conectando.attrs['Config']['Cmd']))

parser = argparse.ArgumentParser(description="Meu CLI docker zica feito durante a aula do HPD.")
subparser = parser.add_subparsers()

listar_opt = subparser.add_parser('listar')
listar_opt.set_defaults(func=listar)

cmd = parser.parse_args()
cmd.func(cmd)

#listar()
