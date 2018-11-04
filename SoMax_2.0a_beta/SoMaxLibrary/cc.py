'''import OSC
import random
from multiprocessing import Process

class Server(Process):
    def run(self, inport = 4567, outport = 1234):
        self.outPort = outport
        self.inPort = 4567
        self.server = OSC.OSCServer(("127.0.0.1",self.inPort))
        self.server.addMsgHandler("/random", self.outputRandom)
        self.server.addMsgHandler("/server/stop", self.stopServer)
        self.client = OSC.OSCClient()
        self.server.serve_forever()

    def stopServer(self, *args):
        self.server.close()

    def outputRandom(self, *args):
        message = OSC.OSCMessage("/random")
        message.append(random.random())
        self.client.sendto(message, ("127.0.0.1",self.outPort))



s = Server()
s.start()
'''

import GenCorpus as gc

gc.readAudioFiles('macomposition.aif', 'corpus')
