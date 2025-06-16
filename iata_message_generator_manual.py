
import streamlit as st

st.set_page_config(page_title="IATA Message Generator", layout="wide")
st.title("🛫 IATA Message Generator (Manual Input)")

with st.form("manual_form"):
    st.subheader("Flight Details")
    col1, col2, col3, col4 = st.columns(4)
    flight_no = col1.text_input("Flight Number (e.g., XY583)").upper()
    date = col2.text_input("Flight Date (e.g., 16)").upper()
    registration = col3.text_input("Registration (e.g., HZNS28)").upper()
    dep_airport = col4.text_input("Departure Airport").upper()

    col5, col6, col7, col8 = st.columns(4)
    ad_time = col5.text_input("Chocks off Time (e.g., 0453)").upper()
    aa_time = col6.text_input("Airborne Time (e.g., 0501)").upper()
    ea_time = col7.text_input("Estimated Arrival Time (e.g., 0643)").upper()
    arr_airport = col8.text_input("Arrival Airport").upper()

    st.subheader("Delays & Passengers")
    delay1 = st.text_input("Delay 1 Code/Time (e.g., DL16/0016)").upper()
    delay2 = st.text_input("Delay 2 Code/Time (e.g., DL89/0017)").upper()
    pax_total = st.text_input("Total PAX (e.g., 143)").upper()
    infants = st.text_input("Infants (e.g., 01INF)").upper()
    si1 = st.text_input("MVT Remark 1 (e.g., DL16 DUE TO SICK PASSENGER)").upper()
    si2 = st.text_input("MVT Remark 2 (e.g., DL17 DUE ATC)").upper()

    st.subheader("LDM Details")
    pax_load_info = st.text_input("Pax Load Info (e.g., 18BC374Y.2/9)").upper()
    ldm_dest = st.text_input("Destination (e.g., CAI)").upper()
    bag_info = st.text_input("Pax Info (e.g., 138/08/01)").upper()
    bag_weight = st.text_input("Total Bags Weight (e.g., 3093)").upper()
    pos_info = st.text_input("Positions Info (e.g., 1/1400.3/1000.4/693.5/00)").upper()
    pax_count = st.text_input("PAX Counts (e.g., 0/104)").upper()
    pad_count = st.text_input("PAD Counts (e.g., 0/0)").upper()
    ldm_si = st.text_input("LDM SI Line (e.g., FRE 0 POS 0 C 00 BAG 3093 EIC 00 TRA)").upper()

    st.subheader("PSM Details")
    psm_date = st.text_input("Origin Date (e.g., 15)").upper()
    psm_origin = st.text_input("Origin Airport (e.g., JED)").upper()
    ssr = st.text_input("PSM SSRs (e.g., 01 WCHR)").upper()

    submitted = st.form_submit_button("Generate Messages")

if submitted:
    st.subheader("Generated Messages")

    mvt = f"""{flight_no}/{date}.{registration}.{dep_airport}
AD{ad_time}/{aa_time} EA{ea_time} {arr_airport}
{delay1}
{delay2}
PX{pax_total}+{infants}
SI  {si1}
SI  {si2}"""

    ldm = f"""{flight_no}/{date}.{registration}.{pax_load_info}
-{ldm_dest}.{bag_info}.T{bag_weight}.{pos_info}.PAX/{pax_count}.PAD/{pad_count}
SI {ldm_si}"""

    psm = f"""{flight_no}/{psm_date}.{psm_origin}
-{ssr}"""

    with st.expander("MVT Message"):
        st.code(mvt, language="plaintext")
    with st.expander("LDM Message"):
        st.code(ldm, language="plaintext")
    with st.expander("PSM Message"):
        st.code(psm, language="plaintext")
