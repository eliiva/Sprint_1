test_num = 1231231

def digit_root(num):
    if num < 10:
        return num

    result = 0
    num_to_string = str(num)
    for i in range(0, len(num_to_string)):
        result += int(num_to_string[i])
        if result > 9:
            result = digit_root(result)

    return result

print(digit_root(test_num))