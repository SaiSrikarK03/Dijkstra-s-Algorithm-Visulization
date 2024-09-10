import pygame
import heapq

# Initialize Pygame
pygame.init()

# Define some constants
WIDTH, HEIGHT = 600, 600
ROWS = 30
CELL_SIZE = WIDTH // ROWS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (169, 169, 169)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Setup the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dijkstra Algorithm Visualization")

# Create grid
def make_grid(rows, width):
    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            grid[i].append(0)  # 0 indicates an empty node (no obstacle)
    return grid

# Draw the grid lines
def draw_grid(screen, rows, width):
    for i in range(rows):
        pygame.draw.line(screen, GREY, (0, i * CELL_SIZE), (width, i * CELL_SIZE))
        for j in range(rows):
            pygame.draw.line(screen, GREY, (j * CELL_SIZE, 0), (j * CELL_SIZE, width))

# Draw the entire grid with obstacles, start, and end
def draw(screen, grid):
    screen.fill(WHITE)
    for i in range(ROWS):
        for j in range(ROWS):
            color = WHITE
            if grid[i][j] == 1:  # Obstacle
                color = BLACK
            elif grid[i][j] == 2:  # Start
                color = BLUE
            elif grid[i][j] == 3:  # End
                color = RED
            elif grid[i][j] == 4:  # Visited
                color = YELLOW
            elif grid[i][j] == 5:  # Path
                color = GREEN
            pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    draw_grid(screen, ROWS, WIDTH)
    pygame.display.update()

# Get neighbors for Dijkstra
def get_neighbors(pos):
    neighbors = []
    x, y = pos
    if x > 0:
        neighbors.append((x-1, y))
    if x < ROWS-1:
        neighbors.append((x+1, y))
    if y > 0:
        neighbors.append((x, y-1))
    if y < ROWS-1:
        neighbors.append((x, y+1))
    return neighbors

# Dijkstra algorithm
def dijkstra(grid, start, end):
    pq = []
    heapq.heappush(pq, (0, start))  # (cost, node)
    dist = {start: 0}
    came_from = {}
    visited = set()

    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_node in visited:
            continue
        visited.add(current_node)
        
        x, y = current_node
        if current_node != start and current_node != end:
            grid[x][y] = 4  # Mark as visited

        if current_node == end:
            reconstruct_path(came_from, end, grid)
            return True

        for neighbor in get_neighbors(current_node):
            nx, ny = neighbor
            if neighbor in visited or grid[nx][ny] == 1:  # Obstacle
                continue
            
            new_dist = current_dist + 1
            if neighbor not in dist or new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                came_from[neighbor] = current_node
                heapq.heappush(pq, (new_dist, neighbor))
        
        draw(screen, grid)

    return False

# Reconstruct the path from start to end
def reconstruct_path(came_from, end, grid):
    current = end
    while current in came_from:
        x, y = current
        grid[x][y] = 5  # Path
        current = came_from[current]
        draw(screen, grid)

# Main loop
def main():
    grid = make_grid(ROWS, WIDTH)
    start, end = None, None
    run = True
    path_found = False  # New flag to track if the path is found

    while run:
        draw(screen, grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Left mouse click to place start, end, or obstacles
            if pygame.mouse.get_pressed()[0]:  
                pos = pygame.mouse.get_pos()
                x, y = pos[1] // CELL_SIZE, pos[0] // CELL_SIZE
                if not start:
                    start = (x, y)
                    grid[x][y] = 2  # Start node
                elif not end:
                    end = (x, y)
                    grid[x][y] = 3  # End node
                elif grid[x][y] == 0:
                    grid[x][y] = 1  # Obstacle

            # Right mouse click to remove obstacle, start, or end
            elif pygame.mouse.get_pressed()[2]:  
                pos = pygame.mouse.get_pos()
                x, y = pos[1] // CELL_SIZE, pos[0] // CELL_SIZE
                grid[x][y] = 0
                if (x, y) == start:
                    start = None
                elif (x, y) == end:
                    end = None

            # Press space to start Dijkstra
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    if not path_found:  # Only run if path not found yet
                        path_found = dijkstra(grid, start, end)

    pygame.quit()

if __name__ == "__main__":
    main()
