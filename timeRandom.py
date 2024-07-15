import random

OPERATORS = ["-", "+", "7", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12

def genarate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)