from socket import *

class PortScanner(object):
    def toto():
        print "toto"

    def connScan(self, tgtHost, tgtPort):
        try:
            connSkt = socket(AF_INET, SOCK_STREAM)
            connSkt.connect((tgtHost, tgtPort))
            print 'connected'
            #connSkt.send('testValue\r\n')
            #results = connSkt.recv(100)
            print '[+]%d/tcp open'% tgtPort
            connSkt.close()
            return 1
        except Exception as inst:
            print type(inst)     # the exception instance
            print inst.args      # arguments stored in .args
            print inst 
            print '[-]%d/tcp closed'% tgtPort
            return 0

    def portScan(self, tgtHost, tgtPorts):
        try:
            tgtIP = gethostbyname(tgtHost)
        except:
          print "[-] Cannot resolve '%s': Unknown host"%tgtHost
          return
        try:
          tgtName = gethostbyaddr(tgtIP)
          print '\n[+] Scan Results for: ' + tgtName[0]
        except:
            print '\n[+] Scan Results for: ' + tgtIP
        setdefaulttimeout(1)
        openPorts = []
        for tgtPort in tgtPorts:
            print 'Scanning port ' + str(tgtPort)
            res = self.connScan(tgtHost, tgtPort)
            if res == 1:
                openPorts.append(tgtPort)
        return openPorts

