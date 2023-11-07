# import csv  
# def main():  
#     # To Open the CSV file  
#     with open(' python.csv ', newline = '') as csv_file:  
#         csv_read = csv.reader( csv_file, delimiter = ',')  
  
#         # To Read and display each row  
#         for row in csv_read:  
#             print(row)  
# if __name__ == '__main__':  
#     main()  

# ####    

# import csv  
# with open('python.csv', mode='r') as csv_file:  
#     csv_reader = csv.DictReader(csv_file)  
#     line_count = 0  
  
#     for row in csv_reader:  
#         if line_count == 0:  
#             print( f'The column names are as follows : {", ".join(row)}' )  
#             line_count += 1  
  
#         print(  f'\t{row[ " Name " ]} lives in {row[" City "]} department and is {row[" Age "]} years old. ')  
#         line_count += 1  
  
#     print(f'Processed {line_count} lines.')    
    