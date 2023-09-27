# TODO a new function goes up here!



# def main():
#     print('Cosplay time! Enter measurements for costume.')

#     print('Enter the bust or chest measurement:')

#     value = input('? ')
#     while not value.isnumeric():
#         print('Please enter an integer number.')
#         value = input('? ')
#     integer_value = int(value)

#     bust = integer_value


#     print('Enter the waist measurement:')

#     value = input('? ')
#     while not value.isnumeric():
#         print('Please enter an integer number.')
#         value = input('? ')
#     integer_value = int(value)

#     waist = integer_value


#     print('Enter the hip measurement:')

#     value = input('? ')
#     while not value.isnumeric():
#         print('Please enter an integer number.')
#         value = input('? ')
#     integer_value = int(value)

#     hips = integer_value


#     print('Enter the height (hollow to hem) measurement:')

#     value = input('? ')
#     while not value.isnumeric():
#         print('Please enter an integer number.')
#         value = input('? ')
#     integer_value = int(value)

#     height = integer_value


#     print('----------------')
#     print('Great job! Your measurements are:')
#     print('Bust:', bust)
#     print('Waist:', waist)
#     print('Hips:', hips)
#     print('Height:', height)
#     print('Have fun cosplaying!')


# main()

def get_measurement():
    value = input('? ')
    while not value.isnumeric():
        print('Please enter an integer number.')
        value = input('? ')
    integer_value = int(value)
    return integer_value

def main():
    print('Cosplay time! Enter measurements for costume.')

    print('Enter the bust or chest measurement:')

    integer_value = get_measurement()

    bust = integer_value


    print('Enter the waist measurement:')

    integer_value=get_measurement()

    waist = integer_value


    print('Enter the hip measurement:')

    integer_value=get_measurement()

    hips = integer_value


    print('Enter the height (hollow to hem) measurement:')

    integer_value=get_measurement()

    height = integer_value


    print('----------------')
    print('Great job! Your measurements are:')
    print('Bust:', bust)
    print('Waist:', waist)
    print('Hips:', hips)
    print('Height:', height)
    print('Have fun cosplaying!')


main()
