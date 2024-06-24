from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSSwitch, Controller
from mininet.log import setLogLevel, info
from mininet.cli import CLI
def create_mynetwork():
	net=Mininet(switch=OVSSwitch, controller=Controller)
	net.addController('c0')
	s1=net.addSwitch('s1')
	s2=net.addSwitch('s2')
	s3=net.addSwitch('s3')
	s4=net.addSwitch('s4')
	s5=net.addSwitch('s5')
	
	h1=net.addHost('h1')
	h2=net.addHost('h2')
	h3=net.addHost('h3')
	h4=net.addHost('h4')
	h5=net.addHost('h5')
	
	net.addLink(s1,s2)
	net.addLink(s2,s3)
	net.addLink(s3,s4)
	net.addLink(s4,s5)
	net.addLink(s1,s5)
	net.addLink(s1,h1)
	net.addLink(s2,h2)
	net.addLink(s3,h3)
	net.addLink(s4,h4)
	net.addLink(s5,h5)
	
	
	net.start()
	CLI(net)
	net.stop()
	
setLogLevel('info')
create_mynetwork()
