readme_template = open('../docs/readme-template.md').read()

table = open('../docs/table.md').read()
thm_stats = open('../docs/thm-stats.md').read()

output = readme_template
output = output.replace('__TABLE__\n', table)
output = output.replace('__THM_STATS__\n', thm_stats)

with open('../README.md', 'w') as file:
    file.write(output)
