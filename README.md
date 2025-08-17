# Tic-Tac-Toe Game with Unbeatable AI

Interactive Tic-Tac-Toe built with **Streamlit**. Human (**X**) vs. AI (**O**) using **minimax with alpha–beta pruning** for unbeatable play.

---

## Features

* **Unbeatable AI** that prioritizes wins, blocks the opponent, and forces draws
* **Real-time** game board updates
* **Game status** display (turn, winner, draw)
* **Reset** button

---

## Requirements

* Python **3.8+**
* Streamlit (`pip install streamlit`)

---

## Installation

```bash
# Clone repo
git clone <repo-url>
cd <repo-folder>

# Install dependencies
pip install -r requirements.txt
# or directly
pip install streamlit
```

---

## Usage

```bash
streamlit run app.py
```

**How to play**

* Click empty cells to play as **X**
* AI responds as **O**
* Click **Reset** to start a new game

---

## Code Structure

* `check_winner(board)`: Detects winner
* `is_full(board)`: Checks draw
* `evaluate(board)`: Scores board
* `minimax(board, depth, alpha, beta, is_maximizing)`: Recursive AI logic with pruning
* `ai_move(board)`: Selects best AI move
* **Streamlit UI**: Handles board, turns, status

---

