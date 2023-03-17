# %%
import pandas as pd
import numpy as np

a = np.random.randint(0, 10, 24).reshape(4,6)
df = pd.DataFrame(a, index=list("가나다라"), columns=list("ABCDEF"))
df


# %%
df

# %%
df["A"]

# %%
df[["B", "C", "D"]]

# %%
df

# %%
df.loc["가", "A"]

# %%
df.loc["가":"다", "A":"D"]

# %%
df.loc["가":"다", ["A", "E", "E", "B"]]

# %%
df.loc["가":"다"]

# %%
df.iloc[0]

# %%



