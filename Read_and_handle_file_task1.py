try:
    file_handler=open('sample1.txt','rt')
    line_1=file_handler.readline()
    line_2=file_handler.readline()
    print("Reding file content")
    print(f'line 1 :{line_1}')
    print(f'line 2 : {line_2}')

except FileNotFoundError as file_error:
    print(file_error)

