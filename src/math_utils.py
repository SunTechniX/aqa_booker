# src/math_utils.py
import math


def calculate_distance(x: float) -> float:
    return math.sqrt(x)


# tests/test_math_utils.py
def test_with_spy(mocker):
    spy = mocker.spy(math, "sqrt")  # Оборачиваем реальную функцию

    result = calculate_distance(9)

    assert result == 3  # Реальное поведение сохранено
    assert spy.call_count == 1  # Но мы видим, что функция была вызвана
    assert spy.spy_return == 3  # И знаем, что она вернула
