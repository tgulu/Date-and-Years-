"""
Restaurant booking Class for customers
"""

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __str__(self):
    return f'Restaurant location = {self.address}'

  def __repr__(self):
    return self.address 

  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus 

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased in purchased_items:
      if purchased in self.items:
        bill += self.items[purchased]
    return bill

  def __repr__(self):
    return self.name + " Menu available from "+ str(self.start_time) + ' - ' + str(self.end_time) 

  # def __str__(self):
  #   return f'Menu = {self.name}\nitems = {self.items}\nstart_time = {self.start_time}\nend_time = {self.end_time}\n'

brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

brunch_menu = Menu("Brunch", brunch_items, 1100, 1600)

early_bird_menu = Menu("Early Bird", early_bird_items, 1500, 1800)

dinner_menu = Menu("Dinner", dinner_items, 1700, 2300)

kids_menu = Menu("Kids", kids_items, 1100, 2100)

menus = [early_bird_menu, brunch_menu, kids_menu, dinner_menu] 

flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

first_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_place = Franchise("189 Fitzgerald Avenue",arepas_menu)

new_business = Business("Take a' Arepa", [arepas_place])

# **print items in the menu**
# print(kids_menu)
# print(brunch_menu)

# **brunch food bill**
# print(brunch_menu.calculate_bill(['pancakes', 'home fries',  'coffee']))

# **early bird food bill**
# print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))


# **print restaurant location**
# print(flagship_store)

# **print available_menus
# print(new_installment.available_menus(1200))

# **print business 
# print(new_business.name)
# print(new_business.franchises[0])


