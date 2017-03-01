import networkx as nx
from scipy import stats

class Graphe :

  def __init__(self):




  def loiPuissance(G) : 
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
    
    
  def calculFitness() : 
    f=self.poidsPonderation[0]*loiPuissance() + self.poidsPonderation[1]*coeffCluster() + self.poidsPonderation[2]*diametreMoyen()
    return f
