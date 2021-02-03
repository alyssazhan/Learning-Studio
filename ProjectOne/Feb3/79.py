class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        for r in range(rows):
            for c in range(cols):
                if self.dfs(board,r,c,word):
                    return True
        return False

    def dfs(self, board, r, c,word):
        if len(word)==0:
            return True
        if r<0 or r>len(board)-1 or c<0 or c>len(board[0])-1 or board[r][c]!=word[0]:
            return False
        temp=board[r][c]
        board[r][c]="#"
        res=self.dfs(board, r+1, c, word[1:]) or self.dfs(board, r-1, c, word[1:]) or self.dfs(board, r, c+1, word[1:]) or self.dfs(board, r, c-1, word[1:])
        board[r][c]=temp
        return res
