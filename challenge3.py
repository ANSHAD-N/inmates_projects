def bmi(h, w):
    return w / (h ** 2)


height = float(input("Enter your height \n (in meter)\t"))
weight = float(input("Enter your weight \n (in Kg)\t"))
print("BMI=", bmi(height, weight))
