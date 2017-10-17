def name_error():  
    print oops

def type_error():
    name_error()
    a = '2'
    b = a + 2

def attribute_error():
    type_error()
    c = 3
    c.append(4)

def index_error():
    letters = ['a', 'b', 'c']
    numbers = [0, 1, 2, 3, 4]
    for number in numbers:
        print letters[number]


def middle_function():
    index_error()


def last_function():
    middle_function()

last_function()

# def syntax_error:
