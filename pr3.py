from timeit import default_timer as timer
import sys
#
# Music Streaming Application
#
# This class is used to store one node in the linked list.
# A node has a song's title and three pointers to other nodes.

class Song:
    def __init__(self, title):
        self.title = title
        self.nextInOrigOrder = None # pointer to next song on list when initial list is created
        self.prevInPlaylist = None # pointer to previous song in the user's playlist
        self.nextInPlaylist = None # pointer to next song in the user's playlist

# methods used to set the pointers
    def setNextInOrigOrder (self, node):
        self.nextInOrigOrder = node
    def setPrevInPlaylist (self, node):
        self.prevInPlaylist = node
    def setNextInPlaylist (self, node):
        self.nextInPlaylist = node
# returns the song title of the node
    def getSongTitle(self):
        return(self.title)
# returns the next node (in the original order)
    def getNextInOrigOrder(self):
        return(self.nextInOrigOrder)
# returns the previous node (in the playlist order)
    def getPrevInPlaylist(self):
        return(self.prevInPlaylist)
# returns the next node (in the playlist order)
    def getNextInPlaylist(self):
        return(self.nextInPlaylist)


# Main Program
if len(sys.argv) != 4:
    raise ValueError('Please provide three file names.')

inputSongs = sys.argv[1]
inputPlaylist = sys.argv[2]
inputCommands = sys.argv[3]

print("\nThe file that has all the songs is:", inputSongs)
print("\nThe file that has the user's playlist is:", inputPlaylist)
print("\nThe file that has the user's commands is:\n", inputCommands)
# Initializing pointers that will be used to create and traverse the linked list
headNodeOrig = None
headNodePlaylist = None
tailNodePlaylist = None
currentNode = None

# TO DO: write your code below this line.
start = timer()

#Process Songs
#creates first song for head
f = open(inputSongs, "r")
songTitle = f.readline().rstrip()
headNodeOrig = Song(songTitle)
currentNode = headNodeOrig

#points new song node to previous song node to fully implement singly linked list
while songTitle:
    songTitle = f.readline().rstrip()
    newSong = Song(songTitle)
    currentNode.setNextInOrigOrder(newSong)
    currentNode = currentNode.getNextInOrigOrder()

f.close()


#Process the Playlist
f = open(inputPlaylist, "r")

#Finds first song from playlist in Orig to create a header node for playlist
songTitle = f.readline().rstrip()
headNodePlaylist = headNodeOrig
check = headNodePlaylist.getSongTitle()
while songTitle != check:
    headNodePlaylist = headNodePlaylist.getNextInOrigOrder()
    check = headNodePlaylist.getSongTitle()
prevPlaylistNode = headNodePlaylist #switch head to previous node

#Finds song from playlist in Orig and points that node to the previous playlist node and vice-versa
songTitle = f.readline().rstrip()
while songTitle:
    currentNode = headNodeOrig
    check = currentNode.getSongTitle()
    while songTitle != check:
        currentNode = currentNode.getNextInOrigOrder()
        check = currentNode.getSongTitle()
    #update node
    tailNodePlaylist = currentNode
    #links pointers for doubly linked playlist
    tailNodePlaylist.setPrevInPlaylist(prevPlaylistNode)
    prevPlaylistNode.setNextInPlaylist(tailNodePlaylist)
    prevPlaylistNode = tailNodePlaylist #switch tail to previous node
    songTitle = f.readline().rstrip()
f.close()

#Process User Commands
f = open(inputCommands, "r")
command = f.readline().strip()
#Iterates through inputCommands and provides the required functionality with conditional statements
#--while this could be implemented with functions, the functionalities were fairly simple and the command already summarizes the code; keeping in same place is better!--
while command:
    if command == "Beginning":
        currentNode = headNodePlaylist
        print("Beginning")
    if command == "End":
        currentNode = tailNodePlaylist
        print("End")
    if command == "Play":
        print("Now Playing: {0}".format(currentNode.getSongTitle()))
    if command == "Previous":
        currentNode = currentNode.getPrevInPlaylist()
        print("Previous")
    if command == "Next":
        currentNode = currentNode.getNextInPlaylist()
        print("Next")
    command = f.readline().rstrip()
f.close()

end = timer()

# TO DO: Print program's runtime.
print("\n***********************")
print("***** RunningTime *****")
print("***********************")
print("Time of Program: {:.8f} milliseconds".format(end - start))