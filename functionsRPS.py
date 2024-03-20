
def PossibleGames(invoer_robot:str, invoer_player:str) -> str:
    if invoer_robot == 'rock' and invoer_player == 'paper':
        return 'je hebt gewonnen!'
    elif invoer_robot == 'paper' and invoer_player == 'rock':
        return 'je hebt verloren!'
    elif invoer_robot == 'paper' and invoer_player == 'scissors':
        return 'je hebt gewonnen!'
    elif invoer_robot == 'scissors' and invoer_player == 'paper':
        return 'je hebt verloren!'
    elif invoer_robot == 'scissors' and invoer_player == 'rock':
        return 'je hebt gewonnen!'
    elif invoer_robot == 'rock' and invoer_player == 'scissors':
        return 'je hebt verloren!'
    elif invoer_robot == 'rock' and invoer_player == 'paper':
        return 'je hebt gewonnen!'
    elif invoer_robot == 'paper' and invoer_player == 'rock':
        return 'je hebt verloren!'
    elif invoer_robot == 'paper' and invoer_player == 'paper':
        return 'je hebt gelijk gespeelt!'
    elif invoer_robot == 'rock' and invoer_player == 'rock':
        return 'je hebt gelijk gespeelt!'
    elif invoer_robot == 'scissors' and invoer_player == 'scissors':
        return 'je hebt gelijk gespeelt!'

