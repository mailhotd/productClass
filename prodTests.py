from product import productList
import time

p = productList()
print(p.fnl)
print(p.pk)

partition = productList()
p.set('sku','ts-022')
p.set('name','shirt')
p.set('price','25.00')

p.add()

p.insert()

p = productList()
p.getAll()
print(p.data)




















