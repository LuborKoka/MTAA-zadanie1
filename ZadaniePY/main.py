#MTAA Zadanie 1 Ľubor Koka

import socketserver
import sipfullproxy as sip


sip.start('192.168.0.108', 5060)

server = socketserver.UDPServer(("0.0.0.0", 5060), sip.UDPHandler)
server.serve_forever()

