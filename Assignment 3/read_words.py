def read_words(words_file):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """
    f = open("wordlist1.txt", "r")
    #x=f.readline()
    #while x!='':
     #   print (x,end='')
      #  x=f.readline()
    x=f.readline().strip('\n')
    while x!='':
        print(x,end='')
        x=f.readline().strip('\n')
