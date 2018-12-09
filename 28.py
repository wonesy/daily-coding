'''
Write an algorithm to justify text. 
Given a sequence of words and an integer line length k, 
return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. 
There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. 
Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] 
and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly

'''

def justify(words:list, char_len:int, max:int):
    num_words = len(words)

    if char_len == max:
        if num_words == 1:
            return words[0]
        raise ValueError('Too many words for this line, need room for spaces')

    spaces = max - char_len
    if num_words == 1:
        return '{message: <{fill}}'.format(message=' ', fill=str(spaces))

    # determine how many spaces are required
    num_gaps = len(words) - 1

    min_gap_size = int(spaces/num_gaps)
    gaps = [min_gap_size]*num_gaps  # initialize list

    spaces -= min_gap_size*num_gaps
    for i in range(len(gaps)):
        if not spaces:
            break
        gaps[i] += 1
        spaces -= 1

    # merge lists
    line = words[0]
    for i,w in enumerate(words[1:]):
        line += '{space: <{fill}}{msg}'.format(space=' ', fill=str(gaps[i]), msg=w)

    return line


def work(words:list, k:int):
    output = []
    justified_line_len = 0
    words_used = 0
    beginning_idx = 0
    for i,word in enumerate(words):
        # if we surpass the max line length, call a justify
        if justified_line_len + len(word) + words_used <= k:
            words_used += 1
            justified_line_len += len(word)

            if i == len(words) - 1:
                output.append(justify(words[beginning_idx:], justified_line_len, k))

        else:
            output.append(justify(words[beginning_idx:i], justified_line_len, k))
            beginning_idx = i
            words_used = 1
            justified_line_len = len(word)

    return output

ex = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 16

print(work(ex, k))