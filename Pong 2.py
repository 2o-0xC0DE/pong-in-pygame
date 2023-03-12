import pygame, random, time
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
MIN_SPEED, MAX_SPEED = 5, 7
PADDLE_WIDTH, PADDLE_HEIGHT = 60, 7
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
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
		self.game_over_end = 0
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
				self.game_over_end = time.time() + 3
				self.move_ball = False
		elif time.time() < self.game_over_end:
			text = self.font.render("Ви програли", True, (255, 255, 255))
			screen.blit(text, (text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))))
		else:
			self.move_ball = True
			self.x = SCREEN_WIDTH // 2
			self.y = SCREEN_HEIGHT // 2
			self.dx = random.choice((random.randint(MIN_SPEED, MAX_SPEED), random.randint(-MAX_SPEED, -MIN_SPEED)))
			self.dy = random.choice((random.randint(MIN_SPEED, MAX_SPEED), random.randint(-MAX_SPEED, -MIN_SPEED)))

class Paddle:
	def __init__(self, screen, ball, color, x, y, width, height):
		self.speed = 7
		self.ball = ball
		self.screen = screen
		self.color = color
		self.x, self.y = x, y
		self.width, self.height = width, height
	def move(self):
		dx = 0
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RIGHT]:
			dx = self.speed
		if keys[pygame.K_LEFT]:
			dx = -self.speed
		if self.x <= 0:
			self.x = 1
			dx = 0
		elif self.x >= SCREEN_WIDTH - self.width:
			self.x = SCREEN_WIDTH - self.width - 1
			dx = 0
		self.x += dx

		if self.x <= self.ball.x - self.ball.radius <= self.x + self.width:
			if self.y <= self.ball.y + self.ball.radius <= self.y + self.height:
				self.ball.dy = -self.ball.dy
	def draw(self):
		pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

ball = Ball(screen, 250, 250, random.choice(
	(random.randint(MIN_SPEED, MAX_SPEED), random.randint(-MAX_SPEED, -MIN_SPEED))
	), random.choice(
	(random.randint(MIN_SPEED, MAX_SPEED), random.randint(-MAX_SPEED, -MIN_SPEED))
	), 8, (255, 255, 255))
paddle = Paddle(screen, ball, (255, 255, 255), SCREEN_WIDTH / 2 - PADDLE_WIDTH / 2, 400, PADDLE_WIDTH, PADDLE_HEIGHT)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	screen.fill((0, 0, 0))
	ball.move()
	ball.draw()
	paddle.move()
	paddle.draw()

	pygame.display.set_caption(f"Pong | {round(clock.get_fps(), 2)} FPS")
	pygame.display.flip()
	clock.tick(60)