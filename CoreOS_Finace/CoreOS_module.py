import os
import platform
from dataclasses import dataclass
from typing import Union
from decimal import Decimal

Number = Union[int, float, Decimal]  # Create Type

@dataclass
class CoreOSFinance:
    @staticmethod
    def simpleInterest(C: Number, taxa_juros: Number, temp: int) -> Number:
        return C + (C * taxa_juros * temp)

    @staticmethod
    def compoundInterest(C: Number, taxa_juros: Number, tempo: int) -> Number:
        return C * ((1 + taxa_juros) ** tempo)

    @staticmethod
    def taxaMensalParaAnual(taxa_mensal: float) -> float:
        return (1 + taxa_mensal) ** 12 - 1

    @staticmethod
    def taxaAnual_paraMensal(taxa_anual: float) -> float:
        return (1 + taxa_anual) ** (1 / 12) - 1
