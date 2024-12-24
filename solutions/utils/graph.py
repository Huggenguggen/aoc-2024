from typing import List, Tuple, Set
from heapq import heappop, heappush
from collections import defaultdict

def generate2DGraph(rows: int, cols: int, \
                    clear: str, obstacle: str, \
                      obstacles: List[Tuple[int, int]]) -> List[List[str]]:
    """
    Generates a 2D array usually for pathfinding problems

    Args:
        rows (int): Number of rows in graph.
        cols (int): Number of columns in graph.
        clear (str): character representing clear tile
        obstacle (int): character representing an obstacle
        obstacles (List[Tuple[int, int]]): list of 2D coordinates holding the obstacle positions

    Returns:
        List[List[str]]: 2D array representing a graph
    """
    graph = [[clear for _ in range(cols + 1)] for _ in range(rows + 1)]
    for ob in obstacles:
        x, y = ob
        graph[y][x] = obstacle
    return graph


def print2DGraph(graph: List[List[str]]) -> None:
    """
    Prints out a 2D array nicely, better to be single char per tile

    Args:
        graph (List[List[str]]): graph to print
      
    Returns:
        None  
    """
    print(*graph, sep='\n')
  
def dijkstra2D(start: Tuple[int, int], end: Tuple[int, int], \
                graph: List[List[str]], options: List[Tuple[int, int, int]], \
                  clear: str, obstacle: str, needAll: bool=False) -> Set:
    """
    Performs Dijkstra's on a 2D array, returning all optimal paths

    Args:
        start (Tuple[int, int]): Starting position on the graph.
        end (Tuple[int, int]): Goal position on the graph.
        graph (List[List[str]]): 2D array of characters representing graph
        options (List[Tuple[int, int, int]]): List of possible directions/moves along with weight, put all as 1 for equal weightage
        clear (str): Character repesenting clear tile
        obstacle (str): Character representing osbtacle tile
        needAll (bool): Whether or not we need all winning paths or just one, by default is set to False

    Returns:
        Set: set of winning path(s)
    """
    rows, cols = len(graph), len(graph[0])
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    
    # Dictionary to store all previous positions that led to current position
    # with optimal distance
    prev = defaultdict(set)
    
    # Priority queue to store (distance, position)
    pq = [(0, start)]
    
    # Set to track visited nodes for when we don't need all paths
    visited = set()
    
    while pq:
        curr_dist, curr_pos = heappop(pq)
        
        # If we've found the end position and don't need all paths, we can break
        if curr_pos == end and not needAll:
            # For single path, only keep one previous position
            for pos in prev:
                if len(prev[pos]) > 1:
                    prev[pos] = {next(iter(prev[pos]))}
            break
            
        # If we don't need all paths and we've visited this node, continue
        if not needAll and curr_pos in visited:
            continue
            
        visited.add(curr_pos)
            
        # Check all possible moves
        for dx, dy, weight in options:
            new_x, new_y = curr_pos[0] + dx, curr_pos[1] + dy
            
            # Check if new position is valid
            if (0 <= new_x < rows and 
                0 <= new_y < cols and 
                graph[new_x][new_y] == clear):
                
                new_dist = curr_dist + weight
                
                # If we found a shorter or equal path
                if new_dist <= distances[(new_x, new_y)]:
                    # If it's a new shortest path, clear previous paths
                    if new_dist < distances[(new_x, new_y)]:
                        prev[(new_x, new_y)] = set()
                    
                    # If we don't need all paths and this position was visited, skip
                    if not needAll and (new_x, new_y) in visited:
                        continue
                        
                    # Add this path
                    prev[(new_x, new_y)].add(curr_pos)
                    distances[(new_x, new_y)] = new_dist
                    heappush(pq, (new_dist, (new_x, new_y)))
    
    # Backtrack to find all optimal paths
    def backtrack(pos: Tuple[int, int], path: Tuple[Tuple[int, int], ...]) -> Set[Tuple[Tuple[int, int], ...]]:
        if pos == start:
            return {path}
        
        paths = set()
        for prev_pos in prev[pos]:
            paths.update(backtrack(prev_pos, (prev_pos,) + path))
        return paths
    
    # If end is not reachable, return empty set
    if distances[end] == float('inf'):
        return set()
    
    # Return all optimal paths from start to end
    return backtrack(end, (end,))

