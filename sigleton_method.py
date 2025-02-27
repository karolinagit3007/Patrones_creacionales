class Dog:
    def speak(self ):
        return 'Woof!'
    
class Cat:
    def speak(self):
        return 'Meow!'
    
class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == 'dog':
            return Dog()
        elif animal_type == 'cat':
            return Cat()
        else:
            raise ValueError("Tipo Desconocido")
        
factory = AnimalFactory()
dog = factory.create_animal('dog')
cat = factory.create_animal('cat')

print (dog.speak())
print (cat.speak())