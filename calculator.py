
# This is a calculator project. It takes two inputs as floats from the user. Where after the user can choose what 
# arethmatic operation he wants to use on the input. 
# It is user-friendly as it handles however the user chooses to write the desired operation. 
# This is doen by converting the input to lowercase and later slicing the string, so it only deals with the first three characters 
# in the string. Hence by using these three characters it matches it to the keys in the library and performs the desired operation 
# on the input. 

a = float(input('Insert a number '))
b = float(input('Insert another number '))

user = input('Insert the operation you want to perform: ').lower()
op = user[:3]

operations = {
    'add': a + b,
    'sub': a - b,
    'mul': a * b,
    'div': a / b
}

if op in operations:
    operation = operations[op]
    print("Result: ", operation)
else: 
    print("Invalid operation")

     