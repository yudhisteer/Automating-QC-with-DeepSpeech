import numpy as np


''' Here in Text we have "Start" '''

text = "start 23 next 34 next 45 stop"
print(" ")

# if "start" and "stop" in text.split():
#        data = np.array(text.split())
#      print(data)
#      b= np.where(data == "start")
#      print(b[0])
#      print(b[0][0])
#      print("len: "+ str(len(b[0])))
#      print("len: " + str(len(b[0]) > 0))
#
#
# ''' Here in Text we do NOT have "Start" '''
#
# # text = "23 next 34 next 45 stop"
# # print(" ")
# #
# # if "start" and "stop" in text.split():
# #      data = np.array(text.split())
# #      print(data)
# #      b= np.where(data == "start")
# #      print(len(b[0]))


#Check if word "Stop" is here:
text = "start 23 next 34 next 45 stop"
if "start" and "stop" in text.split():
    data = np.array(text.split())

    if len(np.where(data == "stop")[0]) > 0:
        stop = np.where(data == "stop")[0][0]

        c = np.where(data == "stop")
        print(c) #printing index where "Stop" is in array - returning index as an array
        print(c[0]) #taking value of index - still a 1D array
        print(c[0].shape)

        print(c[0][0]) #take value of array as int
        print(c[0][0].shape)
        print(stop)
        print("the stop commande is here")
    else:
        print("the stop commande is not here")







#-----------------------------------------------------------------------------------------#
text = "start 23 next 34 next 45 stop"
if "start" and "stop" in text.split():
    data = np.array(text.split())
    if len(np.where(data == "start")[0]) > 0:
        start = np.where(data == "start")[0][0]
        print("the start commande is here")
    else:
        print("the start commande is not here")

    if len(np.where(data == "stop")[0]) > 0:
        stop = np.where(data == "stop")[0][0]
        print(stop)
        print("the stop commande is here")
    else:
        print("the stop commande is not here")


     #We are removing "Start" & "Stop" from Text
    if len(np.where(data == "stop")[0]) > 0 and len(np.where(data == "start")[0]) > 0:
        needed = np.array(data[start + 1:stop])
        print(np.array(data[start+1:stop])) #start = 0; stop = 6. Therefore we take only values of text from index 1 to 6(index 6 is not taken)
        print("needed: " + str(needed))

        nexts = np.where(needed == "next")[0] #we find indexes where word "next" is in new array(needed)
        print(f"nexts = {nexts}")
        print(f"nexts[0] = {nexts[0]}") #value of index of word next in array needed
        print(f"len(nexts) = {len(nexts)}")

        if len(nexts) == 0:
            print("no parametre 'next' was detected")
        elif len(nexts) != 0:
            print(f"{len(nexts) + 1} numbers are detected")
            first = needed[0:nexts[0]]
            print(first) #print first number in array needed
            last = needed[nexts[-1] + 1:]
            print(last) #print last number in array needed




