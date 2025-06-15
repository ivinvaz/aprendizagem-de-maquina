from logic import *


def play_game():
    while True:
        board = initial_state()
        print("Bem-vindo ao Jogo da Velha!")
        print("Você é 'X' e o computador é 'O'.")

        current_turn_player = X 

        while not terminal(board):
            print_board(board)
            current_player_symbol = player(board)
            
            if current_player_symbol == X: 
                print(f"É a vez do jogador {current_player_symbol}.")
                possible_moves = actions(board)

                display_moves = []
                for r, c in possible_moves:
                    if r == 0: display_moves.append(str(c + 1))
                    elif r == 1: display_moves.append(str(c + 4))
                    else: display_moves.append(str(c + 7))
                display_moves.sort()
                print(f"Movimentos disponíveis (1-9): {', '.join(display_moves)}")

                while True:
                    try:
                        user_input = input("Escolha sua jogada (1-9): ")
                        action = map_input_to_coords(user_input)
                        if action in possible_moves:
                            board = result(board, action)
                            break
                        else:
                            print("Entrada inválida ou posição já ocupada. Tente novamente.")
                    except (ValueError, KeyError):
                        print("Entrada inválida. Por favor, digite um número de 1 a 9.")
            else: # Computador (Minimax)
                print(f"É a vez do computador ({current_player_symbol}).")
                print("Computador pensando...")
                action = minimax(board)
                board = result(board, action)
                
        print_board(board)

        game_winner = winner(board)
        if game_winner == X:
            print("\nParabéns! Você (X) ganhou!\n")
        elif game_winner == O:
            print("\nO computador (O) ganhou!\n")
        else:
            print("\nEmpate!\n")

        play_again = input("Jogar novamente? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    play_game()