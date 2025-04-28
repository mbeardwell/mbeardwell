import components
import constants


def read_file(path: str) -> str:
    return open(path, encoding="utf-8").read()


# Create markdown components
components.bio.create()
components.table.create()
components.thmprogress.create()

# Read markdown components and the readme template
bio: str = read_file(constants.BIO_WRAPPED_MD)
thm_stats: str = read_file(constants.THM_STATS_MD)
table: str = read_file(constants.TABLE_MD)
readme_template: str = read_file(constants.README_TEMPLATE_MD)

# Insert markdown components into readme template
output: str = readme_template
output = output.replace("__BIO__\n", bio)
output = output.replace("__THM_STATS__\n", thm_stats)
output = output.replace("__TABLE__\n", table)

# Write readme
with open(constants.README, "w", encoding="utf-8") as file:
    file.write(output)
