from mininet.net import Mininet
from mininet.node import Host
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def create_network():
    net = Mininet()
    net.addController('c0')

    # Add hosts
    server = net.addHost('server', ip='10.0.0.1/24')
    client = net.addHost('client', ip='10.0.0.2/24')

    # Add switch
    switch = net.addSwitch('s1')

    # Add links
    net.addLink(server, switch)
    net.addLink(client, switch)

    net.start()
    return net

if __name__ == '__main__':
    setLogLevel('info')
    net = create_network()
    CLI(net)
    net.stop()
