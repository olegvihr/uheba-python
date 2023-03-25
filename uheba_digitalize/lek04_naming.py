# Именование переменных, классов и методов в коде
from telebot.types import User

customers = User.objects.filter()  # клиенты
paying_customers = User.objects.filter()  # клиенты, которые платят


def get_active_users():
    pass


def get_paying_companies():
    pass


company.is_paying
user.is_active

if city.aoding == '0c5b2444-.....':  # 1 вариант
    pass

MOSCOW_AODING = '0c5b2444-.....'  # 2 вариант правильный
if city.aoding == MOSCOW_AODING:
    pass


def get_cbr_course(from_currency: str, to_currency: str) -> Decimal:
    pass
