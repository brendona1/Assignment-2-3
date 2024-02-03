itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00

Profit = retailPrice - wholesalePrice
salePrice = retailPrice - (0.25 * retailPrice)
saleProfit = salePrice - wholesalePrice

print("Item Name: " + itemName)
print("Retail Price: $" + str(retailPrice))
print("Wholesale Price: $" + str(wholesalePrice))
print("Profit: $" + str(Profit))
print("Sale Price: $" + str(salePrice))
print("Sale Profit: $" + str(saleProfit))
