import pygame

from pygame.locals      import (
    QUIT,
    MOUSEBUTTONUP
)

from menu       import Menu
from omok       import Omok
from config     import *

class Execution:

    def main(self):
        # py게임을 사용하기 위한 기본 선행 코드
        pygame.init()
        surface = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Omok Game")
        surface.fill(bg_color)

        # 게임이 계속 진행되도록 다시 시작할 수있도록 하는 코드
        omok = Omok(surface)
        menu = Menu(surface)
        while True:
            self.run_game(surface, omok, menu)
            menu.is_continue(omok)

    def run_game(self, surface, omok, menu):
        omok.init_game()
        while True:
            for event in pygame.event.get():
                # 종료
                if event.type == QUIT:
                    menu.terminate()
                # 마우스 버튼이 클릿됐을 때
                elif event.type == MOUSEBUTTONUP:
                    # 보드가 아닌 곳에 마우스가 클릭됐을 때
                    if not omok.check_board(event.pos):
                        # 메뉴가 클릭됐는지 확인
                        if menu.check_rect(event.pos, omok):
                            omok.init_game()
            # 매 프레임마다 게임이 종료되었는지 확인
            if omok.is_gameover:
                return

            #
            pygame.display.update()
            fps_clock.tick(fps)


if __name__ == '__main__':
    myomok = Execution()
    myomok.main()