class EmployeeClass:

    def __init__(self,name,id_num,dep,job,salary):
        self.__name = name
        self.__id_num = id_num 
        self.__dep = dep
        self.__job = job 
        self.__salary = salary 


    def get_name(self):
        return self.__name

    def get_id_num(self):
        return self.__id_num

    def get_department(self):
        return self.__dep
    
    def get_job(self):
        return self.__job
    
    def get_salary(self):
        return self.__salary

    def __str__(self):
        return self.__name + '\t' + self.__id_num + '\t \t' + self.__dep + '\t' + self.__job + '\t\t' + self.__salary
