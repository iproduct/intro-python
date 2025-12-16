class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.wordEnd = False
    def __str__(self):
        data = ' '.join([f"{chr(ord('a') + i)}{str(self.child[i])}"
                  for i in range(len(self.child)) if self.child[i] is not None])
        if len(data) > 0:
            return '[' + data + ']'
        return ''


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __str__(self):
        return str(self.root)

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

if __name__ == '__main__':
    words = ['and', 'ant', 'do', 'geek', 'dad', 'ball']
    trie = Trie()
    for word in words:
        trie.insert(word)
    print(trie)

    search_keys = ['do', 'gee', 'bat', 'ball']
    for word in search_keys:
        print(word, ' --> ', trie.search(word))