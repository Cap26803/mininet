from mininet.log import setLogLevel, info
from mininet.node import OVSSwitch, Controller
from mininet.cli import CLI
from mn_wifi.net import Mininet_wifi
import subprocess

def start_wireshark(interface):
    # Start Wireshark to capture traffic on the specified interface
    command = ['wireshark', '-i', interface]
    subprocess.Popen(command)

def create():
    net = Mininet_wifi(switch=OVSSwitch, controller=Controller)
    net.addController('c0')
    
    # Access points
    ap1 = net.addAccessPoint('ap1', mode='g', position='20,20,10', range='20')
    ap2 = net.addAccessPoint('ap2', mode='g', position='40,20,20', range='20')
    
    # Stations
    sta1 = net.addStation('sta1', position='10,10,10', range='5')
    sta2 = net.addStation('sta2', position='10,20,20', range='5')
    sta3 = net.addStation('sta3', position='10,30,10', range='5')
    sta4 = net.addStation('sta4', position='10,40,20', range='5')
    
    # Configuring WiFi nodes
    net.configureWifiNodes()
    
    # Adding links
    net.addLink(ap1, ap2)
    net.addLink(sta1, ap1)
    net.addLink(sta2, ap1)
    net.addLink(sta3, ap2)
    net.addLink(sta4, ap2)
    
    # Starting Mininet-WiFi
    net.plotGraph()
    net.start()
    
    # Start Wireshark for capturing traffic on sta1
    interface = 'ap1-wlan1'
    start_wireshark(interface)
    
    # Open Mininet-WiFi CLI
    CLI(net)
    
    # Stopping Mininet-Wi
    net.stop()
    
setLogLevel('info')
create()
