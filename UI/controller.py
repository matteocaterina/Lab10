import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model
    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        # TODO
        try:
            threshold = float(self._view.guadagno_medio_minimo.value)
            if threshold <=0:
                raise ValueError('metti numero maggiore di 0')

            self._model.costruisci_grafo(threshold)
            num_nodi = self._model.get_num_nodes()
            num_archi = self._model.get_num_edges()

            self._view.lista_visualizzazione.controls.clear()

            self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di nodi: {num_nodi}"))

            self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di archi: {num_archi}"))

            lista_tratte = self._model.get_all_edges()

            for i,tratta in enumerate(lista_tratte, start=1):
                self._view.lista_visualizzazione.controls.append(ft.Text(f'{i}) {str(tratta)}'))
            self._view.update()


        except Exception as e:
            self._view.alert.show_alert(f'Errore: {e}')







