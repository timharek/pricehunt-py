import json
import pync

import main

SCRIPT_NAME = "Pricehunt-py"

main.check_if_data_exists()
product_data = main.load_json(r"" + main.cwd + "/" + "products.json")


for index, product in enumerate(main.products_list):
    if int(product_data[index]["last_checked_price"]) > int(product.price_difference):
        break

    if int(product.purchased_price) > int(product.price):
        pync.notify(product.name + " price has changed!", title=SCRIPT_NAME, open=product.url)
        product_data[index]["last_checked_price"] = int(product.price)
        with open('products.json', 'w') as f:
            json.dump(product_data, f, indent=2)