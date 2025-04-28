import constants
from playwright.sync_api import sync_playwright
from datetime import datetime

def wait_for_xpath(page, xpath):
    page.wait_for_selector(f"xpath={xpath}")

def get_text(page, selector):
    xpath = constants.SELECTORS[selector]
    wait_for_xpath(page, xpath)
    return page.locator(f"xpath={xpath}").all_inner_texts()[0]

def create():
    # Navigate to my profile page
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(
        headless=True,
        args=["--window-size=1920,1080"]
    )
    page = browser.new_page(
        viewport={"width": 1920, "height": 1080},
        device_scale_factor=1,
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    )
    page.goto(constants.URL, wait_until="load")

    # Extract stats
    percentile = get_text(page, "PERCENTILE").title()
    badges = get_text(page, "BADGES")
    labs = get_text(page, "LABS")

    # Write output .md
    with open(constants.THM_STATS_MD, 'w') as file:
        file.write(f"{percentile} | {labs} Rooms | {badges} Badges\n")
        updated_str = f"    (Stats updated: {datetime.today().strftime('%a, %d %b %y')})"
        file.write(updated_str + "\n")

    browser.close()
    playwright.stop()
