import math

def calculate_circle_area(raio):
    """Calcula a área de um círculo dado o raio."""
    if raio < 0:
        raise ValueError("O raio não pode ser negativo.")
    area = math.pi * (raio ** 2)
    return area