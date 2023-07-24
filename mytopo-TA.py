"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        h1 = self.addHost( 'h1' , ip='10.1.1.1/24')
        h2 = self.addHost( 'h2' , ip='10.1.1.2/24')
        h3 = self.addHost( 'h3' , ip='10.1.1.3/24')
        h4 = self.addHost( 'h4' , ip='10.1.1.4/24')
        h5 = self.addHost( 'h5' , ip='10.1.1.5/24')


        #switches
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )

        # Add links
        self.addLink( s1, s3 )
        self.addLink( s1, s2 )
        self.addLink( s2, h1 )
        self.addLink( s2, h2 )
        self.addLink( s3, h4 )
        self.addLink( s1, h5 )
        self.addLink( s1, h3 )



topos = { 'mytopo': ( lambda: MyTopo() ) }
