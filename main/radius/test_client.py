from __future__ import print_function
from pyrad.client import Client
from pyrad.dictionary import Dictionary
import pyrad.packet

#srv = Client(server="localhost", secret=b"changeme")
srv = Client(server="localhost", secret=b"changeme", dict=Dictionary("dictionary"))

# create request
req = srv.CreateAuthPacket(code=pyrad.packet.AccessRequest,
                           User_Name="daniel", NAS_Identifier="localhost")
req["User-Password"] = req.PwCrypt("sparka")

# send request
reply = srv.SendPacket(req)

if reply.code == pyrad.packet.AccessAccept:
    print("access accepted")
else:
    print("access denied")

print("Attributes returned by server:")
for i in reply.keys():
    print("%s: %s" % (i, reply[i]))