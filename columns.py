import pygame
import random

pygame.init()
pygame.display.set_caption('Columns')

class Game():
    
    def __init__(self, screen):
        self.run = True
        self.screen = screen
        self.size = 50
        self.blocks = []
        self.NewColumn()
        self.newfalltime = 1000
        pygame.time.set_timer(self.newfalltime, 500)
        self.base = 600 - self.size
        self.top = {0: self.base, 50: self.base, 100: self.base, 150: self.base, 200: self.base, 250: self.base}

    def Start(self):
        while self.run:
            self.Events()
            self.Updates()
            self.End()
        
    def Left(self) -> bool:
        return(self.top[self.column[2][1]-self.size] >= self.column[2][2])

    def Right(self) -> bool:
        return(self.top[self.column[2][1]+self.size] >= self.column[2][2])

    def Fall(self):
        if self.column[2][2] >= self.top[self.column[2][1]]:
            self.top[self.column[2][1]] -= 3*self.size
            self.blocks += self.column
            self.NewColumn()
        for block in self.column:
            block[2] += self.size

    def Events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            elif e.type == self.newfalltime:
                self.Fall()

    def NewColumn(self):
        colors = [(255,0,0), (255,115,0), (255,255,0), (0,255,10), (0,0,255), (180,0,255)]
        c1 = random.choice(colors)
        colors.remove(c1)
        c2 = random.choice(colors)
        colors.remove(c2)
        c3 = random.choice(colors)
        x = random.choice([0, 50, 100, 150, 200, 250])
        y1 = -3 * self.size
        y2 = -2 * self.size
        y3 = -1 * self.size
        self.column = [[c1, x, y1], [c2, x, y2], [c3, x, y3]]

    def Updates(self):
        self.screen.fill((0, 0, 0))
        if len(self.blocks) > 0:
            for b in self.blocks:
                pygame.draw.rect(self.screen, b[0], (b[1], b[2], 50, 50))
        for block in self.column:
            pygame.draw.rect(self.screen, block[0], (block[1], block[2], 50, 50))

        for i in range(1, 12):
            y = i*self.size
            pygame.draw.line(self.screen, (0, 0, 0), (0, y), (50, y))
        for i in range(1, 6):
            x = i*self.size
            pygame.draw.line(self.screen, (0, 0, 0), (x, 0), (x, 600))
        pygame.display.flip()
        pygame.display.update()

    def End(self):
        minimum = min(self.top.values()) + self.size
        if minimum <= 0:
            self.run = False

while True:
    try:
        g = Game(pygame.display.set_mode((300, 600)))
        g.Start()
    except:
        break