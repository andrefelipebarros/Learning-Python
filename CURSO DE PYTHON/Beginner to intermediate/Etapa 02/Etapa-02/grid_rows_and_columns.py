import os

os.system("CLS or CLEAR")

columns_MAX = 5
rows_MAX = 5
###
rows = 1

while rows <= rows_MAX:
    #criar variável coluna dentro do while
    columns = 1
    while columns <= columns_MAX:
        print(f'{rows=} {columns=}')
        columns += 1
    rows += 1

print("cabo.")
