import pandas as pd
import re 
import os

def load_data(path="C:/Users/Santiago/Desktop/something_project/reviews_segment.pkl"):
    df = pd.read_pickle(path)
    df["review_text_clean"] = df["review_text"].astype(str).str.lower()
    return df

queries = {
    "audio_quality": ("audio", "quality", ["poor"]),
    "wifi_signal": ("wifi", "signal", ["strong"]),
    "mouse_button": ("mouse", "button", ["click", "problem"]),
    "gps_map": ("gps", "map", ["useful"]),
    "image_quality": ("image", "quality", ["sharp"])
}

def match_test(review, aspect1, aspect2, opinions, test_type):
    text = review.lower()
    match = False
    if test_type == 1:
        match = aspect1 in text or aspect2 in text
    elif test_type == 2:
        for op in opinions:
            if (aspect1 in text and op in text) or (aspect2 in text and op in text):
                match = True
                break
    elif test_type == 3:
        match = any(term in text for term in [aspect1, aspect2] + opinions)

    return match

def run_baseline(df, queries):
    output_dir = "Baseline_model"
    os.makedirs(output_dir, exist_ok=True)

    for query_name, (a1, a2, ops) in queries.items():
        for test_num in [1,2,3]:
            filename = f"{output_dir}/{query_name}_test{test_num}.txt"
            with open(filename, "w") as f:
                for _, row in df.iterrows():
                    if match_test(row["review_text_clean"], a1, a2, ops, test_num):
                        f.write(row["review_id"].replace("'", "") + "\n")
    
    print("Base line output files saved in:", output_dir)

if __name__ == "__main__":
    df = load_data("reviews_segment.pkl")
    run_baseline(df, queries)