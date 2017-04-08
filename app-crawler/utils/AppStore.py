from bs4 import BeautifulSoup
from base_app import APP
import requests
import copy
import re


class AppStore(object):
    """ App Store app crawler for get charts.
        By now, the crawler can get two chart types:
        - top paid apps
        - top free apps
    """

    def __init__(self, **kwargs):
        self.base_url = "http://www.apple.com/itunes/charts/{}/"
        self.chart_types = {
            "paid": "free-apps",
            "free": "paid-apps"
        }
        self.apps = []

    def top_paid(self):
        chart_type = self.chart_types.get("paid")
        return self.parse_html(chart_type)

    def top_free(self):
        chart_type = self.chart_types.get("free")
        return self.parse_html(chart_type)

    def parse_html(self, chart_type):
        soup = BeautifulSoup(self.get_html_chart(chart_type))

        apps_html_list = soup.find("section",
                                   {"class": "section apps chart-grid"}
                                   ).find_all("li")

        for app_html in apps_html_list:
            app = copy.deepcopy(APP)
            app["name"] = app_html.h3.text

            ranking = re.sub("[^0-9]", "", app_html.strong.text)
            app["ranking_position"] = int(ranking)

            app["url"] = "asd"
            self.apps.append(app)
        return self.apps

    # Choose a chart type and get the HTML to parse
    def get_html_chart(self, chart_type):
        return requests.get(self.base_url.format(chart_type)).text
