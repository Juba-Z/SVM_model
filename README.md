# 🧩 8-Puzzle Game

A Python implementation of the classic **8-Puzzle** sliding tile game, featuring both manual play and an AI-powered auto-solver using **Greedy Best-First Search** with Manhattan Distance heuristic.

---

## 📌 Description

The 8-puzzle is a 3×3 grid with tiles numbered 1–8 and one blank space. The goal is to slide tiles into the correct order:

```
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 7 | 8 |   |
+---+---+---+
```

This project lets you either play manually or watch an AI solve it step by step.

---

## 🚀 Features

- **Manual Mode** — Play the puzzle yourself with keyboard input
- **Auto Solve Mode** — Let the AI solve any puzzle instantly
- **Hint System** — Get a one-step hint powered by the solver
- **Solvability Check** — Only generates puzzles that are actually solvable (inversion count parity)
- **Step-by-step Visualization** — Watch each move in the terminal with a clear grid display
- **Performance Stats** — See how many nodes the algorithm expanded to find the solution

---

## 🧠 Algorithm

The solver uses **Greedy Best-First Search** with **Manhattan Distance** as the heuristic.

| Property | Detail |
|---|---|
| Algorithm | Greedy Best-First Search |
| Heuristic | Manhattan Distance |
| Data Structure | Min-Heap (priority queue) |
| Completeness | ✅ Complete (for solvable states) |
| Optimality | ❌ Not guaranteed to find shortest path |

**Manhattan Distance** measures how far each tile is from its goal position (sum of row + column distances), giving the algorithm a strong directional signal toward the solution.

---

## 🛠️ Requirements

- Python 3.x
- No external libraries required (uses only `random`, `copy`, `heapq` from the standard library)

---

## ▶️ How to Run

```bash
python puzzle.py
```

Then choose from the menu:

```
==========================================
          8-PUZZLE GAME
==========================================

1. Play manually
2. Auto solve
3. Exit
```

### Manual Mode Controls

| Input | Action |
|---|---|
| `1`–`4` | Select a move from the listed options |
| `h` | Get a hint (shows best next move) |
| `s` | Auto-solve from current state |
| `q` | Quit the game |

---

## 📂 Project Structure

```
8-puzzle/
│
└── puzzle.py       # Main game file (all logic in one file)
```

---

## 📖 How It Works

1. A random solvable board is generated using a **shuffle + inversion parity check**
2. At each step, valid moves are found by locating the blank tile and swapping with neighbors
3. In auto-solve mode, the greedy search expands the state with the lowest Manhattan distance first
4. The solution path is stored and can be replayed step by step

---

## ⚠️ Limitations

- Greedy search does **not** guarantee the shortest solution path
- For optimal solutions, consider upgrading to **A\*** (by adding `g` — path cost — to the priority)
- No GUI (terminal only)

---

## 💡 Possible Improvements

- [ ] Implement **A\*** search for optimal solutions
- [ ] Add a **GUI** using `tkinter` or `pygame`
- [ ] Track and display **best score** (fewest moves)
- [ ] Add difficulty levels (easy / medium / hard based on shuffle depth)
- [ ] Add **IDA\*** for memory-efficient solving

---

## 📄 License

This project is open source and free to use.
