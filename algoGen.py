# -*- coding: utf-8 -*-
import numpy as np
import random
import networkx as nx
import graphe


class AlgoGen:

  def __init__(self, N, n, e, Pm, Pc):
    self.listGraph = []
    for i in range(N):
      G = Graph(i%3, i, n, e)
      self.listGraph.append(G)
    self.pm = Pm
    self.pc = Pc


"""Méthode mutation
Mute aléatoirement les graphes selon 5 modalités de même probabilité:
	- Ajout d'un noeud
	- Suppression d'un noeud
	- Ajout d'une arrête
	- Suppression d'une arrête
	- Modification de l'étiquette d'une arrête
"""
def mutation():
  for i in range(len(self.listGraph)):
    for j in range(len(self.listGraph[i].nodes())):
      #Tire aléatoirement un chiffre r dans la loi uniforme entre 0 et 1
      r=random.random()
      #Si r est inférieur à la probabilité de muter alors on mute le graph
      if (r<self.pm):
        #Tire un entier aléatoirement entre 1 et 5 pour choisir la modalité de 
        #mutation
        c=random.choice([1,2,3,4,5])
        #Si c égal 1, ajout d'un noeud
        if (c==1):
          self.listGraph[i].add_node(max(self.listGraph[i].nodes())+1)
        #Si c égal 2, suppression d'un noeud
        if (c==2):
          self.listGraph[i].remove_node(self.listGraph[i].nodes()[j])
        #Si c égal 3, ajout d'une arrête entre 2 noeuds a et b tirés aléatoirement
        if (c==3):
          a=random.randint(0, len(self.listGraph[i].nodes())-1)
          b=random.randint(0, len(self.listGraph[i].nodes())-1)
          print "a=%i, b=%i"%(a,b)
          self.listGraph[i].add_edge(a,b)
        #Si c égal 4, suppression d'une arrête
        if (c==4):
          self.listGraph[i].remove_edge(*self.listGraph[i].edges()[j])
        #Si c égal 5, modification de l'étiquette d'une arrête
        if (c==5):
          #Tire la nouvelle étiquette
          a=random.randint(0, len(self.listGraph[i].nodes())-1)
          r=random.random()
          if(r<0.5):
            b=self.listGraph[i].edges()[j][0]
            self.listGraph[i].remove_edge(*self.listGraph[i].edges()[j])
            self.listGraph[i].add_edge(b,a)
          else :
            b=self.listGraph[i].edges()[j][1]
            self.listGraph[i].remove_edge(*self.listGraph[i].edges()[j])
            self.listGraph[i].add_edge(b,a)


  def simulation() : 
    n = 5
    while(len(self.listGraph)>n): 
      listeModif = selectionFitness()
      mutation()
      crossingOver()
    affichageGraphe()
