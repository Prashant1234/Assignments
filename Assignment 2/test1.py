def is_longer(dna1, dna2):
    for char in dna1:
        if char in dna2:
            return True
     return False
