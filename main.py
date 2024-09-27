from MUStack import MUStack

run = True
stack = MUStack()

while run:
    string = input("Enter a space-delimited postfix expression. (Enter q to quit): ")
    if string.lower() == "q":
        print("Goodbye.")
        run = False
    else:
        expression = string.split(" ")
        for item in expression:
            if item.isdigit():
                stack.push(int(item))
            else:
                if stack.size() < 2:
                    print("\t Error: Not enough values in the stack.")
                    break
                value2 = stack.pop()
                value1 = stack.pop()

                if item == "+":
                    result = value1 + value2
                elif item == "-":
                    result = value1 - value2
                elif item == "*":
                    result = value1 * value2
                elif item == "/":
                    if value2 == 0:
                        print("\t Error: Number cannot be divided by zero.")
                        break
                    result = value1 / value2
                else:
                    print(f'\t "{item}" is not a valid operator/operand.')
                    break

                stack.push(result)

        if stack.size() == 1:
            print(f"\t Result: {stack.pop()}")
        else:
            print("\t Error: Invalid postfix expression.")

