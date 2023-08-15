from mininet.topo import Topo
from mininet.link import TCLink


class TutorialTopology(Topo):

    def build(self):

        # Add the central switch
        s1 = self.addSwitch('s1')

        # connect n hosts to the switch
        hosts = []
        for h in range(0, 2):
            hosts.append(self.addHost("h{}".format(h+1)))
            self.addLink(s1, hosts[h], cls=TCLink, bw=100, delay='0', loss=0)


topos = {
    'tutorialTopology': (lambda: TutorialTopology())
}
