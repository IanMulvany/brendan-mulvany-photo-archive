
## 2024-08-17
Having some success using aider - the llm powered support tool for coding. 
Also noticed that there is no good documentation about my overall thinking and approach about what I am aiming to do. 


## 2023-12-24 
Retrobatch-2 is definitly the image processing engine that I should use for most of the image processing:
https://flyingmeat.com/retrobatch/

I did a quick test to convert files in 
/Users/devian/Documents/code/brendan-mulvany-photo-archive/images/test_negatives

to 
/Users/devian/Documents/code/brendan-mulvany-photo-archive/images/test-retrobatch-write

and it worked perfectly. 

It can also support clasfficaiton, and intergartion with scripts.

Scripting documentation
https://flyingmeat.com/retrobatch/docs-2.0/shellscripts/

Documentation for classificaiton:
https://flyingmeat.com/retrobatch/docs-2.0/classification/
Can be comgined with the Rules node, and can be used to filter out specific classifications, will need some time to work out what I want to do. 

CoreML models from Apple are available here:
https://developer.apple.com/machine-learning/models/ 

## 2023-06-19 

https://photoswipe.com/getting-started/ could be useful for creating the online image library when I get around to doing that. 


## 2022-08-07 


lots of progress with the help of co-pilot, now have working MD in datasette. 

Am trying out how to get image views in datasetts. 
I tried https://github.com/kracekumar/datasette-render-local-images, but it made datasette return an error, so I am dropping this. 
I'm going to try having a look at https://simonwillison.net/2020/Jul/30/fun-binary-data-and-sqlite/ and https://datasette.io/plugins/datasette-media 

This shows how to render customer templates that allow you to view images:
https://datasette.io/tools/dogsheep-photos

This shows you how to input blob data: 

And this shows you how to configre the media plugin to show media:
https://simonwillison.net/2020/Jul/30/fun-binary-data-and-sqlite/

Some other changes 

- now have the repo using conda env, use:

$ conda activate bm_archive 

- now have a set of scripts for creating the sqlitedb 
- am liberally using sqlite-utils for update the schema, and experimeting with images and blobs. 



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

