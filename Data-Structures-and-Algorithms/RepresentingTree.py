'''
Node and References Implementation of a Tree.
'''
class BinrayTree(object):

    def __init__(self, root_obj):

        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        
        if not self.left_child:
            self.left_child = BinrayTree(new_node)
        else:
            t = BinrayTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        
        if not self.right_child:
            self.right_child = BinrayTree(new_node)
        else:
            t = BinrayTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key