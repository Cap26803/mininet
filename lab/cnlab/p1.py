from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSSwitch, Controller
from mininet.log import setLogLevel, info
from mininet.cli import CLI


def create():
	net=Mininet(switch=OVSSwitch ,controller=Controller)
	
	net.addController('c0')
	
	#switches
	
	s1=net.addSwitch('s1')
	s2=net.addSwitch('s2')
	s3=net.addSwitch('s3')
	
	#hostes
	
	h1=net.addHost('h1')
	h2=net.addHost('h2')
	h3=net.addHost('h3')
	h4=net.addHost('h4')
	h5=net.addHost('h5')
	h6=net.addHost('h6')
	h7=net.addHost('h7')
	
	#adding links
	
	net.addLink(s1,s2)
	net.addLink(s1,s3)
	net.addLink(s2,h1)
	net.addLink(s2,h2)
	net.addLink(s2,h3)
	net.addLink(s3,h4)
	net.addLink(s3,h5)
	net.addLink(s3,h6)
	net.addLink(s1,h7)
	
	net.start()
	CLI(net)
	net.stop()
	
setLogLevel('info')
create()

#here use pingall command to testreachablity

	 
	
