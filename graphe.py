import networkx as nx
from scipy import stats


class Graphe :

  def __init__(self):




  def loiPuissance(self, G) :
    k=[]
    pk=[]
    for i in range(self.size) :
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
    for u in self.graph.nodes():
      neighbors = u.neighbors()
      n = 0
      while neighbors:
        v = neighbors[0]
        del neighbors[0]
        #ATTENTION ici on enleve un element de la liste sur laquelle on itere
        #trouver un autre moyen
        for w in neighbors:
          if (v,w) in self.graph.edges() or (w,v) in self.graph.edges():
            n += 1
      C_u = 2*n/(self.graph.degree(u)*(self.graph.degree(u)-1))
      loc_coeffCluster.append(C_u)
    C = sum(loc_coeffCluster)/ self.size
    S = abs(C - 1/log(self.size))/(1/log(self.size))
    if S > 5 :
      S = 5
    r = 5 - S
    return r
    
  def calculFitness() : 
    f=self.poidsPonderation[0]*loiPuissance() + self.poidsPonderation[1]*coeffCluster() + self.poidsPonderation[2]*diametreMoyen()
    return f
