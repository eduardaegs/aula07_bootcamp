basket1: list = ['banana', 'kiwifruits', 'grapefruits', 'apples', 'apricots', 'nectarines', 'oranges', 'peaches', 'pears', 'lemons']

basket2: list = ['grapes', 'dragonfruits', 'limes', 'papaya']

# Transfer fruits from basket1 to basket2
while len(basket1) > len(basket2):
    item_to_transfer = basket1.pop()
    basket2.append(item_to_transfer)

print('Basket 1: ' + str(basket1))
print('Basket 2: ' + str(basket2))