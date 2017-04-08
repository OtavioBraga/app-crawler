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
        - search a app

        Due the App Store limitation, we can get
        only the 100's first apps on chart.
    """

    def __init__(self, **kwargs):
        self.base_url = "http://www.apple.com/itunes/charts/{}/"
        self.chart_types = {
            "paid": "free-apps",
            "free": "paid-apps"
        }
        self.country = kwargs.get("country", "")

    # List top 100 paid apps
    def top_paid(self):
        chart_type = self.chart_types.get("paid")
        return self.parse_apps_list(chart_type)

    # List top 100 free apps
    def top_free(self):
        chart_type = self.chart_types.get("free")
        return self.parse_apps_list(chart_type)

    # Show app information if they are on free or paid top chart
    def app_info(self, name):
        name = name.lower()

        # TODO: optmize this. maybe with zip(top_free, top_paid)
        for app in self.top_free():
            if app["name"].lower().startswith(name):
                return self.parse_app(app)

        for app in self.top_paid():
            if app["name"].lower().startswith(name):
                return self.parse_app(app)

        return {"warning": "not_on_charts"}

    # Get the html and parse it to separe the apps in a list
    def parse_apps_list(self, chart_type):
        soup = BeautifulSoup(self.apps_list_html(chart_type), "html.parser")

        apps_html_list = soup.find("section",
                                   {"class": "section apps chart-grid"}
                                   ).find_all("li")
        apps = []
        for app_html in apps_html_list:
            app = copy.deepcopy(APP)
            app["name"] = app_html.h3.text
            app["category"] = app_html.h4.text

            ranking = re.sub("[^0-9]", "", app_html.strong.text)
            app["ranking_position"] = int(ranking)

            app["url"] = app_html.a.get("href")

            app_icon = "http://www.apple.com/{}".format(app_html.img.get("src"))
            app["icon"] = app_icon

            apps.append(app)

        return apps

    # Parse the app page html to extract app info
    def parse_app(self, app):
        soup = BeautifulSoup(self.app_info_html(app["url"]), "html.parser")

        app["description"] = soup.find("p", {"itemprop": "description"}).text

        for image in soup.find_all("img", {"itemprop": "screenshot"}):
            app["screenshots"].append(image.get("src"))

        return app

    # Choose a chart type and get the HTML to parse
    def apps_list_html(self, chart_type):
        return requests.get(self.base_url.format(chart_type)).text

    # Get the app info page html
    def app_info_html(self, app_link):
        return requests.get(app_link).text
