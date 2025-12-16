class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.wordEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            letter_index = ord(letter) - ord('a')
            if current.child[letter_index] is None:
                current.child[ord(letter) - ord('a')] = TrieNode()
            current = current.child[letter_index]
        current.wordEnd = True

    def search(self, word):
        current = self.root
        for letter in word:
            letter_index = ord(letter) - ord('a')
            if current.child[letter_index] is None:
                return False
            current = current.child[letter_index]
        return current.wordEnd

