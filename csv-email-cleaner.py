import sys
import os
import pandas as pd


def get_country(file_name: str):
    return file_name.split('.')[0]


def get_domain(country_name: str):
    domains = {
        "bolivia": "bo",
        "brasil": "br",
        "chile": "cl",
        "colombia": "co",
        "equador": "ec",
        "mexico": "mx",
        "paraguai": "py",
        "peru": "pe"
    }

    return domains.get(country_name)


# This function requires some understanding of series of data in pandas library
def filter_csv_dataframe(csv_dataframe, country_domain : str):
    # Gets a subset of the dataframe, in which the values in column EMAIL
    # match the condition of ending with ".com" substring 
    ends_with_com = csv_dataframe[csv_dataframe['EMAIL'].str.lower()
    .str.endswith(".com", na=False)]
    
	# Same, but now ending with each country domain
    ends_with_country_domain = csv_dataframe[csv_dataframe['EMAIL'].str.lower()
    .str.endswith(f".{country_domain}", na=False)]

	# na=False is needed so it understands NA as not matching conditions
    # .str is used so we may apply string methods to series data

	# Returns a dataframe with both subsets
    return pd.concat([ends_with_com, ends_with_country_domain])


def create_clean_csv_file(dataframe, destination_dir: str, country_name : str):
    # If theres no such directory, creates it
    if not os.path.isdir(destination_dir):
        os.mkdir(destination_dir)

    dataframe.to_csv(f"{destination_dir}/{country_name}.csv", index=False)
    print(f"File {destination_dir}/{country_name}.csv created")


def clean_csv(file_name: str, origin_dir : str, destination_dir: str):
    country_name = get_country(file_name)
    domain_name = get_domain(country_name)
    csv_dataframe = pd.read_csv(f"{origin_dir}/{file_name}")

    filtered_csv = filter_csv_dataframe(csv_dataframe, domain_name)
    create_clean_csv_file(filtered_csv, destination_dir, country_name)


def main():
    if len(sys.argv) != 3:
        print(f"Invalid number of arguments.\nRun script as it follows:\n")
        print(
            f"{sys.argv[0]} <directory with .csv files> <destination directory>")
        return

    directory = os.fsencode(sys.argv[1])
    destination_dir = sys.argv[2]

    try:
        dirlist = os.listdir(directory)
    except:
        print(f"Directory {sys.argv[1]} not found. Shutting down.")
        return

	# Iterates over directory, looking for .csv files to be cleaned
    for file in dirlist:
        file_name = os.fsdecode(file)
        if file_name.endswith(".csv"):
            clean_csv(file_name, sys.argv[1], destination_dir)

    print("\nClean e-mail .csv files created.")


main()
