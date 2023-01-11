from datetime import date

e = {
    "Name": "Siva Prakash",
    "Age": date.today().year - 2001,
    "Job": "Analyst",
    "Education": {
        "College": "College of Engineering, Guindy",
        "Year": range(2022, 2025),
    },
    "Monthly Salary": 30_000,
    "CTC": 6_00_000,
}

for k, v in e.items():
    print(f"{k} : {v}")
