# Dijkstra-s-Algorithm-Visulization
This Pygame script visualizes Dijkstra's algorithm on a grid where users can place start points, end points, and obstacles. The algorithm computes the shortest path from the start to the end while avoiding obstacles, updating the grid as it progresses.

## Project Structure

- **Dijkstra's-Visualization**: Folder containing the Python script for the visualization.
  - **DijkstraPathVisualization.py**: Main Python script that runs the visualization.

## Features

- **Interactive Grid**: Users can place start and end nodes, as well as obstacles, by clicking on the grid.
- **Dijkstra's Algorithm Visualization**: The algorithm's progress is shown visually, with visited nodes and the final path.
- **Customizable Grid**: Modify grid size and colors for a unique visualization experience.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/SaiSrikarK03/Dijkstra-s-Algorithm-Visulization.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Dijkstra-s-Algorithm-Visulization
   ```
3. Install the required dependencies (Pygame):
   ```bash
   pip install pygame
   ```
4. Run the script:
   ```bash
   python DijkstraPathVisualization.py
   ```

## Controls

- **Left Mouse Button**: 
  - First click places the **start node**.
  - Second click places the **end node**.
  - Further clicks place **obstacles**.
  
- **Right Mouse Button**: 
  - Removes obstacles, start, or end node.

- **Spacebar**: 
  - Starts the Dijkstra algorithm to find the shortest path.
  

## Future Enhancements

- Add diagonal movement to the algorithm.
- Implement additional algorithms like A* for comparison.
- Allow grid resizing dynamically.
