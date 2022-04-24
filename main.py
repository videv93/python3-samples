from functools import reduce

class ItemManager: 
  items = []

  def addItem(self, item):
    self.items.append(item)

  def printItems(self):
    for item in self.items:
      print(f'{item.name}-{item.price}-{item.total}-{item.type}')

  def assets(self):
    return filter(lambda x: x.type == ItemType.asset, self.items)
  
  def liabilities(self):
    return filter(lambda x: x.type == ItemType.liability, self.items)

  def totalPrice(self):
    return reduce(lambda x,y: x.price + y.price, map(lambda x: x.price, self.items))


class ItemType:
  asset = 'asset'
  liability = 'liability'

class Item:
  def __init__(self, name, price, total, type) -> None:
    self.name = name
    self.price = price
    self.total = total
    self.type = type

manager = ItemManager()
manager.addItem(Item('table', 520000, 1, ItemType.asset))
manager.addItem(Item('chair', 999000, 2, ItemType.asset))
manager.addItem(Item('coca', 12000, 2, ItemType.liability))

manager.printItems()
print(manager.totalPrice())