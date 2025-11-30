from dataclasses import dataclass


@dataclass
class Tratta:
    hub1_id:int
    hub2_id:int
    nome1:str
    nome2:str
    valore_medio: int

