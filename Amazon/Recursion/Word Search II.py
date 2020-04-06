"""
URL : https://leetcode.com/explore/interview/card/amazon/84/recursion/2990/
"""


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        WORD_KEY = '$'

        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word

        row_num = len(board)
        col_num = len(board[0])

        matched_words = []

        def backtracking(row, col, parent):
            letter = board[row][col]
            current_node = parent[letter]

            word_match = current_node.pop(WORD_KEY, False)

            if word_match:
                matched_words.append(word_match)

            board[row][col] = '#'

            for (row_offset, col_offset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_row, new_col = row + row_offset, col + col_offset

                if new_row < 0 or new_row >= row_num or new_col < 0 or new_col >= col_num:
                    continue
                if not board[new_row][new_col] in current_node:
                    continue
                backtracking(new_row, new_col, current_node)

            board[row][col] = letter

            if not current_node:
                parent.pop(letter)

        for row in range(row_num):
            for col in range(col_num):
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matched_words


board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
print(Solution().findWords(board, words))