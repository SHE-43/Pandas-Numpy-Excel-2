# Read an excel (.xlsx) file.
# To dict, to CSV, To JSON
# Bdays days remaining
# This is the one we are working on for a full GitHub package,
# We convert this to Tkinter, SQL database and entry, either use Java or C# to make full projec.
# May be you can make a venv version of investment bank project - a simple one with website
# With a personal desktop CRM and a way to schedule daily new investment, failures, profits and with end of day reports.
# The process works old school where calls are made or they go online to make an order.
# Make a fake Dunder Miflin website, CRM and what not.
# Attempt to use the Py app that generates an Excel file to open an excel file here and convert to DataFrame.

import pandas as pd, numpy as np
import sys, os

s = sys.path[0]
folder = 'Spreadsheets'
files = ['product_details.xlsx', 'Book1.xlsx', 'Book2.xlsx']

# The file we need to read.

def path_file(s, folder, files, n = 0) -> "s = this py file path; folder = foldername; files = list of files; n = which file?":
    file = files[n]
    L = [folder, file]
    for x in L:
        s = os.path.join(s, x)
    return s


all_in_dict = {'s' : s, 'folder' : folder, 'files' : files, 'n' : 0}
path_1 = path_file(**all_in_dict)

all_in_dict = {'s' : s, 'folder' : folder, 'files' : files, 'n' : 1}
path_2 = path_file(**all_in_dict)

all_in_dict = {'s' : s, 'folder' : folder, 'files' : files, 'n' : 2}
path_3 = path_file(**all_in_dict)

print(path_1) # 'product_details.xlsx'
print(path_2) # 'Book1.xlsx'
print(path_3) # 'Book2.xlsx'




print("\n\nUsing Book1.xlsx and convert to dataframe.\n")

reader_1_a = pd.read_excel(path_3, header = 0, sheet_name = 'Sheet1')

reader_1_a_header_1 = pd.read_excel(path_3, header = 1, sheet_name = 'Sheet1', usecols=[0,2,4], 
dtype={1:int,2:str,0:float}, # This how you can change dtype of each column
)

cols = [0,2,4]
c = lambda x: f"Col {str(x)}"
names = list(map(c, cols))

reader_1_a_header_1_col_names = pd.read_excel(path_3, header = 1, sheet_name = 'Sheet1', usecols=cols, 
names = names, 
dtype={1:int,2:str,0:float}) # This how you can change dtype of each column
#skiprows=[0,2])

reader_1_a_header_1_col_names_skiprows = pd.read_excel(path_3, header = 1, sheet_name = 'Sheet1', usecols=cols, 
names = names, 
dtype={1:int,2:str,0:float}, # This how you can change dtype of each column
skiprows=(0,1,2)) # When header is 1, then row number 1 is 



print(f"The dtype of reader_1_c column 1 is {reader_1_a_header_1.columns}")
print("\n\n")

print("\nBook 2 has header row 0 and no other specific attributes.")

print(reader_1_a)

print("\n")
print("\nBook 2 has header row 1 columns 0,2,4.")
print(reader_1_a_header_1)

print("\n")
print("\nBook 2 has header row 1 columns 0,2,4 named.")
print(reader_1_a_header_1_col_names)

print("\n")
print("\nBook 2 has header row 1 columns 0,2,4 and row 0,3 skipped.")
print(reader_1_a_header_1_col_names_skiprows)


print("\n\nNow to play with path_1 which is product_details.xlsx\n")

reader_2 = pd.read_excel(path_1, header=None, squeeze=1)
print(reader_2)

print("\n\n")

reader_2 = pd.read_excel(path_1, header=1, squeeze=0,)
print(reader_2)



# Play with Address and DOB.
# Any new values in the lists will update in the dataframe.
# Have inputs that can be either args or taken as inputs using tkinter.
# The tkinter window has a main window with 2 buttons - button 1 takes you to a window that let's you add values
#           The second window let's you search up the items you are looking for
#           The third window lets you view ALL records, sort them using either column ascending or descending.
# Later convert to investment bank with customers, transactions, companies, stats, percentages, predictions, maps of customer
#           addresses, company addresses, ALL IN LONDON, future prices, 
# Address is to be divided into a list and then into dictionary of first line, second line and city and postcode
# DOB is to be subtracted from today's date and then the days remaining from bday are to be figured out using methods.
#           A new excel sheet is to be made with the new values and columns - save to GitHub this new manipulation.
# THe previous file creates the spreadsheets and this one is to read it.
# Use the previous one to create random names, addresses, dobs, contact numbers, genders and adds them to a spreadsheet.
# What if the excel sheet has no headers - can we take values and assign our own columns to it? Make a portable system and add to GHub

