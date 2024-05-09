def longest_substring(s):
    longest = ''
    current = ''
    for c in s:
            if current == '' or c >= current[-1]:
                current += c
            else:
                current = c
            longest = max(current, longest, key=len)
    return longest
print(longest_substring("abdualrahman"))