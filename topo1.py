from mininet.topo import Topo

class MyTopo( Topo ):

    def __init__( self ):

        # initilaize topology   建立拓扑
        Topo.__init__( self )

        # add hosts and switches添加主机和交换机
        host1 = self.addHost( 'h1' )  #添加8个主机
        host2 = self.addHost( 'h2' )
	host3 = self.addHost( 'h3' )
	host4 = self.addHost( 'h4' )
	host5 = self.addHost( 'h5' )
	host6 = self.addHost( 'h6' )
	host7 = self.addHost( 'h7' )
	host8 = self.addHost( 'h8' )
        switch1 = self.addSwitch( 's1' )   #添加7个交换机
        switch2 = self.addSwitch( 's2' )
        switch3 = self.addSwitch( 's3' )
        switch4 = self.addSwitch( 's4' )
	switch5 = self.addSwitch( 's5' )
	switch6 = self.addSwitch( 's6' )
	switch7 = self.addSwitch( 's7' )

        # add links添加链接，建立树状拓扑
        self.addLink(switch1,switch2)
        self.addLink(switch1,switch3)
        self.addLink(switch2,switch4)
        self.addLink(switch2,switch5)
	self.addLink(switch3,switch6)
	self.addLink(switch3,switch7)
        self.addLink(switch4,host1)
	self.addLink(switch4,host2)
	self.addLink(switch5,host3)
	self.addLink(switch5,host4)
	self.addLink(switch6,host5)
	self.addLink(switch6,host6)
	self.addLink(switch7,host7)
	self.addLink(switch7,host8)

topos = { 'mytopo': ( lambda: MyTopo() ) }
