from Statistics.Proportion import proportion
from Calculators.Subtraction import subtraction
from Calculators.Division import division
from Calculators.Multiplication import multiplication


def var_pop_proportion(data):
    p = proportion(data)
    q = subtraction(1, p)
    data = [num for elem in data for num in elem]
    new_data = [float(x) for x in data]
    n = len(new_data)
    return division(n, multiplication(p, q))
