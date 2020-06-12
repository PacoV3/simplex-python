from tablero import Tablero

def crear_tabla(cant_variables, cant_restricciones, lista_base):
    tabla_final = []
    for renglon in range(cant_restricciones + 1):
        renglon_temp = []
        if renglon != cant_restricciones:
            print("Llenar restriccion ", renglon + 1)
            for variable in range(cant_variables):
                renglon_temp.append(int(input("X" + str(variable + 1) + ": ")))
            for s in range(cant_restricciones):
                renglon_temp.append(int(s == renglon))
        else:
            print("Llenar Z")
            for variable in range(cant_variables):
                renglon_temp.append(int(input("X" + str(variable + 1) + ": ")))
            for s in range(cant_restricciones):
                renglon_temp.append(0)
        renglon_temp.append(int(input("Solución: ")))
        tabla_final.append(renglon_temp)
        tabla_final.append(lista_base)
    return tabla_final

z_function = True
base_row_vals = ["s1", "s2", "s3"]
base_col_vals = ["X1", "X2", "s1", "s2", "s3"]
#                           CORECTO
table_vals = [[15, 5, 1, 0, 0], [10, 6, 0, 1, 0], [8, 12, 0, 0, 1]]
solution_vals = [300, 240, 450]
z_vals = [-500, -300, 0, 0, 0, 0]
# OUTPUT = ['x1: 15.00', 'x2: 15.00', 's3: 150.00', 'Z: 12,000.00']

#                           CORECTO
# table_vals = [[1, 3, 1, 0, 0], [2, 2, 0, 1, 0], [0, 1, 0, 0, 1]]
# solution_vals = [200, 300, 60]
# z_vals = [-1, -2, 0, 0, 0, 0]
# OUTPUT = ['x1: 125.00', 's3: 35.00', 'x2: 25.00', 'Z: 175.00']

t = Tablero(z_function, base_row_vals, base_col_vals, table_vals, solution_vals, z_vals)
result = t.solve_table()
print(result)
