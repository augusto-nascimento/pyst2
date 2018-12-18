#!/usr/bin/env python

"""
.. module:: fastagi
   :synopsis: FastAGI service for Asterisk

Requires modified pyst2 to support reading stdin/out/err
 
 Copyright 2011 VOICE1, LLC
 By: Ben Davis <ben@voice1-dot-me>

Specification
-------------
"""

import sys
from six import PY3
from asterisk.agi import AGI
if PY3:
    import socketserver as SocketServer
else:
    import SocketServer
# import pkg_resources
# PYST_VERSION = pkg_resources.get_distribution("pyst2").version

__verison__ = 0.1

# TODO: Read options from config file.
# HOST, PORT = "127.0.0.1", 4573


class FastAGI(SocketServer.StreamRequestHandler):

    # Close connections not finished in 5seconds.
    timeout = 5

    def run(self):
        raise NotImplementedError

    def handle(self):
        try:
            self.run()
        except TypeError as e:
            sys.stderr.write(
                'Unable to connect to agi://{} {}\n'.format(
                    self.client_address[0], str(e)
                    )
                )
        except SocketServer.socket.timeout:
            sys.stderr.write(
                'Timeout receiving data from {}\n'.format(
                    self.client_address
                )
            )
        except SocketServer.socket.error:
            sys.stderr.write(
                """Could not open the socket.
                Is someting else listening on this port?\n"""
            )   
        except Exception as e:
            sys.stderr.write("""An unknown error: {}\n""".format(str(e)))


# if __name__ == "__main__":
#     # server = SocketServer.TCPServer((HOST, PORT), FastAGI)
#     server = SocketServer.ForkingTCPServer((HOST, PORT), FastAGI)

#     # Keep server running until CTRL-C is pressed.
#     server.serve_forever()
