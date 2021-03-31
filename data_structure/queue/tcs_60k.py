class Person(object):
    def __init__(self, name, height, weight, bmi=0, status=''):
        self.set_param(name, height, weight, bmi, bmi_status)

    def set_param(self, name, height, weight, bmi, bmi_status):
        if type(name) == str:
            self.name = name
        else:
            raise TypeError("Name must be string")
        if type(height) == int:
            self.height = height
        else:
            raise TypeError("height must be integer")
        if type(weight) == int:
            self.weight = weight
        else:
            raise TypeError("Weight must be integer")
        if type(bmi) == int:
            self.bmi = bmi
        else:
            raise TypeError("bmi must be a number")
        if type(bmi_status) == str:
            self.bmi_status = bmi_status
        else:
            raise TypeError("bmi_status must be string")

    def calculateBmi(self):
       self.bmi = round(self.weight / (self.height * self.height))

class Society:
    def __init__(self, bmi_status, person_list):
        self.bmi_status = bmi_status
        self.person_list = person_list

    def calculateBmiAndStatusByName(self, name):
        flag = False
        for person in self.person_list:
            if person.name.lower() == name.lower():
                flag = True
                person.calculateBmi()
                print(person.bmi, end=' ')
                for val in self.bmi_status.keys():
                    value = self.bmi_status[val]
                    if value[0] <= person.bmi <= value[1]:
                        print(val)
                        person.bmi_status = val
        return flag

    def removeInvalidPersons(self, bmi):
        li = []
        for person in self.person_list:
            person.calculateBmi()
            if person.bmi < bmi:
                li.append(person)
                #print(person.name, person.bmi)
        return li


list_of_persons = []
n = int(input("n: "))
for _ in range(n):
    name = input()
    height = int(input())
    weight = int(input())
    p = Person(name, height, weight)
    list_of_persons.append(p)
bmi_status = {}
N = int(input("N: "))
for _ in range(N):
    status = input()
    l, u = int(input("l: ")), int(input("u: "))
    if l > u:
        l, u = u, l
    bmi_status[status] = (l, u)
society = Society(bmi_status, list_of_persons)
Name = input("Name: ")
num = int(input("num: "))
flag = society.calculateBmiAndStatusByName(Name)
if not flag:
    print('No Person Exists')
res = society.removeInvalidPersons(num)
for x in res:
    print(x.name, x.bmi)