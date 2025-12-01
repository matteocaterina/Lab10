from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.tratte_valide = None
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        # TODO
        self.G.clear()
        lista_hub = DAO.get_hub()
        for hub in lista_hub:
            self.G.add_node(hub)
        self._nodes = self.G.number_of_nodes()

        self.tratte_valide = DAO.get_tratte_valide(threshold)
        for tratta in self.tratte_valide:
            self.G.add_edge(tratta.nome1,tratta.nome2, weight = tratta.valore_medio)

        self._edges = self.G.number_of_edges()



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
        lista = []
        for tratta in self.tratte_valide:
            lista.append((tratta.nome1, tratta.nome2, tratta.valore_medio))
        return lista