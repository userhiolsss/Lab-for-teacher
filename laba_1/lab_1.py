import time

name = "Ярема"
birth_year = 2006

print("Обчислення віку...")
time.sleep(2) 

current_year = time.localtime().tm_year
age = current_year - birth_year

print("Визначення статусу...")
time.sleep(1)  
status = "мужичара" if age >= 18 else "школотрон"

print(f"{name} є {age} років і він вважається {status}.")