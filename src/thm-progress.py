from playwright.sync_api import sync_playwright

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

URL = "https://tryhackme.com/p/mbeardwell"

def get_text(page, xpath):
    return page.locator(f"xpath={xpath}").all_inner_texts()[0]

# Navigate to my profile page
playwright = sync_playwright().start()
browser = playwright.chromium.launch()
page = browser.new_page()
page.goto(URL)

# Extract stats
percentile = get_text(page, SELECTORS["PERCENTILE"]).title()
badges = get_text(page, SELECTORS["BADGES"])
labs = get_text(page, SELECTORS["LABS"])

# Write output .md
with open('../docs/thm-stats.md', 'w') as file:
    file.write(f"{percentile} TryHackMe | {labs} Labs | {badges} Badges\n")

browser.close()
playwright.stop()
