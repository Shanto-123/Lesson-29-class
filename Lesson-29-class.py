class Keyboard:
   def defination(self):
      print("Keyboard is an input device")
   def number_of_keys(self):
         print("There are 101 keys")
my_keyboard = Keyboard()       
my_keyboard.defination()
my_keyboard.number_of_keys()
my_keyboard = Keyboard()
my_keyboard.brand = "logitech"
print(my_keyboard.brand)
new_keyboard = Keyboard()
new_keyboard.defination()
new_keyboard.brand = "dell"
print(new_keyboard.brand)