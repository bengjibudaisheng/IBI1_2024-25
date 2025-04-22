# Defien a class.
class patients:
    def __init__(self,name,age,date,medical_history):
        self.name=name
        self.age=age
        self.date=date
        self.medical_history=medical_history

    # Define a funtion that could print the information of patient.    
    def print_details(self):
        print(f'name:{self.name}\nage:{self.age}\ndate:{self.date}\nmedical_history:{self.medical_history}')    

# Record the information of patient.
x=patients('ABC','18','2025-01-01','None')

x.print_details()