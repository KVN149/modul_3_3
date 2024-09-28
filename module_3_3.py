def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params()
print_params(b=25)
print_params(c = [1,2,3])

variety_list = ['String', 10, (5,15)]
values_dict  = {'a':2,'b':'символ','c':False}
print_params(*variety_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)