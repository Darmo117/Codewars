from operator import*
class Node:
 def __init__(s,*v):s.v=v
 compute=lambda s:s.o(*[v.compute()for v in s.v]);o=None
class value(Node):compute=lambda s:s.v[0]
class add(Node):o=add
class sub(Node):o=sub
class mul(Node):o=mul
class truediv(Node):o=truediv
class mod(Node):o=mod
class pow(Node):o=pow