#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from Crypto.Cipher import AES
#import base64
#import os

import sys
sys.path.insert(0,"/home/art/prgosay/requests/")
import requests

import time
import socket
import hashlib
import cPickle as pickle

from Crypto.Cipher import AES
from Crypto import Random


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
#import math
#import threading

HOST = 'localhost'
PORT = 8000
BUFSIZE = 2048
ADDR = (HOST,PORT)


SEANSKEY = ''
sessionkey = ''


HOSTNAMESERVER = 'gosay.net.ru'
public_key_Server_DB = ['0x3dd','0x19a9aa6a0205d2a82bb1f98d1531e1e466b07d8f5cfed38bea5f9ce4ded8af6872988f0abc80a1636b4eb05f2f6577538b3f638a9103ca779f33880ac6e080cae1ee8bfdc1732396ee1ccec5deeb6e93c1bc8c90de85bc445396c5eba258e780d7bf8b9dc0233f918ce7d5aacf69250721f55c1e0db0ced19d3e40e16ce53d9']
 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverCertificateMessage = '1'

serverKeyExchangeMessage = '3'

STATUSCONNECTION = False
ACCEPTEDTMESSAGE = []
PUBLICKEYFROMSERVER = []
clientKeyExchangeMessage = []



def getHashMD5(text):
	hash_md5 = hashlib.md5()
	hash_md5.update(str(text))
	return hash_md5.hexdigest()
 
def messageProcessing(data):
    
    print'.......mess proc........'
    RESULT = pickle.loads(data)    

    return RESULT
   
 
 
def createClientKeyExchangeMessage(publicKeyfromServer):
    sessionkey = Random.new().read(32)      # 256 bit
    #print sessionkey
    listMess = []
    listHesh = []
    
    ExchangeMessage = []
    
    listMess.append('2')
    listMess.append(sessionkey)
    listHesh.append(getHashMD5(listMess))
    
    ExchangeMessage.append(listMess)
    ExchangeMessage.append(listHesh)

    bytesForSend = pickle.dumps(ExchangeMessage,2)
    key = RSA.importKey(publicKeyfromServer)
    cipher = PKCS1_OAEP.new(key)
    clientExchangeMessage = cipher.encrypt(bytesForSend)
    
    return clientExchangeMessage
          
        
def closeConnect():
        sock.shutdown()
        print 'conn close!'    
    
                
def checkServerKeyExchangeMessage(data):
    sendMoreClientKeyExchangeMessage = True
    statusConnection = False
    if not data:
        closeConnect()
        sendMoreClientKeyExchangeMessage = False
        statusConnection = False
    else:
        clientKeyExchangeMessage = messageProcessing(data)
        if(clientKeyExchangeMessage == ['3','key passed to the encrypted mode']):
            sendMoreClientKeyExchangeMessage = False
            statusConnection = True
            print 'server connection estabilished'
        if(clientKeyExchangeMessage == ['3','error encrypted connection']):
            sendMoreClientKeyExchangeMessage = True
            statusConnection = False
            print 'server connection error'
    
    return sendMoreClientKeyExchangeMessage, statusConnection
  

            
def estabilishConnection():
    sock.settimeout(15)
    sock.connect(ADDR)
    statusConnection = False

    data = sock.recv(1024)

    Data = messageProcessing(data)    
    print 'bery hesh'
    hesh = getHashMD5(Data[0])
    if(Data[1][0] == hesh):
        print 'ok!\n'
        f = open('/home/art/Documents/alisapublickey.txt','rb')
        publicKeyfromServer = f.read(); f.close()
        print publicKeyfromServer
        
        if(Data[0][1] == publicKeyfromServer):
            print 'pubkey True\n'
            iv = Random.new().read(16)              # 128 bit
            
            sock.send(createClientKeyExchangeMessage(publicKeyfromServer))
            #print sessionkey
            #print iv            
            #objAES = AES.new(sessionkey, AES.MODE_CFB, iv)
            #ciphertext = iv + objAES.encrypt('hi')
            
            #print ciphertext
            
    else:
        print 'tobi pizda'
        statusConnection = False
        
        
    if(statusConnection):
        #SEANSKEY = createClientKeyExchangeMessage(PUBLICKEYFROMSERVER)
        print 'statusConnection true ...... action pacage'
        
        
    print statusConnection   
    return statusConnection





      
def estabilishConnectio():
    #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(15)
    sock.connect(ADDR)
    statusConnection = False  
    
    statusCreateClientKeyExchangeMessage = False
    while(statusConnection == False):
        data = sock.recv(1024)
        #Data = messageProcessing(data)
        Data = messageProcessing(data)    
        print 'bery hesh'
        hesh = getHashMD5(Data[0])
        if(Data[1][0] == hesh):
            print 'ok!\n'
        else:
            print 'tobi pizda'
        #ACCEPTEDTMESSAGE = messageProcessing(data)
        #statusServerCertificate, CHECKACCEPTEDTMESSAGE, PUBLICKEYFROMSERVER = checkCertificateFromServer(data)
        statusConnection = True
        time.sleep(2)
        statusServerCertificate = False
        break
        while(statusServerCertificate):
            print 'yra!!!!'
            if (statusCreateClientKeyExchangeMessage != True):
                SEANSKEY = createClientKeyExchangeMessage(PUBLICKEYFROMSERVER)
                statusCreateClientKeyExchangeMessage = True
            sendMess(clientKeyExchangeMessage)
            print 'i send clientKeyExchangeMessage use key hex : ' + SEANSKEY
            print ' '
            time.sleep(0.01)
            data = sock.recv(1024) 
            print 'tut i kak bi jdy serverKeyExchangeMessage: ' + str(data)
            
            statusServerCertificate, statusConnection = checkServerKeyExchangeMessage(data)
            print ' '
            print 'statusCreateClientKeyExchangeMessage: ' + str(statusCreateClientKeyExchangeMessage)
            print ' '
            print 'statusServerCertificate: ' + str(statusServerCertificate)
            print ' '
            print 'statusConnection: '  + str(statusConnection)
            print ' '
            print CHECKACCEPTEDTMESSAGE
            print clientKeyExchangeMessage
            
    
    #STATUSCONNECTION, SEANSKEY = statusConnection, SEANSKEY   
    #print str(STATUSCONNECTION)
    #print str(SEANSKEY)        
    #print STATUSCONNECTION
    #print SEANSKEY   
    
    #return STATUSCONNECTION,SEANSKEY,sock
    return statusConnection


def sendMess(message):
    sock.send(str(message))
    

def regestrationAction(login,password):
    listForRegestration = []
    listForRegestration.append('10')
    listForRegestration.append(str(login))
    listForRegestration.append(str(password))
    print listForRegestration
    sendMess(listForRegestration)
    firstname, statusRegistration = requests.searchUserByNameOrLogin(login)
    print str(firstname) + ' lol ' + str(statusRegistration)
    if(statusRegistration):
        print ' scha bydem regati'
        requests.registrationUserRequest(login)
    else:
        print 'user yge esti'
    print ''
    
def CreateNewThread():
    requests.StartTheadSearchDB()    
   
   
   
   
 
 
