from password_hash import simple_hash
HASH_CODE = 81445731
HASH_SIZE = 10**9

def crack_hash(permutations,words):
   if permutations == 1:
      return words
   else:
      return [ 
         y + x
         for y in crack_hash(1, words)
         for x in crack_hash(permutations - 1, words)
      ]
def main():
   lines = []
   file = open("dictionary.txt","r")
   for line in file:
      lines.append(line.strip("\n"))
   for i in range(1,5):
      for word in crack_hash(i, lines):
         if simple_hash(word, HASH_SIZE) == HASH_CODE:
            print(word)

main()