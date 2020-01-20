# - Graph Data Structures
  # - What are they?
    #  - collections of data that are represented by nodes and the connections
    #    between them.

  # - What are they comprised of?
    # - "Nodes" (or "vertices")
      # - represent objects in a data set
      # - i.e. - cities, animals, web pages
    # - "Edges"
      # - connections between vertices; can be BIDRECTIONAL (point in both
      #   directions to indicate a two-way relationship)
    # - "Weights"
      # - values assigned to edges used to describe the relationship between its
      #   nodes.
      # - the "cost" to travel across an edge
      
  # - What are they useful for?
    # - illustrating or representing relationships between entities
      # - i.e. - social networks, physical networks (cell towers), maps of
      #   underground subway, cities, etc.
      
  # - What kinds of graphs exist?
    # - "Directed Graphs" ("digraphs")
      # - graphs that only allow movement in ONE direction along the edges.
    # - "Undirected Graphs"
      # - graphs that allow movement in BOTH directions along the edges during traversal.
    # - "Weighted Graphs" 
      # - allows the edges (between vertices/nodes) to have weights on them.
    # - "Unweighted Graphs" 
      # - does not allow the edges (between vertices/nodes) to have weights on them.
    # - "Cyclic Graphs"
      # - the edges of this graph allow you revisit at least one vertex during traversal.
    # - "Acyclic Graphs"
      # - nodes/vertices that can be visited only ONCE during traversal
      
  # - Summary of Graphs
    # - Graphs are a set of vertices and edges that connect those vertices.
    # - Graphs can be used to represent a variety of different networks or
    #   related pieces of data.
    # - "Graph Theory" came from mathematics, where graphs were used to formally
    #   represent a network, which is basically just a collection of objects
    #   that are all interconnected.
    # - In mathematics, graphs are defined as ordered pairs, using the variable 
    #   names, 'v' and 'e' to describe 'vertices' and 'edges', respectively, 
    #   very much in the same way that 'x' and 'y' are used to describe an 
    #   ordered pair of coordinates.
    
      
  # - Graphs vs Trees
    # - A 'tree' will always be a 'graph', but NOT ALL graphs will be trees.
      # - Tree Rules
        # - Trees need AT LEAST one node to be considered a tree (root node).
        # - Trees can only flow in one direction while graphs can be bidirectional.
          # - i.e. - Child nodes can only hace one parent node.
        # - Trees are nothing more than restricted types of graphs, just with more
        #   rules to follow.
          # - i.e. - Binary trees are a type of graph (directed acyclic graphs).
      # - Graph Rules
        # - Graphs MUST have AT LEAST a single node to be considered a graph (a
        #   "singleton graph").
        # - Edges can connect nodes/vertices in ANY possible way! 
          # - Directed Edges
            # - Two nodes are connected in a very specific way.
            # - "Origin" node (starting node) connects to the "destination" node
            #   (ending node).
          # - Undirected Edges
            # - Two nodes are NOT connected in any specific way and can be bidirectional.
            # - The "origin" node (starting node) and the "destination" node
            #   are not fixed.
        
      
