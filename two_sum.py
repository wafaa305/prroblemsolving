'''
Question: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

''' This function takes a target integer and an array containing several integers to determine
    which two elements of them the result of their summing gives the target number'''
def whichAddUpToTarget(whichAddUpToTargetArray,target):

    addUpToTargetElements = [] # we define this list to put the elements that addd up to target on it

    for outerIndex in range(len(whichAddUpToTargetArray)):
        innerIndex = outerIndex + 1
        for innerIndex in range(len(whichAddUpToTargetArray)):
            '''this piece of code check if the two refrenced element in the list are adds up to target '''
            if whichAddUpToTargetArray[outerIndex] + whichAddUpToTargetArray[innerIndex] == target:
                 addUpToTargetElements.append(whichAddUpToTargetArray[outerIndex])
                 addUpToTargetElements.append(whichAddUpToTargetArray[innerIndex])
                 return addUpToTargetElements # here we return an array that contains the elements that are add up to target
    return [] # if there is no elements are add up to target we return an empty list

target = int(input("Plese enter a target number: ")) #  this line asks user to enter  a target number
whichAddUpToTargetArray = [2,7,11,15] # here we defined the array that contains some integers that we check it if its contains to entegers that are adds up to target
addUpToTargetElements = whichAddUpToTarget(whichAddUpToTargetArray,target) # her4e we calling the function whichAddUpToTarget and pass the arrgument to it

print(addUpToTargetElements) # this to print the result
