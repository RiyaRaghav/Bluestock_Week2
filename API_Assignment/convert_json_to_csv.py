import json
import pandas as pd

with open("Bluestock_Week2/API_Assignment/posts_user1.json", "r", encoding="utf-8") as file:
    data = json.load(file)

df = pd.DataFrame(data)

df.to_csv("Bluestock_Week2/API_Assignment/posts_user1.csv", index=False)

print("JSON successfully converted to CSV.")
print(df)