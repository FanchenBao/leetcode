# from pudb import set_trace; set_trace()
from typing import List, Set
from collections import defaultdict


class Solution1:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """LeetCode 126

        First, create a graph.

        Then, BFS. But for child who are not in the same level as its parent
        and not the grandparent, we also record the path that leads to this
        child. This is because we can have a situation where two paths converge
        into one that leads to the end word. In the generic implementation of
        BFS, only one such path will be handled. Thus, we need to keep a record
        of the existence of the other path, such that once the correct path is
        found, we can backtrack the correct path and see if any additional path
        can lead to one of the nodes in the correct path.

        Finally, we reconstruct all the path based on the completely separate
        paths that lead to end word. For each such separate path, we backtrack
        and add any paths that have diverged somewhere upstream. The important
        trick here is to also backtrack the newly added diverged path. I know
        this doesn't make any sense, so we will just have to read the code and
        understand there.

        I don't know the big O for this. Too complicated. 260 ms, 11% ranking.
        """
        graph = defaultdict(list)
        for i, a in enumerate(wordList):
            for j in range(i + 1, len(wordList)):
                b = wordList[j]
                if sum(le_a != le_b for le_a, le_b in zip(a, b)) == 1:
                    graph[a].append(b)
                    graph[b].append(a)
        if beginWord not in graph:
            for a in wordList:
                if sum(le_a != le_begin for le_a, le_begin in zip(a, beginWord)) == 1:
                    graph[beginWord].append(a)
                    graph[a].append(beginWord)
        # Edge case
        if endWord not in graph:
            return []
        # BFS
        queue = [(beginWord, [beginWord])]
        visited, queue_set = set([beginWord]), set([beginWord])
        res = []
        pot_paths = defaultdict(list)
        while queue and not res:
            temp = []
            temp_set = set()
            for word, path in queue:
                # print(word, path)
                if word == endWord:
                    res.append(path)
                    continue
                if res:
                    continue
                for child in graph[word]:
                    if child not in visited or child == endWord:
                        visited.add(child)
                        temp_set.add(child)
                        temp.append((child, path + [child]))
                    elif child not in queue_set and path[-2] != child:
                        pot_paths[child].append(path)
            queue = temp
            queue_set = temp_set
        if not res:
            return []
        min_length = len(res[0])
        # The starting point in a correct path where we shall start backtrack.
        # Note that for a newly added path, we do not start from the end, but
        # from where the newly addition ends.
        check_start = [min_length - 2] * len(res)
        for i, r in enumerate(res):
            for j in range(check_start[i], -1, -1):
                for pp in pot_paths.get(r[j], []):
                    if len(pp) == j:
                        res.append(pp + r[j:])
                        # add the backtrack starting position for the newly
                        # added path
                        check_start.append(j - 1)
        return res


class Solution2:
    def find_neighbors(self, word: str, words_set: Set[str]) -> Set[str]:
        """O(26K^2) where K is the length of word.
        """
        res = set()
        for i in range(len(word)):
            for j in range(26):
                new = word[:i] + chr(97 + j) + word[i + 1:]
                if new != word and new in words_set:
                    res.add(new)
        return res

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """Official solution.

        https://leetcode.com/problems/word-ladder-ii/solution/

        The idea is to first create a DAG that leads to endWord using BFS. Then
        use DFS to traverse the DAG and find all possible paths.

        O(NK^2 + M), where N is the length of wordList, K is the length of each
        word, and M is the number of paths.

        60 ms, 54% ranking.
        """
        # Build dag using BFS
        dag = defaultdict(set)
        queue, words_set = set([beginWord]), set(wordList)
        if beginWord in words_set:
            words_set.remove(beginWord)
        while queue:
            temp = set()
            for w in queue:
                if w == endWord:
                    dag[w].add('')
                    break
                neighbors = self.find_neighbors(w, words_set)
                temp = temp.union(neighbors)
                dag[w] = dag[w].union(neighbors)
            words_set -= temp  # key step to make sure we do not point backwards
            if endWord in dag:
                break
            queue = temp
        if endWord not in dag:
            return []

        res = []

        # Traverse dag using DFS
        def dfs(word: str, path: List[str]) -> None:
            if word == endWord:
                res.append(path[:])
            else:
                for nei in dag[word]:
                    dfs(nei, path + [nei])

        dfs(beginWord, [beginWord])
        return res


