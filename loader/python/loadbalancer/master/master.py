""" 
This class is used for creating the master that will rule multiple slaves
A master is a Node
A master can create slaves and monitor them
"""
from loadbalancer import Node
import uuid

class Master(Node):
	"""docstring for Master"""
	def __init__(self, port):
		self.port=port #The port on which the master must listen
		self.id="master-"+str(uuid.uuid4()) #create a master with a uuid
		self.slaves=[] #all the salves for the master "loadbalancer"
		self.address=super(Master,self).ip #get the ip for this node
	def getSlaves(self):
		pass
	def isSlaveOccupied(self):
		pass
	def createSlave(self):
		pass	
	def getSlave(self,id):
		pass