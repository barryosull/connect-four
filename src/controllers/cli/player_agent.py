import time
from domain.actions import Action
from domain.checker import Checker
from domain.board import Board
from domain.agent import Agent
from controllers.cli.player_interface import PlayerInterface
from controllers.cli.renderer import Renderer

type Actions = list[Action]

# Player that is controlled by a basic agent


class PlayerAgent(PlayerInterface):
    def __init__(
        self, checker: Checker, agent: Agent, renderer: Renderer, sleep_time: int = 2
    ):
        self.checker = checker
        self.__agent = agent
        self.__renderer = renderer
        self.__sleep_time = sleep_time

    def select_action(self, board: Board) -> Action:
        # Pretend to think
        self.__renderer.print_agent_thinking(self.checker)
        time.sleep(self.__sleep_time)

        return self.__agent.select_next_slot(self.checker, board)
