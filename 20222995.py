#!/usr/bin/env python
# coding: utf-8

# In[9]:


# SHEHU KAKALE TILLI
# REG NO. 20222995


# Question 11
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is now open!")

restaurant = Restaurant("The Great Eats", "Italian")

print(f"Restaurant Name: {restaurant.restaurant_name}")
print(f"Cuisine Type: {restaurant.cuisine_type}")

# Calling methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Creating three different instances
restaurant1 = Restaurant("Burger Palace", "American")
restaurant2 = Restaurant("Sushi Haven", "Japanese")
restaurant3 = Restaurant("Spice Kingdom", "Indian")

# Calling describe_restaurant() for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


# In[3]:


# Question 1B
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print(f"Number of Customers Served: {self.number_served}")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

# Creating an instance called 'restaurant'
restaurant = Restaurant("The Great Eats", "Italian")

# Printing the initial number of customers served
restaurant.describe_restaurant()

# Changing the number of customers served and printing again
restaurant.number_served = 50
restaurant.describe_restaurant()

# Using the set_number_served() method
restaurant.set_number_served(100)
restaurant.describe_restaurant()

# Using the increment_number_served() method
restaurant.increment_number_served(30)
restaurant.describe_restaurant()


# In[4]:


# Question 1C
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print(f"Number of Customers Served: {self.number_served}")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        # Call the constructor of the base class (Restaurant)
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("Available Ice Cream Flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


# Creating an instance of IceCreamStand
ice_cream_stand = IceCreamStand("Sweet Treats", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip"])

# Calling methods from both the base class and the derived class
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()


# In[6]:


# Question 2A
class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

# Creating instances of the User class
user1 = User("John", "Doe", 25, "john.doe@example.com", "New York")
user2 = User("Jane", "Smith", 30, "jane.smith@example.com", "Los Angeles")
user3 = User("Bob", "Johnson", 22, "bob.johnson@example.com", "Chicago")

# Calling methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()


# In[7]:


# question 2B
class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
        print(f"Login Attempts: {self.login_attempts}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# Creating an instance of the User class
user = User("John", "Doe", 25, "john.doe@example.com", "New York")

# Calling increment_login_attempts() several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Printing the value of login_attempts
print(f"Login Attempts: {user.login_attempts}")

# Calling reset_login_attempts() to reset the value
user.reset_login_attempts()

# Printing login_attempts again to make sure it was reset to 0
print(f"After resetting, Login Attempts: {user.login_attempts}")


# In[8]:


# Question 2C
class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
        print(f"Login Attempts: {self.login_attempts}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Administrator Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, email, location, privileges):
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = Privileges(privileges)

# Creating an instance of Admin
admin_privileges = ["can add post", "can delete post", "can ban user"]
admin_user = Admin("Admin", "User", 30, "admin@example.com", "Admin City", admin_privileges)

# Calling the show_privileges() method for the Admin instance
admin_user.privileges.show_privileges()


# In[ ]:



