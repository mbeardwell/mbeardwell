from datetime import datetime
from typing import Optional

import requests
from requests import Response

import constants


def create() -> None:
    r: Optional[Response] = None

    try:
        # Download my statistics from TryHackMe profile API
        r = requests.get(constants.ENDPOINT, timeout=30000)
    except Exception as e:
        raise TimeoutError(f"Failed to get TryHackMe stats: {e}") from e

    r.raise_for_status()
    data = r.json()["data"]

    # Extract stats
    top_percentage = data["topPercentage"]
    badges = data["badgesNumber"]
    rooms = data["completedRoomsNumber"]

    # Write output .md
    with open(constants.THM_STATS_MD, "w", encoding="utf-8") as file:
        file.write(f"Top {top_percentage}% | {rooms} Rooms | {badges} Badges\n")
        updated_str = (
            " " * 4 + f"(Stats updated: {datetime.today().strftime('%a, %d %b %Y at %H:%M:%S')})"
        )
        file.write(updated_str + "\n")
