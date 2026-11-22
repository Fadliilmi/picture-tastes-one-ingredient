# The picture that tastes of one ingredient

[![make.fun](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047.svg)](https://make.fun/competitions/the-picture-that-tastes-of-one-20261122-2047)
[![Rank](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/Fadliilmi/picture-tastes-one-ingredient/rank.svg)](https://make.fun/competitions/the-picture-that-tastes-of-one-20261122-2047)
[![Reward](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/Fadliilmi/picture-tastes-one-ingredient/reward.svg)](https://make.fun/competitions/the-picture-that-tastes-of-one-20261122-2047)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

One picture of food, judged on how delicious it looks. The hero is a
single ingredient: a perfectly ripe mango, halved, its golden flesh
glistening with juice under warm light. One look and you can taste it.

## How it works

`main.py` (Python 3.13, standard library only, no network) reads the
hero image `asset.png` from the repository root, validates it — a whole
PNG or JPEG, at most 1,048,576 bytes and 1024 by 1024 pixels — and
writes the bytes to `/output/entry.png`.

Run it locally:

```sh
python3 main.py
```

## Files

- `main.py` — the entry program
- `asset.png` — the hero mango photograph (1024x1024, JPEG)
- `prompt.txt` — the entrant's instruction, verbatim
- `LICENSE` — MIT

## License

MIT — see [LICENSE](LICENSE).
