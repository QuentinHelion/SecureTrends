"""
Get feed
"""

from application.interfaces.controllers.database_controller import DatabaseController
from infrastructure.data.env import EnvReader


class Feed:
    """
    All feed operation
    """

    def __init__(self):
        self.dotenv = EnvReader()
        self.db_controller = DatabaseController(
            host=self.dotenv.get("DB_HOST"),
            database=self.dotenv.get("DB_NAME"),
            user=self.dotenv.get("DB_USER"),
            password=self.dotenv.get("DB_PASS")
        )

    def get_feed(self):
        """
        get basic feed
        :return: all articles of last days
        """
        return self.db_controller.get_articles()

    def get_feed_from(self, platform):
        """
        get feed from given platform
        :param platform:
        :return:
        """
        return self.db_controller.get_articles(
            platform=platform
        )

    def get_feed_to(self, interval):
        """
        :param interval:
        :return:
        """
        return self.db_controller.get_articles(
            interval=interval
        )

    def get_feed_from_to(self, interval, platform):
        """
        :param interval:
        :param platform:
        :return:
        """
        return self.db_controller.get_articles(
            interval=interval,
            platform=platform
        )
