import random
import time

#OPERATORS = ["-", "+", "/", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
OPERATORS.remove(OPERATORS[1])
TOTAL_PROBLEMS = 10

def genarate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left)+" "+ operator +" "+str(right)
    result = eval(expr)
    #print(expr," = ", result)
    return expr, result

#genarate_problem()

wrong = 0
input("Press Enter to start")
print("----------------------")

start_time = time.time()

for i in range (TOTAL_PROBLEMS):
    expr, result = genarate_problem()
    while True:
        guess = input("PROBLEM "+str(i+1)+": "+expr+" = ")
        if guess == str(result):
            break
        wrong += 1
        print("fals! Try again:")

end_time = time.time()
total_time = round(end_time - start_time, 2)
print("----------------------")
print("du hast " +str(wrong)+ " Fehler gemacht")
print("Good work, you finished in ", total_time, " seconds")
