import pandas as pd
def load_reviews(filepath="reviews_segment.pkl"):
    df = pd.read_pickle(filepath)
    return df;

if __name__ == "__main__":
    df = load_reviews()
    print("Columns:", df.columns.tolist())
    print(df.head(5))



