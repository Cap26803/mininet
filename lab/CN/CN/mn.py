
from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch, Host
from mininet.cli import CLI
from mininet.log import setLogLevel, info
import sys

def myNetwork():
    if len(sys.argv) != 3:
        print("Usage: python script.py <num_switches> <num_hosts>")
        return

    num_switches = int(sys.argv[1])
    num_hosts = int(sys.argv[2])

    net = Mininet(topo=None, build=False, ipBase='10.0.0.0/8')

    info('* Adding controllers\n')
    c0 = net.addController(name='c0', controller=Controller, protocol='tcp', port=6633)

    info('* Add switches\n')
    switches = []
    for i in range(num_switches):
        switch = net.addSwitch('s{}'.format(i + 1), cls=OVSKernelSwitch)
        switches.append(switch)

    s_central = net.addSwitch('s_central', cls=OVSKernelSwitch, dpid='00:00:00:00:00:01')  # Provide a specific DPID
    net.addLink(s_central, switches[0])  # Connect central switch to the first switch

    # Add hosts and link them to switches
    info('* Add hosts and links\n')
    for i in range(num_hosts):
        host = net.addHost('h{}'.format(i + 1), cls=Host, ip='10.0.0.{}'.format(i + 1), defaultRoute=None)
        switch_index = i % num_switches  # Round-robin assignment of hosts to switches
        net.addLink(host, switches[switch_index])

    info('* Starting network\n')
    net.build()

    info('* Starting controllers and switches\n')
    net.start()

    info('* Post configure switches and hosts\n')
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()

