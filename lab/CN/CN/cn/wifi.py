from mininet.net import Mininet 
from mininet.log import setLogLevel,info
from mininet.node import OVSSwitch,Controller
from mininet.cli import CLI
from mn_wifi.net import Mininet_wifi

import os
import subprocess

def wire(infer):
	command=['wireshark' ,'-i', infer]
	subprocess.Popen(command)

def create():
	net=Mininet_wifi(switch=OVSSwitch,controller=Controller)
	
	#controller
	c0=net.addController('c0')
	
	#
	ap1=net.addAccessPoint('a1' ,ssid="simpletopo", mode="g", chanel="g" ,range=116)
	
	sta1=net.addStation('s1')
	net.configureWifiNodes()
	#switch
	s1=net.addSwitch('s1', bw='10')
	s2=net.addSwitch('s2', bw='5')
	s3=net.addSwitch('s3', bw='5')
	s4=net.addSwitch('s4', bw='5')
	s5=net.addSwitch('s5' ,bw='5')
	
	
	
	#host
	
	h1=net.addHost('h1')
	h2=net.addHost('h2')
	h3=net.addHost('h3')
	h4=net.addHost('h4')
	h5=net.addHost('h5')
	
	#server
	server=net.addHost('server')
	
	
	net.addLink(server,s1)
	net.addLink(s1,s2) 
	net.addLink(s1,s3)
	net.addLink(s2,h1)
	net.addLink(s2,h2)
	net.addLink(s3,h3)
	net.addLink(s3,s4)
	net.addLink(s3,s5)
	net.addLink(s4,h4)
	net.addLink(s5,h5)
	net.addLink(ap1,sta1)
	
	server.cmd('ping -c  10.0.0.1')
	
	
	net.start()
	ap1.start([c0])
	CLI(net)
	inf='s1-eth1'
	wire(inf)
	
	net.stop()
	
setLogLevel('info')
create()
