import networkx as nx
from scipy import stats
import math


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
    k=[]
    pk=[]
    for i in range(len(self.graph.nodes())) :
      k.append(self.graph.degree(i))
      pk.append(i)
    lr= stats.linregress(k,pk)
    S=abs(lr[0]-(2.3))/(2.3)
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
        loc_coeffCluster.append(C_u)
        degrees.append(self.graph.degree(u))
    lr = stats.linregress(degrees,loc_coeffCluster)
    S = abs(lr[0] - 1.0)
    if S > 5 :
      S = 5
    r = 5 - S
    return r

  def diametreMoyen(self):
    D = nx.diameter(self.graph)
    ref = math.log(len(self.graph.nodes()))/math.log(math.log(len(self.graph.nodes())))
    S = abs(D - ref)/float(ref)
    if S > 5 :
      S = 5
    r = 5 - S
    return r
    
  def calculFitness(self) :
    f=self.poidsPonderation[0]*self.loiPuissance() + self.poidsPonderation[1]*self.coeffCluster() + self.poidsPonderation[2]*self.diametreMoyen()
    return f

