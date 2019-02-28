import csv


# Returns the value of a given result column (res_col)
# corresponding to the lowest spread between 2 other columns (col1 and col2)
def minimum_spread(filename, col1, col2, res_col):
    min_spread = 9223372036854775807
    min_result = ""
    with open(filename) as file:
        data = csv.reader(file, delimiter="\n")
        for line in data:
            try:
                line[0] = line[0].split()
                spread = abs(int(''.join(char for char in line[0][col1] if char.isdigit())) - int(''.join(char for char in line[0][col2] if char.isdigit())))
                # print(line[0][res_col] + " " + line[0][col1] + " " + line[0][col2] + " " + str(spread))
                if spread < min_spread:
                    min_spread = spread
                    min_result = line[0][res_col]
            except:
                continue
        return min_result


print(minimum_spread('w_data (5).dat', 2, 1, 0))
print(minimum_spread('soccer.dat', 6, 8, 1))
