from copy import deepcopy

class Tablero:
    def __init__(self, mode, base_row, base_col, table, solution, z):
        # True = Max
        # False = Min
        self.mode = mode
        self.base_row = base_row
        self.base_col = base_col
        self.table = table
        self.solution = solution
        self.z = z

    def found_x(self):
        # Copia de la ultima fila
        copy_of_z = deepcopy(self.z[:])
        # Si es Max
        if self.mode:
            # Busca el menor en el último renglón
            x = copy_of_z.index(min(copy_of_z[:-1]))
        # Si es Min
        else:
            # Busca el mayor en el último renglón
            x = copy_of_z.index(max(copy_of_z[:-1]))
        return x
    
    def found_y(self, x):
        solution_over_col_pivot = []
        col_pivot_vals = []
        # Por cada renglón en la tabla
        for row in self.table:
            # Añade el valor en x
            col_pivot_vals.append(row[x])
        # Por cada valor en solución, crea una lista solución / col_pivote
        for index in range(len(self.solution)):
            # Manda a -1 a los negativos en col_pivote
            if col_pivot_vals[index] < 0:
                solution_over_col_pivot.append(-1)
            # De otra forma agrega la solución / col_pivote
            else:
                if col_pivot_vals[index] == 0:
                    solution_over_col_pivot.append(-1)
                else:
                    solution_over_col_pivot.append(self.solution[index] / col_pivot_vals[index])
        # y = inf para poder evaluar bien el menor positivo
        y_val = float('inf')
        # Por cada valor en sol / col pivote
        for value in solution_over_col_pivot:
            if value >= 0:
                if value < y_val:
                    y_val = value
        y = solution_over_col_pivot.index(y_val)
        return y
    
    def found_pivot(self):
        # En el estado actual trae el pivote x,y
        x = self.found_x()
        y = self.found_y(x)
        return x,y

    def z_has_negatives(self):
        # Por cada valor en z, antes de la solución
        for z in self.z[:-1]:
            # Si z es negativo regresa cierto
            if z < 0:
                return True
        # Regresa falso
        return False

    def change_base(self, x, y):
        # Mover el nombre de columna en x a fila en y
        self.base_row[y] = self.base_col[x]

    def change_table_and_solution(self, x, y):
        # Crea una copia
        copy_of_table = deepcopy(self.table)
        copy_of_solution = deepcopy(self.solution)
        # Cambiar la fila pivote
        for index in range(len(self.table[y])):
            self.table[y][index] = copy_of_table[y][index] / copy_of_table[y][x]
        # Cambiar solución del pivote
        self.solution[y] = copy_of_solution[y] / copy_of_table[y][x]
        # Cambiar las demás filas
        for y_index, row in enumerate(self.table):
            if y_index != y:
                if copy_of_table[y_index][x] != 0:
                    for x_index in range(len(row)):
                        self.table[y_index][x_index] = self.table[y][x_index] *- copy_of_table[y_index][x] + copy_of_table[y_index][x_index]
        # Cambiar soluciones no pivote
        for y_index in range(len(self.solution)):
            if y_index != y:
                if copy_of_table[y_index][x] != 0:
                    self.solution[y_index] = self.solution[y] *- copy_of_table[y_index][x] + copy_of_solution[y_index]
        # Cambiar la fila z
        copy_of_z = deepcopy(self.z)
        if copy_of_z[x] != 0:
            for x_index in range(len(copy_of_z) - 1):
                self.z[x_index] = self.table[y][x_index] *- copy_of_z[x] + copy_of_z[x_index]
            self.z[-1] = self.solution[y] *- copy_of_z[x] + copy_of_z[-1]

    def final_result(self):
        result = []
        for index in range(len(self.base_row)):
            result.append('{}: {:,.2f}'.format(self.base_row[index], self.solution[index]))
        result.append('{}: {:,.2f}'.format('Z', self.z[-1]))
        return result
        
    def solve_table(self):
        while self.z_has_negatives():
            current_pivot = self.found_pivot()
            self.change_base(*current_pivot)
            self.change_table_and_solution(*current_pivot)
        result = self.final_result()
        return result
