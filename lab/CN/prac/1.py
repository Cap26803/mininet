from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

class CustomTopo(Topo):
    def build(self):
        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        
        # Add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        
        # Add links between switches (with redundancy)
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s2, s3)
        
        # Add links between switches and hosts
        self.addLink(s1, h1)
        self.addLink(s1, h2)
        self.addLink(s2, h3)
        self.addLink(s2, h4)
        self.addLink(s3, h5)
        self.addLink(s3, h6)

def run():
    topo = CustomTopo()
    net = Mininet(topo=topo, controller=Controller, switch=OVSKernelSwitch, autoSetMacs=True)
    net.start()
    
    info('*** Running pingall test\n')
    net.pingAll()
    
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
