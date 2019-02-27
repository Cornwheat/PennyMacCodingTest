import csv


def minimum_spread(filename, min_col, max_col, res_col, data_start_line = 0):
    min_spread = 9223372036854775807
    min_result = ""
    with open(filename) as file:
        data = csv.reader(file, delimiter="\n")
        for i in range(1, data_start_line):
            next(data)
        for line in data:
            try:
                line[0] = line[0].split()
                spread = int(''.join(char for char in line[0][max_col] if char.isdigit())) - int(''.join(char for char in line[0][min_col] if char.isdigit()))
                print(line[0][0] + " " + line[0][1] + " " + line[0][2] + " " + str(spread))
                if spread < min_spread:
                    min_spread = spread
                    min_result = line[0][res_col]
            except:
                continue
        return min_result


print(minimum_spread('w_data (5).dat', 2, 1, 0, 5))
