import peewee
import random

db = peewee.SqliteDatabase('data.db')


class Product(peewee.Model):
    name = peewee.CharField()
    category = peewee.CharField(null=True)
    price = peewee.IntegerField()

    stock = peewee.IntegerField()

    class Meta:
        database = db


class Category(peewee.Model):
    name = peewee.CharField()

    class Meta:
        database = db


# Достать из базы все товары одной категории
d1 = Product.filter(category=1)
for i in d1:
    print(i.name)

# Узнать сумарную стоимость всех товаров на складе
d2 = Product.filter()
c = 0
for i in d2:
    c = i.price + c
print(f'Cумма склада равна {c} грн')


# Сделать функцию купить товар, которая возвращает True Если удалось купить товар,
# и False, если товар закончилился.

def zakupka(name:str, zakaz:int):
    x = Product.get(name=name)
    if x.stock - zakaz > 0:
        print('True')
    else:
        print('False')


zakupka('product_name11', 40)


"""
c1 = Category.create(name='category1')
c2 = Category.create(name='category2')
c3 = Category.create(name='category3')



p3 = Product.create(name='product_name1',category=c1, price=random.randint(300, 500), stock=random.randint(10, 700))
p4 = Product.create(name='product_name1',category=c2, price=random.randint(300, 500), stock=random.randint(10, 700))
p5 = Product.create(name='product_name1',category=c3, price=random.randint(300, 500), stock=random.randint(10, 700))
p6 = Product.create(name='product_name1',category=c1, price=random.randint(300, 500), stock=random.randint(10, 700))
p7 = Product.create(name='product_name1',category=c2, price=random.randint(300, 500), stock=random.randint(10, 700))
p8 = Product.create(name='product_name1',category=c3, price=random.randint(300, 500), stock=random.randint(10, 700))
p9 = Product.create(name='product_name1',category=c1, price=random.randint(300, 500), stock=random.randint(10, 700))
p10 = Product.create(name='product_name1',category=c2, price=random.randint(300, 500), stock=random.randint(10, 700))
p11 = Product.create(name='product_name1',category=c3, price=random.randint(300, 500), stock=random.randint(10, 700))
p12 = Product.create(name='product_name1',category=c1, price=random.randint(300, 500), stock=random.randint(10, 700))
p13 = Product.create(name='product_name1',category=c2, price=random.randint(300, 500), stock=random.randint(10, 700))

"""
