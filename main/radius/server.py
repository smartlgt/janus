from pyrad import packet, server
import logging

from radius.package import calculate_HMAC_MD5

logging.basicConfig(filename="pyrad.log", level="DEBUG",
                    format="%(asctime)s [%(levelname)-8s] %(message)s")


class RadiusServer(server.Server):

    '''
    example auth request (unifi):
    Received an authentication request
    Attributes:
    User-Name: ['admin']
    NAS-IP-Address: ['192.168.50.218']
    NAS-Identifier: ['f09fc23cb986']
    NAS-Port: [0]
    Called-Station-Id: ['02-9F-C2-3E-B9-86:test1']
    Calling-Station-Id: ['00-B3-62-7F-70-61']
    Framed-MTU: [1400]
    NAS-Port-Type: ['Wireless-802.11']
    Connect-Info: ['CONNECT 0Mbps 802.11b']
    EAP-Message: ['\x02c\x00\n\x01admin']
    Message-Authenticator: [b'\xef\xf6\x89X\xa7l\xe6?="\xd8\xac\x04\x88\xd3\xf8']

    '''

    def HandleAuthPacket(self, pkt):
        print("Received an authentication request")
        print("Attributes: ")
        for attr in pkt.keys():
            print("%s: %s" % (attr, pkt[attr]))

            if attr == "User-Password":
                decrypt = pkt.PwDecrypt(pkt[attr][0])
                print("%s: %s" % (attr, decrypt))

            if attr == "Message-Authenticator":
                hash = calculate_HMAC_MD5(pkt)
                print("HMAC_MD5: %s" % (hash, ))

        reply = self.CreateReplyPacket(pkt, **{
            "Service-Type": "Framed-User",
            "Framed-IP-Address": '192.168.0.1',
            "Framed-IPv6-Prefix": "fc66::1/64"
        })

        reply.code = packet.AccessAccept
        self.SendReplyPacket(pkt.fd, reply)

    def HandleAcctPacket(self, pkt):

        print("Received an accounting request")
        print("Attributes: ")
        for attr in pkt.keys():
            print("%s: %s" % (attr, pkt[attr]))

        reply = self.CreateReplyPacket(pkt)
        self.SendReplyPacket(pkt.fd, reply)

    def HandleCoaPacket(self, pkt):

        print("Received an coa request")
        print("Attributes: ")
        for attr in pkt.keys():
            print("%s: %s" % (attr, pkt[attr]))

        reply = self.CreateReplyPacket(pkt)
        self.SendReplyPacket(pkt.fd, reply)

    def HandleDisconnectPacket(self, pkt):

        print("Received an disconnect request")
        print("Attributes: ")
        for attr in pkt.keys():
            print("%s: %s" % (attr, pkt[attr]))

        reply = self.CreateReplyPacket(pkt)
        # COA NAK
        reply.code = 45
        self.SendReplyPacket(pkt.fd, reply)