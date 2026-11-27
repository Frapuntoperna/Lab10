import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_collegamenti(self, e):
        """
        Funzione che controlla prima se il valore dell'importo inserito sia valido (es. non deve essere una stringa) e
        poi popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Filiali presenti
        * Numero di Collegamenti
        * Lista di Collegamenti che superano l'importo indicato come soglia
        """
        # TODO
        if self._view.importo_medio_minimo.value is not str:

            self._view.lista_visualizzazione.controls.clear()

            self._model.costruisci_grafo(self._view.importo_medio_minimo.value)

            # funzione get_num_nudes
            numero_filiali = int(self._model.get_num_nodes())
            self._view.lista_visualizzazione.controls.append(
                ft.Text(str(f'Numero di Filiali: {numero_filiali}')))

            #funzione get_num_edge
            numero_collegamenti=int(self._model.get_num_edges())
            self._view.lista_visualizzazione.controls.append(
                ft.Text(str(f'Numero di Collegamenti: {numero_collegamenti}')))

            #funzione get_all_edge STAMPA COLLEGAMENTI

            for collegamento in self._model.get_all_edges():
                self._view.lista_visualizzazione.controls.append(ft.Text(str(collegamento)))

            self._view.update()

        else:
            print('importo medio non è un intero')