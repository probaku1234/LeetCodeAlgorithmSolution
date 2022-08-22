from collections import defaultdict
import random

class ConsistentHashing:

    def __init__(self, initialNodes: int):
        self.node_to_keys = defaultdict(set)
        self.key_to_nodes = defaultdict(set)
        self.nodes = [i + 1 for i in range(initialNodes)]
        self.next_node = initialNodes + 1

    def getNodeForKey(self, key: int) -> int:
        if key in self.key_to_nodes and self.key_to_nodes[key]:
            return random.choice(list(self.key_to_nodes[key]))

        else:
            node_to_take_key = random.choice(self.nodes)
            self.node_to_keys[node_to_take_key].add(key)
            self.key_to_nodes[key].add(node_to_take_key)
            return node_to_take_key

    def removeNode(self, node: int) -> int:
        self.nodes.remove(node)
        keys_to_reassign = self.node_to_keys[node]
        node_to_take_keys = random.choice(self.nodes)

        for key in keys_to_reassign:
            self.key_to_nodes[key].remove(node)
            self.key_to_nodes[key].add(node_to_take_keys)
            self.node_to_keys[node_to_take_keys].add(key)

        return node_to_take_keys

    def addNode(self) -> List[int]:
        node_to_reassign_keys = random.choice(self.nodes)
        new_node = self.next_node
        self.nodes.append(self.next_node)
        self.next_node += 1

        for key in self.node_to_keys[node_to_reassign_keys]:
            self.key_to_nodes[key].add(new_node)
            self.node_to_keys[new_node].add(key)

        return (new_node, node_to_reassign_keys)

    def getKeysInNode(self, node: int) -> List[int]:
        return list(self.node_to_keys[node])