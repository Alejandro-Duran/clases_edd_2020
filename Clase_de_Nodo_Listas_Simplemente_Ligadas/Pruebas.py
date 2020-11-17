from Simplemente_Ligadas import Linked_List

l = Linked_List()
print(f"L esta vacia ? {l.is_empty()}")
l.append(10)
l.append(5)
l.append(6)
l.append(20)
print(f"L esta vacia ? {l.is_empty()}")
l.transversal()
