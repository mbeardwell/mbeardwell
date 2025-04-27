import constants
from playwright.sync_api import sync_playwright

def get_text(page, xpath):
    return page.locator(f"xpath={xpath}").all_inner_texts()[0]

def create():
    # Navigate to my profile page
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto(constants.URL)

    # Extract stats
    percentile = get_text(page, constants.SELECTORS["PERCENTILE"]).title()
    badges = get_text(page, constants.SELECTORS["BADGES"])
    labs = get_text(page, constants.SELECTORS["LABS"])

    # Write output .md
    with open(constants.THM_STATS_MD, 'w') as file:
        file.write(f"{percentile} TryHackMe | {labs} Rooms | {badges} Badges\n")

    browser.close()
    playwright.stop()
