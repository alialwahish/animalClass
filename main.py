import animal

anm=animal.Animal("cat",100)
dog=animal.Dog()
drag=animal.Dragon()




anm.walk()
anm.walk()
anm.walk()
anm.run()
anm.run()
anm.display()

dog.walk()
dog.walk()
dog.walk()
dog.run()
dog.run()
dog.pet()
dog.display()

drag.fly()
drag.displayHealth()

newAnm=animal.Animal("bash",50)
#>>> newAnm.pet() "AttributeError: 'Animal' object has no attribute 'pet' ""
#dog.fly() "AttributeError: 'Dog' object has no attribute 'fly' "