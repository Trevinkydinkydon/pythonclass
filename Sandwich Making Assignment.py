def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)
      
      
def animal_crackers(text):
    words = text.split()
    return words[0][0].lower() == words[1][0].lower()

  
def makes_twenty(n1, n2):
    if n1 == 20 or n2 == 20 or n1 + n2 == 20:
        return True
    else:
        return False
