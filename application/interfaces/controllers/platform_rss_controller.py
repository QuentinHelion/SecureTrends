"""
Platform rss feed
"""

from application.interfaces.presenters.rsspresenter import RSSPresenter
from application.use_cases.save_article import SaveArticle


class PlatformRssController:
    """
    PlatformRssController usage class
    """

    def __init__(self, platform, link):
        self.presenter = RSSPresenter(f"{link}")
        self.platform = platform
        self.save_article = SaveArticle()

    def get_title(self):
        """
        :return: feed title
        """
        return self.presenter.get_feed_title()

    def get_feed(self):
        """
        :return: feed entries in array
        """
        result = []
        entries = self.presenter.get_feed_entries()
        for entry in entries:
            result.append({
                "title": self.presenter.get_entry_title(entry),
                "summary": self.presenter.get_entry_summary(entry),
                "link": self.presenter.get_entry_link(entry)
            })
        return result

    def save_feed(self):
        """
        :return: bool depend on great job working
        """
        entries = self.presenter.get_feed_entries()
        if len(entries) == 0:
            return False
        for entry in entries:
            article = {
                "title": self.presenter.get_entry_title(entry),
                "platform": self.platform,
                "summary": self.presenter.get_entry_summary(entry),
                "link": self.presenter.get_entry_link(entry)
            }
            self.save_article.save(article=article)
        return True
