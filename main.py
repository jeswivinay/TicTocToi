import streamlit as st
import random
import copy

# Function to check for a winner
def check_winner(board):
    """
    Checks the Tic-Tac-Toe board for a winner.
    
    Args:
        board (list of lists): 3x3 game board.
    
    Returns:
        str: 'X' or 'O' if there's a winner, None otherwise.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

# Function to check if the board is full (draw)
def is_full(board):
    """
    Checks if the Tic-Tac-Toe board is full.
    
    Args:
        board (list of lists): 3x3 game board.
    
    Returns:
        bool: True if board is full, False otherwise.
    """
    return all(cell != " " for row in board for cell in row)

# Evaluate the board for minimax
def evaluate(board):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    return 0

# Minimax function
def minimax(board, depth, is_max):
    if check_winner(board) or is_full(board):
        return evaluate(board)
    
    if is_max:  # AI 'O' maximizing
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:  # Human 'X' minimizing
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

# AI move using minimax
def ai_move(board):
    """
    Selects the best move for the AI using minimax.
    
    Args:
        board (list of lists): 3x3 game board.
    
    Returns:
        tuple: (row, col) for the AI's move.
    """
    best_score = -float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# Initialize session state variables
if 'board' not in st.session_state:
    st.session_state.board = [[" " for _ in range(3)] for _ in range(3)]
if 'turn' not in st.session_state:
    st.session_state.turn = "X"  # Human is X, AI is O
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'winner' not in st.session_state:
    st.session_state.winner = None

# Streamlit app title
st.title("Interactive Tic-Tac-Toe Game")
st.subheader("Human (X) vs. AI (O) - Unbeatable AI")

# Display the game board
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        cell_value = st.session_state.board[i][j]
        if cell_value == " " and not st.session_state.game_over and st.session_state.turn == "X":
            # Button for human move
            if cols[j].button(" ", key=f"cell_{i}_{j}"):
                st.session_state.board[i][j] = "X"
                winner = check_winner(st.session_state.board)
                if winner:
                    st.session_state.winner = winner
                    st.session_state.game_over = True
                elif is_full(st.session_state.board):
                    st.session_state.game_over = True
                else:
                    st.session_state.turn = "O"
                    # AI move
                    ai_pos = ai_move(st.session_state.board)
                    if ai_pos:
                        st.session_state.board[ai_pos[0]][ai_pos[1]] = "O"
                        winner = check_winner(st.session_state.board)
                        if winner:
                            st.session_state.winner = winner
                            st.session_state.game_over = True
                        elif is_full(st.session_state.board):
                            st.session_state.game_over = True
                        else:
                            st.session_state.turn = "X"
                st.rerun()
        else:
            # Display occupied cell
            cols[j].markdown(f"<h1 style='text-align: center;'>{cell_value}</h1>", unsafe_allow_html=True)

# Display game status
if st.session_state.game_over:
    if st.session_state.winner:
        st.success(f"Winner: {st.session_state.winner}")
    else:
        st.warning("It's a Draw!")
else:
    st.info(f"Current Turn: {st.session_state.turn}")

# Reset button
if st.button("Reset Game"):
    st.session_state.board = [[" " for _ in range(3)] for _ in range(3)]
    st.session_state.turn = "X"
    st.session_state.game_over = False
    st.session_state.winner = None
    st.rerun()