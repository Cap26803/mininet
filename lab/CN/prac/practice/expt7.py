#!/usr/bin/python

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

    info('*** Adding controller\n')
    info('*** Add switches/APs\n')
    ap1 = net.addAccessPoint('ap1', cls=OVSKernelAP, ssid='ap1-ssid',
                             channel='1', mode='g', position='303.0,290.0,0')
    ap2 = net.addAccessPoint('ap2', cls=OVSKernelAP, ssid='ap2-ssid',
                             channel='1', mode='g', position='529.0,291.0,0')

    info('*** Add hosts/stations\n')
    sta1 = net.addStation('sta1', ip='10.0.0.1',
                          position='417.0,199.0,0')
    sta2 = net.addStation('sta2', ip='10.0.0.2',
                          position='300.0,433.0,0')
    sta3 = net.addStation('sta3', ip='10.0.0.3',
                          position='530.0,430.0,0')

    info("*** Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=3)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info('*** Add links\n')
    net.addLink(ap1, sta1)
    net.addLink(ap1, sta2)
    net.addLink(ap1, sta3)
    net.addLink(ap2, sta1)
    net.addLink(ap2, sta2)
    net.addLink(ap2, sta3)

    net.plotGraph(max_x=800, max_y=800)

    info('*** Starting network\n')
    net.build()
    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info('*** Starting switches/APs\n')
    net.get('ap1').start([])
    net.get('ap2').start([])

    info('*** Configuring mobility\n')
    net.startMobility(time=0)

    # Adding mobility to stations
    net.mobility(sta1, 'start', time=1, position='417.0,199.0,0')
    net.mobility(sta1, 'stop', time=20, position='600.0,500.0,0')

    net.mobility(sta2, 'start', time=1, position='300.0,433.0,0')
    net.mobility(sta2, 'stop', time=20, position='500.0,100.0,0')

    net.mobility(sta3, 'start', time=1, position='530.0,430.0,0')
    net.mobility(sta3, 'stop', time=20, position='100.0,100.0,0')

    net.stopMobility(time=21)

    info('*** Post configure nodes\n')

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()
