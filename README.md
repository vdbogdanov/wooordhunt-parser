# wooordhunt-translate-parser

This program allows you to get the translation and transcription of various words in English using [wooordhunt.ru](https://wooordhunt.ru) website.

```
INPUT:
rug
sniff
shone
altered

OUTPUT:
rug |rʌɡ| ковер, коврик, плед, меховая полость, тащить с усилием
sniff |snɪf| нюхать, вдыхать, фыркать, сопеть, чуять, сопение, вдох, фырканье, хмыканье
shone |ʃɒn| светить, светиться, сиять, блистать, блестеть, отсвечивать, чистить, придавать блеск
altered |ˈɔːltəd| изменять, изменяться, менять, меняться, переделывать, вносить изменения, перешить
```

## Getting Started

Clone the repository:

```bash
git clone https://github.com/dallings/wooordhunt-parser.git
```

Install requirements:

```bash
pip install -r requirements.txt
```

## Usage

First, specify the words in the file `/src/words.txt` in a column, the transcription and translation of which you need to get. Then run python script:

```bash
python wooordhunt_parser.py
```

then the output of the execution result will be displayed in the file `/src/readywords.txt`