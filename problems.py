# Problem 1:  6 kyu Back and forth then Reverse!

def arrange(s):
    left = 0
    right = -1
    t = []
    while len(t) < len(s):
        t.append(s[left])
        t.append(s[right])
        if left > right:
            left, right = right -1, left + 1
        else:
            left, right = right +1, left -1
    if len(t) > len(s):
        t.pop()
    return t

#linear time complexity.

# Problem 2: 7 kyu The Office I - Outed

def outed(meet, boss):

    tot_score = 0
    num_pep = 0 
    for pers in meet:
        num_pep += 1
        if pers == boss:
            tot_score += meet[pers]*2
        else:
            tot_score +=meet[pers]
    office = tot_score/num_pep
    
    if office <=5:
        return 'Get Out Now!'
    else:
        return 'Nice Work Champ!'
    
#linear time complexity.

# Problem 3:8 kyu Did she say hallo?
def validate_hello(greetings):
    valid_hellos = ('hello','ciao','salut','hallo','hola','ahoj','czesc')
    for words in valid_hellos:
        if words in greetings.lower():
            return True
    return False

#linear time complexity 