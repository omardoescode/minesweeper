import pygame

class GridGUI:
    def __init__(self, rows, columns, cell_size):
        self.rows = rows
        self.columns = columns
        self.cell_size = cell_size
        self.width = columns * cell_size
        self.height = rows * cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.grid = [['X' for _ in range(columns)] for _ in range(rows)]

    def draw_grid(self):
        for row in range(self.rows):
            for col in range(self.columns):
                pygame.draw.rect(self.screen, (255, 255, 255),
                                 (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size), 1)

    def update_tile(self, row, column, value):
        self.grid[row][column] = value

        font = pygame.font.Font(None, 36)
        text = font.render(str(value), True, (255, 255, 255))
        self.screen.blit(text, (column * self.cell_size + 10, row * self.cell_size + 10))

    def run(self):
        pygame.init()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((0, 0, 0))
            self.draw_grid()

            # Update a tile (for demonstration purposes)
            self.update_tile(0, 0, '1')

            pygame.display.flip()

        pygame.quit()

# Example usage
if __name__ == "__main__":
    difficulties = {
        1: (8, 8),
        2: (16, 16),
        3: (16, 30)
    }

    print("Choose the difficulty:")
    print("1. Easy (8x8)")
    print("2. Medium (16x16)")
    print("3. Hard (16x30)")
    print("4. Custom")

    choice = int(input("Enter your choice: "))

    if choice in difficulties:
        rows, columns = difficulties[choice]
    elif choice == 4:
        rows = int(input("Enter the number of rows: "))
        columns = int(input("Enter the number of columns: "))
    else:
        print("Invalid choice. Choosing Easy by default.")
        rows, columns = difficulties[1]

    grid = GridGUI(rows, columns, 30)  # Change cell size as needed
    grid.run()