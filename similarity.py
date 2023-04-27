from functools import reduce
from typing import Union


def similarity(number: Union[float, int], coefficient: Union[float, int]) -> dict:
    division = number / coefficient
    multiplication = number * coefficient

    division_sum = [int(n) for n in str(division).replace(".", "")]
    multiplication_sum = [int(n) for n in str(multiplication).replace(".", "")]
    
    return {
        'number': number,
        'coefficient': coefficient,
        'division': division,
        'multiplication': multiplication,
        'division_sum': reduce(lambda x, y: x + y, division_sum),
        'multiplication_sum': reduce(lambda x, y: x + y, multiplication_sum)
    }
