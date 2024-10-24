salary_camp = [6800, 5460.25, 6400.2456, 3200.1556, 8000.452]
emplo_camp = ['Виктор', 'Николай', 'Василий', 'Максим', 'Данил']
campain = dict(zip(emplo_camp, salary_camp))


def aver_salary():  # Возвращает средний заработной платы через переменную
    avg_sal = round(sum(salary_camp) / len(salary_camp), 2)
    return avg_sal


def max_salary():  # Возвращает максимальную зарплату через функцию
    return round(max(salary_camp), 2)


def min_salary():  # Возвращает максимальную зарплату через функцию
    return round(min(salary_camp), 2)


print(campain)
print(campain[emplo_camp[3]])
print(campain['Василий'])
print(f'Максимальная зарплата в кампании: {max_salary()}')
print(f'Минимальная зарплата в кампании: {min_salary()}')
print(f'Средняя зарплата в кампании: {aver_salary()}')
