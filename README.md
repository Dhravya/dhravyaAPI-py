# This is a python wrapper for my api

api_url = "https://api.dhravya.me/"

## This wrapper now has async support, its basically the same except it uses asyncio

## Features:
- Generate a qr code for text, url, image, or basically anything, in many different, fancy formats
- OCR: Get text from an image or an image URL
- Meme: Smartly get a meme from any topic (sourced from reddit)
- Basic generators are:
  - compliment: returns a compliment
  - would you rather: returns a would you rather question
  - joke: Returns a (bad) joke

## Getting started
- Install the package from pypi
```
pip install dhravyaAPI
```

> Dependency: requests
```
pip install --upgrade requests
```

## Usage and examples
```python
>>> # Get an 8ball response
>>> from dhravyaapi import DhravyaAPI
>>> dhravyaapi = DhravyaAPI() # Create a new instance of the API
>>> response = dhravyaapi.eightball()
```

For OCR:
```python
>>> from dhravyaapi import DhravyaAPI
>>> dhravyaapi = DhravyaAPI()
>>> text = dhravyapi.ocr(image=BytesIO(open("1u8om0jymh581.jpg", "rb").read()))
>>> # Or, if you have a url:
>>> text = dhravyaapi.ocr(url="https://i.imgur.com/sdfsfXyYsf8Q.jpg")
```

To get a Meme:
```python
>>> from dhravyaapi import DhravyaAPI
>>> dhravyaapi = DhravyaAPI()
>>> meme = dhravyaapi.meme(topic="memes")
>>> # Note that this returns a dictionary if url_only is False
```

To generate a qr code:
```python
>>> from dhravyaapi import DhravyaAPI
>>> dhravyaapi = DhravyaAPI() # Create a new instance of the API
>>> qr_code= dhravyaapi.qrcode(query="Hello, World!", drawer=1, mask=1)))
>>> # Note that this returns an image object that can be saved to a file
```

Basic generators:
```python
>>> from dhravyaapi import DhravyaAPI
>>> dhravyaapi = DhravyaAPI()
>>> compliment = dhravyaapi.compliment()
```

```python
>>> from dhravyaapi import DhravyaAPI
>>> dhravyaapi = DhravyaAPI()
>>> wyr = dhravyaapi.wyr()
```

```python
>>> from dhravyaapi import DhravyaAPI
>>> dhravyaapi = DhravyaAPI()
>>> joke = dhravyaapi.joke()
```





