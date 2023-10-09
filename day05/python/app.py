import statistics

# pas e constante 
CONST = 2 

age = 25 
sympa = "okok"

print(age, sympa)

print(age, end=None)

def hw():
    print("hello World")
    print("hello World")
    print("hello World")

hw()


def add(x, y):
    return x + y
    

def div(x, y):
    return x / y

print(add(5,9))


try:
    print(div(8, 2)) 
    print(div(8, 0)) 
except (ZeroDivisionError, TypeError) as e:
    print(e.args)

if(age > 18):
    print("Buy alcool")
elif age < 4:
    print("Milk see")
else:
    pass

if age in range(1, 25):
    print("should not  drink")    

names = ["jack", "jim", "Johny", "minou","koko","toto"]
print(names)
print(names[1:4])
print(names[2:])
print(names[:-2])
print(names[::3])

names.append("Mahalia")
names.insert(0, "Alexandre")
names.insert(0, "Alexandre")
print(names)
names.pop()
names.pop(0)

print(names)
print(sorted(names))
names.extend(["Omar", "Arthur", "Garance", "Kaoutar", "Kilian"])
print(names)

for i in range(0, len(names)):
    print(i)

for i in names:
    print(i)

for i, name in enumerate(names):
    print(i)
    print(name)

def funcArgs(*args):
    print(args)

def funcKArgs(**kargs):
    print(kargs)



funcArgs("arg1", "arg2", "arg3")
funcKArgs(name="arg1", age="arg2", job="arg3")

# type de donné simple
# int float boo 

# type de donné collection
# string"collection de lettre", list[sequence de caleur indexe alterables", tuple (indexé, inalterable), set {sequence, unique, inalterable, non indéxé}, dictionnaire {name: "elel", othername: "pkl" }

elm = ("1", "2", "3", "4")
print(elm)
elm += ("5",)

print(elm)
print("1" in elm)
print("99" in elm)
individu = {
    "nom": "Carlier",
    "age": 25,
    "enfants": ["Jeremy", "William", "Thomas"],
    "epouses": [
        {"name": "Virginie", "age": 19},
        {"name": "Sophie", "age": 59},
        {"name": "Alice", "age": 99}
    ]
}

print(individu)

# AVEZRAGE CALCULE
cumul = 0
for epouse in range(0, len(individu["epouses"])):
    cumul += individu["epouses"][epouse]["age"]

print(cumul / len(individu["epouses"]))

# Average calcule in one line
print(statistics.mean([i["age"] for i in individu["epouses"]]))


# CLASS

class Human:
    def __init__(self):
        self.connerie = True

    def parler():
        print("blabla")
    
class Bipede:
    def __init__(self):
        self.pattes = 2
  
class Utilisateur(Bipede, Human):
    
    __age_private = 23
    age_public = 50

    def __init__(self):
        super().__init__()
        self.name = "Richnou"
        self.age = 50

    def show_name(self):
        print(self.name)

    def set_name(self, newName):
        self.name = newName

    def user_talk():
        Human.parler()
  
    
prof = Utilisateur()
print(prof.age_public)
print(Utilisateur.age_public)
print(Utilisateur.age_public)
print(Utilisateur.user_talk())
print(Utilisateur.__dict__)
print(Utilisateur.__sizeof__)

































