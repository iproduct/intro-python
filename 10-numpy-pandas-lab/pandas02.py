import numpy as np
import pandas as pd

if __name__ == "__main__":
    pd.options.display.max_rows = 9999
    workouts = pd.read_csv("data/workouts.csv")
    workouts.to_json("data/workouts.json")
    workouts2 = pd.read_json("data/workouts.json")
    print(workouts2)
    print(workouts2.info())