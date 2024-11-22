import json
from collections import Counter

# Чтение данных из файла
with open('orders_july_2023.json', 'r') as file:
    data = json.load(file)

# Самый дорогой заказ
max_price_order = max(data, key=lambda x: data[x]['price'])
print(f"Самый дорогой заказ: {max_price_order}")

# Заказ с наибольшим количеством товаров
max_quantity_order = max(data, key=lambda x: data[x]['quantity'])
print(f"Заказ с наибольшим количеством товаров: {max_quantity_order}")

# День с максимальным количеством заказов
dates = [order['date'] for order in data.values()]
most_orders_day = Counter(dates).most_common(1)[0][0]
print(f"День с максимальным количеством заказов: {most_orders_day}")

# Средняя стоимость заказа
total_cost = sum(order['price'] for order in data.values())
average_cost = total_cost / len(data)
print(f"Средняя стоимость заказа: {average_cost:.2f}")

# Средняя стоимость товара
total_items = sum(order['quantity'] for order in data.values())
average_item_cost = total_cost / total_items
print(f"Средняя стоимость товара: {average_item_cost:.2f}")

# Пользователь с наибольшим количеством заказов
user_orders_count = {}

for order in data.values():
    user_id = order['user_id']
    if user_id not in user_orders_count:
        user_orders_count[user_id] = 1
    else:
        user_orders_count[user_id] += 1

most_active_user = max(user_orders_count, key=user_orders_count.get)
print(f"Пользователь с наибольшим количеством заказов: {most_active_user}")

# Пользователь с самой большой суммарной стоимостью заказов
user_total_costs = {}

for order in data.values():
    user_id = order['user_id']
    cost = order['price']

    if user_id not in user_total_costs:
        user_total_costs[user_id] = cost
    else:
        user_total_costs[user_id] += cost

biggest_spender = max(user_total_costs, key=user_total_costs.get)
print(f"У пользователя {biggest_spender} самая большая суммарная стоимость заказов")

