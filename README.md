# srttranslator-bariskeser

## Kurulum

[PyPI](https://pypi.org/project/srttranslator-bariskeser/)

```bash
pip install srttranslator-bariskeser
```
## Script ile Kullanım

Gerekli modülleri içe aktarın

```python
import os

# SRT Dosyası
from srtranslator import SrtFile
# ASS Dosyası
from srtranslator import AssFile

from srtranslator.translators.deepl_api import DeeplApi
from srtranslator.translators.deepl_scrap import DeeplTranslator
from srtranslator.translators.translatepy import TranslatePy
from srtranslator.translators.pydeeplx import PyDeepLX
```

Çeviriciyi başlatın. Herhangi bir çevirici olabilir, hatta kendi çeviricinizi bile oluşturabilirsiniz, belgelerde her çevirici için talimatlar ve kendi çeviricinizi nasıl oluşturacağınız hakkında bilgiler bulunmaktadır.

```python
translator = DeeplTranslator() # veya TranslatePy() veya DeeplApi(api_key) veya DeepLX()
```

Yükleyin, çevirin ve kaydedin. Klasördeki birden fazla dosya için, `examples folder` klasörüne bakın.

```python
filepath = "./filepath/to/srt"

# SRT Dosyası
sub = SrtFile(filepath)
# ASS Dosyası
sub = AssFile(filepath)

# Çevir
sub.translate(translator, "en", "es")

# Sonuç altyazıları daha güzel hale getirme
sub.wrap_lines()

sub.save(f"{os.path.splitext(filepath)[0]}_translated.srt")
```

Çeviriciyi kapatın

```python
translator.quit()
```

```bash
# SRT dosyası
python -m srtranslator ./filepath/to/srt -i SRC_LANG -o DEST_LANG

# ASS dosyası
python -m srtranslator ./filepath/to/ass -i SRC_LANG -o DEST_LANG
```

## Gelişmiş kullanım

```
usage: __main__.py [-h] [-i SRC_LANG] [-o DEST_LANG] [-v] [-vv] [-s] [-w WRAP_LIMIT] [-t {deepl-scrap,translatepy,deepl-api,pydeeplx}] [--auth AUTH] path

Bir .STR ve .ASS dosyasını çevirin

konumsal argümanlar:
  path                  Çevrilecek dosya

seçenekler:
  -h, --help            Yardım mesajını göster ve çık
  -i SRC_LANG, --src-lang SRC_LANG
                        Kaynak dil. Varsayılan: auto
  -o DEST_LANG, --dest-lang DEST_LANG
                        Hedef dil. Varsayılan: es (İspanyolca)
  -v, --verbose         Çıktı ayrıntı seviyesini artır
  -vv, --debug          Hata ayıklama için çıktı ayrıntı seviyesini artır
  -s, --show-browser    Tarayıcı penceresini göster
  -w WRAP_LIMIT, --wrap-limit WRAP_LIMIT
                        Bir metin satırını sarmak için karakter sayısı (boşluklar dahil). Varsayılan: 50
  -t {deepl-scrap,translatepy,deepl-api}, --translator {deepl-scrap,translatepy,deepl-api,pydeeplx}
                        Kullanılacak yerleşik çevirici
  --auth AUTH           Çevirici için gerekliyse API anahtarı
  --proxies             pydeeplx için varsayılan olarak proxy kullan
```
