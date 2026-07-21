#LOW LEVEL - it only performs calculation. It doesn't interact with user
def calculate (a:float, b:float, op:str):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b #zeroDivision if b==0

#MIDDLE LEVEL - parsing. Convert string into numbers
def pars(a_str: str, b_str: str, op: str):
    a = float(a_str) #value error if not number
    b = float (b_str) #value error if not number
    return calculate (a, b, op)

#TOP LEVEL - dialog. It captures everything and explains it to the user
def run_calculator ():
    try:
        a = input ("Enter first number: ")
        b = input ("Enter second number: ")
        op = input ("Enter Action (+, -, /, *): ")
        result = pars (a, b, op)
        print (f"Result:{result}")
    except ValueError as e:
        print (f"Invalid data: {e}")
    except ZeroDivisionError as e:
        print("You can't divide by zero!")

run_calculator()