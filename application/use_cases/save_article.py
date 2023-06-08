"""
Permit to save article on database
"""

from application.interfaces.controllers.database_controller import DatabaseController
from infrastructure.data.env import EnvReader


class SaveArticle:
    """
    Class permit to save article
    """

    def __init__(self):
        self.dotenv = EnvReader()

        self.db_controller = DatabaseController(
            host=self.dotenv.get("DB_HOST"),
            database=self.dotenv.get("DB_NAME"),
            user=self.dotenv.get("DB_USER"),
            password=self.dotenv.get("DB_PASS")
        )

    def save(self, article):
        """
        :param article: article to save
        :return:
        """
        if not self.db_controller.check_exist(
                title=article["title"].replace("'", "\""),
                platform=article["platform"].replace("'", "\"")
        ):
            return self.db_controller.save_article(
                title=article["title"].replace("'", "\""),
                platform=article["platform"].replace("'", "\""),
                link=article["link"].replace("'", "\""),
                summary=article["summary"].replace("'", "\"")
            )
        return False

    def remove(self, article):
        """
        :param article: article to save
        :return:
        """
        print('remove article')
        if self.db_controller.check_exist(
                title=article["title"],
                platform=article["platform"]
        ):
            return self.db_controller.remove_article(
                title=article["title"],
                platform=article["platform"]
            )
        return False
