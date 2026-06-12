import requests

def fetch_difficulty_data():
    url = "https://kenkoooo.com/atcoder/resources/problem-models.json"
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"取得失敗: {e}")
        return None

from pathlib import Path

def get_problem_ids(directory: str) -> list[str]:
    dir_path = Path(directory)
    problem_ids = []
    
    for file in dir_path.iterdir():
        if file.is_file():
            problem_id = file.stem
            problem_ids.append(problem_id)
    
    return problem_ids

def get_color_folder(difficulty) -> str:
    if difficulty is None:
        return "unclassified"
    if difficulty < 400:
        return "gray"
    elif difficulty < 800:
        return "brown"
    elif difficulty < 1200:
        return "green"
    elif difficulty < 1600:
        return "cyan"
    elif difficulty < 2400:
        return "blue"
    elif difficulty < 2800:
        return "yellow"
    elif difficulty < 3200:
        return "orange"
    else:
        return "red"