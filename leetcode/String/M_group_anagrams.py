'''
["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"] ->
[
  ["yo", "oy"],
  ["act", "tac", "cat"],
  ["flop", "olfp"],
  ["foo"]
]
'''

def groupAnagrams(words):
    sorted_words = {}
    for word in words:
        sw = ''.join(sorted(word))
        sorted_words[sw] = sorted_words.get(sw,[])+[word]
    return list(sorted_words.values())