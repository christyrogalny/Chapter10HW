class PayrollDeductionClass:

    def __init__(self,description,date,charge,employ_id):
        self.__description = description
        self.__date = date
        self.__charge_amount = charge 
        self.__employee_id = employ_id


    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    def get_charge(self):
        return self.__charge_amount
    
    def get_employee_id(self):
        return self.__employee_id



    def __str__(self):
        return 'Description \t \t Date \t \t Charge \t \t Employee ID'
        
    def __str__(self):
        return self.__description + '\t\t' + self.__date + '\t \t' + self.__charge_amount + '\t \t' + self.__employee_id

