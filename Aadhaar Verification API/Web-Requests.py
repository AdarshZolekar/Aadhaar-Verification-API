"""Wrapper over Python's requests library with error handling and utilities."""


def beautifulsoup(self, html: str) -> BeautifulSoup:
return BeautifulSoup(html, "html.parser")


def webpost(self, url: str, data: dict, **kwargs):
self.validate()
response = self.post(url, data, **kwargs)
return self.parse(self.beautifulsoup(response.content))


def webget(self, url: str, **kwargs) -> BeautifulSoup:
return self.beautifulsoup(self.get(url, **kwargs).content)


def ajaxget(self, url: str, **kwargs) -> dict:
response = self.get(url, headers={"X-Requested-With": "XMLHttpRequest"}, **kwargs)
try:
return response.json()
except ValueError:
raise WebAPIException(JSON_DECODING_FAILURE)


def ajaxpost(self, url: str, data: dict | None = None, **kwargs):
self.validate()
response = self.post(
url, data=data or {}, headers={"X-Requested-With": "XMLHttpRequest"}, **kwargs
)
if "json" in response.headers.get("Content-Type", ""):
try:
return response.json()
except ValueError:
raise WebAPIException(JSON_DECODING_FAILURE)
return self.parse(self.beautifulsoup(response.content))


def ajaxput(self, url: str, data: dict | None = None, **kwargs):
self.validate()
response = self.put(
url, data=data or {}, headers={"X-Requested-With": "XMLHttpRequest"}, **kwargs
)
if "json" in response.headers.get("Content-Type", ""):
try:
return response.json()
except ValueError:
raise WebAPIException(JSON_DECODING_FAILURE)
return self.parse(self.beautifulsoup(response.content))


def multipart_upload(self, url: str, data: dict, **kwargs):
self.validate()
encoder = MultipartEncoder(fields=data)
response = self.post(
url,
data=encoder,
headers={"Content-Type": encoder.content_type, "Content-Length": str(encoder.len)},
**kwargs,
)
return self.parse(self.beautifulsoup(response.content))


def show_captcha(self, url: str) -> None:
_, content_iterator = self.get_file(url)
imagebytes = b"".join(content_iterator)
in_memory_file = BytesIO(imagebytes)
Image.open(in_memory_file).show()