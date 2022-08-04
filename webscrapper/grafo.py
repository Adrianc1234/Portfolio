
import numpy as np
import networkx as nx 
from pyvis.network import Network
import matplotlib.pyplot as plt

def visualizar1(G):
    #nx.draw_kamada_kawai(G)
	ax = plt.gca()
	ax.set_facecolor('grey')
	nx.draw(G, pos = nx.spring_layout(G, scale=2), node_size=30, node_color='green', linewidths=0.25, with_labels=False, edge_color = 'black') 
	plt.show()

def visualizar2(G):
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

	net.save_graph(f'my_graf.html')

my_contact_original = np.load('my_contact_original.npy',allow_pickle=True)
my_contact = np.load('my_contact.npy',allow_pickle=True)
friend_contacts = np.load('friend_contacts.npy',allow_pickle=True)
#print('Your friend list:\n',my_contact_original)
#print('Your scrapped friends:\n', my_contact)
#print("Your friend's friends:\n", friend_contacts)

G = nx.read_gexf("linkedin_graf.gexf")

#visualiza1(G)
visualizar2(G)

#=============== AQUI HACEN SU LINK PREDICTION ===============

