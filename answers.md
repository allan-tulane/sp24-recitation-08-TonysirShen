# CMPS 2200 Recitation 08

## Answers

**Name:**_____Sean Hall____________________
**Name:**______________Tony Shen___________


Place all written answers from `recitation-08.md` here for easier grading.



- **1b)** We call this function once per edge, since a node may be added multiple times for each edge. Thus the work is O(E log E)

Because this algorithm must be completed sequentially, the span must also be O(E log E)
        - Work:  O(E log E)
          Span: O(E log E)


- **2b)**
- def get_path(parents, destination):
  if destination not in parents:
    return ''
  else:
    parent = parents[destination]
    return get_path(parents, parent) + parent
This recursive function checks the destination's parent and prepend the parent's prentn's to it until there is no parent.
Its work and span are both O(N)
