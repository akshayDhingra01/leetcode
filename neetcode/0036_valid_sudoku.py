# https://leetcode.com/problems/valid-sudoku/

# first Approach Time o(n2) Space o(n) Line of code  124

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_map_value( dict_number):
            for key, value in dict_number.items():
                if value < 0:
                    return False
            return True

        number_dict = {
            "1":1 , "2":1, '3':1, "4":1, '5':1, '6':1, '7':1, '8':1, '9':1
        }

        for first in range(9):
            dup_map = number_dict.copy()
            for second in range(9):
                if board[first][second] != '.':
                    dup_map[board[first][second]] -= 1
            if not check_map_value(dup_map):
                return False
            
        for first in range(9):
            dup_map_2 = number_dict.copy()
            for second in range(9):
                if board[second][first] != '.':
                    dup_map_2[board[second][first]] -= 1
            if not check_map_value(dup_map_2):
                return False




        dup_map_3 = number_dict.copy()
        dup_map_4 = number_dict.copy()
        dup_map_5 = number_dict.copy()

        for first in range(3):
            for second in range(3):
                if board[first][second] != '.':
                    dup_map_3[board[first][second]] -= 1

            for second in range(3,6):
                if board[first][second] != '.':
                    dup_map_4[board[first][second]] -= 1

            for second in range(6,9):
                if board[first][second] != '.':
                    dup_map_5[board[first][second]] -= 1

        if not check_map_value(dup_map_3):
            return False

        if not check_map_value(dup_map_4):
            return False

        if not check_map_value(dup_map_5):
            return False



        dup_map_3 = number_dict.copy()
        dup_map_4 = number_dict.copy()
        dup_map_5 = number_dict.copy()

        for first in range(3,6):
            for second in range(3):
                if board[first][second] != '.':
                    dup_map_3[board[first][second]] -= 1

            for second in range(3,6):

                if board[first][second] != '.':
                    dup_map_4[board[first][second]] -= 1

            for second in range(6,9):
                if board[first][second] != '.':
                    dup_map_5[board[first][second]] -= 1

        if not check_map_value(dup_map_3):
            return False

        if not check_map_value(dup_map_4):
            return False

        if not check_map_value(dup_map_5):
            return False


        dup_map_3 = number_dict.copy()
        dup_map_4 = number_dict.copy()
        dup_map_5 = number_dict.copy()

        for first in range(6,9):
            for second in range(3):
                if board[first][second] != '.':
                    dup_map_3[board[first][second]] -= 1

            for second in range(3,6):
                if board[first][second] != '.':
                    dup_map_4[board[first][second]] -= 1

            for second in range(6,9):
                if board[first][second] != '.':
                    dup_map_5[board[first][second]] -= 1

        if not check_map_value(dup_map_3):
            return False

        if not check_map_value(dup_map_4):
            return False

        if not check_map_value(dup_map_5):
            return False



        return True
