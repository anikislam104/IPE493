# p = a - bD where p is price, D is demand, and a and b are constants
import numpy as np
import matplotlib.pyplot as plt
#install matplotlib using pip install matplotlib
#install numpy using pip install numpy


def demand_function(a,b,p):
    demand = (a - p) / b
    return demand

def total_revenue_function(price,demand):
    total_revenue = price * demand
    return total_revenue

def total_revenue_function(a,b,D):
    total_revenue = a * D - b * D**2
    return total_revenue

def get_demand_for_max_total_revenue(a,b):
    demand = a / (2 * b)
    return demand

def plot_revenue_vs_demand_graph(a,b):
    x = np.arange(0, 100, 0.1)
    y = total_revenue_function(a,b,x)
    plt.plot(x,y)
    plt.xlabel("Demand")
    plt.ylabel("Total Revenue")
    plt.title("Total Revenue vs Demand")
    #point out max total revenue 
    demand_for_max_total_revenue = get_demand_for_max_total_revenue(a,b)
    total_revenue_for_max_total_revenue = total_revenue_function(a,b,demand_for_max_total_revenue)
    plt.plot(demand_for_max_total_revenue,total_revenue_for_max_total_revenue,'ro')
    plt.annotate("Max Total Revenue",xy=(demand_for_max_total_revenue,total_revenue_for_max_total_revenue),xytext=(demand_for_max_total_revenue+5,total_revenue_for_max_total_revenue+5),arrowprops=dict(facecolor='black',shrink=0.05))
    #point out demand for max total revenue
    plt.plot(demand_for_max_total_revenue,demand_for_max_total_revenue,'ro')
    plt.annotate("Demand for Max Total Revenue",xy=(demand_for_max_total_revenue,demand_for_max_total_revenue),xytext=(demand_for_max_total_revenue+5,demand_for_max_total_revenue+5),arrowprops=dict(facecolor='black',shrink=0.05))
    plt.show()

def total_cost_function(cv,Cf,D):
    total_cost = cv * D + Cf
    return total_cost

def total_profit_function(a,b,cv,Cf,D):
    total_profit = total_revenue_function(a,b,D) - total_cost_function(cv,Cf,D)
    return total_profit

def demand_for_max_total_profit(a,b,cv):
    demand = (a - cv) / (2 * b)
    return demand

def demands_for_break_even(a,b,cv,Cf):
    D1 = -(a - cv) / (2 * b) + np.sqrt((a - cv)**2 / (4 * b**2) + Cf / b)
    D2 = -(a - cv) / (2 * b) - np.sqrt((a - cv)**2 / (4 * b**2) + Cf / b)
    return D1,D2



# plot_revenue_vs_demand_graph(100,1)
