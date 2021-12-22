import httpx


class ServerError(Exception):
    pass


class DhravyaAPI:
    """Api that does a lot of things. Check https://api.dhravya.me/ for endpoints
    Basic Usage:
    >>> from dhravyaapi import DhravyaAPI
    >>> dhravyaapi = DhravyaAPI() # Create a new instance of the API
    >>> response = dhravyaapi.eightball()"""

    def __init__(self) -> None:
        """Api that does a lot of things. Check https://api.dhravya.me/ for endpoints
        Basic Usage:
        >>> from dhravyaapi import DhravyaAPI
        >>> dhravyaapi = DhravyaAPI() # Create a new instance of the API
        >>> response = dhravyaapi.eightball()"""
        pass

    def httpx_get(self,url, params=None):
        params = params if params else {}
        with httpx.Client() as client:
            try:
                return client.get(url, params = params)
            except Exception as e:
                return e

    def httpx_post(self, url, files = None):
        with httpx.Client() as client:
            try:
                return client.post(url, files = files if files else {}) 
            except Exception as e:
                return e

    def eightball(self) -> str:
        """Returns a random response from the 8ball
        Basic Usage:
        >>> from dhravyaapi import DhravyaAPI
        >>> dhravyaapi = DhravyaAPI() # Create a new instance of the API
        >>> response = dhravyaapi.eightball()"""
        url = "https://api.dhravya.me/8ball"
        # Get response using httpx
        response = self.httpx_get(url)
        return response.json()["response"]

    def qrcode(
        self, query: str = "No query provided", drawer: int = 1, mask: int = 1
    ) -> str:

        """Returns a random response from the 8ball.
        Basic Usage:
        >>> from dhravyaapi import DhravyaAPI
        >>> dhravyaapi = DhravyaAPI() # Create a new instance of the API
        >>> qr_code= dhravyaapi.qrcode(query="Hello, World!", drawer=1, mask=1)))
        >>> # Note that this returns an image object that can be saved to a file"""

        url = "https://api.dhravya.me/qrcode"
        if not drawer in range(1, 7):
            raise ValueError("Drawer must be a number between 1 and 6")
        if not mask in range(1, 6):
            raise ValueError("Mask must be a number between 1 and 5")
        params = {"query": query, "drawer": drawer, "mask": mask}
        response = self.httpx_get(url, params=params)
        # response is an image
        return response.content

    def meme(
        self,
        topic: str = "random",
        url_only: bool = False,
        url_and_title_only: bool = False,
    ) -> str:
        """Gets a random meme of your provided topic
        Basic Usage:
        >>> from dhravyaapi import DhravyaAPI
        >>> dhravyaapi = DhravyaAPI()
        >>> meme = dhravyaapi.meme(topic="memes")
        >>> # Note that this returns a dictionary if url_only is False"""
        url = "https://api.dhravya.me/meme/"

        response = self.httpx_get(url + topic)
        if response.status_code != 200:
            raise ServerError("Server returned an error")

        if url_only:
            return response.json()["url"]
        if url_and_title_only:
            return response.json()["url"], response.json()["title"]
        return response.json()

    def meme_as_image(self, subreddit: str = None) -> bytes:
        """Gets a random meme of your provided subreddit
        Basic Usage:
        >>> from dhravyaapi import DhravyaAPI
        >>> dhravyaapi = DhravyaAPI()
        >>> meme = dhravyaapi.meme_as_image(subreddit="memes")
        >>> # Note that this returns an image object that can be saved to a file or displayed
        >>> # with PIL
        >>> from io import BytesIO
        >>> from PIL import Image
        >>> img = Image.open(BytesIO(meme))
        >>> img.show()
        """
        url = "https://api.dhravya.me/meme"

        response = self.httpx_get(url, params={"subreddit": subreddit})
        if response.status_code != 200:
            raise ServerError("Server returned an error : " + str(response.status_code))
        return response.content

    def ocr(self, image: bytes = None, url: str = None) -> bytes:
        """Gets the text from an image
        Basic Usage:
        >>> from dhravyaapi import DhravyaAPI
        >>> dhravyaapi = DhravyaAPI()
        >>> text = dhravyapi.ocr(image=BytesIO(open("1u8om0jymh581.jpg", "rb").read()))
        >>> # Or, if you have a url:
        >>> text = dhravyaapi.ocr(url="https://i.imgur.com/sdfsfXyYsf8Q.jpg")
        """
        apiurl = "https://api.dhravya.me/ocr"
        if image is None and url is None:
            raise ValueError("You must provide either an image or a url")
        if url:
            response = self.httpx_get(apiurl, {"url": url})
        else:
            response = self.httpx_post(apiurl, {"image": image})
        if response.status_code != 200:
            raise ServerError("Server returned an error : " + str(response.status_code))
        return response.json()["text"]

    def compliment(self) -> str:
        """Returns a random compliment
        Basic Usage:
        >>> from dhravyaapi import DhravyaAPI
        >>> dhravyaapi = DhravyaAPI()
        >>> compliment = dhravyaapi.compliment()
        """
        url = "https://api.dhravya.me/compliment"
        response = self.httpx_get(url)
        return response.json()["compliment"]

    def wyr(self) -> str:
        """Returns a random wyr
        Basic Usage:
        >>> from dhravyaapi import DhravyaAPI
        >>> dhravyaapi = DhravyaAPI()
        >>> wyr = dhravyaapi.wyr()
        """
        url = "https://api.dhravya.me/wyr"
        response = self.httpx_get(url)
        return response.json()["wyr"]

    def joke(self) -> str:
        """Returns a random joke
        Basic Usage:
        >>> from dhravyaapi import DhravyaAPI
        >>> dhravyaapi = DhravyaAPI()
        >>> joke = dhravyaapi.joke()
        """
        url = "https://api.dhravya.me/joke"
        response = self.httpx_get(url)
        return response.json()["joke"]

    def mcstats(self, host : str=None, port:int=25565) -> dict:
        """Returns a dictionary of the Minecraft server's status
        Basic Usage:
        >>> from dhravyaapi import DhravyaAPI
        >>> dhravyaapi = DhravyaAPI()
        >>> mcstats = dhravyaapi.mcstats(host="mc.hypixel.net")
        >>> print(mcstats)
        """
        url = "https://api.dhravya.me/mcstats"
        if host is None or port is None:
            raise ValueError("You must provide a host and port")
        params = {"host": host, "port": port}
        response = self.httpx_get(url, params)
        return dict(response.json())

