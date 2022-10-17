starts = ["∁α","αx","⤐","⫝","α⇂","ȡ","ȅ","⌢","ʌ"]
middles = ["lα","τlo","☼","αlα","loβ","ƿ"]
ends = ["βlαβ","loβ","⭉","τlγ","τlo","l϶","ϵf"]
import random

words_to_be_genned = []
def new_word():
    return random.choice(starts)+random.choice(middles)+random.choice(ends)
with open("New_Words.txt","w") as t:
    for i in words_to_be_genned:
        t.write("{} -> ".format(i))
        t.write(new_word()+"\n")