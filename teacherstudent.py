import numpy as np
## Creating authoratative Data

## Defining Range for F,R,C,K

fah1 = np.arange(-459.67, 211.9710, 0.1)
rankine1 = np.arange(0, 671.641, 0.1)
celcius1 = np.arange(-272.15, 99.98, 0.1)
kelvin1 = np.arange(0, 373.1339, 0.1)

##Rounding to 10th Decimal place
fah = ['%.1f' % elem for elem in fah1]
rankine = ['%.1f' % elem for elem in rankine1]
celcius = ['%.1f' % elem for elem in celcius1]
kelvin = ['%.1f' % elem for elem in kelvin1]

#Input unit of Measure
unitofmeasure = ["Fahrenheit", "Rankine", "Celcius", "Kelvin"]

#Target Unit of Measure
targetunitofmeasure = ["Fahrenheit", "Rankine", "Celcius", "Kelvin"]


## Taking input from Users/Teacher and round to 10th decimal place

num1 = float(input("Enter Numerical Value:"))
num = float(round(num1, 1))
print(num)

inputunitofmeasure = input("Enter Unit of Measure")
print(inputunitofmeasure)

studenttargetunitofmeasure = input("Enter Target Unit of Measure")
print(studenttargetunitofmeasure)

studentnumericresponse1 = float(input("Enter Student's Numeric Response"))
studentnumericresponse = float(round(studentnumericresponse1, 1))
print(studentnumericresponse)


print(" the value is ", fah)


if ((num in fah) and (inputunitofmeasure in unitofmeasure) and (studenttargetunitofmeasure in targetunitofmeasure) and (studentnumericresponse in fah,rankine,celcius,kelvin)):
    print("Correct")
else:
    print("Incorrect")





