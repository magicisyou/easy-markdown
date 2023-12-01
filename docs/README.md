# Easy Markdown

Markdown viewer and editor

Easy markdown is a free and open source markdown editor and viewer.

![screenshot dark](/docs/screenshot1.webp)
![screenshot light](/docs/screenshot2.webp)

## To run the app

Install dependencies

```
pip install -r requirements.txt
```
Run
```
flet run main.py
```
## Build on local sytem
Install dependencies
```
pip install -r requirements.txt
```

Build

```
flet pack main.py --icon assets/icon.png --name easymarkdown --add-data "assets:assets"
```
The binary will be placed on the dist directory