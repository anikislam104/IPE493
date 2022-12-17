def breakeven_point():
    selling_price_per_hour = float(input("Enter the selling price of the product: "))
    variable_cost_per_hour = float(input("Enter the variable cost of the product: "))
    fixed_cost_per_year = float(input("Enter the fixed cost of the product: "))
    #fix zero division error
    if selling_price_per_hour - variable_cost_per_hour == 0:
        print("The selling price per hour and the variable cost per hour cannot be the same")
        return 0
    quantity = fixed_cost_per_year / (selling_price_per_hour - variable_cost_per_hour)
    print("The breakeven point is", quantity)
    return quantity

def capacity_of_breakeven_point(breakeven_point,maximum_output_hour_per_year):
    capacity = breakeven_point / maximum_output_hour_per_year
    print("The percentage capacity in the breakeven point is", capacity*100, "%")


def main():
    break_even_point=breakeven_point()
    max_ouput_hour_per_year = float(input("Enter the maximum output per hour per year: "))
    capacity_of_breakeven_point(break_even_point,max_ouput_hour_per_year)

main()