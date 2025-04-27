from constants import *
import components

readme_template = open(README_TEMPLATE_MD).read()

# Create and read markdown components
components.bio.create()
components.table.create()
components.thmprogress.create()

bio = open(BIO_WRAPPED_MD).read()
thm_stats = open(THM_STATS_MD).read()
table = open(TABLE_MD).read()

# Install component markdown files into README
output = readme_template
output = output.replace('__BIO__\n', bio)
output = output.replace('__THM_STATS__\n', thm_stats)
output = output.replace('__TABLE__\n', table)

# Write README
with open('../README.md', 'w') as file:
    file.write(output)
