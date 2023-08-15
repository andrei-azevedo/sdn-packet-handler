import csv

def write_to_file(filepath, row):
    with open(filepath, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', 
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(row)