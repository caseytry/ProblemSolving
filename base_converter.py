from pythonds3.basic import Stack


def base_converter(decimal_num, base):
    digits = "0123456789ABCDEF"
    remainder_stack = Stack()

    while decimal_num > 0:
        remainder = decimal_num % base
        remainder_stack.push(remainder)
        decimal_num = decimal_num // base
    
    new_string = ""
    while not remainder_stack.is_empty():
        new_string = new_string + digits[remainder_stack.pop()]

    return new_string

#print(base_converter(25,2))
#print(base_converter(25, 16))
#print(base_converter(25,8))