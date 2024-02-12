"""
    Author: AaronTook (https://AaronTook.github.io)
    File Last Modified: 2/12/2024
    File Name: app.py
    Project Name: NormalDistributionPercent
"""

from scipy.integrate import quad
import math

def normal_probability_density_function(mu, sigma, x):
    f_x = ( 1 / (sigma * math.sqrt(2 * math.pi)) ) * math.pow(math.e, (-1 * ( math.pow((x - mu), 2) / (2 * math.pow(sigma, 2)))))
    return f_x

def percentage_integral(a, b, mu, sigma):
    percentage, error = quad(lambda x: normal_probability_density_function(mu, sigma, x), a, b)
    return percentage

if __name__ == "__main__":
    print("Welcome to the normal distribution percentage calculator!\nAll values are assumed to have the same units.")
    average_mean = float(input("Average (Mean) Value: "))
    standard_deviation = float(input("Standard Deviation: "))
    minimum_value = float(input("Minimum value: "))
    maximum_value = float(input("Maximum value: "))
    percent = percentage_integral(minimum_value, maximum_value,  average_mean, standard_deviation)
    print(f"{percent}%")