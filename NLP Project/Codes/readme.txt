This project implements and evaluates three methods (Baseline, Advanced M1, Advanced M2) for retrieving relevant Amazon reviews based on specific 
query aspects such as audio quality, GPS map usability, image quality, Wi-Fi signal strength, and mouse button performances.

reviews_segment.pkl: Contains the main review dataset with fields: review_id, review_text, review_title, and customer_review_rating.

src/
Source code for loading data, filtering reviews, and runing different search models: 
    baseline_boolean.py
    load_data.py
    m1.py
    m2.py

outputs/
Contains output .txt files with top retrieved reviews IDs per query and method.

Queries Evaluated
    audio_quality
    wifi_signal
    mouse_button
    gps_map
    image_quality

Methods 
    Baseline: Simple boolean keyword matching on review text.
    Advanced M1: Improved keyword matching with reduced noise.
    Advanced M2: Proximity-based matching, rating polarity constraints, and opinion-word filtering.

How to Run 
    1. Ensure Python 3.8+ installed
    2. Install required packages (if any): pip install pandas
    3. Run baseline_boolean.py/m1.py/m2.py in order to retrieve the related reviews.