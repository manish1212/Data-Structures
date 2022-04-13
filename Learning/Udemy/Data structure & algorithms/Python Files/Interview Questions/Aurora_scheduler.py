from collections import deque

class Employee:
    def __init__(self, name, type, availability):
        self.name = name
        self.type = type
        self.availability = availability
        
    def __str__(self):
        return str(self.name)+' '+ str(self.type) + ' '+ str(self.availability) + '\n'

class Building:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        
    def __str__(self):
        return str(self.name)+' '+ str(self.type) + '\n'


def Schedule(buildings, employees):
    weekdays  = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    employee_availability = {
        'monday':{},
        'tuesday':{},
        'wednesday':{},
        'thursday':{},
        'friday':{}
    }

    for employee in employees:
        for day in employee.availability:
            if day in employee_availability:
                employee_availability[day].setdefault(employee.type, deque()).append(employee)

    output = []
    for building in buildings:
        for day in weekdays:
            certified_installer = employee_availability[day]['certified_installer']
            ipc = employee_availability[day]['installers_pending_certification']
            laborers = employee_availability[day]['laborers']
            if building.type == 'one_story':
                if len(certified_installer)>0:
                    output.append((certified_installer.popleft().name,building.name, day))
                    break
            elif building.type == 'two_story':
                if len(certified_installer)>0 and (len(ipc)>0 or len(laborers)>0):
                    output.append((certified_installer.popleft().name,building.name, day))
                    if len(laborers)>0:
                        output.append((laborers.popleft().name,building.name, day))
                    else:
                        output.append((ipc.popleft().name,building.name, day))
                    break
            elif building.type == 'commercial_building':
                if len(certified_installer)>1 and len(ipc)>1 and (len(certified_installer) + len(ipc) + len(laborers))>7:
                    for i in range(2):
                        output.append((certified_installer.popleft().name,building.name, day))
                        output.append((ipc.popleft().name,building.name, day))

                    for i in range(4):
                        if len(laborers)>0:
                            output.append((laborers.popleft().name,building.name, day))
                        elif len(ipc)>0:
                            output.append((ipc.popleft().name,building.name, day))
                        else:
                            output.append((certified_installer.popleft().name,building.name, day))
                    break
            
    # print_emp_avail(employee_availability) # to print map of the type of employees working as per day 
    return output


def print_emp_avail(employee_availability):
    print("List of Emp available working on particular day")
    for day in employee_availability:
        print(day)
        for type in employee_availability[day]:
            print(type)
            for e in employee_availability[day][type]:
                print(e.name)
        print('\n')

def print_schedule(op):
    print("---Schedule---")
    for l in op:
        print(l,'\n')

# Create list of employees (name, type, availability)
list_of_employees = [
    Employee('employee1', 'certified_installer',['tuesday','wednesday','thursday']),
    Employee('employee2', 'certified_installer',['monday','tuesday','wednesday','thursday','friday']),
    Employee('employee3', 'certified_installer',['monday','tuesday','wednesday','thursday','friday']),
    Employee('employee4', 'certified_installer',['monday','tuesday','wednesday','thursday','friday']),
    Employee('employee5', 'installers_pending_certification',['monday','tuesday','wednesday','thursday','friday']),
    Employee('employee6', 'installers_pending_certification',['monday','tuesday','wednesday','thursday','friday']),
    Employee('employee7', 'installers_pending_certification',['monday','tuesday','wednesday','thursday','friday']),
    Employee('employee8', 'installers_pending_certification',['monday','tuesday','wednesday','thursday','friday']),
    Employee('employee9', 'laborers',['monday','tuesday','wednesday','thursday','friday']),
    Employee('employee10', 'laborers',['monday','tuesday','wednesday','thursday','friday']),
    Employee('employee11', 'laborers',['monday','tuesday','wednesday','thursday','friday']),
    Employee('employee12', 'laborers',['monday','tuesday','wednesday','thursday','friday'])
]

# create buildings (name, type)
buildings = [
    Building('building1','one_story'),
    Building('building2','one_story'),
    Building('building3','two_story'),
    Building('building4','two_story'),
    Building('building5','commercial_building'),
    Building('building6','commercial_building')
]

schedule_output = Schedule(buildings, list_of_employees)
print_schedule(schedule_output)


# Please make and state assumptions as needed. 
# One of the goals of this challenge is to see how you approach solving a problem so the instructions are intentionally somewhat ambiguous.

'''
# Approach
I divided the problme into 2 parts
1. availability of Employee in days of week 
2. order and requirement of the building
After calculation of the availability of the Employee for a day in a week, we could check the requirements for the specific building. We checked how many building can meet the requirements with the current availability of the employee on a specific day in a week and depending on that those buildings are assigned to the specific day to those employees. As the Employees who are available on that day was calculated before, then assigning them to a specific building was done if the building's requirement are matched.


# Assumption
I did not decide on Employee priority has not been decided and hence I have not considered the work load balancing for the employees
for e.g some workers would work more than others

# Edge cases 
1. If a specific building doesnt match the employment availability for the whole week because of the order, it would never be scheduled
2. distribution of work load over all the employees 
3. employee availabilty could be added -> if some workers have already covered certain number of installations and some have not then it should also be considered (similar to point 2)
'''
