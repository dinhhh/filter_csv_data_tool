import pandas as pd
from os import listdir
from os.path import isfile, join
from code_to_list import convert_to_list

data_path = "./data"

_filter = convert_to_list("./code.csv")
print("Filter: ", _filter)
query_template = 'Material == "{part_num}" | '
filter_query = "".join([query_template.format(part_num=pn) for pn in _filter])[:-3]
print(filter_query)

data_files = [f for f in listdir(data_path) if isfile(join(data_path, f))]
print(data_files)

filtered_row_count = 0
for file in data_files:
    print("File ", file)
    df = pd.read_csv(data_path + "/" + file)
    print("Raw data frame Shape ", df.shape)
    filterd_data_frame = df.query(filter_query)
    print("Filtered data frame Shape ", filterd_data_frame.shape)
    filtered_row_count += filterd_data_frame.shape[0]
    filterd_data_frame.to_csv("./{file}-result.csv".format(file=file[:-4]), mode="a", index=False, header=False)

print("Total result row ", filtered_row_count)
