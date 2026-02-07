import pandas as pd
import numpy as np
from itertools import product

regions = ["Gorenjska", "Primorska", "Štajerska", "Dolenjska", "Prekmurje", "Koroška"]
months = range(1, 13)

combinations = list(product(regions, months))

data = {
    "Regija": [combo[0] for combo in combinations],
    "Mesec": [combo[1] for combo in combinations],
    "Št. turistov": np.random.randint(100, 5000, size=len(combinations)),
    "Povprečna nočitev (noči)": np.random.randint(1, 7, size=len(combinations))
}

df = pd.DataFrame(data)
df.to_csv("vhodni-podatki-turizem.csv", index=False)