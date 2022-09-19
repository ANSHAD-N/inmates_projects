def studentDiscount(amount):
    amount = amount - (amount*10)/100
    return amount
    

def regularBuyersDiscount(amount):
    amount = amount-(amount*5)/100
    return amount

sellingAmount = 100

print("selling amount with student discount= ",studentDiscount(sellingAmount))
print(" selling amount with regular discount= ",regularBuyersDiscount(sellingAmount))
print(" with both discount= ",regularBuyersDiscount(studentDiscount(sellingAmount)))