d = {
    "Krishna": "28/08/2001",
    "Siva Prakash": "03/10/2001",
    "Aravind": "30/06/2001",
    "Sanjay": "22/03/2001",
    "Akhil": "24/01/2001",
}
print(f"Original dict : \n{dict(sorted(d.items(), key=lambda x: x[0]))}")
k = input("Enter the name : ").title()
if k in d:
    print(d[k])

else:
    b = input("Enter the date of birth (dd/mm/yyyy) : ")
    d[k] = b
    print(f"Updated dict : \n{dict(sorted(d.items(), key=lambda x: x[0]))}")
