def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if(len(dna1)>len(dna2)):
            return True
    return False


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count = 0
    for char in dna:
        if(char==nucleotide):
            count+=1
    return count;

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """
    if(dna2 in dna1):
        return True;
    else:
        return False;
def is_valid_sequence(dna):
    sequence=[ 'A', 'T', 'C', 'G' ]
    count=0
    if dna:
        for char in dna:
            if not char in sequence:
                count+=1
        return False if count>0 else True
    if dna=='':
        return True
    
        
def insert_sequence(dna1,dna2,index):
    """(str,str,int)->str
    Return the new string with insertion of dna2 string.
    >>>insert_sequence('CCGG','AT',2)
    'CCATGG'
    """
    return dna1[:index]+dna2+ dna1[index:];

def get_complement(nucleotide):
    for char in nucleotide:
        if char == "A":
            return "T"
        if char == "C":
            return "G"
        if char =="T":
            return "A"
        if char =="G":
            return "C"

def get_complementary_sequence(dna): 
    """Return the complementary sequence string.""" 
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
    letters = list(dna) 
    letters = [basecomplement[base] for base in letters] 
    return ''.join(letters) 
        

