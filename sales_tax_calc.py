import re

# key = state name,
# value (in percentages) = (average state+local sales tax rate)
sales_tax_rates = {"Alabama": 8.91,
                   "Alaska": 1.76,
                   "Arizona": 8.17,
                   "Arkansas": 9.26,
                   "California": 8.44,
                   "Colorado": 7.44,
                   "Connecticut": 6.35,
                   "Delaware": 0.00,
                   "Florida": 6.65,
                   "Georgia": 6.96,
                   "Hawaii": 4.35,
                   "Idaho": 6.01,
                   "Illinois": 8.19,
                   "Indiana": 7.00,
                   "Iowa": 6.78,
                   "Kansas": 8.20,
                   "Kentucky": 6.00,
                   "Louisiana": 8.91,
                   "Maine": 5.50,
                   "Maryland": 6.00,
                   "Massachusetts": 6.25,
                   "Michigan": 6.00,
                   "Minnesota": 7.20,
                   "Mississippi": 7.07,
                   "Missouri": 7.81,
                   "Montana": 0.00,
                   "Nebraska": 6.80,
                   "Nevada": 7.94,
                   "New Hampshire": 0.00,
                   "New Jersey": 6.97,
                   "New Mexico": 7.35,
                   "New York": 8.48,
                   "North Carolina": 6.90,
                   "North Dakota": 6.56,
                   "Ohio": 7.10,
                   "Oklahoma": 8.77,
                   "Oregon": 0.00,
                   "Pennsylvania": 6.24,
                   "Rhode Island": 7.00,
                   "South Carolina": 7.13,
                   "South Dakota": 5.83,
                   "Tennessee": 9.45,
                   "Texas": 8.05,
                   "Utah": 6.68,
                   "Vermont": 6.14,
                   "Virginia": 5.63,
                   "Washington": 8.89,
                   "West Virginia": 6.07,
                   "Wisconsin": 5.43,
                   "Wyoming": 5.47,
                   "D.C.": 5.75
                   }

def get_dollar_amount():
    amount = input("Enter a dollar amount: ")
    amount = amount.strip()
    regex = re.compile("\d*\.?\d+$")
    try:
        dollars = regex.search(amount).group()
    except:
        dollars = 0
    return float(dollars)

def get_state():
    state = input("Enter a state (or D.C.): ")
    state = state.strip()
    if state in sales_tax_rates:
        tax_rate = sales_tax_rates[state]
    else:
        tax_rate = -1
    return (state, float(tax_rate))

def compute_total(amount, tax_rate):
    """ tax rate expressed as n.nn be sure to divide rate by 100"""
    total = amount + (amount * (tax_rate/100))
    return total

def run_calc():
    while True:
        print("\n\n\n\n\n\n\n\n\n")
        dollars = get_dollar_amount()
        if dollars == 0:
            print("The dollar amount must be a number greater than 0 (ex: 23.05, 9, $15.25)")
            continue
        state, tax_rate = get_state()
        if tax_rate == -1:
            print("{} is not a valid state".format(state))
            continue
        total = compute_total(dollars, tax_rate)
        print("\n\n")
        print("Average purchase price in {}".format(state))
        print("{:>20}".format("$ "+ str(dollars)))
        print("Tax Rate: {:>10}".format("x "+ str(tax_rate)))
        print("-"*20)
        print("Total: {:>13}".format("$ " + str(total)))
        print("\n\n")
        cont = input("Would you like to test against another state? (Y/n): ")
        if cont[0] in "Nn":
            break
