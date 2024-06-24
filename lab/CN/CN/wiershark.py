import os
import subprocess
import time
from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller
from mininet.log import setLogLevel, info
from mininet.cli import CLI

def start_wireshark(interface):
    # Start Wireshark to capture traffic on the specified interface
    command = ['wireshark', '-i', interface]
    subprocess.Popen(command)

def create_mynetwork():
    net = Mininet(switch=OVSSwitch, controller=Controller)
    net.addController('c0')
    s1 = net.addSwitch('s1')
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    net.addLink(s1, h1, bw=10, delay='5ms')
    net.addLink(s1, h2)

    net.start()

    # Start Wireshark to capture traffic on the interface between switch and h1
    interface = 's1-eth1'
    start_wireshark(interface)

    CLI(net)

    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_mynetwork()

