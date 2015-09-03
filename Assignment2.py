
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSController
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel
import sys
print "enter number of switch"
x=raw_input()
print "enter number of host"
y=raw_input()
switchlist=[]
hostlist=[]
class MyTopo(Topo):
	def __init__(self,**opts):
		"create custom topo"
		super(MyTopo,self).__init__(**opts)
		
		for i in range (0,int(x)):
			name = 's'+str(i)
			switchlist.append(self.addSwitch(name))
		'''S1 = self.addSwitch('s1')
		S2 = self.addSwitch('s2')
		S3 = self.addSwitch('s3')
		S4 = self.addSwitch('s4')'''
		for i in range (0,int(y)):
			hname= 'h' + str(i)
			hostlist.append(self.addHost(hname))
		'''H1 = self.addHost('h1')
		H2 = self.addHost('h2')'''
		#switchlist =(S1,S2,S3,S4)
		

		# Add Links
		for index in range (0,len(switchlist)):
			if(index == len(switchlist)-1):
				break;
			#for index2 in range(index+1,len(switchlist)):
			self.addLink(switchlist[index],switchlist[index+1])
		
		i=0
		for j in range(len(switchlist)):
			self.addLink(hostlist[i],switchlist[j],bw=1,delay='5ms',loss=1,max_quque_size=1000,use_htb=True)
			i=i+1
			self.addLink(hostlist[i],switchlist[j],bw=2)
			i=i+1

		#self.addLink(H1,S1)
		#self.addLink(H2,S3)

topos = {'mytopo' : ( lambda:MyTopo() ) }
'''net = Mininet(topo=MyTopo)
net.start()
h1,h2 = net.hostlist[0],net.hostlist[3]
print h1.cmd('ping -c1 %s' % h2.IP())
net.stop()'''
	
#def Test():

topo = MyTopo()
net =Mininet(topo=topo,host=CPULimitedHost,link=TCLink,controller=OVSController)
count=1
for i in range(0,int(y),2):
	str1="h"
	stri2="10.0.0."
	stri2=stri2+str(count)
	count=count+1
	str1=str1+str(i)
	hi=net.get(str1)
	hi.setIP(stri2,24)

for i in range(1,int(y),2):
	str1="h"
	stri2="192.168.0."
	stri2=stri2+str(count)
	count=count+1
	str1=str1+str(i)
	hi=net.get(str1)
	hi.setIP(stri2,29)
net.start()
dumpNodeConnections(net.hosts)
net.pingAll()
net.stop()
