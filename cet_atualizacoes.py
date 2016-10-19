#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests,telepot,random,time
from bs4 import BeautifulSoup

# Esse Bot foi desenvolvido por mim para acompanhar as atualizacoes do processo seletivo CET 2016 - Cabo Especialista Temporario 2016 do exercito Brasileiro e me notificar pelo telegram.
# Jhonathan Davi A.K.A jh00nbr / Insightl4b lab.insightsecurity.com.br
# Blog: lab.insightsecurity.com.br
# Github: github.com/jh00nbr
# Twitter @jh00nbr

__author__ = "Jhonathan Davi A.K.A jh00nbr"
__email__ = "jhoon@rtfm-ctf.org"

config = {"bot_key":"key_do_seu_bot","grupo_id":id_do_grupo(int),"url":"http://www.11rm.eb.mil.br/index.php/ultimas-noticias/143-cet-cabo-especialista-temporario-2016"}
bot = telepot.Bot(config['bot_key'])
group = config['grupo_id']

qnt_novidades = 10 # Quantidade de noticias em 19/10/2016

def carregar_useragents():
    uas = []
    with open("user-agents.txt", 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[0:-1-0])
    random.shuffle(uas)
    return uas

def verificar_novidades():
    ua = random.choice(carregar_useragents())
    req = requests.get(config['url'],headers={'User-Agent': ua})
    soup = BeautifulSoup(req.content,'html.parser')

    conteudo_div = soup.find('div',{'class':'item-page'})
    atualizacoes = conteudo_div.findAll('a')

    novidades = []

    for novidade in atualizacoes:
        if novidade.string:
            novidades.append(novidade.string)
            qnt_novas_novidades = len(novidades)
            novidade = novidade.string 

    if int(qnt_novas_novidades) > qnt_novidades:
        novidade = novidades[1]
        qnt_novidades += 1
        bot.sendMessage(group,novidade)
        print novidade, " | Novidades: ", qnt_novidades
    else:
        print "[+] Sem novidades :("

if __name__ == '__main__':
    while True:
        time.sleep(600) # Verifica de 7 em 7 minutos
        verificar_novidades()
