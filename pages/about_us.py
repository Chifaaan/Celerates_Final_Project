import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(
    page_title="Celerates's Group 5",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="icons/smart_toy.svg")


columns_data = [
    {
        "image": "images/sidungu.png",
        "name": "Muhammad Nur Irfan",
        "description": "Politeknik Negeri Jakarta",
        "caption": "Tukang bersihin cache",
        "buttons": [
            {"label": " ", "icon": ":material/nest_heat_link_gen_3:", "type": "secondary", "url":"https://instagram.com/pannuromon_"},
            {"label": " ", "icon": ":material/deployed_code:", "type": "secondary", "url":"https://github.com/Chifaaan"},
            {"label": " ", "icon": ":material/diversity_3:", "type": "secondary", "url":"https://www.linkedin.com/in/muhammad-nur-irfan/"}
        ]
    },
    {
        "image": "images/sidungu.png",
        "name": "John Doe",
        "description": "University of Example",
        "caption": "Tukang ngetik lorem ipsum",
        "buttons": [
            {"label": " ", "icon": ":material/nest_heat_link_gen_3:", "type": "secondary","url":" "},
            {"label": " ", "icon": ":material/deployed_code:", "type": "secondary","url":" "},
            {"label": " ", "icon": ":material/diversity_3:", "type": "secondary","url":" "}
        ]
    },
    {
        "image": "images/sidungu.png",
        "name": "John Doe",
        "description": "University of Example",
        "caption": "Tukang makan cookies",
        "buttons": [
            {"label": " ", "icon": ":material/nest_heat_link_gen_3:", "type": "secondary","url":" "},
            {"label": " ", "icon": ":material/deployed_code:", "type": "secondary","url":" "},
            {"label": " ", "icon": ":material/diversity_3:", "type": "secondary","url":" "}
        ]
    },
        {
        "image": "images/sidungu.png",
        "name": "John Doe",
        "description": "University of Example",
        "caption": "Tukang mainan cloud",
        "buttons": [
            {"label": " ", "icon": ":material/nest_heat_link_gen_3:", "type": "secondary","url":" "},
            {"label": " ", "icon": ":material/deployed_code:", "type": "secondary","url":" "},
            {"label": " ", "icon": ":material/diversity_3:", "type": "secondary","url":" "}
        ]
    }
]
st.markdown("<h1 style='text-align: center;'>Meet Our Team</h1>", unsafe_allow_html=True)
st.caption("<i style='text-align: center;'>This group is a powerhouse of ambitious students from diverse universities, united by a shared passion for excellence and a relentless drive to conquer every challenge that comes their way! Brought together by the visionary leadership of Ceretates, this team is on a mission to dominate the world of Data Science, one obstacle at a time.</i>", unsafe_allow_html=True)
add_vertical_space(5)
st.subheader("Group 5 of Celerates's Data Science Track")



# Create 4 columns dynamically
cols = st.columns(len(columns_data))
for idx, (col, data) in enumerate(zip(cols, columns_data)):
    with col:
        card = col.container(height = 650)
        card.image(data["image"], output_format="PNG", width=400)
        card.html(f"<b style='font-size: 20px;'>{data['name']}</b>")
        card.markdown(data["description"])
        card.caption(data["caption"])
        ig, wa, gh = card.columns((1, 1, 1))
        for i, (button, btn_data) in enumerate(zip([ig, wa, gh], data["buttons"])):
            button.link_button(
                label=btn_data["label"],
                icon=btn_data["icon"],
                type=btn_data["type"],
                url=btn_data["url"],
                use_container_width=True,
            )

