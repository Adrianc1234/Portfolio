
import numpy as np
import networkx as nx 
from pyvis.network import Network
import matplotlib.pyplot as plt
import os


def visualizar(G):
	net = Network('1500px', '2000px',bgcolor='#222222', font_color='white',heading="My linkedIn Network")
	nodes = sorted(G.nodes)
	#add nodes
	for index in range(0,len(nodes)):
		net.add_node(index, label=nodes[index])
	
	#print(G.edges)

	#add edges
	for edge in G.edges:
		p1 = nodes.index(edge[0])
		p2 = nodes.index(edge[1])
		net.add_edge(p1,p2)

	print('Your .html file have been generated successfully')
	print('Please, open this file with you favourite web navigator :)')


	net.save_graph(f'my_graf.html')

os.system('clear')
print('Reading your files... 0%')
my_contact_original = np.load('my_contact_original.npy',allow_pickle=True)
my_contact = np.load('my_contact.npy',allow_pickle=True)
friend_contacts = np.load('friend_contacts.npy',allow_pickle=True)
print('Loading your files... 100%')
G = nx.read_gexf("linkedin_graf.gexf")

visualizar(G)

#=============== AQUI HACEN SU LINK PREDICTION ===============

