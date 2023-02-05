import pandas as pd

def convert_to_list(csv_code_file_path):
    csv_code_file_path = "./code.csv"

    df = pd.read_csv(csv_code_file_path)

    print(df.to_numpy())

    np_array = df.to_numpy()

    result = []
    for e in np_array:
        for i in e:
            result.append(i)

    print(result)
    return result