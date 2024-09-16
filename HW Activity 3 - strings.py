song = """When an eel grabs your arm,\n... And it causes great harm,\n... That's - a moray!"""
song = song.replace(" m", " M")
print(song)

questions = ["We don't serve strings around here. Are you a string?","What is said on Father's Day in the forest?","What makes the sound 'Sis! Boom! Bah!'?"]
answers = ["An exploding sheep.","No, I'm a frayed knot.","'Pop!' goes the weasel."]
q_a = ((0,1),(2,0),(1,2))
for q,a in q_a:
    print("Q:",questions[q])
    print("A",answers[a])
    print()  # This is for print space

poem = '''... My kitty cat likes %s,\n... My kitty cat likes %s,\n... My kitty cat fell on his %s\n... And now thinks he's a %s....'''
args = ('roast beef', 'ham', 'head', 'clam')
print(poem % args)
