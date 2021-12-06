import re
# using match to find the word and use search for looking every part of the str
# string = "is the national animal of india"
# # pattern = "tiger"
# # pattern_2 = "lion"
# # mo = re.match(pattern_2, string)
#
# # print(mo)

# pattern_3 = "is"
# mo_2  = re.match(pattern_3, string)
# print(mo_2)



# getting the indexes by using finditer
string_2 = "is the national animal of india and national sport of turkey"
pattern_4 = "national"
mo_3 = re.finditer(pattern_4, string_2)
for m in mo_3:
    print(m.end())

# working with numbers

string = "ron was born in 12-09-2021 and accepted to school on 15-12-2021"
pattern = "\d{2}-\d{2}-\d{4}"
print(re.findall(pattern, string))
print(re.sub(pattern, "Monday", string))