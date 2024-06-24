#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller
from mininet.log import setLogLevel, info
from mininet.cli import CLI

def setup_network():
    net = Mininet(controller=Controller)

    info('*** Adding controller\n')
    net.addController('c0')

    info('*** Adding hosts\n')
    h1 = net.addHost('h1', ip='10.0.0.1')
    h2 = net.addHost('h2', ip='10.0.0.2')

    info('*** Adding switch\n')
    s1 = net.addSwitch('s1')

    info('*** Creating links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    info('*** Starting network\n')
    net.start()

    info('*** Configuring web server on h1\n')
    h1.cmd('echo "<html><body><h1>Hello, Mininet!</h1></body></html>" > /tmp/index.html')
    h1.cmd('python3 -m http.server 80 --directory /tmp &')

    info('*** Network setup complete\n')
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    setup_network()



'''kushal@kushal:~/Downloads$ sudo python ex3a.py
*** Adding controller
*** Adding hosts
*** Adding switch
*** Creating links
*** Starting network
*** Configuring hosts
h1 h2 
*** Starting controller
c0 
*** Starting 1 switches
s1 ...
*** Configuring web server on h1
*** Network setup complete
*** Starting CLI:
mininet> h2 wget http://10.0.0.1
--2024-06-22 17:21:51--  http://10.0.0.1/
Connecting to 10.0.0.1:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3276 (3.2K) [text/html]
Saving to: ‘index.html.4’

index.html.4        100%[===================>]   3.20K  --.-KB/s    in 0s      

2024-06-22 17:21:51 (141 MB/s) - ‘index.html.4’ saved [3276/3276]

mininet> 

'''

