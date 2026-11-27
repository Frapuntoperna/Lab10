from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutte le Filiali (i nodi) presenti e filtrando i Collegamenti con
        importo medio per bonifico >= threshold (euro)
        """
        # TODO
        #print(threshold, ' thresold')
        dao = DAO()
        lista_di_liste = dao.get_filiali()
        self.G.clear()
        for lista_singola in lista_di_liste:

            if int(lista_singola[2])>=int(threshold):
                self.G.add_edge(lista_singola[0], lista_singola[1], weight=float(lista_singola[2]))

        return self.G

    def get_num_edges(self):
        """
        Restituisce il numero di Collegamenti (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO

        numero_collegamenti=self.G.number_of_edges()
        #print(f'numero di Collegamenti get_num_edge: {numero_collegamenti}')
        return numero_collegamenti


    def get_num_nodes(self):
        """
        Restituisce il numero di Filiali (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO

        numero_nodi = self.G.number_of_nodes()
        return numero_nodi

    def get_all_edges(self):
        """
        Restituisce tutti i Collegamenti (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        lista_collegamenti=[]
        for filiale_origine, filiale_destinazione in self.G.edges:
            #print(self.G[filiale_origine][filiale_destinazione]['weight'])
            lista_collegamenti.append(f'{len(lista_collegamenti)+1}) [{filiale_origine} --> {filiale_destinazione}] --- Importo medio per bonifico: £ {self.G[filiale_origine][filiale_destinazione]['weight']:.2f}')

        print(lista_collegamenti)
        return lista_collegamenti