
def PossibleGames(invoer_robot:str, invoer_player:str) -> str:
    if invoer_robot == 'rock' and invoer_player == 'paper':
        return 'u won!'
    elif invoer_robot == 'paper' and invoer_player == 'rock':
        return 'u lost! :('
    elif invoer_robot == 'paper' and invoer_player == 'scissors':
        return 'u won!'
    elif invoer_robot == 'scissors' and invoer_player == 'paper':
        return 'u lost! :('
    elif invoer_robot == 'scissors' and invoer_player == 'rock':
        return 'u won!'
    elif invoer_robot == 'rock' and invoer_player == 'scissors':
        return 'u lost! :('
    elif invoer_robot == 'rock' and invoer_player == 'paper':
        return 'u won!'
    elif invoer_robot == 'paper' and invoer_player == 'rock':
        return 'u lost! :('
    elif invoer_robot == 'paper' and invoer_player == 'paper':
        return "it's a draw! :O"
    elif invoer_robot == 'rock' and invoer_player == 'rock':
        return "it's a draw! :O"
    elif invoer_robot == 'scissors' and invoer_player == 'scissors':
        return "it's a draw! :O"

