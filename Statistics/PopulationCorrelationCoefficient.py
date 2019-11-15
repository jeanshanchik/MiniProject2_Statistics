from CSVReader.CSVReader import CsvReader
from Statistics.PopulationStandardDeviation import pop_stand_dev
from Statistics.PopulationMean import population_mean
from Calculators.Calculator import multiplication
from Calculators.Calculator import subtraction
from Calculators.Calculator import division


def pop_correlation_coefficient(data):
    # x_data = CsvReader('Tests/Data/female_height.csv').data
    # y_data = CsvReader('Tests/Data/male_height.csv').data
    x_data = [num for elem in data for num in elem]
    y_data = [num for elem in data for num in elem]
    new_x_data = [float(x) for x in x_data]
    new_y_data = [float(x) for x in y_data]
    x = pop_stand_dev(new_x_data)
    y = pop_stand_dev(new_y_data)
    divisor = multiplication(x, y)
    z = len(new_x_data)

    # Covariance calculation:
    a = subtraction(new_x_data, population_mean(new_x_data))
    b = subtraction(new_y_data, population_mean(new_y_data))
    c = multiplication(a, b)
    covariance = division(z, (sum(c)))

    # Population Correlation Coefficient calculation:
    d = division(divisor, covariance)
    return d
