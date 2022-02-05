msg_0 = 'Enter an equation'
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
memory = 0


def main_play():
    while True:
        print(msg_0)
        calc = input().split()
        x, oper, y = calc[0], calc[1], calc[2]
        if x == 'M':
            x = memory
        if y == 'M':
            y = memory
        try:
            x, y = float(x), float(y)
            if oper == '+' or oper == '-' or oper == '*' or oper == '/':
                check(x, y, oper)
                operation(x, oper, y)
                break
        except ValueError:
            print(msg_1)
        except ZeroDivisionError:
            print(msg_3)
        else:
            print(msg_2)


def operation(x, oper, y):
    global result
    if oper == '+':
        result = x + y
    if oper == '-':
        result = x - y
    if oper == '*':
        result = x * y
    if oper == '/':
        result = x / y
    print(result)


def calc_play():
    while True:
        global memory
        print(msg_4)
        answer = input()
        if answer == 'y':
            memory = result
            print(msg_5)
        if answer == 'n':
            print(msg_5)
        answer2 = input()
        if answer2 == 'y':
            main_play()
        if answer2 == 'n':
            break


def check(x, y, operator):
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg += msg_6
    if (x == 1 or y == 1) and operator == "*":
        msg += msg_7
    if (x == 0 or y == 0) and (operator == "*" or operator == "+" or operator == "-"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def is_one_digit(v):
    if -10 < v < 10 and v == int(v):
        return True
    else:
        return False


main_play()
calc_play()
