weight = float(input("What is your weight? "))

measure = str(input("K(g) or L(b)s? "))
if measure == 'K' or measure == 'k':
    weight = weight * 2.2
    print("Your weight in L(b)s is:", weight)
    
elif measure == 'L' or measure == 'l':
    weight = weight * 0.453592
    print("Your weight in K(g) is:", weight)