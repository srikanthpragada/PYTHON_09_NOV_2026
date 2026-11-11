#Accept USD and display INR and Euros
usd = float(input('Enter value in USD :'))
inr = usd * 93.6
euro = usd * 0.896
print(f'{usd:.2f} $ is equal to {inr:.2f} inr and {euro:.2f} EUR')