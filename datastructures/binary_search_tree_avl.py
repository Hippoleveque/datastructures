#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BinarySearchTree:

    class Node:

        def __init__(self,value):
            self._value = value
            self._balance = 0
            self._right = None
            self._left = None
        
        @property
        def value(self):
            return self._value
        
        @property
        def left(self):
            return self._left
        
        @property
        def balance(self):
            return self._balance

        @property
        def right(self):
            return self._right
        
        @left.setter
        def left(self,new_left):
            self._left = new_left
        
        @right.setter
        def right(self,new_right):
            self._right = new_right

        @balance.setter
        def balance(self,new_balance):
            self._balance = new_balance
        
        @value.setter
        def value(self,new_value):
            self._value = new_value

    def __init__(self):
        self._root = None
        self._size = 0 
    
    def __len__(self):
        return self._size

    def empty(self):
        return len(self) == 0

    @property
    def root(self):
        if self.empty():
            raise ValueError("The tree is empty")
        return self._root.value

    def contains(self,value):
        return self._contains(self._root, value)
    
    def _contains(self,tree,value):
        if tree is None:
            return False
        if tree.value == value:
            return True
        if value < tree.value:
            return self._contains(tree.left, value)
        # value > tree.value
        else:
            return self._contains(tree.right,value)

    def insert(self,value):
        new_node = self.Node(value)
        new_root, _ = self._insert_avl(self._root,new_node)
        if new_root is not None:
            self._root = new_root
        self._size += 1


    def _insert_avl(self,tree,node):
        if tree is None:
            return node, 1
        elif tree.value == node.value:
            return None, 0
        else:
            if node.value < tree.value:
                insert, delta = self._insert_avl(tree.left,node)
                if insert is not None:
                    tree.left = insert
                if delta == 0:
                    return None, 0
                #delta is 1
                else:
                    # inserting left so now the node is balance
                    if tree.balance == 1:
                        tree.balance = 0
                        return None, 0
                    # tree is balance, inserting left no you propagate the balance change upwards    
                    elif tree.balance == 0:
                        tree.balance = -1
                        return None, 1
                    #inserting left worsen the imbalance : you need to fix it 
                    else:
                        to_ret = self._fix_left_imbalance(tree)
                        return to_ret, 0 
            # node.value > tree.value
            else:
                insert, delta = self._insert_avl(tree.right,node)
                if insert is not None:
                    tree.right = insert
                if delta == 0:
                    return None,0
                #delta = 1
                else:
                    # inserting right so now the node is balance
                    if tree.balance == -1:
                        tree.balance = 0
                        return None, 0
                    # tree is balance, inserting right to propagate the balance change upwards
                    elif tree.balance == 0:
                        tree.balance = 1
                        return None, 1
                    #inserting right worsen the imbalance : you need to fix it 
                    else:
                        to_ret = self._fix_right_imbalance(tree)
                        return to_ret, 0
    

    def _fix_left_imbalance(self,node):
        # first case : the balance is the same for node and its left child
        if node.balance == node.left.balance:
            # so you need just one rotation 
            left = node.left
            node.left = left.right
            left.right = node
            # fix balances
            left.balance = 0
            node.balance = 0
            return left
        else:
            # you need two rotations (be careful)
            left = node.left
            left_right = left.right # that is where the imbalance comes from
            # you need a right rotation there
            left.right = left_right.left
            left_right.left = left
            node.left = left_right
            # there you go, now you need a left rotation like above
            node.left = left_right.right
            left_right.right = node
            # now fixing balances depends on which side of the left right node the new node was inserted
            # case 1 : it was inserted on its left
            if left_right.balance == -1:
                # then the tree on the left of left right is now the right of the left node
                left.balance = 0
                node.balance = 1
                left_right.balance = 0
            elif left_right.balance == 1:
                left.balance = -1 
                node.balance = 0 
                left_right.balance = 0
            # left_right balance == 0
            else:
                left.balance = 0
                node.balance = 0
                left_right.balance = 0
            return left_right


    def _fix_right_imbalance(self,node):
        # first case : imbalance is on the same side
        if node.right.balance == node.balance:
            # you only need one left rotation
            right = node.right
            node.right = right.left
            right.left = node
            right.balance = 0
            node.balance = 0
            # return right as the new root
            return right
        
        else:
            right = node.right
            right_left = right.left
            # one right rotation on the lower level (right)
            right.left = right_left.right
            right_left.right = right
            node.right = right_left
            # now you just need a left rotation as in the case above
            node.right = right_left.left
            right_left.left = node

            if right_left.balance == 1:
                right.balance = 0
                node.balance = -1
                right_left.balance = 0
            elif right_left.balance == -1:
                right.balance = 1
                node.balance = 0
                right_left.balance = 0
            # right_left balance == 0
            else:
                right.balance = 0 
                node.balance = 0
                right_left.balance = 0
            # return right_left as the new root
            return right_left
    

    def remove(self, value):
        new_root, _ = self._remove(self._root, value)
        if self._root is not new_root:
            self._root = new_root
        self._size -= 1
        
    
    def _remove(self, node, value):
        # take care of this later
        if node is None:
            return None, False
        if value < node.value:
            child, update = self._remove(node.left,value)
            if child is not node.left:
                node.left = child
            if update:
                # then you need to update your balance factor
                if node.balance == 0:
                    node.balance = 1
                    # you dont have to propagate it upward because the depth of the tree starting this node did not change
                    return node,False 
                elif node.balance == -1:
                    node.balance = 0
                    # you need to propagate upward that the depth of this root diminished
                    return node,True
                # node.balance == 1
                else:
                    # now you have a balance problem on your right : fix it
                    self._fix_right_imbalance(node)
                    return node,False
            return node,False
        elif value > node.value:
            child, update = self._remove(node.right,value)
            if child is not node.right:
                node.right = child
            if update:
                # then you need to update the balance factor
                if node.balance == 0:
                    node.balance = -1
                    return node,False
                elif node.balance == 1:
                    node.balance = 0
                    return node,True
                # node.balance == -1
                else:
                    self._fix_left_imbalance(node)
                    return node,False
            return node,False
        # tree.value == value
        else:
            # there are three cases : tree can be a leaf, three can have 1 child or 2 children
            # first case : tree is a leaf
            if node.left is None and node.right is None:
                # you just need to propagate upward that the node should be deleted
                return None, True
            # if node only has a right child
            if node.left is None:
                # just replace it with the its right child
                return node.right, True
            # if node only has a left child
            if node.right is None:
                # just replace it with its left child
                return node.left, True
            # is that case node has a right and a left child
            else:
                # the idea is to replace the root of the tree rooted in node by the leftmost node of its right branch
                # (or we could have chosen the rightmost element of its leftbranch)
                curr = node.right
                while (curr.left is not None):
                    curr = curr.left
                # now curr is the leftmost element of the right branch
                # just swapping the values of node and curr (for simplicity)
                old_node_value = node.value
                node.value = curr.value
                curr.value = old_node_value
                # then just delete the curr node
                child, update = self._remove(node.right,old_node_value)
                if child is not node.right:
                    node.right = child
                if update:
                    if node.balance == 0:
                        node.balance = -1
                        return node,False
                    elif node.balance == 1:
                        node.balance = 0
                        return node,True
                    # node.balance == -1
                    else:
                        self._fix_left_imbalance(node)
                        return node,False
                return node,False


    def return_inorder_list(self):
        to_ret = []
        self._return_inorder_list(self._root,to_ret)
        return to_ret
    
    def _return_inorder_list(self,node,res):
        if node is not None:
            self._return_inorder_list(node.left,res)
            res.append(node.value)
            self._return_inorder_list(node.right,res)


    def print_inorder(self):
        self._print_inorder(self._root,"")
    
    def _print_inorder(self, node, prefix):
        if node is not None:
            self._print_inorder(node.right, prefix + "  ")
            print(prefix,node.value)
            self._print_inorder(node.left,prefix + "  ")
    
    def print_postorder(self):
        self._print_postorder(self._root)
    
    def _print_postorder(self,node):
        if node is not None:
            self._print_postorder(node.left)
            self._print_postorder(node.right)
            print(node.value)
    
    def print_preorder(self):
        self._print_preorder(self._root,)
    
    def _print_preorder(self,node):
        if node is not None:
            print(node.value)
            self._print_preorder(node.left)
            self._print_preorder(node.right)
    



if __name__ == "__main__": 
    print("hello")
    tree = BinarySearchTree()
    for el in range(10,0,-1):
        tree.insert(el)
    print(tree.return_inorder_list())