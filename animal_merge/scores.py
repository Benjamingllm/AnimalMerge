import json

from .config import SCORES_FILE


def load_scores():
    try:
        with open(SCORES_FILE, encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def write_scores(scores):
    with open(SCORES_FILE, "w", encoding="utf-8") as file:
        json.dump(scores, file, ensure_ascii=False, indent=2)


def save_score(name, score):
    scores = load_scores()
    for entry in scores:
        if entry["name"] == name:
            if score > entry["score"]:
                entry["score"] = score
                write_scores(scores)
            return
            
    scores.append({"name" : name, "score" : score})
    write_scores(scores)

def get_best_score (name):
    scores = load_scores()
    for entry in scores:
        if entry["name"] == name:
            return entry["score"]
    return 0

  

    
    
