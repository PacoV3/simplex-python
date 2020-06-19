import xlwings as xw
from tablero import Table

wb = xw.Book('test_python.xlsx')
# Primer Hoja en el documento
simplex_sheet = wb.sheets[0]
# O por nombre
simplex_sheet = wb.sheets['Simplex']
# Traer una lista de filas desde D8
values = simplex_sheet.range('D10').options(expand='table').value
z_values = simplex_sheet.range('C4').options(expand='table').value

# Crear solución
solution_vals = [solution.pop(-1) for solution in values]
# Crear bases en filas y columnas
relational_operators = [operator.pop(-1) for operator in values]
amount_of_variables = len(values[0])
base_col_vals = ["X" + str((index + 1)) for index in range(amount_of_variables)]
base_row_vals = []
count_of_r = 0
count_of_s = 0
for operator in relational_operators:
    if operator == '>=':
        count_of_r += 1
        base_col_vals.append('r' + str(count_of_r))
        base_row_vals.append('r' + str(count_of_r))
        base_col_vals.append('e' + str(count_of_r))
    elif operator == '<=' or operator == '=':
        count_of_s += 1
        base_col_vals.append('s' + str(count_of_s))
        base_row_vals.append('s' + str(count_of_s))

# Crear la ultima fila
last_row_vals= []
for base in base_col_vals:
    if 'r' in base:
        last_row_vals.append(-1)
    else:
        last_row_vals.append(0)
last_row_vals.append(0)
# Crear los valores de la funcion Z original
z_function_vals = [bool(z_values.pop(0)), z_values]
# Agregar los valores r y s a la tabla
table_vals = [row for row in values]
for index,operator in enumerate(relational_operators):
    for table_index in range(len(table_vals)):
        if index == table_index:
            if operator == '>=':
                table_vals[table_index].append(1)
                table_vals[table_index].append(-1)
                for extra_zeroes in range(len(table_vals)):
                    if extra_zeroes != table_index:
                        table_vals[extra_zeroes].append(0)
            elif operator == '<=':
                table_vals[table_index].append(1)
            elif operator == '=':
                table_vals[table_index].append(0)
        else:
            table_vals[table_index].append(0)

print(base_col_vals)
for row in table_vals:
    print(row)
print(last_row_vals)
print(solution_vals)
print()
# print(base_row_vals)
# print(z_function_vals)

t = Table(base_row_vals, base_col_vals, table_vals, solution_vals, last_row_vals, z_function_vals)
result = t.solve_table()
# print(result)
simplex_sheet.range('C6').value = result

print("Fila de Base: {}".format(t.base_col))
print("Columna de Base: {}".format(t.base_row))
print("Lista del tablero: {}".format(t.table))
print("Columna Solución: {}".format(t.solution))
print("Última fila + Solución en ella: {}".format(t.last_row))
print()
