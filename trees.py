# Whiteboarding with Sue and Lena


class Node:
    def __init__(self, data, children):
        self.data = data
        if not children:
            self.children = []
        else:
            self.children = children


    def return_greater_list(self, x):
        to_visit = [self]
        greater = []
        while to_visit:
            current = to_visit.pop()
            if current.data > x:
                greater.append(current.data)
            to_visit.extend(current.children)
        return greater


    def remove_nodes_with_decendents(self, x):
        to_visit = [self]
        while to_visit:
            if self.data == x:
                self.data = None
                self.children = []
                return
            to_visit = [self]
            while to_visit:
                current = to_visit.pop()
                for child in current.children:
                    if child.data == x:
                        current.children.remove(child)
                to_visit.extend(current.children)