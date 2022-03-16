import datetime as dt
from sys import getsizeof


def get_data_ranges() -> tuple:
    return (
        range(100000, 600000, 100000),
        range(1000, 6000, 100),
        range(100, 600, 100),
        range(10, 60, 10),
        range(1000000, 6000000, 1000000)
    )


def append_data(data: tuple) -> list:
    dados = []
    aux = 0
    for range_data in data:
        memory_accumulator = 0
        aux += 1
        for value in range_data:
            inicio = dt.datetime.now()
            acumulador = 0
            for i in range(value, 0, -1):
                acumulador += i
            memory_accumulator += getsizeof(value)
            duracao = dt.datetime.now() - inicio
            dados.append(
                (value, memory_accumulator, duracao.microseconds, dt.datetime.now() + dt.timedelta(days=aux)))
    return dados


def generate_data() -> list:
    dados = append_data(get_data_ranges())
    return dados
