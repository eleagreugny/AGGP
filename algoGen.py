import graph

class AlgoGen:

  def __init__(self, N, n, e, Pm, Pc):
    self.listGraph = []
    for i in range(N):
      G = Graph(i%3, i, n, e)
      self.listGraph.append(G)
    self.pm = Pm
    self.pc = Pc


def simulation() : 
  nb_graph = 5
  while(len(self.listGraph)>n): 
    listeModif = selectionFitness()
    mutation(listeModif)
    crossingOver(listeModif)
  affichageGraphe()
