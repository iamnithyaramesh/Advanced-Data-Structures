class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def count_frequencies(text):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def build_huffman_tree(text):
    frequency = count_frequencies(text)
    nodes = [HuffmanNode(char, freq) for char, freq in frequency.items()]

    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)
        parent = HuffmanNode(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        nodes.append(parent)

    return nodes[0]

def build_huffman_codes(node, prefix="", codes={}):
    if node:
        if node.char is not None:
            codes[node.char] = prefix
        build_huffman_codes(node.left, prefix + "0", codes)
        build_huffman_codes(node.right, prefix + "1", codes)
    return codes


def huffman_encode(text):
    if len(text) == 0:
        return "", {}

    root = build_huffman_tree(text)

    codes = build_huffman_codes(root)

    encoded_text = ''.join(codes[char] for char in text)
    return encoded_text, codes

def huffman_decode(encoded_text, codes):
    if len(encoded_text) == 0:
        return ""

    decoded_text = []
    current_code = ""

    reverse_codes = {v: k for k, v in codes.items()}
    print(reverse_codes)

    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text.append(reverse_codes[current_code])
            current_code = ""

    return ''.join(decoded_text)

# Example usage:
text = "hello world this is my proverb that world should know"

# Build Huffman codes and encode text
encoded_text, codes = huffman_encode(text)
print("Encoded text:", encoded_text,codes)

# Decode the encoded text using Huffman codes
decoded_text = huffman_decode(encoded_text, codes)
print("Decoded text:", decoded_text)






# import heapq

# class BNode:
#     def _init_(self, num, letter = None, left = None, right = None) -> None:
#         self.letter = letter
#         self.num = num
#         self.left = left
#         self.right = right
#         self.codes = {}
        
#     def _lt_(self, other):
#         temp = self.num < other.num
#         if self.num == other.num:
#             if self.letter and other.letter:
#                 temp = self.letter < other.letter
#             elif self.letter:
#                 temp = True 
#         return temp
    
# class BinaryTree:
#     def _init_(self) -> None:
#         self.root = None
#         self.codes = {}
        
#     def preorder(self, root, code):
#         if not root: return
#         if root.letter:
#             self.codes[root.letter] = code
#         self.preorder(root.left, code + "0")
#         self.preorder(root.right, code + "1")
    
#     def bfs(self):
#         ans = []
#         queue = [(self.root, 0)]
#         while len(queue) > 0:
#             temp = queue.pop()
#             node = temp[0]
#             level = temp[1]
#             if len(ans) == level:
#                 if node.letter:
#                     ans.append([(node.letter, node.num)])
#                 else:
#                     ans.append([node.num])
#             else:
#                 if node.letter:
#                     ans[level].append((node.letter, node.num))
#                 else:
#                     ans[level].append(node.num)
#             if node.left: queue.append((node.left, level + 1))
#             if node.right: queue.append((node.right, level + 1))
#         print(ans)
    
# if _name_ == '_main_':
#     sentence = "Eerie eyes seen near lake."

#     freq = {}
#     for ch in sentence:
#         if ch not in freq:
#             freq[ch] = 1
#         else:
#             freq[ch] += 1

#     nodes = []
#     heapq.heapify(nodes)

#     for key in freq:
#         node = BNode(freq[key], key)
#         heapq.heappush(nodes, node)
    
#     BTree = BinaryTree()
        
#     while len(nodes) > 1:
#         first = heapq.heappop(nodes)
#         second = heapq.heappop(nodes)
#         node = BNode(first.num + second.num, left = second, right = first)
#         BTree.root = node
#         BTree.bfs()
#         heapq.heappush(nodes, node)

#     BTree.root = heapq.heappop(nodes)
#     BTree.preorder(BTree.root, "")
#     BTree.bfs() 
#     codes = BTree.codes
#     compressed_text = ""
#     for ch in sentence:
#         compressed_text += codes[ch]
#     print(codes)
#     print(compressed_text)
