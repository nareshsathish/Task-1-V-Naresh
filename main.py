import json

data = {
    "customer_name": "Ravi",
    "city": "Chennai",
    "product": "Laptop",
    "quantity": 3,
    "unit_price": 45000,
    "discount": 10,
    "payment_method": "UPI",
    "order_id": "ORD1001"
}

with open("output.json", "w") as file:
    json.dump(data, file, indent=4)

print(json.dumps(data, indent=4))