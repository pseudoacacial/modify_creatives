import os
import re

subfolders = [ f.path for f in os.scandir() if f.is_dir() ]

# replaces text in a [file] that matches a regex [pattern] and  applies [transformation] on second capturing group in [pattern]
def replaceText(file, pattern, transformation, test):
    with open(file, 'r', encoding='utf-8') as f:
        file_content = f.read()
        search = re.search(pattern, file_content)
        if(search):
            number = float(search.group(2))
            new_number = transformation(number)
            replacement = search.group(1) + str(new_number) + search.group(3);
            print(search.group(), "-->", replacement)
            
            if not test:
                x = re.sub(pattern,replacement,file_content) 
                f = open(file, "w")
                f.write(x)
                f.close()

# applies [transformation] on every occurence of [pattern] in [filename] files for all subfolders
def modifyCreatives(pattern, transformation, filename='settings.json', test=False):
    for folder in subfolders:
        file_exists = os.path.exists(folder+'\\'+filename)
        if file_exists:
            replaceText(folder+'\\' + filename, pattern, transformation, test)
    print("finished replacing", pattern)
    if test: print("Test mode active, no files have been changed.")
    if not test: print("FILES MODIFIED")

#YOUR CODE HERE

# patterns to find in all [filename] files - second capturing group will be replaced with new number           
query1 = '(.offer-enlarger-name\s*>\s*p\s*span\s*{[\n]?\s*font-size:\s*)(\d\d?)(px)'
# transformations to be applied to the number
def transformation1(number):
    return round(number*1.3)
#function call
modifyCreatives(query1, transformation1, 'css\style.css', test=True)