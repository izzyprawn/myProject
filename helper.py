import csv

def create_new_summary_report_file():
    with open('summary_report.txt', 'w') as file:
        pass

def open_csv(file_location):
    """
    opens csv file and returns headers and rows
    """
    with open(file_location, encoding='utf-8-sig') as file:
        csvreader = csv.reader(file)
        csvheader = next(csvreader)

        csvrows = []

        for row in csvreader:
            csvrows.append(row)

        return csvheader, csvrows 


def get_column_index_of_header(csvheader, header_to_find):
    """
    gets index of given header
    """
    for index, value in enumerate(csvheader):
        if value == header_to_find:
            return index

def write_output_text_to_summary_report(output_text):
    with open("summary_report.txt", "a") as file:
        file.write(output_text)
