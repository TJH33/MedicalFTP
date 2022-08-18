from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

#The port the FTP server will listen on

FTP_PORT = 2121

#FTP Username

FTP_USER = "padmin"

#FTP Pass

FTP_PASSWORD = "Summertime2022!"

#The directory the FTP user will have read/write access to.

FTP_DIRECTORY = "/srv/users/SYSUSER/apps/APPNAME/public/"

def main():
        authorizer = DummyAuthorizer()

        #Define a new users having full r/w permissions
        authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmw')

        handler = FTPHandler
        handler.authorizer = authorizer

        #Define a custom banner

        handler.banner = "pyftpdlib based ftpd ready, no naughty stuff"

        #Optionally specify range of ports to be used for passive connections

        handler.passive_ports = range(60000,65535)

        address = ('',FTP_PORT)
        server = FTPServer(address,handler)

        server.max_cons = 256
        server.max_cons_per_ip = 5

        server.serve_forever()


if __name__ == '__main__':
        main()