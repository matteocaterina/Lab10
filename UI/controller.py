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
            print(lista_tratte)

            for i,tratta in enumerate(lista_tratte, start=1):
                print(tratta)
                self._view.lista_visualizzazione.controls.append(ft.Text(f'{i}) [{tratta[1]} - > {tratta[0]}] -- guadagno medio: € {tratta[2]}'))
            self._view.update()


        except Exception as e:
            self._view.alert.show_alert(f'Errore: {e}')







