
import streamlit as st
import pandas as pd

st.set_page_config(page_title="IATA Message Generator", layout="wide")

st.title("🛫 IATA Message Generator from Excel")

uploaded_file = st.file_uploader("Upload the IATA_Message_Generator.xlsx file", type="xlsx")

if uploaded_file:
    df = pd.read_excel(uploaded_file, sheet_name="Input")
    st.success("✅ File successfully uploaded and read.")

    for idx, row in df.iterrows():
        st.markdown(f"### ✈️ Flight {idx + 1}: {row['Flight Number']} on {row['Date']}")

        mvt = f"""{row['Flight Number']}/{row['Date']}.{row['Registration']}.{row['Departure Airport']}
AD{int(row['AD (Actual Departure Time)']):04}/{int(row['AA (Actual Arrival Time)']):04} EA{int(row['EA (Estimated Arrival)']):04} {row['Arrival Airport']}
{row['Delay 1 Code/Time']}
{row['Delay 2 Code/Time']}
PX{row['PAX Total']}+{row['PAX Infants']}
SI  {row['SI 1']}
SI  {row['SI 2']}"""

        ldm = f"""{row['Flight Number']}/{row['Date']}.{row['Registration']}.{row['LDM - Pax Load Info']}
-{row['LDM - Destination']}.{row['LDM - Bags/Pax Info']}.T{row['LDM - Total Bags Weight']}.{row['LDM - Position Info']}.PAX/{row['LDM - PAX Counts']}.PAD/{row['LDM - PAD Counts']}
SI {row['LDM - SI Line']}"""

        psm = f"""{row['Flight Number']}/{row['PSM - Origin Date']}.{row['PSM - Origin Airport']}
-{row['PSM - SSRs (e.g. WCHR)']}"""

        with st.expander("MVT Message"):
            st.code(mvt, language="plaintext")
        with st.expander("LDM Message"):
            st.code(ldm, language="plaintext")
        with st.expander("PSM Message"):
            st.code(psm, language="plaintext")
