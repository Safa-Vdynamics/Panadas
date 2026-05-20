import pandas as pd

df = pd.DataFrame(
    {
        "Species": ["Chinook", "Chum", "Coho", "Steelhead", "Bull Trout"],
        "Population": [
            "Skokomish",
            "Lower Skokomish",
            "Skokomish",
            "Skokomish",
            "SF Skokomish",
        ],
        "Count": [1208, 2396, 3220, 6245, 8216],
    }
)


print(df)
