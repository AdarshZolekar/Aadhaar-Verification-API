import os
from urllib.parse import urlparse, parse_qs, parse_qsl, urlencode, unquote, ParseResult
from json import dumps




def parse_query_paras(url: str, flat: bool = True) -> dict:
parsed_url = urlparse(url)
parsed_paras = parse_qs(parsed_url.query, strict_parsing=False)
if flat:
return {k: v[0] if len(v) == 1 else v for k, v in parsed_paras.items()}
return parsed_paras




def add_url_params(url: str, params: dict) -> str:
url = unquote(url)
parsed_url = urlparse(url)
parsed_get_args = dict(parse_qsl(parsed_url.query))
parsed_get_args.update(params)


parsed_get_args.update({k: dumps(v) for k, v in parsed_get_args.items() if isinstance(v, (bool, dict))})


encoded_get_args = urlencode(parsed_get_args, doseq=True)
new_url = ParseResult(
parsed_url.scheme,
parsed_url.netloc,
parsed_url.path,
parsed_url.params,
encoded_get_args,
parsed_url.fragment,
).geturl()
return new_url




def filename_fix_existing(filename: str) -> str:
dirname = "."
name, ext = filename.rsplit(".", 1)
names = [x for x in os.listdir(dirname) if x.startswith(name)]
names = [x.rsplit(".", 1)[0] for x in names]
suffixes = [x[2:-1] for x in names if x.startswith(" (") and x.endswith(")")]
indexes = [int(x) for x in suffixes if x.isdigit()]
idx = 1 + (max(indexes) if indexes else 0)
return f"{name} ({idx}).{ext}"