starts = ["∁α","αx","⤐","⫝","α⇂","ȡ","ȅ","⌢","ʌ"]
middles = ["lα","τlo","☼","αlα","loβ","ƿ"]
ends = ["βlαβ","loβ","⭉","τlγ","τlo","l϶","ϵf"]
import random

words_to_be_genned = ["Pog"]
def new_word():
    i = random.choice([0,0,0,0,1,1,1,2,2,2,3])
    if i == 0:
        return random.choice(starts)+random.choice(middles)+random.choice(ends)
    elif i == 1:
        return random.choice(starts)+random.choice(starts)+random.choice(middles)+random.choice(ends)
    elif i == 2:
        return random.choice(starts)+random.choice(starts)+random.choice(middles)+random.choice(middles)+random.choice(ends)
    else:
        return random.choice(starts)+random.choice(starts)+random.choice(middles)+random.choice(middles)+random.choice(ends)+random.choice(ends)
with open("New_Words.txt","w") as t:
    for i in words_to_be_genned:
        t.write("{} -> ".format(i))
        t.write(new_word()+"\n")
