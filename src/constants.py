
BIO_MD = '../docs/bio.md'
PROJECTS_CSV = '../docs/projects.csv'
README_TEMPLATE_MD = '../docs/readme-template.md'

BIO_WRAPPED_MD = '../docs/output/bio-wrapped.md'
TABLE_MD = '../docs/output/table.md'
THM_STATS_MD = '../docs/output/thm-stats.md'

BIO_WIDTH = 100
DESCR_WIDTH = 60

HEADERS = {"Title": 0, "Repo": 1, "Description": 2}
TABLE_STYLE = 'grid' # plain / grid / pipe / html / rst

URL = "https://tryhackme.com/p/mbeardwell"

SELECTORS = {
    "PERCENTILE": "".join("""
                          //*[@id="middle-panel"]/div/main/section/
                          div[1]/div/div[2]/div[1]/div[1]
                          """.split()),
    "BADGES": "".join("""
                      //*[@id="middle-panel"]/div/main/section/
                      div[1]/div/div[2]/div[2]/div[2]/span
                      """.split()),
    "LABS": "".join("""
                    //*[@id="middle-panel"]/div/main/section/
                    div[1]/div/div[2]/div[4]/div[2]/span
                    """.split())
}
