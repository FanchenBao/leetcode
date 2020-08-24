# from pudb import set_trace; set_trace()
from typing import List
from collections import deque, defaultdict


class StreamChecker1:
    """Naive approach.

    Hit time limit.
    """

    def __init__(self, words: List[str]):
        self.words = words
        self.letters, self.first_letter, self.single_letter_words = self.prep()
        self.word_idx = deque()
        self.letter_idx = deque()

    def prep(self):
        letters = set()
        first_letter = defaultdict(list)
        single_letter_words = set()
        for i, word in enumerate(self.words):
            letters = letters.union(set(word))
            if len(word) == 1:
                single_letter_words.add(word)
            else:
                first_letter[word[0]].append(i)
        return letters, first_letter, single_letter_words

    def check_first_letter(self, letter: str) -> bool:
        res = False
        if letter in self.single_letter_words:
            res = True
        if letter in self.first_letter:
            self.word_idx.append(self.first_letter[letter])
            self.letter_idx.append(0)
        return res

    def check_non_first_letter(self, letter: str) -> bool:
        if not self.word_idx:
            return False
        res = False
        for _ in range(len(self.word_idx)):
            word_indices = self.word_idx.popleft()
            letter_index = self.letter_idx.popleft()
            temp = []
            for i in word_indices:
                word = self.words[i]
                if word[letter_index + 1] == letter:
                    if letter_index + 1 == len(word) - 1:  # full match
                        res = True
                    else:
                        temp.append(i)
            if temp:
                self.word_idx.append(temp)
                self.letter_idx.append(letter_index + 1)
        return res

    def query(self, letter: str) -> bool:
        if letter not in self.letters:
            return False
        res1 = self.check_non_first_letter(letter)
        res2 = self.check_first_letter(letter)
        return res1 or res2


class StreamChecker2:
    """Pass OJ with 3100 ms

    We keep a record of all the words that end with a specific letter. We also
    keep the stream itself. Then for each new query, we look for all the words
    that end with the newly queried letter, and compare whether any word
    matches the last portion of the stream of the same length.
    """

    def __init__(self, words: List[str]):
        self.words = words
        self.stream = ''
        self.letters, self.end_letter = self.prep()

    def prep(self):
        letters = set()
        end_letter = defaultdict(list)
        for i, word in enumerate(self.words):
            letters = letters.union(set(word))
            end_letter[word[-1]].append(i)
        return letters, end_letter

    def query(self, letter: str) -> bool:
        self.stream += letter
        if letter not in self.letters:
            return False
        for i in self.end_letter.get(letter, []):
            if self.stream[-len(self.words[i]):] == self.words[i]:
                return True
        return False


class TrieNode:

    def __init__(self):
        self.is_word = False
        self.next = {}


class StreamChecker3:
    """Use a trie, but build it for each work in reversed fashion."""

    def __init__(self, words: List[str]):
        self.trie = self.build_trie(words)
        self.stream = ''

    def build_trie(self, words):
        root = TrieNode()
        for w in words:
            node = root
            for le in reversed(w):
                if le not in node.next:
                    node.next[le] = TrieNode()
                node = node.next[le]
            node.is_word = True
        return root

    def query(self, letter: str) -> bool:
        self.stream += letter
        node = self.trie
        for le in reversed(self.stream):
            if le in node.next:
                node = node.next[le]
                if node.is_word:
                    break
            else:
                break
        return node.is_word


words = ["ab", "ba", "aaab", "abab", "baa"]
sol = StreamChecker2(words)
sol.query('a')
sol.query('a')
sol.query('a')
sol.query('a')
sol.query('a')
sol.query('b')
sol.query('a')
sol.query('b')
sol.query('a')
sol.query('b')
