import pygame, random
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
MIN_SPEED, MAX_SPEED = 5, 7
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

class Ball:
	def __init__(self, screen, x, y, dx, dy, radius, color):
		self.x, self.y = x, y
		self.dx, self.dy = dx, dy
		self.radius = radius
		self.color = color
		self.screen = screen
		self.move_ball = True
		self.font = pygame.font.SysFont("Arial", 16, True, False)
	def draw(self):
		pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
	def move(self):
		if self.move_ball:
			self.x += self.dx
			self.y += self.dy
			if self.x <= self.radius or self.x >= SCREEN_WIDTH - self.radius:
				self.dx = -self.dx
			if self.y <= 0:
				self.dy = -self.dy
			if self.y >= SCREEN_HEIGHT - self.radius:
				self.move_ball = False
		else:
			text = self.font.render("Ви програли", True, (255, 255, 255))
			screen.blit(text, (text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))))
			pass

class Paddle:
	pass

ball = Ball(screen, 250, 250, random.choice(
	(random.randint(MIN_SPEED, MAX_SPEED), random.randint(-MAX_SPEED, -MIN_SPEED))
	), random.choice(
	(random.randint(MIN_SPEED, MAX_SPEED), random.randint(-MAX_SPEED, -MIN_SPEED))
	), 8, (255, 255, 255))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	screen.fill((0, 0, 0))
	ball.move()
	ball.draw()

	pygame.display.set_caption(f"Pong | {round(clock.get_fps(), 2)} FPS")
	pygame.display.flip()
	clock.tick(60)