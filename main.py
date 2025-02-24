class Display():
    def __init__(self):
        self.number = None
        self.field = Digit('','','','','')

    def validate_number(self, number: int):
        try:
            number = int(number)
        except:
            print("Доступні для відображення лише додатні цілі числа!")
            self.validate_number(input("Введіть ціле число: "))
            return
        if number < 0:
            print("Доступні для відображення лише додатні цілі числа!")
            self.validate_number(input("Введіть ціле число: "))
            return
        else: self._set_number(number)

    def _set_number(self, number):
        self.number = number

    def _distinct_digit(self, digit:str):
        match digit:
            case '0':
                return Zero()
            case '1':
                return One()
            case '2':
                return Two()
            case '3':
                return Three()
            case '4':
                return Four()
            case '5':
                return Five()
            case '6':
                return Six()
            case '7':
                return Seven()
            case '8':
                return Eight()
            case '9':
                return Nine()

    def _create_field(self):
        digits_list = list(str(self.number))
        for i in digits_list:
            self.field += self._distinct_digit(i)
    def show_number_on_display(self):
        self._create_field()
        for i in self.field.convert_to_list():
            print(i)
class Digit():
    def __init__(self,first_row,second_row,third_row,fourth_row,fives_row):
        self.first_row = first_row
        self.second_row = second_row
        self.third_row = third_row
        self.fourth_row = fourth_row
        self.fives_row = fives_row
    def __add__(self, other):
        return Digit(self.first_row + " " + other.first_row,
                self.second_row + " " + other.second_row,
                self.third_row + " " + other.third_row,
                self.fourth_row + " " + other.fourth_row,
                self.fives_row + " " + other.fives_row)

    def convert_to_list(self):
        return(self.first_row,
               self.second_row,
               self.third_row,
               self.fourth_row,
               self.fives_row)

class Zero(Digit):
    def __init__(self):
        self.first_row = "###"
        self.second_row = "# #"
        self.third_row = "# #"
        self.fourth_row = "# #"
        self.fives_row = "###"
class One(Digit):
    def __init__(self):
        self.first_row = "  #"
        self.second_row = "  #"
        self.third_row = "  #"
        self.fourth_row = "  #"
        self.fives_row = "  #"

class Two(Digit):
    def __init__(self):
        self.first_row = "###"
        self.second_row = "  #"
        self.third_row = "###"
        self.fourth_row = "#  "
        self.fives_row = "###"

class Three(Digit):
    def __init__(self):
        self.first_row = "###"
        self.second_row = "  #"
        self.third_row = "###"
        self.fourth_row = "  #"
        self.fives_row = "###"

class Four(Digit):
    def __init__(self):
        self.first_row = "# #"
        self.second_row = "# #"
        self.third_row = "###"
        self.fourth_row = "  #"
        self.fives_row = "  #"

class Five(Digit):
    def __init__(self):
        self.first_row = "###"
        self.second_row = "#  "
        self.third_row = "###"
        self.fourth_row = "  #"
        self.fives_row = "###"

class Six(Digit):
    def __init__(self):
        self.first_row = "###"
        self.second_row = "#  "
        self.third_row = "###"
        self.fourth_row = "# #"
        self.fives_row = "###"

class Seven(Digit):
    def __init__(self):
        self.first_row = "###"
        self.second_row = "  #"
        self.third_row = "  #"
        self.fourth_row = "  #"
        self.fives_row = "  #"

class Eight(Digit):
    def __init__(self):
        self.first_row = "###"
        self.second_row = "# #"
        self.third_row = "###"
        self.fourth_row = "# #"
        self.fives_row = "###"

class Nine(Digit):
    def __init__(self):
        self.first_row = "###"
        self.second_row = "# #"
        self.third_row = "###"
        self.fourth_row = "  #"
        self.fives_row = "###"

display = Display()
display.validate_number(input("Введіть ціле число: "))
display.show_number_on_display()
