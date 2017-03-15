import networkx as nx
from scipy import stats
import math
import numpy as np


class Graphe :

  def __init__(self,ID, typeG, nodes, edges):
    if typeG == 1: 
      self.graph = nx.gnm_random_graph(nodes, edges, seed=None, directed=False)
    elif typeG == 2:
      self.graph = nx.barabasi_albert_graph(nodes, edges, seed=None)
    else: #typeG == 3: 
      self.graph = nx.watts_strogatz_graph(nodes, edges, 0.5, seed=None)
    
    self.fitness = 0.0
    self.ID = ID
    self.poidsPonderation = (2,2,1)



  def loiPuissance(self) :
    l_k=[]
    pk=[]
    lg_pk=[]
    lg_k=[]
    d={}
    for i in range(len(self.graph.nodes())) :
      deg=self.graph.degree(self.graph.nodes()[i])
      if d.has_key(deg) : 
        d[deg]= d[deg]+1
      else : 
        d[deg]=1
      #print d
    for k in d.keys():
      pk.append(float(d[k])/len(self.graph.nodes()))
      l_k.append(k)
    for i in range(len(pk)) :
      if l_k[i]!=0 and pk[i]!=0:
        lg_k.append(np.log(l_k[i]))
        lg_pk.append(np.log(pk[i]))
    lr= stats.linregress(lg_k,lg_pk)
    S=abs(lr[0]+(2.3))/(2.3)
    if S>5 : 
      S=5
    r= 5-S
    return r

  def coeffCluster(self):
    loc_coeffCluster = []
    degrees = []
    for u in self.graph.nodes():
      if self.graph.degree(u) > 1:
        neighbors = self.graph.neighbors(u)
        n = 0
        while neighbors:
          v = neighbors[0]
          del neighbors[0]
          for w in neighbors:
            if (v,w) in self.graph.edges() or (w,v) in self.graph.edges():
              n += 1
        C_u = 2*n/float(self.graph.degree(u)*(self.graph.degree(u)-1))
        if C_u != 0:
          invC_u = 1.0/C_u
          loc_coeffCluster.append(invC_u)
          degrees.append(self.graph.degree(u))
    if loc_coeffCluster:
      lr = stats.linregress(degrees,loc_coeffCluster)
      S = abs(lr[0] - 1.0)
      if S > 5 :
        S = 5
      r = 5 - S
    else:
      r = 0.0
    return r

  def diametreMoyen(self):
    if nx.is_connected(self.graph):
      D = nx.diameter(self.graph)
      ref = math.log(len(self.graph.nodes()))/math.log(math.log(len(self.graph.nodes())))
      S = abs(D - ref)/float(ref)
      if S > 5 :
        S = 5
      r = 5 - S
    else:
      r = 0.0
    return r
    
  def calculFitness(self) :
    f=self.poidsPonderation[0]*self.loiPuissance() + self.poidsPonderation[1]*self.coeffCluster() + self.poidsPonderation[2]*self.diametreMoyen()
    self.fitness = f
    return f

