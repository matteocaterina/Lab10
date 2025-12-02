from dataclasses import dataclass


@dataclass
class Tratta:
    hub1_id:int
    hub2_id:int
    stato1:str
    stato2:str
    nome1:str
    nome2:str
    valore_medio: int

    def __str__(self):
        return f'[{self.nome2} ({self.stato2}) -> {self.nome1} ({self.stato1})] -- guadagno Medio Per Spedizione: € {self.valore_medio}'