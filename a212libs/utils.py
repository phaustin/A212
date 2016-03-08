import pandas as pd

def read_data(the_string):
    """
    turn a string into a dataframe,
    assuming the first row contains the
    column headers

    input: multiline string with data
    output: pandas dataframe
    """
    the_string=the_string.strip()
    all_lines=the_string.split('\n')
    column_names=all_lines[0].split()
    row_list=[]
    for line in all_lines[1:]:
        values=line.split()
        numbers = [float(item) for item in values]
        row_list.append(numbers)
    df_data=pd.DataFrame.from_records(row_list,columns=column_names)
    return df_data
