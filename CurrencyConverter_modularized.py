# Client amount input
# check input validity
# Client source currency
# check validity
# Client target currency
# check validity
# Convert and display result


def client_amount_input():
    while True:
        client_amount = input("Enter the amount to convert: ")
        try:
            client_amount = float(client_amount)
            if client_amount<=0:
                raise ValueError()  ###instead of printing an error message, we raise a ValueError
            return client_amount
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")


def get_currency(label):
    currencies = ('USD', 'EUR', 'CAD')
    while True:
        currency = input(f'{label} currency (USD/EUR/CAD): ').upper()
        if  currency not in currencies:
            print("Invalid Currency!")
        else:
            return currency


def currency_converter(source_currency, target_currency, client_amount):
    exchange_rates = {
        'USD' : {'EUR': 0.5, 'CAD': 2},
        'EUR' : {'CAD': 4, 'USD': 2},
        'CAD' : {'EUR': 0.25, 'USD': 0.5}    
    }
    if source_currency == target_currency:
        return client_amount
    return client_amount * exchange_rates[source_currency][target_currency]


def main():
    client_amount = client_amount_input()
    source_currency = get_currency('Source')
    target_currency = get_currency('Target')
    converted_amount = currency_converter(source_currency, target_currency, client_amount)
    print(f"{client_amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}")
    #######################################formatted upto 2 decimal places  ^^^   


if __name__ == "__main__":
    main()
### This is doen so that when this module is imported in a separate Module,
### we will be able to use other functions aswell and not just main.
### Main will be the result only if it is run in Terminal