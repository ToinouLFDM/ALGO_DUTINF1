class node :
	def __init__(self,_index,_x,_y):
		self.index=_index
		self.x=_x
		self.y=_y

class graph:
	def __init__(self):
		self.listNG=[]
		self.order=0
		self.isOriented=False
		self.listNode=[]

	def add_neigbhours(self,indexNeigbhour,indexNode):
		if(len(self.listNode)>indexNode):
			self.listNG[indexNode].append(indexNeigbhour)

	def add_node(self,_x,_y):
		n=len(self.listNode)
		new_node=node(n,_x,_y)
		self.listNode.append(node)

	




