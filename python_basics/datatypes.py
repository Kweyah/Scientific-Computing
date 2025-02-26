# Creating variables of different data types
integer_var = 10
float_var = 10.5
complex_var = 3 + 4j
list_var = [1, 2, 3, 4]
tuple_var = (5, 6, 7, 8)
dict_var = {'name': 'Alice', 'age': 25}
set_var = {1, 2, 3, 4}
bool_var = True

# Printing the type of each variable
print("Type of integer_var:", type(integer_var))
print("Type of float_var:", type(float_var))
print("Type of complex_var:", type(complex_var))
print("Type of list_var:", type(list_var))
print("Type of tuple_var:", type(tuple_var))
print("Type of dict_var:", type(dict_var))
print("Type of set_var:", type(set_var))
print("Type of bool_var:", type(bool_var))

# Converting integer to float and vice versa
int_to_float = float(integer_var)
float_to_int = int(float_var)

# Printing conversion results
print("Integer to Float:", int_to_float, "Type:", type(int_to_float))
print("Float to Integer:", float_to_int, "Type:", type(float_to_int))
