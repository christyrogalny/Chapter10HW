import EmployeeClass as ec
import PayrollDeductionClass as pd

def main():

    name = 'Jimmy Smith'
    id_num = '58475'
    dep = 'Information Systems'
    job = 'Developer'
    salary = '$6,800.00'
    
    print('Name: '+ name +'\n'+ 'ID Number: '+id_num +'\n'+'Department: '+dep +'\n'+'Job Title: '+ job +'\n'+'Monthly Salary: '+salary)
    print('\n')
    print('\n')
    employee_list = [name, id_num, dep, job, salary]
    
    
    description1 = pd.PayrollDeductionClass('food court', '8/14/2022', '22.50', '39119')
    description2 = pd.PayrollDeductionClass('gift contribution', '8/12/2022', '25.00', '58475')
    description3 = pd.PayrollDeductionClass('food court', '8/17/2022', '15.25', '21547')
    description4 = pd.PayrollDeductionClass('vending machine', '8/22/2022', '3.00', '58475')
    description5 = pd.PayrollDeductionClass('vending machine', '8/5/2022', '2.75', '58475')
    
    print('Description \t \t Date \t \t \t  Charge \t  Employee ID')
    print('\n')
    print(description1)
    print(description2)
    print(description3)
    print(description4)
    print(description5)

    
    if id_num == pd.employ_id:
        deduction = salary - pd.charge

        print(deduction)


main()
