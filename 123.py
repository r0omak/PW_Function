# Завдання 1 
def transform_numbers(x, y, z):
    numbers = [x, y, z]
    transformed = [(n ** 2 if n >= 0 else n ** 4) for n in numbers]
    return transformed

x = float(input("Введіть перше число: "))
y = float(input("Введіть друге число: "))
z = float(input("Введіть третє число: "))

result = transform_numbers(x, y, z)
print("Перетворені числа:", result)

# Завдання 2
def closer_to_origin(x1, y1, x2, y2):
    dist_A = (x1 ** 2 + y1 ** 2) ** 0.5
    dist_B = (x2 ** 2 + y2 ** 2) ** 0.5
    if dist_A < dist_B:
        return "Точка A ближче до початку координат"
    elif dist_B < dist_A:
        return "Точка B ближче до початку координат"
    else:
        return "Точки A і B знаходяться на однаковій відстані від початку координат"
       
x1, y1 = map(float, input("Введіть координати точки A (x1, y1): ").split())
x2, y2 = map(float, input("Введіть координати точки B (x2, y2): ").split())

result = closer_to_origin(x1, y1, x2, y2)
print(result)

# Завдання 3
def is_triangle_and_right_angle(angle1, angle2):
    if angle1 + angle2 < 180:
        if angle1 == 90 or angle2 == 90 or angle1 + angle2 == 90:
            return "Трикутник існує і він прямокутний"
        else:
            return "Трикутник існує, але він не прямокутний"
    else:
        return "Трикутник не існує"
       
angle1 = float(input("Введіть величину першого кута: "))
angle2 = float(input("Введіть величину другого кута: "))

result = is_triangle_and_right_angle(angle1, angle2)
print(result)
# Завдання 4
def replace_numbers(x, y):
    if x < y:
        x, y = (x + y) / 2, x * y * 2
    else:
        y, x = (x + y) / 2, x * y * 2
    return x, y

x = float(input("Введіть перше число (x): "))
y = float(input("Введіть друге число (y): "))

new_x, new_y = replace_numbers(x, y)
print("Перетворені числа: x =", new_x, ", y =", new_y)

# Завдання 5
def point_position(x, y):
    if x == 0 and y == 0:
        return "Точка знаходиться на початку координат"
    elif x == 0:
        return "Точка знаходиться на осі Y"
    elif y == 0:
        return "Точка знаходиться на осі X"
    elif x > 0 and y > 0:
        return "Точка знаходиться в першій чверті"
    elif x < 0 and y > 0:
        return "Точка знаходиться в другій чверті"
    elif x < 0 and y < 0:
        return "Точка знаходиться в третій чверті"
    elif x > 0 and y < 0:
        return "Точка знаходиться в четвертій чверті"

x = float(input("Введіть координати точки A (x): "))
y = float(input("Введіть координати точки A (y): "))

result = point_position(x, y)
print(result)

# Завдання 6
def replace_if_equal(a, b):
    if a != b:
        max_value = max(a, b)
        a, b = max_value, max_value
    else:
        a, b = 0, 0
    return a, b

a = int(input("Введіть перше число (a): "))
b = int(input("Введіть друге число (b): "))

new_a, new_b = replace_if_equal(a, b)
print("Перетворені числа: a =", new_a, ", b =", new_b)

# Завдання 7
def count_negatives(a, b, c):
    numbers = [a, b, c]
    count = sum(1 for n in numbers if n < 0)
    return count

a = int(input("Введіть перше число (a): "))
b = int(input("Введіть друге число (b): "))
c = int(input("Введіть третє число (c): "))

result = count_negatives(a, b, c)
print("Кількість негативних чисел:", result)

# Завдання 8
def count_positives(a, b, c):
    numbers = [a, b, c]
    count = sum(1 for n in numbers if n > 0)
    return count

a = int(input("Введіть перше число (a): "))
b = int(input("Введіть друге число (b): "))
c = int(input("Введіть третє число (c): "))

result = count_positives(a, b, c)
print("Кількість додатних чисел:", result)

# Завдання 9
def count_integers(a, b, c):
    numbers = [a, b, c]
    count = sum(1 for n in numbers if n == int(n))
    return count

# Введення чисел
a = float(input("Введіть перше число (a): "))
b = float(input("Введіть друге число (b): "))
c = float(input("Введіть третє число (c): "))

result = count_integers(a, b, c)
print("Кількість цілих чисел:", result)
