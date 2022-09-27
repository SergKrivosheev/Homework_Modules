from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime, date, time
import pyTelegramBotAPI

def get_time():
    date(2022, 9, 27)
    time(15, 11)
    return print(datetime.now())

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    get_time()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
