# [haberpy](https://pypi.org/project/haberpy/)

Son dakika haberleri çekebilmenize yarar.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -U haberpy
```

## Usage

```python
from haberpy import Haberler

haber = Haberler()

# returns 'text'
text = haber.text(limit=1)
"En güncel haber metinlerini çeker."

# returns 'img'
img = haber.img(limit=1)
"En güncel haberlere dair görselleri çeker."

# returns 'ornekler'
text, img = haber.text_and_img(limit=1)
"Güncel haberlerin metin ve görselini tek istekte verir."

######### Sport #####################

from haber.sport import Sport

spor = Sport()

# returns 'title'
spor.title(limit=1)
"Güncel spor haberine ait başlığı çeker."

# returns 'about'
spor.about(limit=1)
"Güncel spor haberine ait içeriği çeker."

# returns 'img'
spor.img(limit=1)
"Güncel spor haberine ait görseli çeker."
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contact

[Telegram](https://t.me/ReWoxi) - [Github](https://github.com/Meinos10) - Discord: ```emree#0010```
