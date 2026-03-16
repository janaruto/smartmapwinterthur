import streamlit as st

st.set_page_config(page_title="Smartmap Winterthur", layout="wide")

st.title("Smartmap Winterthur")

st.markdown("""
### ⚠️ Visualization temporarily unavailable

Unfortunately the Smartmap visualization is **currently offline**.

I was a bit of a *naughty data scientist* and did not fully follow the **legal and data usage requirements** regarding the smartvote dataset before publishing the visualization.

After being kindly contacted by **smartvote**, I have therefore **removed the dataset and the visualization** until the data usage can be clarified properly.

The data used in this project originates from **smartvote.ch** and is subject to their terms of use.  
Datasets may not be redistributed without prior permission.

See the official terms here:  
https://smartvote.ch/de/legal-and-privacy

### What happens next?

I will reach out to smartvote to clarify whether the data can be used under the appropriate conditions.  
If permission is granted, the visualization will come back online.

Until then, please stay tuned.

---

🙏 Many thanks to **smartvote** for their work in providing high-quality political transparency tools.

**Jan Guddal**
""")