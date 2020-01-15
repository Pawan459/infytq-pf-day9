# "99 Bottles of Beer" is a traditional song in the United States and Canada. 
# It is popular to sing this song during long trips, as it has a repetitive 
# format which is easy to memorize, and takes a long time to sing.
# The song's simple lyrics are as follows:
# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down, pass it around, 98 bottles of beer on the wall.

# The same verse is repeated, each time with one fewer bottle. 
# The song is completed when the singer or singers reach zero.
# Write a python function to generate all the verses of the song.

#PF-Tryout


def sing_99_bottles():
   #start writing your code here
   for i in range(99, 0, -1):
       print('{} bottles of beer on the wall, {} bottles of beer.\nTake one down, pass it around, {} bottles of beer on the wall.'.format(i,i,i-1))


sing_99_bottles()
