
#def count_batteries_by_usage(cycles):
  #return {
    #"lowCount": 0,
   # "mediumCount": 0,
  #  "highCount": 0
 # }


#def test_bucketing_by_number_of_cycles():
  #print("Counting batteries by usage cycles...\n");
  #counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  #assert(counts["lowCount"] == 1)
  #assert(counts["mediumCount"] == 3)
  #assert(counts["highCount"] == 2)
 # print("Done counting :)")


#if __name__ == '__main__':
 # test_bucketing_by_number_of_cycles()

import re

def binarySearch(sumList, whattofind):
    a=0
    if len(sumList) == 0:
        return False
    else:
        midpoint = len(sumList)/2
        if sumList[midpoint]==whattofind:
            a=a+1
            print(a)
            return True
        else:
            if whattofind<sumList[midpoint]:
                a+=1
                return binarySearch(sumList[:midpoint],whattofind)
            else:
                a+=1
                return binarySearch(sumList[midpoint+1:],whattofind)
        print(a)
result = re.findall(r'\w\w', open("text.txt","r").read())
sumList=[]
for line in result:
    sumList.append(ord(line[0])+ord(line[1]))
sumList.sort()
whattofind=int(input('Enter number: '))
print (sumList)
print(binarySearch(sumList, whattofind))
