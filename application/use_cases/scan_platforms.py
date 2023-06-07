"""
Scan all platforms
"""

from application.interfaces.controllers.platform_rss_controller import PlatformRssController
from infrastructure.data.json_reader import JSONReader


class ScanPlatforms:
    """
    Scan all platforms class
    """

    def __init__(self, json):
        self.json_reader = JSONReader(f"{json}")
        platforms = self.json_reader.read_json()
        platforms_array = []
        if platforms is not None:
            for platform in platforms:
                print(platform)
                platforms_array.append(
                    PlatformRssController(
                        platform=platform["name"],
                        url=platform["url"]
                    )
                )