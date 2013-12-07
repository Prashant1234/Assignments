def is_valid_word(wordlist, word):
    ''' (list of str, str) -> bool
    Return True if and only if word is an element of wordlist.
    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    '''
    i = ''
    for i in wordlist:
      return word in wordlist
def make_str_from_row(board, row_index):
    ''' (list of list of str, int) -> str
    Return the characters from the row of the board with index row_index
    as a single string.
    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    '''
    a = ''
    i = ''
    for i in board:
        a = board[row_index]
        return ''.join(a)
def make_str_from_column(board, column_index):
    ''' (list of list of str, int) -> str
    Return the characters from the column of the board with index column_index
    as a single string.
    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    '''
    #a = ''
    #for i in board:
    #    a = board[i][column_index] + board[i + 1][column_index]
    #    return ''.join(a)
    L = board
    total = ''
    for index in range(len(L)):
        b = board[index][column_index]
        total = total + b
    return total
def board_contains_word_in_row(board, word):
    ''' (list of list of str, str) -> bool
    Return True if and only if one or more of the rows of the board contains
    word.
    Precondition: board has at least one row and one column, and word is a
    valid word.
    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    '''
    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True
    return False
def board_contains_word_in_column(board, word):
    ''' (list of list of str, str) -> bool
    Return True if and only if one or more of the columns of the board
    contains word.
    Precondition: board has at least one row and one column, and word is a
    valid word.
    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    '''
    for column_index in range(len(board)):
        if word in make_str_from_column(board, column_index):
            return True
    return False
def board_contains_word(board, word):
    '''(list of list of str, str) -> bool
    Return True if and only if word appears in board.
    Precondition: board has at least one row and one column.
    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    '''
    a = ''
    for word in range(len(board)):
        if a in make_str_from_row(board, word):
            return True
    return False
def word_score(word):
    '''(str) -> int
    Return the point value the word earns.
    Word length: < 3: 0 points
                 3-6: 1 point per character in word
                 7-9: 2 points per character in word
                 10+: 3 points per character in word
    >>> word_score('DRUDGERY')
    16
    '''
    points = 0
    i = 0
    if len(word) <= 2:
        return 0
    elif len(word) <= 6:
        points = len(word) * 1
        return points
    elif len(word) <= 9:
        points = len(word) * 2
        return points
    elif len(word) >= 10:
        points = len(word) * 3
        return points
def update_score(player_info, word):
    '''([str, int] list, str) -> NoneType
    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.
    >>> update_score(['Jonathan', 4], 'ANT')
    '''
    player_info[1] += word_score(word)
def num_words_on_board(board, words):
    '''(list of list of str, list of str) -> int
    Return how many words appear on board.
    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    '''
    num = 0
    for i in range(len(board)):
        if board_contains_word(board, words) == True:
            num = num + 1
            return num
def read_words(words_file):
    ''' (file open for reading) -> list of str
    Return a list of all words (with newlines removed) from open file
    words_file.
    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    '''
    #words_file = open('C:/Users/diske/Desktop/words_file.txt', 'r')
    #words_file2 = [item.rstrip() for item in words_file]
    #print(words_file2)
    #words_file = askopenfile(mode='r', title='Select word list file')
    #words = a3.read_words(words_file)
    words_file2 = [item.rstrip() for item in words_file]
    return words_file2
def read_board(board_file):
    ''' (file open for reading) -> list of list of str
    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    '''
    #words_file = askopenfile(mode='r', title='Select word list file')
    #words = a3.read_words(words_file)
    #board_file = open('C:/Users/diske/Desktop/board_file.txt', 'r')
    board_file2 = [item.rstrip('\n') for item in board_file]
    print(board_file2)
    line = board_file.readline()
