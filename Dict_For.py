fcc_dict = {"name": "TechCampEthiopia",
           "type": "non-profit", 
           "mode": "remote", 
           "paid": "no"}

for key in fcc_dict:
    print(key, end=" ")

# Output: name type mode paid 
#Using for loop for getting value
for values in fcc_dict.values():
    print(values , end=" ")

# Output: CodeCampEthiopia non-profit remote no
