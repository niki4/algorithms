"""
A topological sort or topological ordering of a directed graph is a linear ordering of its vertices
such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.
"""


# Based on Depth-First-Search algorithm. Sort works to Directed Acyclic Graph (DAG).
# Unvisited v has 'white' color.
def topological_sort_dfs(v):
    v.color = "grey"  # in process
    for w in v.adjastments:
        if w.color == "black":  # already visited
            continue
        if w.color == "grey":
            print("Graph contains cycle. Topological sort inapplicable.")
        topological_sort_dfs(w)
    v.color = "black"
    print(v)
