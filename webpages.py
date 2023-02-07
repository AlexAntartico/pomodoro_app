import webbrowser
import constants as const
webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(const.chrome_path))


class Webpage:
    """A class to represent webpages I want to open."""

    def __init__(self):
        self.titles = const.webpages.keys()
        self.url = const.webpages.values()

    def open_all(self):
        """Opens all the webpages from dictionary"""
        for i in self.url:
            webbrowser.get("chrome").open(i)

    def print_attributes(self):
        """Prints the attributes of the class and its types"""
        print(f"Titles type: {type(self.titles)}\nTitles values: {self.titles}\n")
        print(f"URLs type: {type(self.url)}\nURLs values: {self.url}\n")


def main():
    test = Webpage()
    test.print_attributes()
    test.open_all()


if __name__ == "__main__":
    main()
