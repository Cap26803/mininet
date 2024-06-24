from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSSwitch, Controller
from mininet.log import setLogLevel, info
from mininet.cli import CLI
def create_mynetwork():
	net=Mininet(switch=OVSSwitch, controller=Controller)
	#adding controller
	net.addController('c0')
	#adding switches
	s1=net.addSwitch('s1')
	s2=net.addSwitch('s2')
	#adding hosts
	h1=net.addHost('h1')
	h2=net.addHost('h2')
	#adding links
	net.addLink(s1,h1)
	net.addLink(s1,s2)
	net.addLink(s2,h2)
	#starting the network
	net.start()
	CLI(net)
	#stoping the network
	net.stop()
	
setLogLevel('info')
create_mynetwork()
