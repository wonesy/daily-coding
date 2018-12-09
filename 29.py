'''
Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a single count and character. 
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. 
You can assume the string to be encoded have no digits and consists solely of alphabetic characters. 
You can assume the string to be decoded is valid.
'''

def enc(msg:str):
    encoded_msg = ""
    trail_marker = msg[0]
    count = 1

    for c in msg[1:]:
        if c == trail_marker:
            count += 1
        else:
            encoded_msg += f'{count}{trail_marker}'
            trail_marker = c
            count = 1
    
    # there will always be that last one
    encoded_msg += f'{count}{trail_marker}'
    return encoded_msg


def dec(msg:str):
    decoded_msg = ""
    for i,c in enumerate(msg):
        if not c.isdigit():
            continue
        count = c
        character = msg[i+1]

        decoded_msg += (f'{character}'*int(count))
    return decoded_msg

example_encoded = "4A3B2C1D2A"
example_decoded = "AAAABBBCCDAA"

print(enc(example_decoded))
print(dec(example_encoded))


test = "liuhaewfrlnhhhhdddkdlkwennnnnvvvvllpspeoooeoo"
print(enc(test))
assert(dec(enc(test)) == test)