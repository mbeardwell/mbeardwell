import constants
from playwright.sync_api import sync_playwright

def wait_for_xpath(page, xpath):
    page.wait_for_selector(f"xpath={xpath}")

def get_text(page, selector):
    xpath = constants.SELECTORS[selector]
    wait_for_xpath(page, xpath)
    return page.locator(f"xpath={xpath}").all_inner_texts()[0]


def create():
    # Navigate to my profile page
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto(constants.URL)

    # Extract stats
    percentile = get_text(page, "PERCENTILE").title()
    badges = get_text(page, "BADGES")
    labs = get_text(page, "LABS")

    # Write output .md
    with open(constants.THM_STATS_MD, 'w') as file:
        file.write(f"{percentile} TryHackMe | {labs} Rooms | {badges} Badges\n")

    browser.close()
    playwright.stop()
