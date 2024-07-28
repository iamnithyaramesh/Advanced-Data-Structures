'''import heapq

class HuffMann:

    def __init__(self,freq,key,left=None,right=None):
        self.key=key
        self.freq=freq
        self.left=left
        self.right=right
        self.huff=''

    def __lt__(self,nxt):
        return self.freq<nxt.freq
    
    def __repr__(self):
        return str(self.key)
    
def printNodes(node,val=''):
    newVal=val+str(node.huff)
    if node.left:
        printNodes(node.left,newVal)
    if node.right:
        printNodes(node.right,newVal)
    
    if (not node.left and not node.right):
        print(f"{node.key} with frequency {node.freq} is denoted by the HuffMann Code {newVal}")

chars=['A','n','l','e','d','y','p','a','space']
freq=[1,1,1,1,1,1,2,3,3]
prob_list=[freq[i]/sum(freq) for i in freq]
print(prob_list)

node=[]
for x in range(len(chars)):
    heapq.heappush(node,HuffMann(freq[x],chars[x]))

while len(node)>1:

    left=heapq.heappop(node)
    right=heapq.heappop(node)
    print(node)

    left.huff=0
    right.huff=1

    newNode=HuffMann(left.freq+right.freq,left.key+right.key,left,right)

    heapq.heappush(node,newNode)

printNodes(node[0])'''


import heapq

class HuffMann_Node:

    def __init__(self, freq, symbol, left=None, right=None):

        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq

    def __repr__(self):
        return str(self.symbol)

def printNodes(node, val=''):
    newVal = val + str(node.huff)

    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)
    if not node.left and not node.right:
        print(f'{node.symbol} with frequency {node.freq} is denoted by the Huffman Code {newVal}')

def get_frequencies(string):
    char_list = []
    freq_list = []
    for i in string:
        if i not in char_list:
            char_list.append(i)
            freq_list.append(string.count(i))
    return char_list, freq_list

input_string = 'An apple a day'
chars, freq = get_frequencies(input_string)
prob_list = [freq[i] / sum(freq) for i in range(len(freq))]
print(prob_list)

nodes = []
for z in range(len(chars)):
    heapq.heappush(nodes, HuffMann_Node(freq[z], chars[z]))

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)

    left.huff = 0
    right.huff = 1

    newNode = HuffMann_Node(left.freq + right.freq, left.symbol + right.symbol, left, right)

    heapq.heappush(nodes, newNode)

printNodes(nodes[0])

