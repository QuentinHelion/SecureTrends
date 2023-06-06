"""
Database controller
"""

from application.interfaces.presenters.database_presenter import MySQLDatabaseGateway


class DatabaseController:
    """
    Database controller
    """

    def __init__(self, host, user, password, database):
        self.db_presenter = MySQLDatabaseGateway(
            host=host,
            database=database,
            user=user,
            password=password
        )

    def check_exist(self, title, platform):
        """
        :param title: title of article
        :param platform: platform where article from
        :return: bool depend on if exist
        """
        self.db_presenter.connect()
        result = self.db_presenter.execute_query(
            f"SELECT title FROM ARTICLES WHERE title = '{title}' AND platform = '{platform}'")
        self.db_presenter.disconnect()
        if len(result) == 0:
            return False
        return True

    def save_article(self, title, platform, link, summary):
        """
        :param title:
        :param platform:
        :param link:
        :param summary:
        :return: bool depend on if save is done
        """
        self.db_presenter.connect()
        result = self.db_presenter.execute_command(
            f"INSERT INTO ARTICLES(title, platform, link, summary) "
            f"VALUES ('{title}', '{platform}', '{link}', '{summary}')"
        )
        self.db_presenter.disconnect()
        return result

    def remove_article(self, title, platform):
        """
        :param title:
        :param platform:
        :return:
        """
        self.db_presenter.connect()
        result = self.db_presenter.execute_command(
            f"DELETE FROM ARTICLES WHERE platform='{platform}' AND title='{title}'"
        )
        self.db_presenter.disconnect()
        return result
