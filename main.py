Items = []

class SalesTax:

    totalPrice = 0
    tax_amount = 0

    def basicSalesTax(self, quantity, price):
        temp_price = price
        actual_price = (price * 10)/100
        actual_price = round(actual_price, 2)
        SalesTax.tax_amount += (actual_price * quantity)
        actual_price += price
        actual_price = round((quantity * actual_price), 2)
        # if actual_price != 0:
        #     self.price_without_tax += (temp_price * quantity)
        SalesTax.totalPrice += actual_price
        return actual_price

    def importTax(self, quantity, price):
        temp_price = price
        actual_price = (price * 5)/100
        actual_price = round(actual_price, 2)
        SalesTax.tax_amount += (actual_price * quantity)
        actual_price = price + actual_price
        actual_price = round((quantity * actual_price), 2)
        SalesTax.totalPrice += actual_price
        return actual_price

    def importandbasicTax(self, quantity, price):
        temp_price = price
        actual_price = (price * 15) / 100
        actual_price = round(actual_price, 2)
        SalesTax.tax_amount += (actual_price * quantity)
        actual_price = price + actual_price
        actual_price = round((quantity * actual_price), 2)
        SalesTax.totalPrice += actual_price
        return actual_price

    def nonTaxable(self, quantity, price):
        SalesTax.totalPrice += (price * quantity)
        return price * quantity

    def printTaxandTotal(self):
        print(f'Taxes: {round(SalesTax.tax_amount, 2)}')
        print(f'Total: {SalesTax.totalPrice}')

if __name__ == '__main__':
    while 1:
        print('Select Category:')
        print('1. Food / Medicine / Books')
        print('2. Others')
        category = input()
        if not(category == '1' or category == '2'):
            print('Please select a valid category')
            continue

        print('Enter 1 if imported, else 2:')

        imported = False

        while 1:
            x = input()
            if x == '1':
                imported = True
                break
            elif x != '2':
                print('Please choose correct option')
                print('Enter 1 if imported, else 2:')
                continue
            else:
                break
        print('Enter item in the format: 1 biscuit at 1.99 ,or , 1 imported chocolate at 3.5, if imported.')
        item = input()
        item = item.split()
        if len(item) < 4:
            print('Please enter the items in the specified format')
            continue
        try:
            if float(item[-1]) < 0:
                print('Please enter valid price in the specified format')
                continue
        except:
            print('Please enter valid item and valid price in the specified format')
            continue
        item1 = item[:-2] + [': '+item[-1]]
        item1 = ' '.join(item1)
        quantity = item[0]
        try:
            if int(quantity) < 0:
                print('Please enter valid quantity')
                continue
        except:
            print('Please enter valid quantity')
            continue
        price = item[-1]
        salesTax = SalesTax()
        if imported:
            if int(category) == 1:
                selling_price = str(salesTax.importTax(int(quantity), float(price)))
                item1 = item1.replace(price, selling_price)
                Items.append(item1)
            elif int(category) == 2:
                selling_price = str(salesTax.importandbasicTax(int(quantity), float(price)))
                item1 = item1.replace(price, selling_price)
                Items.append(item1)
        else:
            if int(category) == 1:
                selling_price = str(salesTax.nonTaxable(int(quantity), float(price)))
                item1 = item1.replace(price, selling_price)
                Items.append(item1)
            elif int(category) == 2:
                selling_price = str(salesTax.basicSalesTax(int(quantity), float(price)))
                item1 = item1.replace(price, selling_price)
                Items.append(item1)
        print('If you want to add items press y, else n:')
        choice = input()
        if not(choice == 'y'):
            break

    for items in Items:
        print(items)
    salesTax.printTaxandTotal()
