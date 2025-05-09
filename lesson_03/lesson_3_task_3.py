from Address import Address
from Mailing import Mailing

# Создаем адреса
to_addr = Address("123456", "Москва", "Ленинский проспект", "10", "15")
from_addr = Address("654321", "Санкт-Петербург", "Невский проспект", "20", "25")

# Создаем отправление
mail = Mailing(to_addr, from_addr, 150.0, "AB1234567890")

# Распечатываем информацию
print(f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} "
      f"в {mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, {mail.to_address.house} - {mail.to_address.apartment}. Стоимость {mail.cost} рублей.")