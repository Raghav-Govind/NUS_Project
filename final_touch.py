import pandas as pd

# Define the file paths
excel_file_path = r'D:\E(prev)\Acads(Official)\NUS Summer\Project_S\modified_MLA_list.xlsx'
csv_file_path = r'D:\E(prev)\Acads(Official)\NUS Summer\Project_S\All_States_AE.csv'
output_file_path = r'D:\E(prev)\Acads(Official)\NUS Summer\Project_S\merged.csv'

# Load the data
modified_mla_list = pd.read_excel(excel_file_path)
all_states_ae = pd.read_csv(csv_file_path)

# Ensure the 'Candidate' columns are in the same case for comparison
modified_mla_list['Candidate'] = modified_mla_list['Candidate'].str.lower()
all_states_ae['Candidate'] = all_states_ae['Candidate'].str.lower()

# Merge the dataframes
merged_df = pd.merge(modified_mla_list, 
                     all_states_ae[['Year', 'Age', 'Constituency', 'Candidate', 'Votes']], 
                     on=['Year', 'Age', 'Constituency', 'Candidate'], 
                     how='left')

# Save the merged data to a new CSV file
print(merged_df)
