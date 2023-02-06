from pythonds3.basic import Stack

def divide_by_2(decimal_num):
    remainder_stack = Stack()

    while decimal_num > 0:
        remainder = decimal_num % 2
        remainder_stack.push(remainder)
        decimal_num = decimal_num // 2
    
    binary_string = ""
    while not remainder_stack.is_empty():
        binary_string = binary_string + str(remainder_stack.pop())

    return binary_string

print(divide_by_2(42))
print(divide_by_2(31))