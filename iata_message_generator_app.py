
import streamlit as st

st.set_page_config(page_title="IATA Message Generator", layout="wide")

st.title("✈️ IATA Message Generator (MVT, LDM, PSM)")

with st.form("flight_form"):
    st.subheader("Flight Info")
    col1, col2, col3, col4 = st.columns(4)
    flight_no = col1.text_input("Flight Number (e.g., XY583)")
    date = col2.text_input("Flight Date (e.g., 16)")
    iata_code = col3.text_input("IATA Message Code (e.g., HZNS28)")
    dep_airport = col4.text_input("From (Departure Airport)")

    col5, col6, col7, col8 = st.columns(4)
    ad_time = col5.text_input("Actual Departure (e.g., 0453)")
    aa_time = col6.text_input("Actual Arrival (e.g., 0501)")
    ea_time = col7.text_input("Estimated Arrival (e.g., 0643)")
    arr_airport = col8.text_input("To (Arrival Airport)")

    st.subheader("Delays and PAX")
    delay1 = st.text_input("Delay 1 (Code/Time) (e.g., DL16/0016)")
    delay2 = st.text_input("Delay 2 (Code/Time) (e.g., DL89/0017)")
    pax_total = st.text_input("Total Pax (e.g., 143)")
    infants = st.text_input("Infants (e.g., 01INF)")

    st.subheader("Remarks (MVT)")
    si1 = st.text_input("Remark 1 (e.g., DL16 DUE TO SICK PASSENGER)")
    si2 = st.text_input("Remark 2 (e.g., DL17 DUE ATC)")

    st.subheader("LDM Details")
    ldm_pax_info = st.text_input("Pax Load Info (e.g., 18BC374Y.2/9)")
    ldm_dest = st.text_input("Destination (e.g., CAI)")
    ldm_bag_info = st.text_input("Bags/Pax Info (e.g., 138/08/01)")
    ldm_bag_weight = st.text_input("Total Bags Weight (e.g., 3093)")
    ldm_pos_info = st.text_input("Position Info (e.g., 1/1400.3/1000.4/693.5/00)")
    ldm_pax_count = st.text_input("PAX Counts (e.g., 0/104)")
    ldm_pad_count = st.text_input("PAD Counts (e.g., 0/0)")
    ldm_si = st.text_input("LDM Remarks (e.g., FRE 0 POS 0 C 00 BAG 3093 EIC 00 TRA)")

    st.subheader("PSM Details")
    psm_date = st.text_input("Origin Date (e.g., 15)")
    psm_origin = st.text_input("Origin Airport (e.g., JED)")
    ssr = st.text_input("SSR (e.g., 01 WCHR)")

    submitted = st.form_submit_button("Generate Messages")

if submitted:
    st.subheader("Generated Messages")

    mvt = f"""{flight_no}/{date}.{iata_code}.{dep_airport}
AD{ad_time}/{aa_time} EA{ea_time} {arr_airport}
{delay1}
{delay2}
PX{pax_total}+{infants}
SI  {si1}
SI  {si2}"""

    ldm = f"""{flight_no}/{date}.{iata_code}.{ldm_pax_info}
-{ldm_dest}.{ldm_bag_info}.T{ldm_bag_weight}.{ldm_pos_info}.PAX/{ldm_pax_count}.PAD/{ldm_pad_count}
SI {ldm_si}"""

    psm = f"""{flight_no}/{psm_date}.{psm_origin}
-{ssr}"""

    st.code(mvt, language="plaintext")
    st.code(ldm, language="plaintext")
    st.code(psm, language="plaintext")
