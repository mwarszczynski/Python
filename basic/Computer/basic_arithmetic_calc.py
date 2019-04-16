class Basic_arithmetic_calc:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    global add_values, sub_values, mul_values, div_values
    global num1, num2

    def operations(self):
        num1 = int(input('Enter number: '))
        num2 = int(input('Enter number: '))

        print('Available operations:')
        print('1. Add')
        print('2. Sub')
        print('3. Mul')
        print('4. Div')

        detail_choice = int(input('Which operation?: '))
        if detail_choice == 1:
             add_values(self, num1, num2)
        elif detail_choice == 2:
            sub_values(self, num1, num2)
        elif detail_choice == 3:
            mul_values(self, num1, num2)
        elif detail_choice == 4:
            div_values(self, num1, num2)
        else:
            print('Nothing has been selected')

    def add_values(self, x, y):
        result = x + y
        print(f'{x} + {y} = {result}')
        # return result

    def sub_values(self, x, y):
        result = x - y
        print(f'{x} - {y} = {result}')
        # return result

    def mul_values(self, x, y):
        result = x * y
        print(f'{x} * {y} = {result}')
        # return result

    def div_values(self, x, y):
        result = x / y
        print(f'{x} / {y} = {result}')
        # return result