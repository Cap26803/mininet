from mininet.net import Mininet
from mininet.log import setLogLevel,info
from mininet.node import OVSSwitch ,Controller
from mininet.cli import CLI
import os
import subprocess
import time

def wier(interface):
	command =['wireshark','-i',interface]
	subprocess.Popen(command)

def create():
	net=Mininet(switch=OVSSwitch, controller=Controller)
	net.addController('c0')
	s1=net.addSwitch('s1')
	h1=net.addHost('h1')
	h2=net.addHost('h2')
	 
	net.addLink(s1,h1)
	net.addLink(s1,h2)
	
	net.start()
	inter='s1-eth1'
	wier(inter)
	CLI(net)
	
	net.stop()
setLogLevel('info')
create()
	
