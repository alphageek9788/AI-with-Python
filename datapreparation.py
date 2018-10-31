from csv import reader

# URL https://machinelearningmastery.com/load-machine-learning-data-scratch-python/
#load a CSV file - METHOD ONE

# def load_csv(filename):
#     file = open(filename, "r")
#     lines = reader(file)
#     dataset = list(lines)
#     return dataset

#load a CSV file - METHOD TWO

def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
        return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())




# Load dataset
filename = 'gpa.csv'
dataset = load_csv(filename)
print("Loaded data file {0} with {1} rows and {2} columns".format(filename, len(dataset), len(dataset[0])))
print(dataset[0])

# convert string columns to float
for i in range(len(dataset[0])):
	str_column_to_float(dataset, i)
print(dataset[0])