print("\nReader 2 is the dataframe we will use.")

print("\nReader_2 columns\n")

reader_2_columns = reader_2.columns
reader_2_columns_list_ravel = reader_2_columns.ravel()
reader_2_columns_list_toList = reader_2_columns.tolist()

print(f"\nList of columns using ravel == {reader_2_columns_list_ravel}")
print(f"\n\nList of columns using tolist() == {reader_2_columns_list_toList}")

cols_final = reader_2_columns_list_toList
dtypes_needed = [int, str,str,str,str,str,str]

cols_dtype_dict = {col:dtype_ for col,dtype_ in zip(cols_final, dtypes_needed)}
print("\ncols_dtype_dict is below...")
print(cols_dtype_dict)

print("\nColumn dtype below applying 'astype' via dictionary!\n")

print(reader_2.dtypes)

print("\nand now after the astype method - btw... str becomes object.")

reader_2 = reader_2.astype(cols_dtype_dict)

print(reader_2.dtypes)

print("\nNow that dtypes are set, lets convert the dataframe to dictionary of key as column and value as list of rows.\n")

# Changing name of variable to make it simple

df = reader_2
df_dict_manual = dict()

for col in df.columns.to_list():
    print(df[col].to_list())
    df_dict_manual[col] = df[col].to_list()

print("\n\nDict made manually and now printing...\n")

print(df_dict_manual)

print("\n\nMake dict, json and csv using Pandas builtin methods...\n\n")

df_dict = df.to_dict()
df_json = df.to_json()
df_csv = df.to_csv()

print("\ndf_dict\n")
print(df_dict)
print("\ndf_json\n")
print(df_json)
print("\ndf_csv\n")
print(df_csv)

addresses_only = df_dict['Address']
dobs_only = df_dict['DOB']

print("\nAddresses only...\n")
print(addresses_only)


print("\nDOBs only...\n")
print(dobs_only)

from datetime import datetime, timedelta

# Convert addresses into lists of different aspects of an address.

address_list = [x for x in addresses_only.values()]
dob_list = [x for x in dobs_only.values()]

print("\n\naddress list\n")
print(address_list)
print("\n\ndobs list\n")
print(dob_list)


# DOBs first
# Make a list of timedeltas of time left between their birthday from today.
# If birthday has passed, write passed already, this many days ago.

date_format = '%Y-%m-%d' # typical format for this file
timeDeltas = dict()
current_date = datetime.today() # today's date
current_date = datetime.strftime(current_date, '%Y-%m-%d') # only need the year-month-day
current_date = datetime.strptime(current_date, date_format)

sample = dob_list[0] # one sample of a dob

# current year
year_current = datetime.strftime(current_date, '%Y')
print(year_current)

latest_bday = str(year_current) + sample[4:]
print(latest_bday)

dict_of_remaining_days = dict()
print("\n\nThis be foor loop \n\n")
for dob in dob_list:
    latest_bday = str(year_current) + dob[4:]
    latest_bday = datetime.strptime(latest_bday, date_format)
    current_date = datetime.today()
    current_date = datetime(current_date.year, current_date.month, current_date.day)
    # current_date = datetime(2020,1,1)
    days_left = current_date-latest_bday
    days_left = days_left.__str__().split(",")[0]
    print(days_left)
    dict_of_remaining_days[dob] = days_left

# Let's add a column to it then.

df['Days To Bday'] = list(dict_of_remaining_days.values())

print(df)

save_path = sys.path[0] + "/"+ "Spreadsheets"

def create_path(py_path, folder, excel_file):
    path = py_path + '\\' + folder + '\\' + excel_file
    return path

file_name = 'product_details.xlsx'

a = create_path(sys.path[0], 'Spreadsheets', file_name)
print(a)

df1 = pd.read_excel(a)

