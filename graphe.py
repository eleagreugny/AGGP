import networkx as nx
from scipy import stats
import math
import numpy as np
import matplotlib.pyplot as plt


class Graphe :

  def __init__(self,ID,nodes, edges): #typeG
    self.graph = nx.gnm_random_graph(nodes, edges, seed=None, directed=False)

    #self.graph = nx.barabasi_albert_graph(nodes, edges, seed=None)
    #else: #typeG == 3: 
     # self.graph = nx.watts_strogatz_graph(nodes, edges, 0.5, seed=None)
    
    self.fitness = 0.0
    self.ID = ID
    self.poidsPonderation = (4,2,1)




  def loiPuissance(self,plot,time=0) :
    #print ("loi puissance")
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
        if l_k[i]!=1 and pk[i]!=1:
          lg_k.append(np.log(l_k[i]))
          lg_pk.append(np.log(pk[i]))
    if lg_k:
      lr= stats.linregress(lg_k,lg_pk)
      if not math.isnan(lr[0]):
        S=abs(lr[0]+(2.3))/(2.3)
        if S>5 :
          S=5
        r= 5-S
        if plot:
          lg_k = np.array(lg_k)
          fig = plt.figure()
          plt.plot(lg_k,lg_pk,'o')
          plt.plot(lg_k,lr[1]+lr[0]*lg_k,'r')
          plt.title('Regression lineaire - loi de Puissance - gamma = %f'%lr[0])
          plt.savefig('puissance_%i'%time,format='png')
          plt.close(fig)
      else:
        r = 0.0
    else:
      r = 0.0
    return r

  def coeffCluster(self,plot,time=0):
    #print("coeff")
    loc_coeffCluster = []
    degrees = []
    for u in self.graph.nodes():
      if self.graph.degree(u) > 1:
        C_u = nx.clustering(self.graph,u)
        if C_u != 0:
          invC_u = 1.0/C_u
          loc_coeffCluster.append(invC_u)
          degrees.append(self.graph.degree(u))
    if loc_coeffCluster:
      lr = stats.linregress(degrees,loc_coeffCluster)
      if not math.isnan(lr[0]):
        S = abs(lr[0] - 1.0)
        if S > 5 :
          S = 5
        r = 5 - S
        if plot:
          degrees = np.array(degrees)
          fig = plt.figure()
          plt.plot(degrees,loc_coeffCluster,'o')
          plt.plot(degrees,lr[1]+lr[0]*degrees,'r')
          plt.title('Regression lineaire - coefficient Clustering - pente = %f'%lr[0])
          plt.savefig('cluster_%i'%time,format='png')
          plt.close(fig)
      else:
        r = 0.0
    else:
      r = 0.0
    return r

  def diametreMoyen(self):
    #print ("diametre")
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
    f=self.poidsPonderation[0]*self.loiPuissance(False)+self.poidsPonderation[1]*self.coeffCluster(False)+self.poidsPonderation[2]*self.diametreMoyen()
    self.fitness = f
    return f

