import pygame

from rule   import Rule
from menu   import Menu

from config import (
    board_size, grid_size,
    black_stone, white_stone,
    white, black, red,
    empty,
)

class Omok(object):
    def __init__(self, surface):
        # surface : 화면에 출력할 때 필요한 변수를 class 멤버 변수로 생성
        self.surface = surface
        # board : 화면의 픽셀 좌표를 순서대로 저장할 이차원 리스트
        self.board = [[0 for i in range(board_size)] for j in range(board_size)]
        # menu : 메뉴와 텍스트를 다루는 class인 객체
        self.menu = Menu(surface)
        # rule : 오목과 관련된 rule을 판별하는 기능을 하게 될 Rule class의 객체
        self.rule = Rule(self.board)
        # pixel_coords : 마우스가 클릭됐을 때의 위치확인 및 board의 좌표를 생성할 때 필요한 모든 칸에 대한 left_top 좌표를 저장할 list 변수
        self.pixel_coords = []
        # is_show : 바둑알에 번호를 넣을지 말지를 결정하는 변수
        self.is_show = True
        # set_coords() : 픽셀 좌표를 구하는 함수
        self.set_coords()
        # set_image_font() : 이미지 객체와 바둑알에 번호를 넣을 때 필요한 image와 font의 객체 생성을 위한 함수
        self.set_image_font()

    # -- 매 게임마다 초기화가 필요한 변수와 함수들을 모아둔 함수
    def init_game(self):
        # turn : 오목은 항상 선이 흑이므로 흑으로 초기화
        self.turn = black_stone
        # coords, redos : 게임 진행 중 취소 또는 다시 실행 할 수 있도록 좌표 데이터를 저장할 list 변수
        self.coords = []
        self.redos = []
        # id : 몇 수가 두어졌나를 기록하는 변수
        self.id = 1
        # is_gameover : 게임의 종료여부를 저장할 변수
        self.is_gameover = False
        # draw_board() : 게임이 끝나고 다시 시작하려면 바둑돌들을 치워야 하므로 보드를 다시 그리기 위한 함수
        self.draw_board()
        # menu.show_msg(EMPTY) : 게임이 끝날 때 화면에 결과를 게임 화면에 표시되므로 이를 지워주기 위한 함수
        self.menu.show_msg(empty)
        # init_board() : 화면을 깨끗이 했으면 저장된 데이터도 초기화하는 함수
        self.init_board()

    # 이미지와 폰트를 생성하는 함수
    def set_image_font(self):
        white_img = pygame.image.load('image/white.png')
        black_img = pygame.image.load('image/black.png')
        self.font = pygame.font.Font("freesansbold.ttf", 14)
        self.white_img = pygame.transform.scale(white_img, (grid_size, grid_size))
        self.black_img = pygame.transform.scale(black_img, (grid_size, grid_size))
        self.last_w_img = pygame.image.load('image/white_a.png')
        self.last_b_img = pygame.image.load('image/black_a.png')
        self.board_img = pygame.image.load('image/board.PNG')

    # 보드를 0으로 초기화
    def init_board(self):
        for y in range(board_size):
            for x in range(board_size):
                self.board[y][x] = 0

    # 보드를 저장되어있는 이미지로 화면을 구성
    def draw_board(self):
        self.surface.blit(self.board_img, (0, 0))

    # 바둑돌을 그리는 함수
    def draw_image(self, img_index, x, y):
        img = [self.black_img, self.white_img, self.last_b_img, self.last_w_img]
        self.surface.blit(img[img_index], (x, y))

    # 바둑돌을 그리는 함수
    def draw_stone(self, coord, stone, increase):
        x, y = self.get_point(coord)
        self.board[y][x] = stone

        for i in range(len(self.coords)):
            x, y = self.coords[i]
            self.draw_image(i % 2, x, y)
        # 마지막 돌은 표시가있는 이미지로 그린다.
        if self.coords:
            x, y = self.coords[-1]
            self.draw_image(i % 2 + 2, x, y)

        self.id += increase
        self.turn = 3 - self.turn

    # 게임 루프가 돌아가는 run_game() 함수에서 마우스가 클릭 되었을 때 호출
    # 화면에서 게임판에서 마우스가 클릭이 되었는지 확인을 위해 get_coord() 함수를 호출하여 확인
    def check_board(self, pos):
        # get_coord : 화면에서 게임판에 마우스가 클릭이 되었는지 확인
        coord = self.get_coord(pos)
        if not coord:
            return False
        x, y = self.get_point(coord)
        if self.board[y][x] != empty:
            return True

        self.coords.append(coord)
        self.draw_stone(coord, self.turn, 1)
        if self.check_gameover(coord, 3 - self.turn):
            self.is_gameover = True
        if len(self.redos):
            self.redos = []
        return True

    def check_gameover(self, coord, stone):
        x, y = self.get_point(coord)
        if self.id > board_size * board_size:
            self.show_winner_msg(stone)
            return True
        elif 5 <= self.rule.is_gameover(x, y, stone):
            self.show_winner_msg(stone)
            return True
        return False

    def show_winner_msg(self, stone):
        for i in range(3):
            self.menu.show_msg(stone)
            pygame.display.update()
            pygame.time.delay(200)
            self.menu.show_msg(empty)
            pygame.display.update()
            pygame.time.delay(200)
        self.menu.show_msg(stone)

    # 픽셀 좌표를 구하는 함수
    def set_coords(self):
        for y in range(board_size):
            for x in range(board_size):
                self.pixel_coords.append((x * grid_size + 25, y * grid_size + 25))

    # 마우스 포인트 좌표를 넘겨받아 픽셀 좌표들과 비교하여 마우스 포인트 좌표가 위치한 곳을 찾는 함수
    def get_coord(self, pos):
        for coord in self.pixel_coords:
            x, y = coord
            rect = pygame.Rect(x, y, grid_size, grid_size)
            if rect.collidepoint(pos):
                return coord
        return None

    # 픽셀 좌표를 board list에 사용될 순서 좌표로 바꿔서 반환
    def get_point(self, coord):
        x, y = coord
        x = (x - 25) // grid_size
        y = (y - 25) // grid_size
        return x, y