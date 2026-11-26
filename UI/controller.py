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



            lista_collegamenti=self._model.costruisci_grafo(self._view.importo_medio_minimo.value)

            self._view.lista_visualizzazione.controls.append(ft.Text(str(f'Numero di Collegamenti: {len(lista_collegamenti)}')))

            for collegamento in lista_collegamenti:
                self._view.lista_visualizzazione.controls.append(ft.Text(str(collegamento)))

            self._view.update()

        else:
            print('importo medio non è un intero')