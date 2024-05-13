'''Given a paragraph count number of words, sentences. Every sentence ends with either . or ? or !
Print Count of how many normal sentences ending with . , how many interrogative sentences ( ending
with ?) and how many exclamatory sentences ( ending with !).
Ex.
Input : “I am at CDAC. What about you? I am surprised by current weather!”
'''

def find_stop(input):
  start=0
  end=len(input)
  count=0
  for i in range(0,end):
    idx=input.find(".",start,end)
    if idx!=-1:
      count+=1
      start=idx+1
  print(count)

def find_interrogative(input):
  start=0
  end=len(input)
  count=0
  for i in range(0,end):
    idx=input.find("!",start,end)
    if idx!=-1:
      count+=1
      start=idx+1
  print(count)

def find_exclamatory(input):
  start=0
  end=len(input)
  count=0
  for i in range(0,end):
    idx=input.find("?",start,end)
    if idx!=-1:
      count+=1
      start=idx+1
  print(count)

def count_sentence(input):
    print("Normal sentence:",end=" ")
    find_stop(input)

    print("Interrogative:",end=" ")
    find_exclamatory(input)

    print("Exclamatory:",end=" ")
    find_interrogative(input)
  
input="I am at CDAC. What? about you?! I am surprised by current weather!"
count_sentence(input)


