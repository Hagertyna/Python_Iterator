 a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
 for key in a_dict:
   print(key)
   
#Sorted by key
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
for key in sorted(incomes):
    print(key, '->', incomes[key])
