import django
from pyrad import dictionary, server

from radius.server import RadiusServer

django.setup()

print("django loaded")


from janus.models import Profile

profiles = Profile.objects.all()

for profile in profiles:
    print(profile)




############ start up radius server

# create server and read dictionary
#srv = RadiusServer(dict=dictionary.Dictionary("dictionary"), coa_enabled=True)
srv = RadiusServer(dict=dictionary.Dictionary("dictionary"))

# add clients (address, secret, name)
#srv.hosts["127.0.0.1"] = server.RemoteHost("127.0.0.1", b"Kah3choteereethiejeimaeziecumi", "localhost")
#srv.BindToAddress("")

# add clients (address, secret, name)
srv.hosts["127.0.0.1"] = server.RemoteHost("127.0.0.1", b"changeme", "localhost")
srv.hosts["192.168.50.218"] = server.RemoteHost("192.168.50.218", b"abc123", "unifi")
srv.hosts["*"] = server.RemoteHost("*", b"abc123", "unifs")
srv.BindToAddress("")


# start server
print("start radius server")
srv.Run()