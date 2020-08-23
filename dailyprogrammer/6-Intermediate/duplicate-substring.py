#!/usr/bin/env python3

import re

# This looks for a sequence of 1 or more arbitrary characters (.+?) (as a non-greedy match, so that it tries
# shorter sequences first), followed by 1 or more repetitions of the matched sequence \1+, and replaces it
# all with just the matched sequence \1.

lst = ['aaatestBlaBlatestBlaBla', 'aaathisBlaBlathisBlaBla', 'aaathatBlaBlathatBlaBla', 'aaagoodBlaBlagoodBlaBla',
       'aaagood1BlaBla123good1BlaBla123']

for item in lst:
    print(re.sub(r"(.+?)\1+", r"\1", item))
