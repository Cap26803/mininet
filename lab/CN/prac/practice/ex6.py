#!/usr/bin/python

from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.net import Mininet_wifi
from mn_wifi.node import Station, OVSKernelAP
from mn_wifi.cli import CLI
from mn_wifi.link import wmediumd
from mn_wifi.wmediumdConnector import interference
from subprocess import call


def myNetwork():

    net = Mininet_wifi(topo=None,
                       build=False,
                       link=wmediumd,
                       wmediumd_mode=interference,
                       ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0 = net.addController(name='c0',
                           controller=Controller,
                           protocol='tcp',
                           port=6653)

    info( '*** Add switches/APs\n')
    ap1 = net.addAccessPoint('ap1', cls=OVSKernelAP, ssid='ssid-ap1',
                             channel='1', mode='g', position='364.0,291.0,0')
    ap2 = net.addAccessPoint('ap2', cls=OVSKernelAP, ssid='ssid-ap2',
                             channel='6', mode='g', position='492.0,296.0,0')
    ap3 = net.addAccessPoint('ap3', cls=OVSKernelAP, ssid='ssid-ap3',
                             channel='11', mode='g', position='620.0,294.0,0')

    info( '*** Add hosts/stations\n')
    sta1 = net.addStation('sta1', ip='10.0.0.1',
                           position='380.0,191.0,0')
    sta2 = net.addStation('sta2', ip='10.0.0.2',
                           position='484.0,195.0,0')
    sta3 = net.addStation('sta3', ip='10.0.0.3',
                           position='589.0,195.0,0')
    sta4 = net.addStation('sta4', ip='10.0.0.4',
                           position='371.0,387.0,0')
    sta5 = net.addStation('sta5', ip='10.0.0.5',
                           position='494.0,399.0,0')
    sta6 = net.addStation('sta6', ip='10.0.0.6',
                           position='591.0,394.0,0')

    info("*** Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=3)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info( '*** Add links\n')

    net.plotGraph(max_x=1000, max_y=1000)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches/APs\n')
    net.get('ap1').start([c0])
    net.get('ap2').start([c0])
    net.get('ap3').start([c0])

    info( '*** Post configure nodes\n')

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

