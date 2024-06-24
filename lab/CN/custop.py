#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    info( '*** Add switches\n')
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    Intf( '10.0.0.1', node=s4 )
    Intf( '10.0.0.2', node=s4 )
    Intf( '192.1.1.2', node=s4 )
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    Intf( '10.0.0.3', node=s5 )
    Intf( '10.0.0.4', node=s5 )
    Intf( '192.1.1.1', node=s5 )
    Intf( '192.1.1.3', node=s5 )
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    Intf( '10.0.0.5', node=s6 )
    Intf( '10.0.0.6', node=s6 )
    Intf( '192.1.1.2', node=s6 )

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute='via 192.1.1.1')
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute='via 192.1.1.1')
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute='via 192.1.1.2')
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute='via 192.1.1.2')
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute='via 192.1.1.3')
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute='via 192.1.1.3')

    info( '*** Add links\n')
    net.addLink(s4, h1)
    net.addLink(s4, h2)
    net.addLink(s5, h3)
    net.addLink(s5, h4)
    net.addLink(s6, h5)
    net.addLink(s6, h6)
    net.addLink(s4, s5)
    net.addLink(s5, s6)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s4').start([])
    net.get('s5').start([])
    net.get('s6').start([])

    info( '*** Post configure switches and hosts\n')
    s4.cmd('ifconfig s4 192.1.1.1')
    s5.cmd('ifconfig s5 192.1.1.2')
    s6.cmd('ifconfig s6 192.1.1.3')

    CLI(net)
