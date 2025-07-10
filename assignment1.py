#!/usr/bin/env python
# coding: utf-8

# In[1]:


# employee data
emp_data={101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}}


# In[2]:


def main_menu():
    while True:
        print("Select from this menu")
        print("1. Add an Employee")
        print("2. View all Employees")
        print("3. Search for an Employee")
        print("4. Exit")

        choice = int(input("Enter your choice(1-4):"))
        if (choice==1):
            add_employee()
        elif (choice == 2):
            view_employee()
        elif (choice == 3):
            search_employee()
        elif (choice == 4):
            print("Thank you for using Employee management system.")
            break
        else:
            print("Invalid choice! please make your choice between 1-4.")


# In[3]:


def add_employee():
    emp_id = int(input("Enter employee's Id:"))

    if emp_id in emp_data:
        print("This Employee ID already exist.Type another Employee ID.")
        return

    name = input("Enter Employee's name:")
    age = int(input("Enter Employee's age:"))
    department = int(input("Enter Employee's departement:"))
    salary = float(input("Enter Employee's Salary:"))

    emp_data[emp_id] = {"name":name,"age":age,"department":departemnt,"salary": salary}
    print(name,"Added successfully")


# In[8]:


def view_employee():
    if not emp_data:
        print("No employees available!")
        return
    
    print("\n--- Employee List ---")
    print("{:>10} {:<15} {:<10} {:<15} {:<10}".format("Emp ID", "Name", "Age", "Department", "Salary"))
    print("-" * 60)

    for emp_id, info in emp_data.items():
        print("{:<10} {:<15} {:<10} {:<15} {:<10}".format(
            emp_id, info['name'], info['age'], info['department'], info['salary']
        ))


# In[6]:


def search_employee():
    emp_id = int(input("Enter the employee Id you are searching for"))

    if emp_id in emp_data:
        emp = emp_data[emp_id]
        print(f"\n--- Details for Employee ID {emp_id} ---")
        print(f"Name      : {emp['name']}")
        print(f"Age       : {emp['age']}")
        print(f"Department: {emp['department']}")
        print(f"Salary    : {emp['salary']}")


# In[7]:


main_menu()


# In[ ]:




