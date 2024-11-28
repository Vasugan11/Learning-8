def add_everything_up(a, b):
    try:
       rezult = a + b
    except TypeError as exc:
        print(a,b, exc)
    else:
        print(rezult)
add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)