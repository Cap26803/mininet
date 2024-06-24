#!/usr/bin/python
from mininet.node import Controller, OVSSwitch
from mininet.log import setLogLevel, info
from mn_wifi.net import Mininet_wifi
from mn_wifi.cli import CLI
from time import sleep

def myNetwork():
    net = Mininet_wifi(switch=OVSSwitch, controller=Controller)
    info('*** Adding controller\n')
    net.addController('c0')

    info('*** Add switches/APs\n')
    ap1 = net.addAccessPoint('ap1', mode='g', position='394.0,117.0,0', range='300')
    ap2 = net.addAccessPoint('ap2', mode='g', position='546.0,119.0,0', range='300')

    info('*** Add hosts/stations\n')
    sta1 = net.addStation('sta1', position='267.0,265.0,0', range='300')
    sta2 = net.addStation('sta2', position='371.0,268.0,0', range='300')
    sta3 = net.addStation('sta3', position='510.0,293.0,0', range='300')
    sta4 = net.addStation('sta4', position='629.0,276.0,0', range='300')

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info('*** Add links\n')
    net.addLink(ap2, ap1)
    net.plotGraph(max_x=1000, max_y=1000)

    net.startMobility(time=0)
    net.mobility(sta1, 'start', time=1, position='267.0,265.0,0')
    net.mobility(sta2, 'start', time=2, position='371.0,268.0,0')
    net.mobility(sta1, 'stop', time=10, position='510.0,293.0,0')
    net.mobility(sta2, 'stop', time=10, position='510.0,293.0,0')
    net.mobility(sta3, 'start', time=3, position='510.0,293.0,0')
    net.mobility(sta3, 'stop', time=10, position='267.0,265.0,0')
    net.stopMobility(time=11)

    net.start()

    net.pingAll()
    CLI(net)
    net.stop()

setLogLevel('info')
myNetwork()
