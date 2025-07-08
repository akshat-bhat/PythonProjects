# Client amount input
# check input validity
# Client source currency
# check validity
# Client target currency
# check validity
# Convert and display result


while True:
    client_amount = input("Enter the amount to convert: ")
    try:
        client_amount = float(client_amount)
        if client_amount<=0:
            raise ValueError()
        else:
            break
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        continue

currency = ('USD', 'EUR', 'CAD')

while True:
    source_currency = input('Source currency (USD/EUR/CAD): ').upper()
    if  source_currency in currency:
        break
    else:
        print("Invalid Currency!")
        continue


while True:
    target_currency = input('Target currency (USD/EUR/CAD): ').upper()
    if target_currency in currency:
        break
    else:
        print("Invalid Currency!")
        continue


exchange_rates = {
    'USD' : {'EUR': 0.5, 'CAD': 2},
    'EUR' : {'CAD': 4, 'USD': 2},
    'CAD' : {'EUR': 0.25, 'USD': 0.5}    
}
if source_currency == target_currency:
    converted_amount = client_amount
else:
    converted_amount = client_amount * exchange_rates[source_currency][target_currency]

print(f"{client_amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}")
#######################################formatted upto 2 decimal places  ^^^  