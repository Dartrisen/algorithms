# algorithms

## Red-Black Tree

This repository contains an implementation of a red-black tree data structure in Python.

## Description

A red-black tree is a self-balancing binary search tree. It is a variation of the binary search tree that guarantees that the depth of the tree is O(log n). In other words, it ensures that the worst-case running time of the basic operations (search, insertion, deletion) is O(log n).

The nodes of a red-black tree are colored either red or black. The color of the root node is always black. All leaf nodes are black and do not contain data. Every red node must have two black child nodes. Every path from a given node to any of its descendant leaf nodes contains the same number of black nodes. These properties ensure that the tree remains balanced, and the worst-case running time is O(log n).

The implementation includes basic operations such as insertion, deletion, search, and print.

## Installation

The package can be launched with python3
```shell
$ python3 RB.py
```

## Visualization

A visualization of the tree can be generated using matplotlib. The `show_tree()` method generates an image.

## Requirements

The only requirement for this code is matplotlib. You can install it using pip with the following command:
```shell
$ pip install matplotlib
```
