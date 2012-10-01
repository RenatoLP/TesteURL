# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 09:20:56 2012

@author: renatolp
"""

import urllib2 
import datetime
import socket

a = open('/home/renatolp/teste.txt','r')
tlinha = a.readlines()

try:
    for url in tlinha:
        url = url.strip()
        print url
#        ip = socket.gethostbyname(url)
#        print ip   
        t1= datetime.datetime.now()
        t1.microsecond
        req = urllib2.Request(url)  
        urllib2.urlopen(req)
        t2 = datetime.datetime.now()
        t2.microsecond
        tresposta = t2-t1
        print "Tempo de resposta em microsegundos: "
        print tresposta
        print "\t"
        
except urllib2.HTTPError, e:
        print 'Erro codigo : ', e.code
except urllib2.URLError, e:
    print 'Falhou na conexao com o servidor.'
    print 'Razao: ', e.reason
else:
    print "Tudo OK"
   
 #Parte do codigo onde identifica o codigo do erro e da um resumo do erro
#if (self.verbose and BaseHTTPServer.BaseHTTPRequestHandler.responses.has_key(e.code)):
#            title, msg = BaseHTTPServer.BaseHTTPRequestHandler.responses[e.code]
#            print title + ": " + msg
