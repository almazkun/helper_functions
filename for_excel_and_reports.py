import pandas as pd


def str_to_float(str_or_int):
    """Make Float, if not, return error"""
    try:
        return float(str_or_int)
    except:
        return "Not a number"


def values_from_two_columns(file_name, column_one, column_two):
    """From excel file yields pair of cells from two columns from the same row"""
    df = pd.read_excel(file_name, encoding="utf-8")
    i = 0
    for a in df[column_one]:
        pair = [df[column_one][i],df[column_two][i]]
        i += 1
        yield pair
    

def sum_of_column_if(file_name, column_to_sum, criteria_column, criteria):
    """From excel file returns sum of column with criteria form different column"""
    value_crteria_list = []
    sum_list = []
    
    for a in values_from_two_columns(file_name, column_to_sum, criteria_column):
        value_crteria_list.append(a)
    
    for a in value_crteria_list:
        if a[1] == criteria:
            sum_list.append(str_to_float(a[0]))

    return sum(sum_list)

    
def sum_of_column(file_name, column_to_sum):
    """open excel file and return sum of the column"""
    df = pd.read_excel(file_name, encoding="utf-8")
    list_of_numbers_to_sum = []
    
    for item in df[column_to_sum]:
        list_of_numbers_to_sum.append(str_to_float(item))
    
    return sum(list_of_numbers_to_sum)


# Tests
d = {"column_to_sum": [10,10,"10","10","10","10",10], "criteria_column": ["No","No","Yes","No","No","No","Yes"]}
df1 = pd.DataFrame(data=d)
df1.to_excel("output.xlsx") 

assert str_to_float("1.0") == 1.0
assert str_to_float("0") == 0.0
assert str_to_float(1) == 1.0
assert str_to_float(1.0) == 1.0
assert str_to_float("1.0asd") == "Not a number"
assert str_to_float(["1.0asd"]) == "Not a number"
assert str_to_float("") == "Not a number"

assert sum_of_column("output.xlsx", "column_to_sum") == 70.0

assert sum_of_column_if("output.xlsx", "column_to_sum", "criteria_column", "Yes") == 20.0
