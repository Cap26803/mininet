import sys
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology():
    "Create a network."
    net = Mininet_wifi()

    

    sta1 = net.addStation('sta1', position="20,40,0")
    sta2 = net.addStation('sta2', position="50,60,0")
    
    sta3 = net.addStation('sta3', position="10,70.0")
    ap1 = net.addAccessPoint('ap1', ssid='ssid-ap1', channel='1', position='15,30,0')
    ap2 = net.addAccessPoint('ap2', ssid='ssid-ap2', channel='6', position='55,30,0')
    net.addController('c1')

    net.setPropagationModel(model="logDistance", exp=6)

    info("*** Configuring nodes\n")
    net.configureNodes()

    info("*** Creating links\n")
    net.addLink(ap1, ap2)

    
    net.plotGraph(max_x=100, max_y=100)

    net.pingAll()
    net.startMobility(time=0)
    net.mobility(sta1, 'start', time=1, position='10,30,0')
    net.mobility(sta2, 'start', time=2, position='10,40,0')
    net.mobility(sta1, 'stop', time=10, position='60,30,0')
    net.mobility(sta2, 'stop', time=10, position='25,40,0')
    net.mobility(sta3, 'start',time=3,position ='78,50,0')
    net.mobility(sta3, 'stop',time=10,position = '10,40,0')
    net.stopMobility(time=11)

    info("*** Starting network\n")
    net.start()
    
    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()
