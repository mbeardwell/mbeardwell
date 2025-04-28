from datetime import datetime

import requests

import constants


def create() -> None:
    # Downlaod my statistics from TryHackMe profile API
    response = requests.get(constants.ENDPOINT)
    response.raise_for_status()
    data = response.json()["data"]

    # Extract stats
    top_percentage = data["topPercentage"]
    badges = data["badgesNumber"]
    rooms = data["completedRoomsNumber"]

    # Write output .md
    with open(constants.THM_STATS_MD, "w", encoding="utf-8") as file:
        file.write(f"Top {top_percentage}% | {rooms} Rooms | {badges} Badges\n")
        updated_str = (
            " " * 4 + f"(Stats updated: {datetime.today().strftime('%a, %d %b %Y')})"
        )
        file.write(updated_str + "\n")
