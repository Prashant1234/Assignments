def count_vowels(word):
    ''' (str)-> int

    Return the number of vowels
    >>>count_vowels('hello')
    2
    >>>count_vowels('print')
    1
    '''
    return count_vowels(word)

def count_consonants(word):
        '''(str)-> int

    Return the number of consonents
    >>>count_consonents('hello')
    3
    >>>count_consonents('print')
    4
    '''
        return count_consonants(word)
    
def count_letters(word):
    '''(str) -> int

    Return the number of letters in word.
    >>> count_letters('hello')
    5
    >>> count_letters('bonjour')
    7
    '''
    return count_vowels(word) + count_consonants(word)
        
