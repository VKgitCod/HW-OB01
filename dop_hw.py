class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар {item_name} был добавлен в {self.name}")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар {item_name} был удален из {self.name}")

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара {item_name} в магазине {self.name} была изменена на {new_price}")
        else:
            print(f"Товар {item_name} не найден")

store1 = Store("Магнит", "Ленина 12")
store2 = Store("Перекресток", "Ленина 15")
store3 = Store("Спар", "Ленина 17")

store1.add_item("Слайсы", 35)
store1.add_item("Не молоко", 100)
store1.add_item("Яйца", 110)

store1.remove_item("Слайсы")

store1.update_price("Не молоко", 90)

print(store1.get_price("Яйца"))
