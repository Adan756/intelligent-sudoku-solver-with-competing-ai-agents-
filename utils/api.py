import requests
from utils.sudoku_generator import generate_sudoku


def get_sudoku(difficulty="easy"):
    url = f"https://sudoku-api.vercel.app/api/dosuku?difficulty={difficulty}"

    try:
        res = requests.get(url, timeout=3)
        data = res.json()

        board = data["newboard"]["grids"][0]["value"]

        # ✅ validate board
        if board and len(board) == 9 and all(len(row) == 9 for row in board):
            print("✅ API Sudoku loaded")
            return board

    except Exception as e:
        print("❌ API failed:", e)

    # 🔥 fallback
    print("⚠ Using local generator")
    return generate_sudoku(difficulty)