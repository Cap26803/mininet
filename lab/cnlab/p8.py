#!/usr/bin/env python

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi

def web_server_topology():
    "Create a wireless network with a web server and multiple clients."

    net = Mininet_wifi()

    # Add an access point (AP)
    ap1 = net.addAccessPoint('ap1', ssid='wifi-net', mode='g', channel='1', position='50,50,0', range=100)

    # Add a web server host (H1)
    h1 = net.addHost('h1', ip='192.168.0.1/24')

    # Add mobile stations (STA) as clients
    sta1 = net.addStation('sta1', position='10,50,0')
    sta2 = net.addStation('sta2', position='90,50,0')
    sta3 = net.addStation('sta3', position='130,50,0')
    
    net.setPropagationModel(model="logDistance", exp=6)

    # Configure nodes
    net.configureWifiNodes()

    # Add links between AP and H1 (web server)
    net.addLink(ap1, h1)

    # Add links between AP and stations (clients)
    net.addLink(sta1, ap1)
    net.addLink(sta2, ap1)
    net.addLink(sta3, ap1)

    # Start the network
    net.plotGraph(max_x=200, max_y=100)
     # Mobility and load testing
    info("\n*** Starting mobility and load testing ***\n")
    net.startMobility(time=0)
    
    # Simulate mobility of clients (stations)
    net.mobility(sta1, 'start', time=1, position='60,50,0')
    net.mobility(sta1, 'stop', time=10, position='160,50,0')

    net.mobility(sta2, 'start', time=2, position='40,50,0')
    net.mobility(sta2, 'stop', time=10, position='140,50,0')

    net.mobility(sta3, 'start', time=3, position='80,50,0')
    net.mobility(sta3, 'stop', time=10, position='180,50,0')

    # Stop mobility after 10 seconds
    net.stopMobility(time=11)


    net.start()

    # Configure web server on H1
    info("*** Configuring web server on h1 ***\n")
    h1.cmd('echo "<html><body><h1>Welcome to Mininet-WiFi Web Server!</h1></body></html>" > index.html')
    h1.cmd('python3 -m http.server 80 &')

   
    net.pingAll()

    # Start CLI for interactive testing
    info("\n*** Running CLI ***\n")
    CLI(net)

    # Stop the network
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    web_server_topology()

