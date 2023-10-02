#11.1 Базовый уровень 4 вариант
class Product:
    def __init__(self, calorie_content, weight):
        self.calorie_content = calorie_content
        self.weight = weight

    def calculate_total_calories(self):
        return self.calorie_content * self.weight / 100  # переводим вес в граммах в килограммы

    def get_info_string(self):
        return f"Продукт: Калорийность - {self.calorie_content} кКал, Вес - {self.weight} г"
    

calorie_content_input = float(input("Введите калорийность продукта (кКал/100г): "))
weight_input = float(input("Введите вес продукта в граммах: "))

user_product = Product(calorie_content = calorie_content_input, weight=weight_input)

print(user_product.get_info_string())

total_calories = user_product.calculate_total_calories()
print(f"Общая калорийность продукта: {total_calories} кКал")


# 11.2 Базовый уровень 4 вариант
class Vitamins(Product):
    def __init__(self, calorie_content, weight, vitamin_c_content):

        super().__init__(calorie_content, weight)
        self.vitamin_c_content = vitamin_c_content

    def process_vitamin_c_data(self):
        print(f"Обработка данных о витамине C для продукта: {self.vitamin_c_content} мг в 1 г")

    def get_info_string(self):
        product_info = super().get_info_string()
        return f"{product_info}, Витамин C - {self.vitamin_c_content} мг в 1 г"

calorie_content_input = float(input("Введите калорийность продукта (кКал/100г): "))
weight_input = float(input("Введите вес продукта в граммах: "))
vitamin_c_content_input = float(input("Введите количество витамина C в 1 г продукта (мг): "))

vitamin_product = Vitamins(calorie_content=calorie_content_input, weight=weight_input, vitamin_c_content=vitamin_c_content_input)

print(vitamin_product.get_info_string())

vitamin_product.process_vitamin_c_data()
