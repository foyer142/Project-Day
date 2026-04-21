

def get_produtcs_in_stock( products : list[dict]) -> list:
    products_in_stock = []
    for product in products:
        if product['in_stock'] == True:
            products_in_stock.append(product)
    return products_in_stock

def get_name_products(products : list[dict]) ->list:
    name_products = []
    for product in products:
        name_products.append(product['name'])
    return  name_products

def sum_all_products(products : list[dict]) ->int:
    sum_products = 0
    for product in products:
        sum_products += product['price']
    return sum_products

def max_price_products(products : list[dict]) ->dict:
    max_price = products[0]['price']
    max_price_product = products[0]
    for product in products:
        if product['price'] > max_price:
            max_price = product['price']
            max_price_product = product
    return max_price_product

products = [
    {"name": "Laptop", "price": 1000, "in_stock": True},
    {"name": "Mouse", "price": 25, "in_stock": True},
    {"name": "Keyboard", "price": 45, "in_stock": False},
    {"name": "Monitor", "price": 300, "in_stock": True},
]

print('\n',get_produtcs_in_stock(products),'\n')
print(get_name_products(products), '\n')
print(sum_all_products(products), '\n')
print(max_price_products(products))
