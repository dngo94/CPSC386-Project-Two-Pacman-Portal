import pygame as pg
import game_functions as gf
from scorebutton import scorebutton
from score import Scoreboard
from settings import Settings
from maze import Maze, GridPoint
from character import Pacman, Blinky, Inky, Pinky, Clyde
from move import Aliens
from move2 import Aliens2
from pygame.sprite import Group
from button import Button
from game_stats import GameStats
from sound import Sound
# ===================================================================================================
# class Game
# ===================================================================================================
class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode(size=(self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption("PacMan Portal")
        self.font = pg.font.SysFont(None, 48)
        ship_image = pg.image.load('images/ship.bmp')
        self.ship_height = ship_image.get_rect().height
        self.maze = Maze(game=self)
        self.play_button = None
        self.hs_button = None
        self.sound = Sound(bg_music="sounds/main.wav")
        self.sound.play()
        self.sound.pause_bg()
        self.pacman = Pacman(game=self)
        self.ghosts = [Blinky(game=self), Pinky(game=self), Clyde(game=self), Inky(game=self)]
        for ghost in self.ghosts:
            ghost.set_ghosts(self.ghosts)
        self.finished = False
        self.restart()
        self.hs = 0

    def to_grid(self, index):
        row = index // 11
        offset = index % 11
        ss = self.maze.location(row, offset)
        return ss

    def to_pixel(self, grid): pixels = []

    def restart(self):
        alien_group = Group()
        alien_group2 = Group()
        self.play_button = Button(settings=self.settings, screen=self.screen, msg="PLAY")
        self.hs_button = scorebutton(settings=self.settings, screen=self.screen, msg="HIGH SCORES")
        self.stats = GameStats(settings=self.settings)
        self.sb = Scoreboard(game=self, sound=self.sound)
        self.aliens = Aliens(settings=self.settings, screen=self.screen, alien_group=alien_group,
                             ship_height=self.ship_height, stats=self.stats, game=self)
        self.aliens2 = Aliens2(settings=self.settings, screen=self.screen, alien_group2=alien_group2,
                               ship_height=self.ship_height, stats=self.stats, game=self)

        self.hs = self.stats.high_score
        self.sb.prep_high_score()

    def scores(self):
        myfont = pg.font.SysFont("monospace",60)
        label = myfont.render("HIGH SCORES", 1, (171, 130, 255))
        self.screen.blit(label, (165, 50))
        score_display = myfont.render(str(self.hs),1,(171, 130, 255))
        self.screen.blit(score_display, (315, 150))

    def play(self):
        while not self.finished:
            gf.check_events(game=self, stats=self.stats, play_button=self.play_button, hs_button=self.hs_button)
            # self.screen.fill(self.settings.bg_color)

            self.aliens.update()
            if not self.stats.game_active:
                self.screen.fill(self.settings.bg_color)
                self.play_button.draw()
                self.hs_button.draw_button()
                myfont = pg.font.SysFont("monospace", 35)
                label = myfont.render("CHARACTER  /   NICKNAME", 1, (240,255,255))
                self.screen.blit(label, (140, 300))
                red = pg.image.load('images/rgr3.png')
                red = pg.transform.rotozoom(red, 0, 2)

                x = 60
                y = 350
                self.screen.blit(red, (x, y))
                myfont = pg.font.SysFont("monospace", 35)
                label = myfont.render('-SHADOW      "BLINKY"', 1, (255,0,0))
                self.screen.blit(label, (140, 350))
                pin = pg.image.load('images/pgr3.png')
                pin = pg.transform.rotozoom(pin, 0, 2)

                x = 60
                y = 400
                self.screen.blit(pin, (x, y))
                myfont = pg.font.SysFont("monospace", 35)
                label = myfont.render('-SPEEDY      "PINKY"', 1, (255,192,203))

                self.screen.blit(label, (140, 400))
                ink = pg.image.load('images/bgr3.png')
                ink = pg.transform.rotozoom(ink, 0, 2)

                x = 60
                y = 450
                self.screen.blit(ink, (x, y))
                myfont = pg.font.SysFont("monospace", 35)
                label = myfont.render('-BASHFUL     "INKY"', 1, (0,238,238))

                self.screen.blit(label, (140, 450))
                org = pg.image.load('images/ogr3.png')
                org = pg.transform.rotozoom(org, 0, 2)

                x = 60
                y = 500
                self.screen.blit(org, (x, y))
                myfont = pg.font.SysFont("monospace", 35)
                label = myfont.render('-POKEY       "CLYDE"', 1, (255,128,0))

                self.screen.blit(label, (140, 500))

                title = pg.image.load('images/title.png')

                x = 100
                y = 50

                self.screen.blit(title, (x, y))



            if self.stats.ghost:
                self.aliens2.update()

            if not self.stats.hs_active:
                self.aliens2.draw()
                self.aliens.draw()
                self.hs_button.draw_button()
            else:
                self.screen.fill(self.settings.bg_color)
                self.scores()

            if self.stats.game_active:
                if not self.sound.playing_bg:
                    self.sound.unpause_bg()

                # print("hello")
                # gf.check_events(game=self, stats=self.stats, play_button=self.play_button)
                self.maze.update()
                self.pacman.update()
                for ghost in self.ghosts: ghost.update()
                self.pacman.update()

            pg.display.flip()

def main():
    game = Game()
    game.play()
    with open("highscores.txt", 'a') as f:
        f.write(f'The high score was {game.hs}\n')


if __name__ == '__main__': main()

