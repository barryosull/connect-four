
import time
from actions import Action, Option
from checker import Checker
from board import Board
from agent import Agent
from actions import Action, Option
from controllers.cli.player_interface import PlayerInterface
from controllers.cli.renderer import Renderer

type Actions = list[Action]

class PlayerAgent(PlayerInterface):

    def __init__(self, checker: Checker, agent: Agent, renderer: Renderer):
        self.checker = checker 
        self.__agent = agent
        self.__renderer = renderer

    def select_action(self, board: Board) -> Action:
        # Pretend to think
        self.__renderer.print_agent_thinking()
        time.sleep(2)
        return self.__agent.select_next_slot(self.checker, board)
