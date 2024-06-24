#!/usr/bin/python

from mininet.node import Controller, OVSKernelSwitch
from mininet.log import setLogLevel, info
from mn_wifi.net import Mininet_wifi
from mn_wifi.node import OVSKernelAP
from mn_wifi.cli import CLI
from mn_wifi.link import wmediumd
from mn_wifi.wmediumdConnector import interference


def myNetwork():
    net = Mininet_wifi(topo=None,
                       build=False,
                       link=wmediumd,
                       wmediumd_mode=interference,
                       ipBase='10.0.0.0/8')

    info('*** Adding controller\n')
    c0 = net.addController(name='c0',
                           controller=Controller,
                           protocol='tcp',
                           port=6653)

    info('*** Add switches/APs\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    ap1 = net.addAccessPoint('ap1', cls=OVSKernelAP, ssid='ap1-ssid',
                             channel='1', mode='g', ip='10.1.1.1/24', position='352.0,291.0,0')
    ap2 = net.addAccessPoint('ap2', cls=OVSKernelAP, ssid='ap2-ssid',
                             channel='6', mode='g', ip='10.1.1.2/24', position='483.0,294.0,0')
    ap3 = net.addAccessPoint('ap3', cls=OVSKernelAP, ssid='ap3-ssid',
                             channel='11', mode='g', ip='10.1.1.3/24', position='599.0,296.0,0')

    info('*** Add hosts/stations\n')
    sta1 = net.addStation('sta1', ip='10.0.0.1/8', position='186.0,413.0,0')
    sta2 = net.addStation('sta2', ip='10.0.0.2/8', position='323.0,421.0,0')
    sta3 = net.addStation('sta3', ip='10.0.0.3/8', position='430.0,432.0,0')
    sta4 = net.addStation('sta4', ip='10.0.0.4/8', position='575.0,433.0,0')
    sta5 = net.addStation('sta5', ip='10.0.0.5/8', position='692.0,403.0,0')
    sta6 = net.addStation('sta6', ip='10.0.0.6/8', position='820.0,373.0,0')

    info("*** Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=3)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info('*** Add links\n')
    net.addLink(s1, ap1)
    net.addLink(s1, ap2)
    net.addLink(s1, ap3)

    net.plotGraph(max_x=1000, max_y=1000)

    info('*** Starting network\n')
    net.build()
    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info('*** Starting switches/APs\n')
    net.get('s1').start([c0])
    net.get('ap1').start([])
    net.get('ap2').start([])
    net.get('ap3').start([])

    info('*** Configuring Mobility\n')
    net.startMobility(time=0)
    net.mobility(sta1, 'start', time=1, position='186.0,413.0,0')
    net.mobility(sta1, 'stop', time=50, position='820.0,413.0,0')
    net.mobility(sta2, 'start', time=2, position='323.0,421.0,0')
    net.mobility(sta2, 'stop', time=50, position='820.0,421.0,0')
    net.mobility(sta3, 'start', time=3, position='430.0,432.0,0')
    net.mobility(sta3, 'stop', time=50, position='820.0,432.0,0')
    net.mobility(sta4, 'start', time=4, position='575.0,433.0,0')
    net.mobility(sta4, 'stop', time=50, position='820.0,433.0,0')
    net.mobility(sta5, 'start', time=5, position='692.0,403.0,0')
    net.mobility(sta5, 'stop', time=50, position='820.0,403.0,0')
    net.mobility(sta6, 'start', time=6, position='820.0,373.0,0')
    net.mobility(sta6, 'stop', time=50, position='186.0,373.0,0')
    net.stopMobility(time=60)

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()
    
    
    '''sudo python your_script_name.py
'''

