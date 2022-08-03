## 2022-04-29 

Looking at hashing functions, had a bit of a problem working with PIL, ended up using the anaconda version of python:
> /Users/devian/opt/anaconda3/bin/python3 quick_hash.py ../images/osx-export-3/IMG_1670.JPG
../images/osx-export-3/IMG_1670.JPG
0708140c7efeffcf
492f7b20fd4f4e40308ae31f53e41ff4 


## 2022-04-28 

Experimented with a few ways to export photos from an OSX image album. 

osxphotos export --album test-osx-export --exiftool  .
osxphotos export --album test-osx-export . --sidecar XMP
osxphotos export --album test-osx-export .

