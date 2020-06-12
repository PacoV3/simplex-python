from copy import deepcopy

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

class Tablero:
    def __init__(self, mode, base_row, base_col, table, solution, last_row, z_function):
        # True = Max, False = Min
        self.mode = mode
        self.base_row = base_row
        self.base_col = base_col
        self.table = table
        self.solution = solution
        self.last_row = last_row
        #  True = Max, False = Min
        # [ True or False, [z_coefficients, ...] ]
        self.z_function = z_function

    def found_x(self):
        # Copia de la ultima fila
        copy_of_last_row = deepcopy(self.last_row[:])
        # Si es Max
        if self.mode:
            # Busca el menor en el último renglón
            x = copy_of_last_row.index(min(copy_of_last_row[:-1]))
        # Si es Min
        else:
            # Busca el mayor en el último renglón
            x = copy_of_last_row.index(max(copy_of_last_row[:-1]))
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

    def last_row_has_negatives(self):
        # Por cada valor en last_row, antes de la solución
        for val in self.last_row[:-1]:
            # Si last_row es negativo regresa cierto
            if truncate(val, 4) < 0:
                return True
        # Regresa falso
        return False

    def last_row_has_positives(self):
        # Por cada valor en last_row, antes de la solución
        for val in self.last_row[:-1]:
            # Si last_row es positivo regresa cierto
            if truncate(val, 4) > 0:
                return True
        # Regresa falso
        return False

    def change_base(self, x, y):
        # Mover el nombre de columna en x a fila en y
        self.base_row[y] = self.base_col[x]

    def base_row_has_r(self):
        for base in self.base_row:
            if "r" in base:
                return True
        return False

    def is_basic_solution(self):
        index_in_base_col = []
        for base in self.base_row:
            index_in_base_col.append(self.base_col.index(base))
        for index in index_in_base_col:
            if self.last_row[index] != 0:
                return False
        return True

    def make_basic_solution(self):
        index_of_row_col = []
        index_of_negatives = [] 
        for index, base in enumerate(self.base_row):
            index_of_row_col.append((index, self.base_col.index(base)))
        x_list = [x_index[1] for x_index in index_of_row_col]
        for index, num in enumerate(self.last_row):
            if index in x_list and num < 0:
                index_of_negatives.append([y_x for y_x in index_of_row_col if y_x[1] == index][0])
        copy_of_last_row = deepcopy(self.last_row)
        for y_x_index in index_of_negatives:
            for index in range(len(self.last_row) - 1):
                self.last_row[index] += self.table[y_x_index[0]][index] *- copy_of_last_row[y_x_index[1]]
            self.last_row[-1] += self.solution[y_x_index[0]] *- copy_of_last_row[y_x_index[1]]

    def create_z_function(self):
        self.last_row = []
        last_row_len = len(self.base_col) + 1
        self.mode = self.z_function[0]
        for coefficient in self.z_function[1]:
            self.last_row.append(-coefficient)
        for i in range(last_row_len - len(self.last_row)):
            self.last_row.append(0)

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
        # Cambiar la fila last_row
        copy_of_last_row = deepcopy(self.last_row)
        if copy_of_last_row[x] != 0:
            for x_index in range(len(copy_of_last_row) - 1):
                self.last_row[x_index] = self.table[y][x_index] *- copy_of_last_row[x] + copy_of_last_row[x_index]
            self.last_row[-1] = self.solution[y] *- copy_of_last_row[x] + copy_of_last_row[-1]

    def final_result(self):
        result = []
        for index in range(len(self.base_row)):
            result.append('{}: {:,.2f}'.format(self.base_row[index], self.solution[index]))
        result.sort()
        result.append('{}: {:,.2f}'.format('Z', self.last_row[-1]))
        return result
        
    def solve_simplex(self):
        if self.mode:
            while self.last_row_has_negatives():
                current_pivot = self.found_pivot()
                self.change_base(*current_pivot)
                self.change_table_and_solution(*current_pivot)
        else:
            while self.last_row_has_positives():
                current_pivot = self.found_pivot()
                self.change_base(*current_pivot)
                self.change_table_and_solution(*current_pivot)

    def remove_r(self):
        temporal_table = []
        temporal_row = []
        temporal_solution = []
        y_index_of_r = []
        x_index_of_r = []
        for index, base in enumerate(self.base_row):
            if "r" in base:
                y_index_of_r.append(index)
        self.base_row = [row for row in self.base_row if "r" not in row]
        for index, base in enumerate(self.base_col):
            if "r" in base:
                x_index_of_r.append(index)
        self.base_col = [col for col in self.base_col if "r" not in col]
        for y, row in enumerate(self.table):
            if y not in y_index_of_r:
                for x, col_val in enumerate(row):
                    if x not in x_index_of_r:
                        temporal_row.append(col_val)
                temporal_table.append(temporal_row)
                temporal_row = []
        for y in range(len(self.solution)):
            if y not in y_index_of_r:
                temporal_solution.append(self.solution[y])
        self.table = temporal_table
        self.solution = temporal_solution

    def solve_table(self):
        if self.base_row_has_r():
            # Cambiar a Min
            self.mode = False
            if self.is_basic_solution() is not True:
                self.make_basic_solution()
            while self.last_row_has_positives():
                current_pivot = self.found_pivot()
                self.change_base(*current_pivot)
                self.change_table_and_solution(*current_pivot)
            self.remove_r()
        self.create_z_function()
        if self.is_basic_solution():
            self.solve_simplex()
        else:
            self.make_basic_solution()
            self.solve_simplex()
        result = self.final_result()
        return result
