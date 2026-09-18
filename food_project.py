class FoodItem:  #class food items 
    def __init__(self, name,price,category): #construction 
        self.name=name 
        self._price=price  #make it protacted dont directly access 
        self.category=category 
         
    @property 
    def price(self): 
        return self._price 
     
    @price.setter 
    def price(self,value): 
        if value<0: 
            raise ValueError("Price cannot be negative") 
         
        self._price=value 
         
         
    def show_details(self): 
        print(f"{self.name} - {self._price} - {self.category}") 
         
         
class Restaurant: 
    def __init__(self,name): 
        self.name=name 
        self.menu=[] 
         
    def add_food(self,food): 
        self.menu.append(food) 
         
    def remove_food(self,food): 
        self.menu.remove(food) 
         
    def show_menu(self): 
        print(f"\n--{self.name} Menu--") 
         
        for food in self.menu: 
            food.show_details() 
             
    def show_restaurant(self): 
        print(f"Restaurant{self.name}") 
        print(f"Items available  {len(self.menu)}") 
             
     
class Cart: 
    def __init__(self): 
        self.items=[] 
         
    def add_itmes(self,food): 
        self.items.append(food) 
         
    def remove_itmes(self, food): 
        self.items.remove(food) 
         
    def show_cart(self): 
        print("\n--CART--") 
         
        for food in self.items: 
            food.show_details() 
             
    def calculate_total(self): 
        total=0 
        for food in self.items: 
            total+=food.price 
        return total
         
class Customer: 
    def __init__(self,name): 
        self.name=name 
        self.cart=Cart() #Single Responsibility Principle. 
         
    def add_item(self,food): # convient way to access 
        self.cart.add_itmes(food) 
         
    def remove_item(self,food): 
        self.cart.remove_itmes(food) 
        
    def show_cart(self): 
        self.cart.show_cart() 
        
    def get_cart_total(self):  # just a convinent way to access 
        return self.cart.calculate_total() 
         
         
pizza=FoodItem("Pizza", 250, "Fast Food")  #create a object or instance  
burger=FoodItem("Burger",80,"Fast Food") 
briyani=FoodItem("Briyani",200,"Indian") 
momos=FoodItem("Momos",80,"Turkis") 
Noodles=FoodItem("Noodles", 80, "Fast Food") 
 
# print(pizza._price)  #using property we are call the methods without () 
restaurant=Restaurant("Food Palace") 
# pizza.price=90 
# pizza.show_details() 
# burger.show_details() 
# briyani.show_details() 
restaurant.add_food(pizza) 
restaurant.add_food(burger) 
restaurant.add_food(briyani) 
restaurant.add_food(momos) 
restaurant.add_food(Noodles) 
 
restaurant.remove_food(pizza)  # remove food item from list  
 
 
print("---------------------") 
restaurant.show_restaurant() 
print("---------------------") 
restaurant.show_menu() 

cart=Cart() 
# cart.add_itmes(burger) 
# cart.add_itmes(momos) 
# cart.add_itmes(momos) 
# cart.remove_itmes(momos) 
# cart.show_cart() 
# cart.calculate_total() 
 
 
customer=Customer("Prabhanshu Shrivansh") 
# customer.cart.add_itmes(momos) 
# customer.cart.add_itmes(burger)  # i will modify this and now easy way to access it more convinent way  

customer.add_item(Noodles) 
customer.add_item(burger)
customer.add_item(momos)
customer.remove_item(momos) 
print("------------------------")
print(customer.name)
customer.show_cart() 
print("\nTotal Price:", customer.get_cart_total())