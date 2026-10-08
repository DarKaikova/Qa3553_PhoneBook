# class Contact:
    # def __init__(self,name,last_name,phone,email,address,description):
    #     self.name = name
    #     self.last_name = last_name
    #     self.phone = phone
    #     self.email = email
    #     self.address = address
    #     self.description = description
from dataclasses import dataclass


@dataclass
class Contact:
    name:str
    last_name:str
    phone:str
    email:str
    address:str
    description:str


#* Датакласс (@dataclass) = «Класс-контейнер для данных»
#* Зачем нужен: Экономит код. Сам создает __init__, __repr__ (вывод в консоль) и __eq__ (сравнение объектов).
#* Главное правило: Все поля класса обязательно должны иметь аннотацию типа (name: str, age: int).
#* Без типов датакласс не поймёт, какие поля обрабатывать.