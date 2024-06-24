#!/usr/bin/python

from mininet.node import Controller, OVSKernelSwitch
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
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    ap1 = net.addAccessPoint('ap1', cls=OVSKernelAP, ssid='ap1-ssid',
                             channel='1', mode='g', ip='10.1.1.1', position='369.0,360.0,0')
    ap2 = net.addAccessPoint('ap2', cls=OVSKernelAP, ssid='ap2-ssid',
                             channel='1', mode='g', ip='10.1.1.2', position='512.0,362.0,0')
    ap3 = net.addAccessPoint('ap3', cls=OVSKernelAP, ssid='ap3-ssid',
                             channel='1', mode='g', ip='10.1.1.3', position='690.0,367.0,0')

    info( '*** Add hosts/stations\n')
    sta1 = net.addStation('sta1', ip='172.1.1.1',
                           position='269.0,520.0,0')
    sta2 = net.addStation('sta2', ip='172.1.1.2',
                           position='404.0,523.0,0')
    sta3 = net.addStation('sta3', ip='172.1.1.3',
                           position='532.0,513.0,0')
    sta4 = net.addStation('sta4', ip='172.1.1.4',
                           position='670.0,514.0,0')
    sta5 = net.addStation('sta5', ip='172.1.1.5',
                           position='839.0,514.0,0')

    info("*** Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=3)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info( '*** Add links\n')
    net.addLink(s1, ap1)
    net.addLink(s1, ap2)
    net.addLink(s1, ap3)
    net.addLink(s2, ap1)
    net.addLink(s2, ap2)
    net.addLink(s2, ap3)
    net.addLink(s3, ap1)
    net.addLink(s3, ap2)
    net.addLink(s3, ap3)

    net.plotGraph(max_x=1000, max_y=1000)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches/APs\n')
    net.get('s1').start([c0])
    net.get('s2').start([c0])
    net.get('s3').start([c0])
    net.get('ap1').start([])
    net.get('ap2').start([])
    net.get('ap3').start([])

    info( '*** Post configure nodes\n')
    s1.cmd('ifconfig s1 192.1.1.1')
    s2.cmd('ifconfig s2 192.1.1.2')
    s3.cmd('ifconfig s3 192.1.1.3')
    ap1.cmd('ifconfig ap1 10.1.1.1')
    ap2.cmd('ifconfig ap2 10.1.1.2')
    ap3.cmd('ifconfig ap3 10.1.1.3')

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

