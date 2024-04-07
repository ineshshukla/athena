# Athena
Athena is a Python-based chess engine using minimax algorithm with alpha-beta pruning, piece-square tables, Simplified Evaluation Function and move ordering

### Features
---------
- **Alpha-beta Pruning:** Implements alpha-beta pruning for move searching to improve efficiency.
- **Move Ordering:** Orders moves based on heuristics like captures and promotions to prioritize more promising moves.
- **Evaluation Function:** Utilizes Tomasz Michniewski's Simplified Evaluation Function along with piece-square tables for board evaluation.
- **Quiescence Search:** Implements quiescence search to handle positions with high tactical activity and reduce horizon effects.
- **UCI Protocol Support:** Implements a slice of the Universal Chess Interface (UCI) to allow interaction with chess GUIs like lichess.org.
- **Command-line Interface:** Provides a simple command-line user interface for playing chess against the engine.


### Use it via Command Line
---------
Start the engine with:

```python UI.py```

```
  8 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
  7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
  6  · ·  ·  ·  ·  ·  · ·
  5  · ·  ·  ·  ·  ·  · ·
  4  · ·  ·  ·  ·  ·  · ·
  3  · ·  ·  ·  ·  ·  · ·
  2 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
  1 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
    a b c d e f g h

Your move (e.g. g1h3):
```



## UCI Engine
---------
Start the engine with:

```python main.py```

The engine supports the UCI protocol for communication with compatible GUIs. Refer to the UCI interface documentation for more information on interaction.


## Lichess.org
---------
You can play against the engine on lichess.org using the ShailChoksi/lichess-bot bridge and a BOT account. See the section on lichess.org in the Usage instructions for more details.

