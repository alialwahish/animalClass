
class Animal(object):
    def __init__(self,name,health):
        self.name=name
        self.health=health
    def walk(self):
        print self.name,"walked"
        self.health-=1
        return self
    def run(self):
        print self.name,"ran"
        self.health+=5
        return self
    def display(self):
        print self.name,"Health: ",self.health
        return self

class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__("Dog",150)
        
    def pet(self):
        print "Fetting",self.name
        self.health+=5
class Dragon(Animal):
    def __init__(self):
        super(Dragon,self).__init__("Dragon",170)
    def fly(self):
        print "Flying",self.name
        self.health-=10
    def displayHealth(self):
        self.display()
        print "I'm a Dragon"