sol = Solution2()
tests = [
    ('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'], [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]),
    ('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log'], []),
    ('cet', 'ism', ['kid', 'tag', 'pup', 'ail', 'tun', 'woo', 'erg', 'luz', 'brr', 'gay', 'sip', 'kay', 'per', 'val', 'mes', 'ohs', 'now', 'boa', 'cet', 'pal', 'bar', 'die', 'war', 'hay', 'eco', 'pub', 'lob', 'rue', 'fry', 'lit', 'rex', 'jan', 'cot', 'bid', 'ali', 'pay', 'col', 'gum', 'ger', 'row', 'won', 'dan', 'rum', 'fad', 'tut', 'sag', 'yip', 'sui', 'ark', 'has', 'zip', 'fez', 'own', 'ump', 'dis', 'ads', 'max', 'jaw', 'out', 'btu', 'ana', 'gap', 'cry', 'led', 'abe', 'box', 'ore', 'pig', 'fie', 'toy', 'fat', 'cal', 'lie', 'noh', 'sew', 'ono', 'tam', 'flu', 'mgm', 'ply', 'awe', 'pry', 'tit', 'tie', 'yet', 'too', 'tax', 'jim', 'san', 'pan', 'map', 'ski', 'ova', 'wed', 'non', 'wac', 'nut', 'why', 'bye', 'lye', 'oct', 'old', 'fin', 'feb', 'chi', 'sap', 'owl', 'log', 'tod', 'dot', 'bow', 'fob', 'for', 'joe', 'ivy', 'fan', 'age', 'fax', 'hip', 'jib', 'mel', 'hus', 'sob', 'ifs', 'tab', 'ara', 'dab', 'jag', 'jar', 'arm', 'lot', 'tom', 'sax', 'tex', 'yum', 'pei', 'wen', 'wry', 'ire', 'irk', 'far', 'mew', 'wit', 'doe', 'gas', 'rte', 'ian', 'pot', 'ask', 'wag', 'hag', 'amy', 'nag', 'ron', 'soy', 'gin', 'don', 'tug', 'fay', 'vic', 'boo', 'nam', 'ave', 'buy', 'sop', 'but', 'orb', 'fen', 'paw', 'his', 'sub', 'bob', 'yea', 'oft', 'inn', 'rod', 'yam', 'pew', 'web', 'hod', 'hun', 'gyp', 'wei', 'wis', 'rob', 'gad', 'pie', 'mon', 'dog', 'bib', 'rub', 'ere', 'dig', 'era', 'cat', 'fox', 'bee', 'mod', 'day', 'apr', 'vie', 'nev', 'jam', 'pam', 'new', 'aye', 'ani', 'and', 'ibm', 'yap', 'can', 'pyx', 'tar', 'kin', 'fog', 'hum', 'pip', 'cup', 'dye', 'lyx', 'jog', 'nun', 'par', 'wan', 'fey', 'bus', 'oak', 'bad', 'ats', 'set', 'qom', 'vat', 'eat', 'pus', 'rev', 'axe', 'ion', 'six', 'ila', 'lao', 'mom', 'mas', 'pro', 'few', 'opt', 'poe', 'art', 'ash', 'oar', 'cap', 'lop', 'may', 'shy', 'rid', 'bat', 'sum', 'rim', 'fee', 'bmw', 'sky', 'maj', 'hue', 'thy', 'ava', 'rap', 'den', 'fla', 'auk', 'cox', 'ibo', 'hey', 'saw', 'vim', 'sec', 'ltd', 'you', 'its', 'tat', 'dew', 'eva', 'tog', 'ram', 'let', 'see', 'zit', 'maw', 'nix', 'ate', 'gig', 'rep', 'owe', 'ind', 'hog', 'eve', 'sam', 'zoo', 'any', 'dow', 'cod', 'bed', 'vet', 'ham', 'sis', 'hex', 'via', 'fir', 'nod', 'mao', 'aug', 'mum', 'hoe', 'bah', 'hal', 'keg', 'hew', 'zed', 'tow', 'gog', 'ass', 'dem', 'who', 'bet', 'gos', 'son', 'ear', 'spy', 'kit', 'boy', 'due', 'sen', 'oaf', 'mix', 'hep', 'fur', 'ada', 'bin', 'nil', 'mia', 'ewe', 'hit', 'fix', 'sad', 'rib', 'eye', 'hop', 'haw', 'wax', 'mid', 'tad', 'ken', 'wad', 'rye', 'pap', 'bog', 'gut', 'ito', 'woe', 'our', 'ado', 'sin', 'mad', 'ray', 'hon', 'roy', 'dip', 'hen', 'iva', 'lug', 'asp', 'hui', 'yak', 'bay', 'poi', 'yep', 'bun', 'try', 'lad', 'elm', 'nat', 'wyo', 'gym', 'dug', 'toe', 'dee', 'wig', 'sly', 'rip', 'geo', 'cog', 'pas', 'zen', 'odd', 'nan', 'lay', 'pod', 'fit', 'hem', 'joy', 'bum', 'rio', 'yon', 'dec', 'leg', 'put', 'sue', 'dim', 'pet', 'yaw', 'nub', 'bit', 'bur', 'sid', 'sun', 'oil', 'red', 'doc', 'moe', 'caw', 'eel', 'dix', 'cub', 'end', 'gem', 'off', 'yew', 'hug', 'pop', 'tub', 'sgt', 'lid', 'pun', 'ton', 'sol', 'din', 'yup', 'jab', 'pea', 'bug', 'gag', 'mil', 'jig', 'hub', 'low', 'did', 'tin', 'get', 'gte', 'sox', 'lei', 'mig', 'fig', 'lon', 'use', 'ban', 'flo', 'nov', 'jut', 'bag', 'mir', 'sty', 'lap', 'two', 'ins', 'con', 'ant', 'net', 'tux', 'ode', 'stu', 'mug', 'cad', 'nap', 'gun', 'fop', 'tot', 'sow', 'sal', 'sic', 'ted', 'wot', 'del', 'imp', 'cob', 'way', 'ann', 'tan', 'mci', 'job', 'wet', 'ism', 'err', 'him', 'all', 'pad', 'hah', 'hie', 'aim', 'ike', 'jed', 'ego', 'mac', 'baa', 'min', 'com', 'ill', 'was', 'cab', 'ago', 'ina', 'big', 'ilk', 'gal', 'tap', 'duh', 'ola', 'ran', 'lab', 'top', 'gob', 'hot', 'ora', 'tia', 'kip', 'han', 'met', 'hut', 'she', 'sac', 'fed', 'goo', 'tee', 'ell', 'not', 'act', 'gil', 'rut', 'ala', 'ape', 'rig', 'cid', 'god', 'duo', 'lin', 'aid', 'gel', 'awl', 'lag', 'elf', 'liz', 'ref', 'aha', 'fib', 'oho', 'tho', 'her', 'nor', 'ace', 'adz', 'fun', 'ned', 'coo', 'win', 'tao', 'coy', 'van', 'man', 'pit', 'guy', 'foe', 'hid', 'mai', 'sup', 'jay', 'hob', 'mow', 'jot', 'are', 'pol', 'arc', 'lax', 'aft', 'alb', 'len', 'air', 'pug', 'pox', 'vow', 'got', 'meg', 'zoe', 'amp', 'ale', 'bud', 'gee', 'pin', 'dun', 'pat', 'ten', 'mob'], [['cet', 'get', 'gee', 'gte', 'ate', 'ats', 'its', 'ito', 'ibo', 'ibm', 'ism'], ['cet', 'cat', 'can', 'ian', 'inn', 'ins', 'its', 'ito', 'ibo', 'ibm', 'ism'], ['cet', 'cot', 'con', 'ion', 'inn', 'ins', 'its', 'ito', 'ibo', 'ibm', 'ism']]),
    ('magic', 'pearl', ['flail', 'halon', 'lexus', 'joint', 'pears', 'slabs', 'lorie', 'lapse', 'wroth', 'yalow', 'swear', 'cavil', 'piety', 'yogis', 'dhaka', 'laxer', 'tatum', 'provo', 'truss', 'tends', 'deana', 'dried', 'hutch', 'basho', 'flyby', 'miler', 'fries', 'floes', 'lingo', 'wider', 'scary', 'marks', 'perry', 'igloo', 'melts', 'lanny', 'satan', 'foamy', 'perks', 'denim', 'plugs', 'cloak', 'cyril', 'women', 'issue', 'rocky', 'marry', 'trash', 'merry', 'topic', 'hicks', 'dicky', 'prado', 'casio', 'lapel', 'diane', 'serer', 'paige', 'parry', 'elope', 'balds', 'dated', 'copra', 'earth', 'marty', 'slake', 'balms', 'daryl', 'loves', 'civet', 'sweat', 'daley', 'touch', 'maria', 'dacca', 'muggy', 'chore', 'felix', 'ogled', 'acids', 'terse', 'cults', 'darla', 'snubs', 'boats', 'recta', 'cohan', 'purse', 'joist', 'grosz', 'sheri', 'steam', 'manic', 'luisa', 'gluts', 'spits', 'boxer', 'abner', 'cooke', 'scowl', 'kenya', 'hasps', 'roger', 'edwin', 'black', 'terns', 'folks', 'demur', 'dingo', 'party', 'brian', 'numbs', 'forgo', 'gunny', 'waled', 'bucks', 'titan', 'ruffs', 'pizza', 'ravel', 'poole', 'suits', 'stoic', 'segre', 'white', 'lemur', 'belts', 'scums', 'parks', 'gusts', 'ozark', 'umped', 'heard', 'lorna', 'emile', 'orbit', 'onset', 'cruet', 'amiss', 'fumed', 'gelds', 'italy', 'rakes', 'loxed', 'kilts', 'mania', 'tombs', 'gaped', 'merge', 'molar', 'smith', 'tangs', 'misty', 'wefts', 'yawns', 'smile', 'scuff', 'width', 'paris', 'coded', 'sodom', 'shits', 'benny', 'pudgy', 'mayer', 'peary', 'curve', 'tulsa', 'ramos', 'thick', 'dogie', 'gourd', 'strop', 'ahmad', 'clove', 'tract', 'calyx', 'maris', 'wants', 'lipid', 'pearl', 'maybe', 'banjo', 'south', 'blend', 'diana', 'lanai', 'waged', 'shari', 'magic', 'duchy', 'decca', 'wried', 'maine', 'nutty', 'turns', 'satyr', 'holds', 'finks', 'twits', 'peaks', 'teems', 'peace', 'melon', 'czars', 'robby', 'tabby', 'shove', 'minty', 'marta', 'dregs', 'lacks', 'casts', 'aruba', 'stall', 'nurse', 'jewry', 'knuth'], [['magic', 'manic', 'mania', 'maria', 'marta', 'marty', 'party', 'parry', 'perry', 'peary', 'pearl'], ['magic', 'manic', 'mania', 'maria', 'maris', 'paris', 'parks', 'perks', 'peaks', 'pears', 'pearl'], ['magic', 'manic', 'mania', 'maria', 'marta', 'marty', 'marry', 'merry', 'perry', 'peary', 'pearl'], ['magic', 'manic', 'mania', 'maria', 'marta', 'marty', 'marry', 'parry', 'perry', 'peary', 'pearl'], ['magic', 'manic', 'mania', 'maria', 'maris', 'marks', 'parks', 'perks', 'peaks', 'pears', 'pearl']]),
]

for i, (beginWord, endWord, wordList, ans) in enumerate(tests):
    res = sol.findLadders(beginWord, endWord, wordList)
    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail.')
        print('Ans:')
        for a in sorted(ans):
            print(a)
        print('Res:')
        for r in sorted(res):
            print(r)
