with open("story.txt", "r") as f:
    story = f.read()

words = []
start_of_word = 1

target_start = "<"
target_end =">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.append(word)
        start_of_word = -1

#print(words)
for word in words:
   print(word)

answers = {}

for word in words:
    answer = input("Enter a random word instead of "+word+" : ")
    answers[word] = answer
"""
    if len(answers) == 3: #fass answers{} 3 Elemente hat: stop
        break

print(answers) 
"""
for word in words:
    #story.replace(word, answers[word])
    story = story.replace(word, answers[word])

print(story) 
