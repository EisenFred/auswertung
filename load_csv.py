import csv
# Returns two-dimensional array of the given csv file.
def load_csv(filename):
    array = []
    try:
        with open(filename, 'r') as csvFile:
            csv_reader = csv.reader(csvFile)
            for row in csv_reader:
                array.append(row)
    except FileNotFoundError as e:
        print("\033[93m⫷WARNING⫸\033[0m Leeres Array wurde erstellt. <FileNotFoundError> \033[93m⫷WARNING⫸\033[0m")
    except PermissionError as e:
        print("\033[93m⫷WARNING⫸\033[0m Leeres Array wurde erstellt. <PermissionError> \033[93m⫷WARNING⫸\033[0m")
    except UnicodeDecodeError as e:
        print("\033[93m⫷WARNING⫸\033[0m Leeres DataFrame wurde erstellt. <UnicodeDecodeError> \033[93m⫷WARNING⫸\033[0m")
    except csv.Error as e:
        print("\033[93m⫷WARNING⫸\033[0m Leeres DataFrame wurde erstellt. <csv.Error> \033[93m⫷WARNING⫸\033[0m")
    return array