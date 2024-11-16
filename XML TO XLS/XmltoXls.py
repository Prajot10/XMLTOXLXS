import pandas as pd

# Read XML file
df = pd.read_xml("file.xml")

# Save as Excel
df.to_excel("file.xlsx", index=False)
