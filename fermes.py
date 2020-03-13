import datetime
import time

class animal:
    
    def __init__(self, genome, birthday, sex, age):
        self.genome = genome
        self.birthday = birthday
        self.sex = sex
        self.age = age
        
    def __str__(self):
        return "my animals is a " +self.genome+" born the "+str(self.birthday)+" he had "+str(self.age)+" and is a "+self.sex

class farm:
    
    def __init__(self, name, date, animal_list):
        self.name = name
        self.date = date
        self.animal_list = animal_list
               
    def __str__(self):
        return "my farm "+self.name+" born in "+str(self.date)
    
if __name__=="__main__":
    
    date_time= datetime.datetime.now()
    
    farm_list=[]
    animal_list1=[animal("chevre",date_time,"male", 0),animal("deer",date_time,"femmelle",0)]
    animal_list2=[animal("koala",date_time,"male", 0),animal("deer",date_time,"femmelle",0)]
    animal_list3=[animal("chevre",date_time,"male", 0),animal("koala",date_time,"male",0)]
    
    farm_list.append(farm("lafeuferme",date_time,animal_list1))
    farm_list.append(farm("lafaferme",date_time,animal_list2))
    farm_list.append(farm("lafuferme",date_time,animal_list3))

    
    
    while date_time.month<12:
        date_time = date_time + datetime.timedelta(weeks=4)
        
        for farm in farm_list:
            print("=========================================================")
            print("=",farm," =")
            print("=========================================================")
            print("")
            for animal in farm.animal_list:
                animal.age=animal.age+1
                print(animal)
                print("")
                time.sleep(0.5)