import shutil
import re

def count_chinese_characters(text):
    pattern = re.compile(r'[\u4e00-\u9fff]')
    chinese_characters = re.findall(pattern, text)
    count = len(chinese_characters)
    return count

car_sales = {
    "一Toyota Camry": 5000,
    "二二Honda Civic": 4500,
    "三三三Ford Mustang": 6000,
    "Chevrolet Silverado": 5500,
    "Nissan Altima": 4000,
    "BMW 3 Series": 3500,
    "Mercedes-Benz C-Class": 3000,
    "Audi A4": 2500,
    "Lexus RX": 2000,
    "Tesla Model 3": 27000,
    "Hyundai Elantra": 1500
}

sum_of_sales = sum(car_sales.values())
max_len_of_key = max(len(key) for key in car_sales.keys())

screen_width = int(shutil.get_terminal_size().columns)
len_of_result = max_len_of_key + 8
full_percentage_width = screen_width - len_of_result

for key, value in sorted(car_sales.items(), key=lambda x: x[1], reverse=True):
    count_of_chinese = count_chinese_characters(key)
    
    percentage_of_sales = float(value/sum_of_sales) * 100
    percentage_width = int((percentage_of_sales / 100) * (full_percentage_width))
    equal_signs = "=" * percentage_width

    result = f"{key:<{max_len_of_key-count_of_chinese}} {equal_signs:<{full_percentage_width}} {percentage_of_sales:>5.2f}%"
    print(result)