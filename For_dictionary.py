#creating dictionary named fcc_dict
fcc_dict = {"name": "TechCampEthiopia",
           "type": "non-profit", 
           "mode": "remote", 
           "paid": "no"}

for key, value in fcc_dict.items():
    print(key, value)

# Output will be 
# name TechCampEthiopia
# type non-profit
# mode remote
# paid no
fcc_dict = {"name": "TechCampEthiopia",
           "type": "non-profit", 
           "mode": "remote/ In person", 
           "paid": "no"}
#Iterate dictionary using for loop
for a, b in fcc_dict.items():
    # print(a, b)
    if a == "type":
        print("TechCampEthiopia is a non-profit organization")

# Output: TechCampEthiopia is a non-profit organization
