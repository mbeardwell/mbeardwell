import constants
import csv
from tabulate import tabulate
import re
import textwrap

def get_row_val(row, key):
    return row[constants.HEADERS[key]]

def set_row_val(row, key, val):
    row[constants.HEADERS[key]] = val

def filter(table, keys):
    return [[get_row_val(row, key) for key in keys] for row in table]

def create():
    # Read CSV
    with open(constants.PROJECTS_CSV) as csvfile:
        projects = list(csv.reader(csvfile, delimiter=',', quotechar='\"'))

    # Create formatted table
    filtered = filter(projects, ["Title", "Description"])

    for row in filtered:
        indexTitle, indexDesc = 0, 1
        row[indexTitle] = "~{}~".format(row[indexTitle])
        row[indexDesc] = textwrap.fill(row[indexDesc], width=constants.DESCR_WIDTH)

    table_str = tabulate(filtered, headers=["Title", "Description"], tablefmt=constants.TABLE_STYLE, showindex=False)

    # Replace 'Title' with hyperlinked text
    for row in projects:
        repo = get_row_val(row, "Repo")
        title = get_row_val(row, "Title")
        regex = re.escape(f"~{title}~").replace(r'\ ', r'\s+')
        replacement = f"<a href=\"https://github.com/mbeardwell/{repo}\">{title}</a>  "
        table_str = re.sub(regex, replacement, table_str, flags=re.DOTALL)

    with open(constants.TABLE_MD, 'w') as mdfile:
        mdfile.write(table_str + "\n")
