import os

from dotenv import load_dotenv
from exa_py import Exa
# from langchain.tools import tool
from crewai.tools import tool

load_dotenv()


class ExaSearchTool:
    @tool
    def search(self, query: str):
        """Search for a webpage based on the query."""
        return self._exa().search(
            f"{query}",
            use_autoprompt=True,
            num_results=3
        )

    @tool
    def find_similar(self, url: str):
        """Search for webpages similar to a given URL.
        The url passed in should be a URL returned from `search`.
        """
        return self._exa().find_similar(
            url,
            num_results=3
        )

    @tool
    def get_contents(self, ids: str):
        """Get the contents of a webpage.
        The ids must be passed in as a list, a list of ids returned from `search`.
        """
        print("ids from param:", ids)

        ids = eval(ids)
        print("eval ids:", ids)

        contents = str(self._exa().get_contents(ids))
        print(contents)

        contents = contents.split("URL:")
        contents = [content[:1000] for content in contents]
        return "\n\n".join(contents)

    def tools(self):
        return [
            self.search,
            self.find_similar,
            self.get_contents,
        ]

    @staticmethod
    def _exa():
        return Exa(api_key=os.environ["EXA_API_KEY"])


if __name__ == '__main__':
    print(os.environ["EXA_API_KEY"])
