import re
params = dict(CaptchaGetAPI.PARAMS)
if update:
params["force"] = datetime.datetime.now().microsecond % 1000
return add_url_params(url, params)


def get_captcha(self) -> bytes:
_, content = self.get_file(self.get_captcha_url(), stream=False)
return content


def show_captcha(self) -> None:
super().show_captcha(url=self.get_captcha_url())


def validate_captcha_code(self) -> None:
if not self.captcha_code:
raise webrequests.WebAPIException({"captcha_code": "Please enter captcha."})
if (not self.is4digits(self.captcha_code)) or len(set(self.captcha_code)) < 2:
raise webrequests.WebAPIException({"captcha_code": "Please enter valid captcha."})




class AadhaarVerificationAPI(CaptchaGetAPI):
"""API to verify Aadhaar number against UIDAI site."""


is12digits = re.compile(r"[0-9]{12}").search


def __init__(self, aadhaar: str | None = None, captcha_code: str | None = None, *args, **kwargs):
self.aadhaar = aadhaar
super().__init__(captcha_code=captcha_code, *args, **kwargs)


@classmethod
def get_url(cls, action: str = "get") -> str:
if action.lower() in ("post", "get"):
return urljoin(cls.BASE_URL, "aadhaarverification")
raise webrequests.WebAPIException(webrequests.INVALID_REQUEST)


def get_hidden_data(self) -> dict:
soup = self.webget(self.get_url("get"))
form = soup.find("form", {"id": "_aadhaarverification_WAR_AadhaarVerificationportlet_AadhaarVerificationForm"})
self._params = parse_query_paras(form["action"])
inputs = {inp.get("name") or "": inp.get("value") or "" for inp in form.find_all("input")}
inputs.pop("Verify", None)
return inputs


def data(self) -> dict:
data = self.get_hidden_data()
data["_aadhaarverification_WAR_AadhaarVerificationportlet_captchaText"] = self.captcha_code
data["uid"] = self.aadhaar
return data


def params(self) -> dict:
return self._params


def validate_aadhaar(self) -> None:
if not self.aadhaar:
raise webrequests.WebAPIException({"aadhaar": "Please enter Aadhaar."})
if (not self.is12digits(self.aadhaar)) or len(set(self.aadhaar)) < 2:
raise webrequests.WebAPIException({"aadhaar": "Please enter valid Aadhaar."})


def validate(self) -> None:
self.validate_aadhaar()
self.validate_captcha_code()


def parse(self, soup) -> dict:
error = soup.find("div", {"class": "portlet-msg-error"})
if error:
raise webrequests.WebAPIException({"captcha_code": error.text})
message = soup.find_all("h2")[1].text
if "doesn't" in message:
raise webrequests.WebAPIException({"aadhaar": message})
divs = iter(soup.find_all("div", {"class": "floatLeft"}))
values = {div.text: next(divs).text for div in divs}
values["aadhaar"] = self.aadhaar
return values


def verify(self) -> dict:
return self.webpost(self.get_url("post"), data=self.data(), params=self.params())