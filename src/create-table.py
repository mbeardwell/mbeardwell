import csv
from tabulate import tabulate
import re
import textwrap

TABLE_MD = '../docs/table.md'
PROJECTS_CSV = '../docs/projects.csv'
HEADERS = {"Title": 0, "Repo": 1, "Description": 2}
DESCR_WIDTH = 60
TABLE_STYLE = 'grid' # plain / grid / pipe / html / rst

def get_row_val(row, key):
    return row[HEADERS[key]]

def set_row_val(row, key, val):
    row[HEADERS[key]] = val

def filter(table, keys):
    return [[get_row_val(row, key) for key in keys] for row in table]

# Read CSV
with open(PROJECTS_CSV) as csvfile:
    projects = list(csv.reader(csvfile, delimiter=',', quotechar='\"'))

# Create formatted table
filtered = filter(projects, ["Title", "Description"])

for row in filtered:
    indexTitle, indexDesc = 0, 1
    row[indexTitle] = "~{}~".format(row[indexTitle])
    row[indexDesc] = textwrap.fill(row[indexDesc], width=DESCR_WIDTH)

table_str = tabulate(filtered, headers=["Title", "Description"], tablefmt=TABLE_STYLE, showindex=False)

# Replace 'Title' with hyperlinked text
for row in projects:
    repo = get_row_val(row, "Repo")
    title = get_row_val(row, "Title")
    regex = re.escape(f"~{title}~").replace(r'\ ', r'\s+')
    replacement = f"<a href=\"https://github.com/mbeardwell/{repo}\">{title}</a>  "
    table_str = re.sub(regex, replacement, table_str, flags=re.DOTALL)

with open(TABLE_MD, 'w') as mdfile:
    mdfile.write(table_str + "\n")
