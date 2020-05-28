import pandas as pd


def str_to_float(str_or_int):
    if isinstance(str_or_int, float):
        return str_or_int
    if isinstance(str_or_int, int):
        return float(str_or_int)
    if isinstance(str_or_int, str):
        try:
            return float(str_or_int)
        except:
            return "Not a number"

assert str_to_float("1.0") == 1.0
assert str_to_float(1) == 1.0
assert str_to_float(1.0)== 1.0
assert str_to_float("1.0asd") == "Not a number"

def sum_of_column(file_name, column_to_sum):
    """open excel file and return sum of the column"""
    df = pd.read_excel(file_name, encoding="utf-8")
    list_of_numbers_to_sum = []
    for item in df[column_to_sum]:
        list_of_numbers_to_sum.append(str_to_float(item))
    return sum(list_of_numbers_to_sum)

df1 = pd.DataFrame([10,10,10,10,10,10,10],columns=['column_to_sum'])
df1.to_excel("output.xlsx") 

assert sum_of_column("output.xlsx", "column_to_sum") == 70.0
