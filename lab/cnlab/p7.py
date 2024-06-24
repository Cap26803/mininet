from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi

def handover_demo():
    "Create a network with mobility and handover simulation."

    net = Mininet_wifi()

    # Add two access points (APs)
    ap1 = net.addAccessPoint('ap1', ssid='handover-net', mode='g', channel='1', position='50,50,0', range=30)
    ap2 = net.addAccessPoint('ap2', ssid='handover-net', mode='g', channel='6', position='150,50,0', range=30)

    # Add stations (STAs)
    sta1 = net.addStation('sta1', position='10,50,0', range=10)
    sta2 = net.addStation('sta2', position='90,50,0', range=10)
    sta3 = net.addStation('sta3', position='130,50,0', range=10)

    # Set propagation model
    net.setPropagationModel(model="logDistance", exp=4.5)

    # Configure nodes
    net.configureWifiNodes()

    # Add links between APs
    net.addLink(ap1, ap2)

    # Start the network
    net.plotGraph(max_x=200, max_y=100)
     # Mobility simulation
    info("\n*** Starting mobility simulation ***\n")
    net.startMobility(time=0)

    
    net.mobility(sta1, 'start', time=1, position='60,50,0')
    net.mobility(sta1, 'stop', time=10, position='160,50,0')

   
    net.mobility(sta2, 'start', time=2, position='40,50,0')
    net.mobility(sta2, 'stop', time=10, position='140,50,0')

  
    net.mobility(sta3, 'start', time=3, position='80,50,0')
    net.mobility(sta3, 'stop', time=10, position='180,50,0')

    # Stop mobility after 10 seconds
    net.stopMobility(time=11)
    
    #start
    net.start()

    # Print initial connectivity
    info("*** Initial connectivity check ***\n")
    net.ping([sta1, sta2, sta3])

   

    # Print final connectivity
    info("\n*** Final connectivity check ***\n")
    net.ping([sta1, sta2, sta3])

    # Start CLI for user interaction
    CLI(net)

    # Stop the network
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    handover_demo()

