"""
Krebon security rss feed
"""

from application.interfaces.presenters.rsspresenter import RSSPresenter


class KrebonSec:
    """
    KrebonSec usage class
    """

    def __init__(self):
        self.presenter = RSSPresenter("https://krebsonsecurity.com/feed/")

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
                "summary": self.presenter.get_entry_summary(entry)
            })
        return result
