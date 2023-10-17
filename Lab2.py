# Задача №4
def temp_cat(n):
    if int(temp) < -20:
        return '0' # Холодно
    elif int(temp) <= 0:
        return '1' # Прохладно
    elif int(temp) <= 15:
        return '2' # Зябко
    elif int(temp) <= 25:
        return '3' # Тепло
    elif int(temp) > 25:
        return '4' # Жарко
    else:
        print('ERROR')

temp = int(input())
temp_r = temp_cat(temp)
result = temp_r
print(result)

input()

# Задача №5
# def check_phn(phone):
#     if str(phone) 

# phone