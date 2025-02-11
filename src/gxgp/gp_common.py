#   *        Giovanni Squillero's GP Toolbox
#  / \       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 2   +      A no-nonsense GP in pure Python
#    / \
#  10   11   Distributed under MIT License

from copy import deepcopy
import icecream as ic

from .node import Node
from .random import gxgp_random
import random


def xover_swap_subtree(tree1: Node, tree2: Node) -> Node:
    offspring = deepcopy(tree1)
    successors = None
    while not successors:
        node = random.choice(list(offspring.subtree))
        successors = node.successors
        if not successors:
            return offspring
    i = random.randrange(len(successors))
    successors[i] = deepcopy(random.choice(list(tree2.subtree)))
    node.successors = successors
    return offspring