header = df1.columns.to_list()[0]
columns_ = df.columns.to_list()

print(header)
print(columns_)

columns = list(zip(header * len(columns_), columns_)      )

print(columns)
print("\n")
lists = df1.values

df2 = pd.DataFrame(lists)
print("\n\n")
print(df2)

# Add the older title back to it.
# Add style
# Make the file from another PY file using Numpy and then use this one to modify.
# Play with all three spreadsheets, but give them names as in outcome names
"""
columns = list("ABCD")
columns = list(zip(['HEADER'] * 4, columns))             
#[('HEADER', 'A'), ('HEADER', 'B'), ('HEADER', 'C'), ('HEADER', 'D')]
columns = pd.MultiIndex.from_tuples(columns, names=['first', 'second'])    
### >>> end

df = pd.DataFrame(np.random.randn(3,4),index=dates,columns=columns)

"""

# Now, get the original first row/header for the file you were using and add it to the dataframe and save it to new file
# Save the file.
# Create package of the 2 files, go over the to dos above
# Save the spreadsheets folder
# Save to GitHub as Pandas quick tutorial and some tricks.



# A list of all that is available to us for a dataframe.

"""

T', '_AXIS_LEN', '_AXIS_NAMES', '_AXIS_NUMBERS', '_AXIS_ORDERS', '_AXIS_REVERSED', '_AXIS_TO_AXIS_NUMBER', '__abs__', '__add__', 
'__and__', '__annotations__', '__array__', '__array_priority__', '__array_wrap__', '__bool__', '__class__', '__contains__', 
'__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__div__', '__doc__', '__eq__', '__finalize__', 
'__floordiv__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', 
'__iadd__', '__iand__', '__ifloordiv__', '__imod__', '__imul__', '__init__', '__init_subclass__', '__invert__', '__ior__', '__ipow__',
'__isub__', '__iter__', '__itruediv__', '__ixor__', '__le__', '__len__', '__lt__', '__matmul__', '__mod__', '__module__', '__mul__',
'__ne__', '__neg__', '__new__', '__nonzero__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__reduce__', 
'__reduce_ex__', '__repr__', '__rfloordiv__', '__rmatmul__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rsub__',
'__rtruediv__', '__rxor__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__sub__', '__subclasshook__',
'__truediv__', '__weakref__', '__xor__', '_accessors', '_add_numeric_operations', '_add_series_or_dataframe_operations',
'_agg_by_level', '_agg_examples_doc', '_agg_summary_and_see_also_doc', '_aggregate', '_aggregate_multiple_funcs', '_align_frame', 
'_align_series', '_box_col_values', '_builtin_table', '_can_fast_transpose', '_check_inplace_setting', 
'_check_is_chained_assignment_possible', '_check_label_or_level_ambiguity', '_check_setitem_copy', '_clear_item_cache', 
'_clip_with_one_bound', '_clip_with_scalar', '_combine_frame', '_consolidate', '_consolidate_inplace', '_construct_axes_dict',
'_construct_axes_from_arguments', '_construct_result', '_constructor', '_constructor_expanddim', '_constructor_sliced', 
'_convert', '_count_level', '_cython_table', '_data', '_deprecations', '_dir_additions', '_dir_deletions', '_drop_axis', 
'_drop_labels_or_levels', '_ensure_valid_index', '_find_valid_index', '_from_arrays', '_get_agg_axis', '_get_axis', 
'_get_axis_name', '_get_axis_number', '_get_axis_resolvers', '_get_block_manager_axis', '_get_bool_data', '_get_cacher',
'_get_cleaned_column_resolvers', '_get_column_array', '_get_cython_func', '_get_index_resolvers', '_get_item_cache', 
'_get_label_or_level_values', '_get_numeric_data', '_get_value', '_getitem_bool_array', '_getitem_multilevel', '_gotitem', 
'_indexed_same', '_info_axis', '_info_axis_name', '_info_axis_number', '_info_repr', '_init_mgr', '_internal_names', 
'_internal_names_set', '_is_builtin_func', '_is_cached', '_is_copy', '_is_homogeneous_type', '_is_label_or_level_reference',
'_is_label_reference', '_is_level_reference', '_is_mixed_type', '_is_view', '_iset_item', '_iter_column_arrays', '_ix',
'_ixs', '_join_compat', '_maybe_cache_changed', '_maybe_update_cacher', '_metadata', '_needs_reindex_multi', 
'_obj_with_exclusions', '_protect_consolidate', '_reduce', '_reindex_axes', '_reindex_columns', '_reindex_index', 
'_reindex_multi', '_reindex_with_indexers', '_replace_columnwise', '_repr_data_resource_', '_repr_fits_horizontal_', 
'_repr_fits_vertical_', '_repr_html_', '_repr_latex_', '_reset_cache', '_reset_cacher', '_sanitize_column', '_selected_obj', 
'_selection', '_selection_list', '_selection_name', '_series', '_set_as_cached', '_set_axis', '_set_axis_name', 
'_set_is_copy', '_set_item', '_set_value', '_setitem_array', '_setitem_frame', '_setitem_slice', '_slice', '_stat_axis', 
'_stat_axis_name', '_stat_axis_number', '_take_with_is_copy', '_to_dict_of_blocks', '_try_aggregate_string_function', 
'_typ', '_update_inplace', '_validate_dtype', '_values', '_where', 'abs', 'add', 'add_prefix', 'add_suffix', 'agg', 
'aggregate', 'align', 'all', 'any', 'append', 'apply', 'applymap', 'asfreq', 'asof', 'assign', 'astype', 'at', 'at_time',
'attrs', 'axes', 'backfill', 'between_time', 'bfill', 'bool', 'boxplot', 'clip', 'columns', 'combine', 'combine_first', 
'compare', 'convert_dtypes', 'copy', 'corr', 'corrwith', 'count', 'cov', 'cummax', 'cummin', 'cumprod', 'cumsum', 'describe',
'diff', 'div', 'divide', 'dot', 'drop', 'drop_duplicates', 'droplevel', 'dropna', 'dtypes', 'duplicated', 'empty', 'eq', 
'equals', 'eval', 'ewm', 'expanding', 'explode', 'ffill', 'fillna', 'filter', 'first', 'first_valid_index', 'floordiv', 
'from_dict', 'from_records', 'ge', 'get', 'groupby', 'gt', 'head', 'hist', 'iat', 'idxmax', 'idxmin', 'iloc', 'index', 
'infer_objects', 'info', 'insert', 'interpolate', 'isin', 'isna', 'isnull', 'items', 'iteritems', 'iterrows', 'itertuples', 
'join', 'keys', 'kurt', 'kurtosis', 'last', 'last_valid_index', 'le', 'loc', 'lookup', 'lt', 'mad', 'mask', 'max', 'mean',
'median', 'melt', 'memory_usage', 'merge', 'min', 'mod', 'mode', 'mul', 'multiply', 'ndim', 'ne', 'nlargest', 'notna', 
'notnull', 'nsmallest', 'nunique', 'pad', 'pct_change', 'pipe', 'pivot', 'pivot_table', 'plot', 'pop', 'pow', 'prod',
'product', 'quantile', 'query', 'radd', 'rank', 'rdiv', 'reindex', 'reindex_like', 'rename', 'rename_axis', 'reorder_levels', 
'reset_index', 'rfloordiv', 'rmod', 'rmul', 'rolling', 'round', 'rpow', 'rsub', 'rtruediv', 'sample', 'select_dtypes', 'sem', 
'set_axis', 'set_index', 'shape', 'shift', 'size', 'skew', 'slice_shift', 'sort_index', 'sort_values', 'squeeze', 'stack', 'std', 
'style', 'sub', 'subtract', 'sum', 'swapaxes', 'swaplevel', 'tail', 'take', 'replace', 'resample', 
'to_clipboard', 'to_csv', 'to_dict', 'to_excel', 'to_feather', 'to_gbq', 'to_hdf', 'to_html', 'to_json', 'to_latex', 
'to_markdown', 'to_numpy', 'to_parquet', 'to_period', 'to_pickle', 'to_records', 'to_sql', 'to_stata', 'to_string', 
'to_timestamp', 'to_xarray', 'transform', 'transpose', 'truediv', 'truncate', 'tz_convert', 'tz_localize', 'unstack', 
'update', 'value_counts', 'values', 'var', 'where', 'xs']


"""
