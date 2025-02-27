class Dog:
    def speak(self ):
        return 'Woof!'
    
class Cat:
    def speak(self):
        return 'Meow!'
    
class AnimalFactory:
    def  create_dog(self):
        return Dog()
    
    def create_cat(self):
        return Cat()
        
factory = AnimalFactory()
dog = factory.create_dog()
cat = factory.create_cat()

print (dog.speak())
print (cat.speak())