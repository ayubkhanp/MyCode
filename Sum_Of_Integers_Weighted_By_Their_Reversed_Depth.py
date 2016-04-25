'''
 * Given a nested list of integers, returns the sum of all integers in the list weighted by their reversed depth.
 * For example, given the list {{1,1},2,{1,1}} the deepest level is 2. Thus the function should return 8 (four 1's with weight 1, one 2 with weight 2)
 * Given the list {1,{4,{6},5},1} the function should return 17 (one 1 with weight 3, one 4 with weight 2, and one 6 with weight 1)
'''

def sumOfNestedLists(nestedList, depth, max):
     cur_depth = depth
     max_depth = max
     myList = []
     for elem in nestedList:
         if isinstance(elem, int):
             myList.append([elem, cur_depth])
             if max_depth < cur_depth:
                 max_depth = cur_depth
         elif isinstance(elem, list):
             cur_depth += 1
             tempList, max_depth = sumOfNestedLists(elem, cur_depth, max_depth)
             print "temp list is " + str(tempList)
             cur_depth -= 1
             myList.extend(tempList)
     return myList, max_depth

if __name__ ==  "__main__":
    sum = 0
    inputList = [1,[4,[6],5],1]
    list, max = sumOfNestedLists(inputList, 0, 0)
    print list
    print max
    for elem, depth in list:
        sum += elem * (max + 1 - depth)
    print "Sum is " + str(sum)
