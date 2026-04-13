\# 🧩 Intelligent Sudoku Solver with AI Agents



A visually interactive Sudoku game where two AI agents — \*\*DFS\*\* and \*\*BFS\*\* — race each other to solve a puzzle in real time. Built with Python and Pygame.



\---



\## 🎮 Demo



Two robot agents compete side by side on screen, each solving the same Sudoku board using a different algorithm. The faster agent wins!



\---



\## ✨ Features



\- 🤖 \*\*DFS Agent\*\* — Solves using Depth-First Search with backtracking

\- 🔍 \*\*BFS Agent\*\* — Solves using Breadth-First Search with a 15-second timeout

\- 🎯 \*\*Live Animation\*\* — Watch both agents fill the board step by step in real time

\- 🏆 \*\*Winner Detection\*\* — The agent with the faster solve time is declared the winner

\- 🌐 \*\*Online Puzzle Fetching\*\* — Fetches real Sudoku puzzles from a public API

\- ⚙️ \*\*Local Fallback Generator\*\* — Generates puzzles locally if the API is unavailable

\- 🎚️ \*\*Difficulty Selection\*\* — Choose from Easy, Medium, Hard, or Random

\- 🖥️ \*\*Fullscreen GUI\*\* — Clean, dark-themed fullscreen interface built with Pygame



\---



\## 🗂️ Project Structure



```

intelligent-sudoku-solver-with-ai-agents/

│

├── main.py                  # Entry point — launches the game

│

├── agents/

│   ├── bfs\_agent.py         # BFS-based Sudoku solving agent

│   └── dfs\_agent.py         # DFS-based Sudoku solving agent with backtracking

│

├── gui/

│   ├── start\_screen.py      # Title/welcome screen

│   ├── difficulty\_screen.py # Difficulty selection screen

│   ├── versus\_screen.py     # VS intro screen before the race begins

│   ├── game\_screen.py       # Main game loop and animation logic

│   └── grid\_ui.py           # Sudoku grid rendering

│

├── utils/

│   ├── api.py               # Fetches Sudoku puzzles from external API

│   ├── sudoku\_generator.py  # Local puzzle generator (fallback)

│   ├── validator.py         # Validates number placement for agents

│   └── solutions.py         # Solution utilities

│

├── assets/                  # Robot character images and VS screen visuals

│

└── requirements.txt         # Python dependencies

```



\---



\## ⚙️ How It Works



1\. \*\*Start Screen\*\* — Press Enter or Right Arrow to begin

2\. \*\*Difficulty Screen\*\* — Select Easy, Medium, Hard, or Random using arrow keys

3\. \*\*Puzzle Loading\*\* — The game fetches a real Sudoku board from an API (falls back to local generator if offline)

4\. \*\*VS Screen\*\* — A dramatic intro before the race

5\. \*\*Race!\*\* — Both agents solve the board simultaneously in background threads, then the animation plays showing each agent's steps

6\. \*\*Winner\*\* — The agent with the lower solve time wins and is announced on screen



\---



\## 🧠 Algorithms



\### DFS Agent (`agents/dfs\_agent.py`)

Uses recursive \*\*Depth-First Search\*\* with backtracking. Tries placing numbers 1–9 in each empty cell and backtracks when a dead end is reached. Fast and memory-efficient.



\### BFS Agent (`agents/bfs\_agent.py`)

Uses \*\*Breadth-First Search\*\* with a queue of board states. Explores possibilities level by level. Has a \*\*15-second timeout\*\* to prevent infinite loops on complex boards.



\---



\## 🚀 Getting Started



\### Prerequisites

\- Python 3.10 or higher

\- pip



\### Installation



```bash

\# 1. Clone the repository

git clone https://github.com/YOUR\_USERNAME/intelligent-sudoku-solver-with-ai-agents.git



\# 2. Navigate into the project folder

cd intelligent-sudoku-solver-with-ai-agents



\# 3. (Optional) Create and activate a virtual environment

python -m venv venv

venv\\Scripts\\activate        # Windows

source venv/bin/activate     # Mac/Linux



\# 4. Install dependencies

pip install -r requirements.txt



\# 5. Run the game

python main.py

```



\---



\## 🕹️ Controls



| Key | Action |

|-----|--------|

| `Enter` / `→` | Confirm / Next screen |

| `←` | Go back |

| `↑` / `↓` | Navigate difficulty options |

| `Enter` (in game) | Skip animation to final result |



\---



\## 📦 Dependencies



| Package | Purpose |

|---------|---------|

| `pygame` | GUI, rendering, and game loop |

| `requests` | Fetching Sudoku puzzles from the API |



\---



\## 🌐 Sudoku API



Puzzles are fetched from:

```

https://sudoku-api.vercel.app/api/dosuku?difficulty={difficulty}

```

If the API is unavailable or times out, the game falls back to a locally generated puzzle.



\---



\## 👥 Authors



> Developed as an AI Mini Project (Project I)



\---



\## 📄 License



This project is for educational purposes.

