import pygame as pg
from pygame.sprite import Sprite
from timer import Timer


class Aliens:
    def __init__(self, settings, screen, alien_group, ship_height,stats, game):
        self.settings = settings
        self.aliens = alien_group
        self.stats = stats
        self.screen = screen
        self.game = game
        self.ship_height = ship_height
        self.create_fleet()
        self.alien_type = None

    def create_fleet(self):
        settings, screen = self.settings, self.screen
        alien = Alien(settings=settings, screen=self.screen)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        aliens_per_row = self.aliens_per_row(settings=settings, alien_width=alien_width)
        rows_per_screen = self.rows_per_screen(settings=settings, alien_height=alien_height)

        for y in range(4):
            alien_type = y
            n = 0
            a = 0
            b = 90
            d= -30

            for x in range(5):
                alien = Alien(settings=settings, screen=screen, number=0+a, x=580+n-b, y=580+d)
                # alien = Alien(settings=settings, screen=screen, x=alien_width * (1 + 2 * x), y=alien_height * (1 + 2 * y))
                n +=40
                a+=1
                b = 0
                d = 0
                self.aliens.add(alien)

    def aliens_per_row(self, settings, alien_width):
        space_x = settings.screen_width - 2 * alien_width
        return 3

    def rows_per_screen(self, settings, alien_height): return 1
        # space_y = settings.screen_height - (alien_height) - self.ship_height
        # # space_y = settings.screen_height - (3 * alien_height) - self.ship_height
        # return int(space_y / (alien_height))
        # # return int(space_y / (2 * alien_height))

    def add(self, alien): self.aliens.add(alien)

    def remove(self, alien): self.aliens.aliens.remove(alien)

    def change_direction(self):
        for alien in self.aliens:
            alien.rect.y += 0
        self.settings.fleet_direction *= -1

    def check_edges(self):
        for alien in self.aliens:
            if alien.check_edges(): return True
        return False

    def check_aliens_bottom(self):
        r = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom > r.bottom:
                return True
        return False

    def update(self):
        self.aliens.update()
        if self.check_edges():
            for alien in self.aliens.copy():
                self.aliens.remove(alien)
            if len(self.aliens) == 0:
             self.stats.ghost =True



        # for y in range(rows_per_screen):
        #     for x in range(aliens_per_row):
        # row = 5
        for alien in self.aliens.copy():
            alien.update()

    def draw(self):

         for alien in self.aliens.sprites(): alien.draw()


class Alien(Sprite):   # INHERITS from SPRITE
    images = [[pg.image.load('anim/n' + str(number) + str(i) + '.png') for i in range(2)] for number in range(5)]

    timers = []
    for i in range(5):
        timers.append(Timer(frames=images[i], wait=700))


    def __init__(self, settings, screen, number=0, x=0, y=0, speed=0):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.number = number
        self.update_requests = 0

        # self.image = pg.image.load('images/alien.bmp')
        # self.rect = self.image.get_rect()
        # self.images = ['images/invader' + str(number) + str(i) + '.png' for i in range(2)]
        # print(self.images)
        # self.frames = [pg.image.load(self.images[i]) for i in range(len(self.images))]
        self.timer = Alien.timers[number]
        # self.timer = Timer(frames=self.frames, wait=700)
        self.rect = self.timer.imagerect().get_rect()

        self.rect.x = self.x = x
        self.rect.y = self.y = y
        # self.rect.x = self.rect.width
        # self.rect.y = self.rect.height
        print(x)
        self.x = float(self.rect.x)
        self.speed = speed

    def check_edges(self):
        r, rscreen = self.rect, self.screen.get_rect()
        return r.right >= rscreen.right+300 or r.left < 0

    def update(self):

        delta = self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x -= delta
        self.x = self.rect.x

    def draw(self):
        # image = Alien.images[self.number]
        # self.screen.blit(image, self.rect)

        image = self.timer.imagerect()
        image = pg.transform.rotozoom(image, 0, 1.4 )
        rect = image.get_rect()
        rect.x, rect.y = self.rect.x, self.rect.y
        self.screen.blit(image, rect)
        # self.screen.blit(self.image, self.rect)

    @staticmethod
    def run_tests():
        print(Alien.images)

