
#how to use:

0. put the 'modify_creatives.py' file into the main folder of your creative pack (e. g. \bigbox_2020-06-01). Open the folder with a text editor. The exaple code after "#YOUR CODE HERE" can be replaced with your own.
1. create a pattern you want to replace using regex(good site for writing and testing regex: https://regexr.com/). Split the pattern in 3 capturing groups using () symbols. Second capturing group should contain the value which will be modified. 
2. define a transformation function. It should take the input from the second capturing group in the pattern, modify it, and return the result.
3. call the modifyCreatives() function. This function takes the following parameters:
    * **pattern** string containing a regular expression, with three capturing groups.
    * **transformation** function with a single argument
    * **filename** *(optional)* *Default: 'settings.json'*. String with name of the file which will be searched and modified in every subfolder. Most likely either 'settings.json' or 'css\style.css'. 
    * **test** *(optional)* *Default: False*. Boolean which enables testing. If True, old and new values are logged in the console, but no actual replacement occurs. If False, files are overwritten.

The program should be run from the main pack directory (e. g. '\bigbox_2020-06-01').

#examples

Code from examples should be inserted after "#YOUR CODE HERE" in the python file.
Examples are in test mode, remove the "True" argument from modifyCreatives() and run to save the changes.

## make '.offer-enlarger-name > p span' font-size bigger by 30%
```python
# patterns to find in all [filename] files - second capturing group will be replaced with new number 
query1 = '(.offer-enlarger-name\s*>\s*p\s*span\s*{[\n]?\s*font-size:\s*)(\d\d?)(px)'
# transformations to be applied to the number
def transformation1(number):
    return round(number*1.3)
#function call
modifyCreatives(query1, transformation1, 'css\style.css', True)
```

## make logo container bigger by 15%
```python
# patterns to find in all [filename] files - second capturing group will be replaced with new number 
# this regex matches if number is less than 100
query1 = '(\"ALLOFFERS_CONTAINER_HEIGHT\": \")(\d\d(?:.\d)*)(%\")'
query2 = '(\"ALLOFFERS_CONTAINER_WIDTH\": \")(\d\d(?:.\d)*)(%\")'
query3 = '(\"LOGO_CONTAINER_HEIGHT\": \")(\d\d(?:.\d)*)(%\")'
query4 = '(\"LOGO_CONTAINER_WIDTH\": \")(\d\d(?:.\d)*)(%\")'
# transformations to be applied to the number
def transformation1(number):
    return max(round(100 - ( (100-number)*1.15 )), 0)
def transformation2(number):
    return min(round(number*1.15), 100)
#function call
modifyCreatives(query1, transformation1, test=True)
modifyCreatives(query2, transformation1, test=True)
modifyCreatives(query3, transformation2, test=True)
modifyCreatives(query4, transformation2, test=True)
```