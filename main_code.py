import art
print(art.logo)
def add(n1, n2):
    return n1 + n2
def multiply(n1, n2):
    return n1 * n2
def subtract(n1, n2):
    return n1 - n2
def divide(n1, n2):
    return n1 / n2

operation={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
def calculator():

    should_continue=True
    first_number=float(input("What's the first number?: "))

    while should_continue:
        print("+\n-\n*\n\ \npick an operation:")
        operation_to_be_performed=input()
        second_number=float(input("what's the next number?: "))
        answer=operation[operation_to_be_performed](first_number,second_number)
        print(f"{first_number} {operation_to_be_performed} {second_number} = {answer}")
        yes_no=input(f"type 'y' to continue with {answer} and type'n' to stop the calculation").lower()
        if yes_no=="y":
            first_number=answer
        else:
            should_continue=False
            print("\n"*20)
            calculator()
calculator()



