import aiohttp


class AsyncClient:
    def __init__(self, loop):
        """Asynchronous client for the API, uses aiohttp"""

        self.url = "https://api.dhravya.me/"
        self.loop = loop

    async def fetch_json(self, session, url, params=None):
        """Fetches a json from the API"""
        if params == None:
            params = {}
        async with session.get(url, params=params) as response:
            # Return json response
            return await response.json()

    async def fetch_image(self, session, url, params=None):
        """Fetches an image from the API"""
        if params == None:
            params = {}
        async with session.get(url, params=params) as response:
            return await response.content.read()

    async def eightball(self):
        """Returns a random 8ball response"""
        async with aiohttp.ClientSession(loop=self.loop) as session:
            url = self.url + "8ball"
            response = await self.fetch_json(session, url)
            return response["response"]

    async def qrcode(
        self, query: str = "No query provided", drawer: int = 1, mask: int = 1
    ) -> bytes:
        """Returns a qrcode image\n
        Usage:
        >>> import aiohttp
        >>> import asyncio
        >>> from dhravyaAPI.async import AsyncClient
        >>> async def main():
        >>>     client = AsyncClient(asyncio.get_event_loop())
        >>>     qrcode = await client.qrcode(query="test")
        >>>     print(qrcode) # This will print the image as bytes
        """
        async with aiohttp.ClientSession(loop=self.loop) as session:
            url = self.url + "qrcode"
            params = {"query": query, "drawer": drawer, "mask": mask}
            response = await self.fetch_image(session, url, params)
            # response is an image
            return response

    async def meme(
        self,
        topic: str = "random",
        url_only: bool = False,
        url_and_title_only: bool = False,
    ) -> dict:
        """Returns a meme from reddit based on the topic\n
        Usage:
        >>> import aiohttp
        >>> import asyncio
        >>> from dhravyaAPI.async import AsyncClient
        >>> async def main():
        >>>     client = AsyncClient(asyncio.get_event_loop())
        >>>     meme = await client.meme(topic="random")
        >>>     print(meme) # This will print the meme as a dict
        """

        async with aiohttp.ClientSession(loop=self.loop) as session:
            url = self.url + "meme/" + topic
            response = await self.fetch_json(session, url)
            if url_only:
                return response["url"]
            if url_and_title_only:
                return response["url"], response["title"]
            return response

    async def meme_as_image(self, subreddit: str = None) -> bytes:
        """Returns a meme from reddit based on the subreddit, but as a png or jpg (image bytes)\n
        Usage:
        >>> import aiohttp
        >>> import asyncio
        >>> from dhravyaAPI.async import AsyncClient
        >>> async def main():
        >>>     client = AsyncClient(asyncio.get_event_loop())
        >>>     meme = await client.meme_as_image(subreddit="memes")
        >>>     print(meme)
        """

        async with aiohttp.ClientSession(loop=self.loop) as session:
            url = self.url + "meme"
            response = await self.fetch_image(
                session, url, params={"subreddit": subreddit} if subreddit else None
            )
            # response is an image
            return response

    async def ocr(self, image: bytes = None, url: str = None) -> str:
        """Returns the text from an image\n
        Usage:
        >>> import aiohttp
        >>> import asyncio
        >>> from dhravyaAPI.async import AsyncClient
        >>> async def main():
        >>>     client = AsyncClient(asyncio.get_event_loop())
        >>>     ocr = await client.ocr(image=image) # For image
        >>>     # Or if you have a URL of the image
        >>>     ocr = await client.ocr(url=url) # For url
        >>>     print(ocr) # This will print the text
        """

        async with aiohttp.ClientSession(loop=self.loop) as session:
            apiurl = self.url + "ocr"
            if image:
                files = {"image": image}
            elif url:
                params = {"url": url}
            else:
                raise Exception("No image or url provided")

        if not image and not url:
            raise ValueError("You must provide an image or a url")

        async with aiohttp.ClientSession(loop=self.loop) as session:
            apiurl = self.url + "ocr"
            if image:
                async with session.post(apiurl, files=files) as response:
                    response = await response.json()
            else:
                async with session.get(apiurl, params=params) as response:
                    response = await response.json()

        return response["text"]

    async def compliment(self):
        """Returns a random compliment"""

        async with aiohttp.ClientSession(loop=self.loop) as session:
            url = self.url + "compliment"
            response = await self.fetch_json(session, url)
            return response["compliment"]

    async def wyr(self):
        """Returns a random wyr (Would you rather) Question"""
        async with aiohttp.ClientSession(loop=self.loop) as session:
            url = self.url + "wyr"
            response = await self.fetch_json(session, url)
            return response["wyr"]

    async def joke(self):
        """Returns a random joke"""
        async with aiohttp.ClientSession(loop=self.loop) as session:
            url = self.url + "joke"
            response = await self.fetch_json(session, url)
            return response["joke"]

    async def mcstats(self, host: str = None, port:int = None):
        """Returns the Minecraft server status\n
        Usage:
        >>> import aiohttp
        >>> import asyncio
        >>> from dhravyaAPI.async import AsyncClient
        >>> async def main():
        >>>     client = AsyncClient(asyncio.get_event_loop())
        >>>     status = await client.mcstats(host="example.com")
        >>>     print(status)
        """

        async with aiohttp.ClientSession(loop=self.loop) as session:
            url = self.url + "mcstats"
            port = port if port else 25565
            if host is None or port is None:
                raise ValueError("You must provide a host and port")
            params = {"host": host, "port": port}
            response = await self.fetch_json(session, url, params)
            return response

        