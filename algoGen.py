import graph

class AlgoGen:

  def __init__(self, N, n, e, Pm, Pc):
    self.listGraph = []
    for i in range(N):
      G = Graph(i%3, i, n, e)
      self.listGraph.append(G)
    self.pm = Pm
    self.pc = Pc