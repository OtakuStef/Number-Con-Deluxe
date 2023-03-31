def convert_one_digit(number):
    if number == 0:
        return 'zero'
    single_digits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return single_digits[number]

def convert_two_digits(number):
    two_digits = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if number < 10:
        return convert_one_digit(number)
    elif number < 20:
        special_two_digits = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
        return special_two_digits[number-10]
    else:
        first_digit = number // 10
        second_digit = number % 10
        if second_digit == 0:
            return two_digits[first_digit]
        else:
            return two_digits[first_digit] + ' ' + convert_one_digit(second_digit)

def convert_three_digits(number):
    if number < 100:
        return convert_two_digits(number)
    first_digit = number // 100
    remaining_two_digits = number % 100
    if remaining_two_digits == 0:
        return convert_one_digit(first_digit) + ' hundred'
    else:
        return convert_one_digit(first_digit) + ' hundred and ' + convert_two_digits(remaining_two_digits)

def convert_number_to_words(number):
    if number == 0:
        return 'zero'
    if number < 1000:
        return convert_three_digits(number)
    if number < 1000000:
        first_three_digits = number // 1000
        remaining_digits = number % 1000
        if remaining_digits == 0:
            return convert_three_digits(first_three_digits) + ' thousand'
        else:
            return convert_three_digits(first_three_digits) + ' thousand ' + convert_three_digits(remaining_digits)
    if number < 1000000000:
        first_three_digits = number // 1000000
        remaining_digits = number % 1000000
        if remaining_digits == 0:
            return convert_three_digits(first_three_digits) + ' million'
        else:
            return convert_three_digits(first_three_digits) + ' million ' + convert_number_to_words(remaining_digits)
    raise ValueError('Number out of range: {}'.format(number))