from tablero import Table

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

# base_row_vals = ["s1", "s2", "s3"]
# base_col_vals = ["X1", "X2", "s1", "s2", "s3"]
#                           CORECTO
# z_function_vals = [True, [500, 300]]
# table_vals = [[15, 5, 1, 0, 0], [10, 6, 0, 1, 0], [8, 12, 0, 0, 1]]
# solution_vals = [300, 240, 450]
# last_row_vals = [-500, -300, 0, 0, 0, 0]
# OUTPUT = ['x1: 15.00', 'x2: 15.00', 's3: 150.00', 'Z: 12,000.00']

#                           CORECTO
# z_function_vals = [True, [1, 2]]
# table_vals = [[1, 3, 1, 0, 0], [2, 2, 0, 1, 0], [0, 1, 0, 0, 1]]
# solution_vals = [200, 300, 60]
# last_row_vals = [-1, -2, 0, 0, 0, 0]
# OUTPUT = ['X1: 125.00', 'X2: 25.00', 's3: 35.00', 'Z: 175.00']

#                   Prueba Simplex 2 Fases
#                           CORECTO
# base_row_vals = ["r1", "r2", "r3"]
# base_col_vals = ["X1", "X2", "e1", "e2", "e3", "r1", "r2", "r3"] 
# z_function_vals = [False, [2000, 2000]]
# table_vals = [[1, 2, -1, 0, 0, 1, 0, 0], [3, 2, 0, -1, 0, 0, 1, 0], [5, 2, 0, 0, -1, 0, 0, 1]]
# solution_vals = [80, 160, 200]
# last_row_vals = [0, 0, 0, 0, 0, -1, -1, -1, 0]
# OUTPUT ESPERADO = x1 = 40, x2 = 20, e3 = 40, z = 120000
# OUTPUT = ['X1: 40.00', 'X2: 20.00', 'e3: 40.00', 'Z: 120,000.00']

#                   Prueba Simplex 2 Fases
base_row_vals = ["r1", "r2"]
base_col_vals = ["X1", "X2", "e1", "e2", "r1", "r2"] 
z_function_vals = [False, [30, 40]]
table_vals =    [[20, 30, -1, 0, 1, 0], 
                 [40, 30, 0, -1, 0, 1]]
solution_vals = [3000, 4000]
last_row_vals = [0, 0, 0, 0, -1, -1, 0]
# OUTPUT ESPERADO = x1 = 50, x2 = 66.667, z = 4166.667
# OUTPUT = ['X1: 50.00', 'X2: 66.67', 'Z: 4,166.67']

#                Prueba Simplex Problemario H1
# base_row_vals = ["r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "s1", "s2", "s3"]
# base_col_vals = ["X1", "X2", "X3", "X4", "X5", "X6", "X7", "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "s1", "s2", "s3"] 
# z_function_vals = [False, [50, 50, 16, 16, 16, 16, 16]]
# table_vals =    [[1, 1, 1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                  [1, 1, 1, 1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                  [0, 1, 1, 1, 1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
#                  [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
#                  [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
#                  [1, 1, 0, 0, 1, 1, 1, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
#                  [1, 1, 0, 0, 0, 1, 1, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
#                  [1, 1, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
#                  [0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
#                  [1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#                  [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
# solution_vals = [10, 12, 14, 16, 18, 17, 15, 10, 56, 0, 12]
# last_row_vals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0]
# OUTPUT ESPERADO = x1 = 50, x2 = 66.667, z = 4166.667
# OUTPUT = ['X1: 50.00', 'X2: 66.67', 'Z: 4,166.67']

t = Table(base_row_vals, base_col_vals, table_vals, solution_vals, last_row_vals, z_function_vals)
result = t.solve_table()
print(result)
