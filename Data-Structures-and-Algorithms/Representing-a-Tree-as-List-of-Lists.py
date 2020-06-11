'''
Tree Representation Implementation using a List of Lists
'''

def binary_tree(root):
    return [root, [], []]

def insert_left(root, new_branch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    
    return root

def insert_right(root, new_branch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])

    return root

def get_root_val(root):
    return root[0]

def set_root_val(root, val):
    root[0] = val

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

r = binary_tree(3)

print(insert_left(r, 4))
print(insert_left(r, 5))
print(insert_right(r, 6))
print(insert_right(r, 7))
l = get_left_child(r)
print(l)
set_root_val(l, 9)
print(r)

'''
OUTPUT:
[3, [4, [], []], []]
[3, [5, [4, [], []], []], []]
[3, [5, [4, [], []], []], [6, [], []]]
[3, [5, [4, [], []], []], [7, [], [6, [], []]]]
[5, [4, [], []], []]
[3, [9, [4, [], []], []], [7, [], [6, [], []]]]
'''