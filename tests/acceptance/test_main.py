
import subprocess

class TestMain:

    def test_playing_a_game(self):

        # Arrange
        player1Actions = "1 1 1 1"
        player2Actions = "2 2 2 2"

        # Act
        command = f"python /app/src/main.py --player1Actions {player1Actions} --player2Actions {player2Actions}"
        result = subprocess.check_output(command, shell=True, text=True)
        
        # Assert
        assert ("The winner is 'r'" in result)
        assert ("Thanks for playing!" in result)


    def test_quitting_a_game(self):

        # Arrange
        player1Actions = "1 1 1 q"
        player2Actions = "2 2 2 2"

        # Act
        command = f"python /app/src/main.py --player1Actions {player1Actions} --player2Actions {player2Actions}"
        result = subprocess.check_output(command, shell=True, text=True)
        
        # Assert
        assert ("The winner is 'r'" not in result)
        assert ("Thanks for playing!" in result)