import regex as re

# A regex is simply a pattern used to search, extract, validate, replace, or split text.

text = "My phone number is 9876543210"

result = re.search(r"\d{10}", text)

print(result.group())

#findall() function is used to dispaly teh elemenst taht are matched 

re.findall(r"c.t","cat cot cut c9t")  # . representes any character in Ex. the word starts with c and ends with t 

re.findall(r"[cbr]at", "cat bat rat tat") # [] any one letter inside this as to match with the word 

re.findall(r"[a-z]", "Hello123")  #[a-z] gets all the lowercase letter in output there are more [A-Z](uppercase), [0-9](digits), [a-zA-Z](all letters)

re.findall(r"[^0-9]+", "abc456xyz987") #[^0-9] negetaion: basically anything rather than digits, + used for 1 or more times

re.findall(r"\d+","Age 21, marks 95" ) #\d only digits, + : 1 or more times

re.findall(r"\w+","hello world_123")  #\w for words, +: 1 or more times and words can contain any numbers or letters 

re.findall(r"\s+","hello    world") #\s+ for whitespaces 