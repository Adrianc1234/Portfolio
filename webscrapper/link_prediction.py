
import numpy as np
import networkx as nx 
from pyvis.network import Network
import matplotlib.pyplot as plt
import os


G = nx.read_gexf("linkedin_graf.gexf")

e = list(G.edges())
  
def triadic(e):
  new_edges = []
  
  for i in e:
    a, b = i
  
    for j in e:
      x, y = j
  
      if i != j:
        if a == x and (b, y) not in e and (y, b) not in e:
          new_edges.append((b, y))
        if a == y and (b, x) not in e and (x, b) not in e:
          new_edges.append((b, x))
        if b == x and (a, y) not in e and (y, a) not in e:
          new_edges.append((a, y))
        if b == y and (a, x) not in e and (x, a) not in e:
          new_edges.append((a, x))
  
  return new_edges
  
print("The possible new edges according to Triadic closure are :")
new_edges = triadic(e)
print("Sorted List A based on index 0: % s" % (sorted(new_edges, key=lambda x:x[1])))

print('Jaccard coefficient')
print(list(nx.jaccard_coefficient(G)))