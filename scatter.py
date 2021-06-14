import csv
import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
print(df.groupby(["student_id", "level"], as_index=False)["attempt"].mean())
a = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()

fig = px.scatter(a,x="student_id",y="level",color="attempt",size="attempt")
fig.show()