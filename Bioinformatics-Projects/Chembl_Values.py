import requests
import pandas as pd
import argparse
import os, sys

parser = argparse.ArgumentParser(description="Retrieve chembl records")
parser.add_argument('--chemblid', dest='chembl_id_list', help='<Required> List of chembl IDs', nargs='+', default="CHEMBL26")
parser.add_argument('--outputpath', dest='output_path', help='Path for output file', default=os.getcwd())
parser.add_argument('--outputfile', dest='output_filename', help='Output file name', default='default')
parser.add_argument('--operation', dest='operation', help='Operations to perform: full, max, min', default=['max'],  nargs='*')
parser.add_argument('--removeNull', dest='remove_null', help='True/False to remove null values from the operated data', default=False)
parser.add_argument('--target', dest='target_column', help='Column name on which operation is performed', default='pchembl_value')
parser.add_argument('--columns', dest='column_filter', help='Specify desired column list in output. Use "all" to include all columns or "help" to list available columns.', default='default', nargs='*')
args = parser.parse_args()

# Function to get available columns
def get_available_columns():
    all = ['action_type','activity_comment','activity_id','activity_properties','assay_chembl_id',
            'assay_description','assay_type','assay_variant_accession','assay_variant_mutation',
            'bao_endpoint','bao_format','bao_label','canonical_smiles','data_validity_comment',
            'data_validity_description','document_chembl_id','document_journal','document_year',
            'ligand_efficiency','molecule_chembl_id','molecule_pref_name','parent_molecule_chembl_id',
            'pchembl_value','potential_duplicate','qudt_units','record_id','relation','src_id',
            'standard_flag','standard_relation','standard_text_value','standard_type','standard_units',
            'standard_upper_value','standard_value','target_chembl_id','target_organism','target_pref_name',
            'target_tax_id','text_value','toid','type','units','uo_units','upper_value','value']
    default = ['molecule_chembl_id','assay_chembl_id', 'pchembl_value','relation','standard_value','standard_units']
    return(all,default)

def making_directory(output_path):
    import os
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        message = "Created Successfully: "+output_path
    else:
        message = "Already exists: "+ output_path
    return(message)

def A_variables(args):
    if args.column_filter == ["help"]:
        print("Available columns:")
        all, default = get_available_columns()
        print(", ".join(all))
        print("Default columns:")
        print(", ".join(default))
        sys.exit()
    chembl_id_list = args.chembl_id_list
    output_path = args.output_path
    output_filename = args.output_filename
    operation = args.operation
    target_column = args.target_column
    remove_null = args.remove_null
    if args.column_filter == "default":
        columns = default
    elif args.column_filter == "all":
        columns = all
    else:
        columns = args.column_filter
    message = making_directory(output_path)
    print(message)
    return(chembl_id_list,output_path,output_filename,operation,columns,target_column,remove_null)

def B_chembl_code(chembl_id):
    # Define the base URL for the ChEMBL API
    base_url = f"https://www.ebi.ac.uk/chembl/api/data/activity.json"
    # Query the API for bioactivity data for the specified molecule
    response = requests.get(base_url, params={"molecule_chembl_id": chembl_id})
    # Check if the request was successful
    try:
        if response.status_code == 200:
            data = response.json()
        return(data)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(f"Failed to retrieve data for {chembl_id}: {response.status_code}")
        return(None)
    
def C_retrieve_code(chembl_id, data,operation,columns,target_column, remove_null, output_path, output_filename):
    activities = pd.DataFrame(data['activities'])
    activities = filter_NA(activities, target_column, remove_null)
    try:
        if "max" in operation:
            df_max = activities[columns][activities[target_column].astype("float") == max(activities[target_column].astype("float"))]
            max_filename = "{}_Max.csv".format(output_filename) if output_filename != "default" else "{}_Max.csv".format(chembl_id)
            mode = 'a' if os.path.exists("{}/{}".format(output_path,max_filename)) else 'w'
            df_max.to_csv("{}/{}".format(output_path,max_filename), mode = mode, index = False)
        else:
            df_max = pd.DataFrame()
        if "min" in operation:
            df_min = activities[columns][activities[target_column].astype("float") == min(activities[target_column].astype("float"))]
            min_filename = "{}_Min.csv".format(output_filename) if output_filename != "default" else "{}_Min.csv".format(chembl_id)
            mode = 'a' if os.path.exists("{}/{}".format(output_path,min_filename)) else 'w'
            df_min.to_csv("{}/{}".format(output_path,min_filename), mode = mode, index = False)
        else:
            df_min = pd.DataFrame()
        if "full" in operation:
            df_full = activities[columns]
            full_filename = "{}_Full.csv".format(output_filename) if output_filename != "default" else "{}_Full.csv".format(chembl_id)
            mode = 'a' if os.path.exists("{}/{}".format(output_path,full_filename)) else 'w'
            df_full.to_csv("{}/{}".format(output_path,full_filename), mode = mode, index = False)
        else:
            df_full = pd.DataFrame()
    except Exception as e:
        raise RuntimeError(f"Failed to retrieve data for {chembl_id}: {e}")
    return(df_max,df_min,df_full)

def filter_NA(df, target_column, remove_null):
    if remove_null==True:
        df_filtered = df[df[target_column].isna()==False]
    else:
        df_filtered = df
    return(df_filtered)

# Loop through the list of ChEMBL IDs and append results to the DataFrame
chembl_id_list,output_path,output_filename,operation,columns,target_column,remove_null = A_variables(args)
for chembl_id in chembl_id_list:
    try:
        data = B_chembl_code(chembl_id)
        df_max,df_min,df_full = C_retrieve_code(chembl_id, data,operation,columns,target_column, remove_null, output_path, output_filename)
        print("Chembl_ID:",chembl_id,"Retrieved!")
    except RuntimeError as e:
        print(">>>> Chembl_ID:",chembl_id,"Error:",e)
print("Successfully completed. Files saved at: {}".format(output_path))