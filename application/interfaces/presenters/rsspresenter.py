"""
RSS Parser file
"""
import feedparser


class RSSPresenter:
    """
    RSS Parser class
    """
    def __init__(self, url):
        self.url = url

    def fetch_feed(self):
        """
        :return: feed content
        """
        feed = feedparser.parse(self.url)
        return feed

    def get_feed_title(self):
        """
        :return: title
        """
        feed = self.fetch_feed()
        return feed.feed.title

    def get_feed_entries(self):
        """
        :return: feed entries
        """
        feed = self.fetch_feed()
        return feed.entries

    @staticmethod
    def get_entry_title(entry):
        """
        :return: entry title
        """
        return entry.title

    @staticmethod
    def get_entry_summary(entry):
        """
        :return: entry summary
        """
        return entry.summary
