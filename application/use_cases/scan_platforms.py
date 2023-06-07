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
        json_reader = JSONReader(f"{json}")
        platforms = json_reader.read_json()
        self.platforms_array = []
        if platforms is not None:
            for platform in platforms:
                self.platforms_array.append(
                    PlatformRssController(
                        platform=platform["name"],
                        url=platform["url"]
                    )
                )

    def scan_all(self):
        """
        :return:
        """
        for platform in self.platforms_array:
            try:
                platform.save_feed()
            except IndexError:
                # Handle IndexError exception
                print("IndexError occurred")
                return False
        return True
