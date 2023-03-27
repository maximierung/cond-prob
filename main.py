from anytree import Node, RenderTree
from tabulate import tabulate

table = [[None, "A:", "% for A:", "B:", "% for B:", "C:"],
["A:", "AA", None, "AB", None, "AC"],
["B:", "BA", None, "BB", None, "BC"],
["C:", "CA", None, "CB", None, "CC"]]

ca = float(input("Enter the value of A: "))
cb = float(input("Enter the value of B: "))
aa = float(input("Enter the value of branch one for A: "))
ba = float(input("Enter the value of branch two for A: "))
ab = float(input("Enter the value of branch one for B: "))
bb = float(input("Enter the value of branch two for B: "))

tree = Node("Start") #root
tree_a = Node(f"A: {ca} ({str(ca).replace('0.', '')}%)", parent=tree)
tree_b = Node(f"B: {cb} ({str(cb).replace('0.', '')}%)", parent=tree)
tree_ab = Node(f"A1: {aa} ({round(aa / ca, 5)})", parent=tree_a)
tree_ab1 = Node(f"A2: {ba} ({round(ba / ca, 5)})", parent=tree_a)
tree_a1b = Node(f"B1: {ab} ({round(ab / cb, 5)})", parent=tree_b)
tree_a1b1 = Node(f"B2: {bb} ({round(bb / cb, 5)})", parent=tree_b)

input = input("Choose displaytype:\nTree [1]\nTable [2]\nJSON [3]\n\n")
if input == "1":
    for pre, fill, node in RenderTree(tree):
        print("%s%s" % (pre, node.name))
if input == "2":
    table[1][1] = aa
    table[1][2] = str(round(aa / ca, 5)).replace("0.", "") + "%"
    table[1][3] = ab
    table[2][2] = str(round(ba / ca, 5)).replace("0.", "") + "%"
    table[1][5] = round(aa + ab, 5)
    table[2][1] = ba
    table[1][4] = str(round(ab / cb, 5)).replace("0.", "") + "%"
    table[2][3] = bb
    table[2][4] = str(round(bb / cb, 5)).replace("0.", "") + "%"
    table[2][5] = round(ba + bb, 5)
    table[3][1] = round(aa + ba, 5)
    table[3][3] = round(ab + bb, 5)
    table[3][5] = f"{table[3][1] + table[3][3]} | {table[1][5] + table[2][5]}"
    print(tabulate(table))
if input == "3":
    print("Later.")