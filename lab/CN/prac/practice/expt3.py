from mininet.net import Mininet
from mininet.node import Controller
from mininet.link import TCLink
from mininet.log import setLogLevel, info
from mininet.cli import CLI

def simple_topology():
	net = Mininet(controller=Controller, link=TCLink)
	net.addController('c0')
	
	h1 = net.addHost('h1', ip='10.0.0.1')
	h2 = net.addHost('h2', ip='10.0.0.2')
	s1=  net.addSwitch('s1')
	
	net.addLink(h1,s1)
	net.addLink(h2,s1)
	
	net.start()
	
	info('Starting Web Server on h1...\n')
	h1.cmd('echo "<html><body><h1>Hello, Mininet!</h1></body></html>"> /tmp/index.html')
	h1.cmd('cd /tmp && python3 -m http.server 80 &')
	
	info('Retriving webpage from h2...\n')
	result=h2.cmd('wget -O- http://10.0.0.1/index.html')
	info(result)
	
	CLI(net)
	net.stop()

if __name__ == '__main__':
	setLogLevel('info')
	simple_topology()
