# -*- coding: utf-8 -*-
import numpy as np
import random
import networkx as nx
from graphe import Graphe
import matplotlib.pyplot as plt


class AlgoGen:

  def __init__(self, N, n, e, Pm, Pc):
    self.listGraph = []
    for i in range(N):
      G = Graphe(i%3, i, n, e)
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
  def mutation(self):
    for i in range(len(self.listGraph)):
      #Parcours les noeuds
      for j in range(len(self.listGraph[i].graph.nodes())-1):
        #Tire aléatoirement un chiffre r dans la loi uniforme entre 0 et 1
        r=random.random()
        #Si r est inférieur à la probabilité de muter alors on mute le graph
        if (r<(self.pm*0.6) and len(self.listGraph[i].graph.nodes())-1>=j):
          #Tire un entier aléatoirement entre 1 et 5 pour choisir la modalité de 
          #mutation
          c=random.choice([1,2,3])
          #Si c égal 1, ajout d'un noeud
          if (c==1):
            self.listGraph[i].graph.add_node(max(self.listGraph[i].graph.nodes())+1)
          #Si c égal 2, suppression d'un noeud
          if (c==2):
            self.listGraph[i].graph.remove_node(self.listGraph[i].graph.nodes()[j])
          #Si c égal 3, ajout d'une arrête entre 2 noeuds a et b tirés aléatoirement
          if (c==3):
            a=random.randint(0, len(self.listGraph[i].graph.nodes())-1)
            b=random.randint(0, len(self.listGraph[i].graph.nodes())-1)
            self.listGraph[i].graph.add_edge(a,b)
            
      #Parcours les arrêtes
      for k in range(len(self.listGraph[i].graph.edges())-1):
        #Tire aléatoirement un chiffre r dans la loi uniforme entre 0 et 1
        r=random.random()
        #Si r est inférieur à la probabilité de muter alors on mute le graph
        if (r<self.pm*0.4 and len(self.listGraph[i].graph.edges())-1>=k):
          #Tire un entier aléatoirement entre 1 et 5 pour choisir la modalité de 
          #mutation
          c=random.choice([1,2])
          #Si c égal 1, suppression d'une arrête
          if (c==1):
            self.listGraph[i].graph.remove_edge(*self.listGraph[i].graph.edges()[k])
          #Si c égal 2, modification de l'étiquette d'une arrête
          if (c==2):
          #Tire la nouvelle étiquette
           a=random.randint(0, len(self.listGraph[i].graph.nodes())-1)
           r=random.random()
           if(r<0.5):
             b=self.listGraph[i].graph.edges()[k][0]
             self.listGraph[i].graph.remove_edge(*self.listGraph[i].graph.edges()[k])
             self.listGraph[i].graph.add_edge(b,a)
           else :
             b=self.listGraph[i].graph.edges()[k][1]
             self.listGraph[i].graph.remove_edge(*self.listGraph[i].graph.edges()[k])
             self.listGraph[i].graph.add_edge(b,a)
              
              
  """Méthode croisement
  Effectue un crossing over entre les noeuds (et les arrêtes) de deux génomes
  """
  def crossingOver(self):
    for i in range(len(self.listGraph)):
      #Tire aléatoirement un chiffre r dans la loi uniforme entre 0 et 1
      r=random.random()
      #Si r est inférieur à la probabilité de croisement alors on effectue
      #le crossing over entre le graph i et un second graph choisi aléatoirement
      if (r<self.pc):
        #Choisi le second graph avec lequel faire le crossing over
        g=random.randint(0, len(self.listGraph)-1)
        #Tire la position du croisement aléatoire entre les noeuds des 2 graphes
        pn=random.randint(0, len(self.listGraph[i].graph.nodes())-1)
        if (g!=i):
          #Crée une variable temporaire pour stocker les noeuds lors de la 
          #permutation
          temp=[]
          #Ajoute à la variable temporaire la liste des noeuds du graphe i à 
          #permuter
          for k in range(pn, len(self.listGraph[i].graph.nodes())):
            temp.append(self.listGraph[i].graph.nodes()[k])
          #Supprime les noeuds du graphe i à permuter
          for k in range(pn, len(self.listGraph[i].graph.nodes())):
            self.listGraph[i].graph.remove_node(self.listGraph[i].graph.nodes()[pn])
          #Ajoute les noeuds du graphe g dans la liste des noeuds du graphe i
          for k in range(pn, len(self.listGraph[g].graph.nodes())):
            self.listGraph[i].graph.add_node(self.listGraph[g].graph.nodes()[k])
          #Supprime les noeuds du graphe g à permuter
          for k in range(pn, len(self.listGraph[g].graph.nodes())):
            self.listGraph[g].graph.remove_node(self.listGraph[g].graph.nodes()[pn])
          #Ajoute les noeuds présent dans la variable temporaire à la liste de 
          #noeuds du graphe g
          for k in range(0, len(temp)):
            self.listGraph[g].graph.add_node(temp[k])
      
      r=random.random()
      if (r<self.pc and len(self.listGraph[i].graph.edges())!=0): #Vérifie que
        #le nombre d'arrêtes est différent de 0 -> possible puisque l'on a supprimé
        #des noeuds
        #Choisi le second graph avec lequel faire le crossing over
        g=random.randint(0, len(self.listGraph)-1)
        #Tire la position du croisement aléatoire entre les arrêtes des 2 graphes
        pe=random.randint(0, len(self.listGraph[i].graph.edges())-1)
        if (g!=i):
          #Crée une variable temporaire pour stocker les arrêtes lors de la 
          #permutation
          temp=[]
          #Ajoute à la variable temporaire la liste des arrêtes du graphe i à 
          #permuter
          for k in range(pe, len(self.listGraph[i].graph.edges())):
            temp.append(self.listGraph[i].graph.edges()[k])
          #Supprime les arrêtes du graphe i à permuter
          for k in range(pe, len(self.listGraph[i].graph.edges())):
            self.listGraph[i].graph.remove_edge(*self.listGraph[i].graph.edges()[pe])
          #Ajoute les arrêtes du graphe g dans la liste des arrêtes du graphe i
          for k in range(pe, len(self.listGraph[g].graph.edges())):
            self.listGraph[i].graph.add_edge(*self.listGraph[g].graph.edges()[k])
          #Supprime les arrête du graphe g à permuter
          for k in range(pe, len(self.listGraph[g].graph.edges())):
            self.listGraph[g].graph.remove_edge(*self.listGraph[g].graph.edges()[pe])
          #Ajoute les arrêtes présentes dans la variable temporaire à la liste de 
          #arrêtes du graphe g
          for k in range(0, len(temp)):
            self.listGraph[g].graph.add_edge(*temp[k])

  def affiche(self):
    for i in self.listGraph:
      nx.draw(i.graph)
      plt.show()

  def getFitness(self,tupl):
    return tupl[1]

  def selectionFitness(self):
    listeFitness = []
    for i in range(len(self.listGraph)):
      listeFitness.append((i,self.listGraph[i].fitness)) #creation d'une liste de tuples
    sorted(listeFitness, key = self.getFitness)
    for j in range(0, (len(listeFitness)*20/100)-1) :
      del self.listGraph[listeFitness[j][0]]
    #on recupere les ID des 3 meilleurs graph
    ID1 = listeFitness[len(listeFitness)-1][0]
    ID2 = listeFitness[len(listeFitness)-2][0]
    ID3 = listeFitness[len(listeFitness)-3][0]
    
    newListGraph = []
    for i in self.listGraph:
      if i.ID != ID1 and i.ID != ID2 and i.ID != ID3:
        newListGraph.append(i)
    return newListGraph
  
  
  def simulation(self) :
    print('Debut simulation')
    for i in range(len(self.listGraph)):
      self.listGraph[i].calculFitness()
    t=0
    while(t<1000): 
      listeModif = self.selectionFitness()
      self.mutation()
      self.crossingOver()
      for i in range(len(self.listGraph)):
        self.listGraph[i].calculFitness()
      t = t+1
    print(self.listGraph)
    print(len(self.listGraph))
    self.affiche()
