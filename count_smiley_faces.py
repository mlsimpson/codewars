# https://www.codewars.com/kata/583203e6eb35d7980400002a/solutions/python

import re

def count_smileys(arr):
    if not arr:
        return 0

    regex_count = 0
    re_obj = re.compile(r'[:;][-~]?[)D]')

    for smiley in arr:
        # if re.search(re_obj, smiley):
        if re_obj.match(smiley):
            regex_count += 1

    return regex_count


print(count_smileys([':)', ';(', ';}', ':-D']))
