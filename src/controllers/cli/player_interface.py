
from abc import ABC, abstractmethod
from board import Board
from checker import Checker
from actions import Action

class PlayerInterface(ABC):

   checker = '-' 

   @abstractmethod
   def select_action(self, board: Board) -> Action:
      print ("Abstract method, please implement")
      return Option.QUIT