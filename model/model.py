from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()
        self.tratte_valide = None
        self._lista_edges = []

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        # TODO
        self.G.clear()
        lista_hub = DAO.get_hub()
        for hub in lista_hub:
            self.G.add_node(hub)                #nodes
        self._nodes = self.G.number_of_nodes()  #numero dei nodes

        self.tratte_valide = DAO.get_tratte_valide(threshold)

        for tratta in self.tratte_valide:
            self.G.add_edge(tratta.nome1,tratta.nome2, weight = tratta.valore_medio)    #edges
            self._lista_edges.append(tratta)        #lista degli edges
        self._edges = self.G.number_of_edges()      #numero degli edges



    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        return self._edges

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        return self._nodes

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        return self._lista_edges