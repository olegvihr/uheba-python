# Полиморфизм - это механизм, позволяющий выполнить один и тот же код по-разному
# Ducktyping (утиная типизация) - наличие поведения для использования в полиморфизме
# в ЯП со статической типизацией для полиморфизма важно кто ты (какой тип), для питона важно что ты умеешь (поведение)


# class Animal:
#     def make_nois(self):
#         print('shh')
#
#
# class Cat(Animal):
#     def make_nois(self):
#         print('meow')
#
#
# class Dog(Animal):
#     def make_nois(self):
#         print('gavv')
#
#
# class Car:
#     def make_nois(self):
#         print('bi-bi')
#
#
# def noise(animal: Animal):
#     animal.make_nois()
#
#
# if __name__ == '__main__':
#     noise(Car())

class SQLiteDatabase:
    def connect(self):
        print("Connecting to datadase SQLiteDatabase")

    def get_users(self):
        print("get users with SQL")


class MongoDatabase:
    def connect(self):
        print("Connecting to datadase MongoDatabase")

    def get_users(self):
        print("get users with NoSQL")


class Server:
    def get_users(self, db):
        db.connect()
        users = db.get_users()
        return users


def get_db_from_config():
    print("read config")
    return SQLiteDatabase


class FakeDb:
    def connect(self):
        pass

    def get_users(self):
        return [1]


if __name__ == '__main__':
    server = Server()
    # server.get_users(get_db_from_config())
    assert [1] == server.get_users(FakeDb())
