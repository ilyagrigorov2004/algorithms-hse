def group_anagrams(strs: list):
    d = {}
    for i in range(len(strs)):
        key = ''.join(sorted(strs[i]))
        if key in d:
            d[key].append(strs[i])
        else:
            d[key] = [strs[i]]
    return list(d.values())

#print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
