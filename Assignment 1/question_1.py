first_name = input("Enter the 1st name: ")
second_name = input("Enter the 2nd name: ")

T_count = first_name.lower().count('t')
T_count += second_name.lower().count('t')

R_count = first_name.lower().count('r')
R_count += second_name.lower().count('r')

U_count = first_name.lower().count('u')
U_count += second_name.lower().count('u')

E_count = first_name.lower().count('e')
E_count += second_name.lower().count('e')


L_count = first_name.lower().count('l')
L_count += second_name.lower().count('l')

O_count = first_name.lower().count('o')
O_count += second_name.lower().count('o')

V_count = first_name.lower().count('v')
V_count += second_name.lower().count('v')

E_count = first_name.lower().count('e')
E_count += second_name.lower().count('e')

True_count = T_count + R_count + U_count + E_count
Love_count = L_count + O_count + V_count + E_count

Total = int(str(True_count) + str(Love_count))

if Total < 10 and Total > 90:
    print(f"Your score is {Total}, you go together like coke and mentos.")

elif Total > 40 and Total < 50:
    print(f"Your score is {Total}, you are alright together.")

else:
    print(f"Your score is {Total}.")
    
    






