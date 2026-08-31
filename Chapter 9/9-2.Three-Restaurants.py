
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

restaurant1 = Restaurant("Mama's Kitchen", "Italian")
restaurant2 = Restaurant("Spice Route", "Indian")
restaurant3 = Restaurant("Ocean Basket", "Seafood")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()