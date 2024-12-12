import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(
    page_title="Celerates's Group 5",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="icons/coffee_ic.png")


columns_data = [
    {
        "image": "images/ireng.jpg",
        "name": "Muhammad 'Pannur' Nur Irfan",
        "description": "Politeknik Negeri Jakarta",
        "caption": "Tukang bersihin cache",
        "buttons": [
            {"label": " ", "icon": ":material/nest_heat_link_gen_3:", "type": "secondary", "url":"https://instagram.com/chifaaanub"},
            {"label": " ", "icon": ":material/deployed_code:", "type": "secondary", "url":"https://github.com/Chifaaan"},
            {"label": " ", "icon": ":material/diversity_3:", "type": "secondary", "url":"https://www.linkedin.com/in/muhammad-nur-irfan/"}
        ]
    },
    {
        "image": "images/friska.jfif",
        "name": "Friska Cindi Claudia Simanjuntak ",
        "description": "Universitas Sumatera Utara",
        "caption": "Tukang ngetik lorem ipsum",
        "buttons": [
            {"label": " ", "icon": ":material/nest_heat_link_gen_3:", "type": "secondary","url":"https://www.instagram.com/aihetmatcha?igsh=bXQ2MG53bng1aWI5"},
            {"label": " ", "icon": ":material/diversity_3:", "type": "secondary","url":"www.linkedin.com/in/friskasimanjuntak"},
            None
            
        ]
    },
    {
        "image": "images/Demon.jpg",
        "name": "M. Singgih Priadi Nugroho",
        "description": "University of Example",
        "caption": "Tukang makan cookies",
        "buttons": [
            {"label": " ", "icon": ":material/nest_heat_link_gen_3:", "type": "secondary","url":" "},
            {"label": " ", "icon": ":material/deployed_code:", "type": "secondary","url":" "},
            {"label": " ", "icon": ":material/diversity_3:", "type": "secondary","url":" "}
        ]
    },
        {
        "image": "images/GH.jpg",
        "name": "Jonathan Matthew Fernaldy",
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
        card = col.container(height=620)
        img = card.container(height=350)
        img.image(data["image"], output_format="PNG", width=280)
        card.html(f"<b style='font-size: 25px;'>{data['name']}</b>")
        card.markdown(data["description"])
        card.caption(data["caption"])

        # Cek jika ada tombol untuk Card ini
        if "buttons" in data and data["buttons"]:
            ig, wa, gh = card.columns((1, 1, 1))
            
            # Buat tombol hanya jika data tombol tidak kosong
            for button, btn_data in zip([ig, wa, gh], data["buttons"]):
                if btn_data is not None:  # Perbaikan di sini
                    button.link_button(
                        label=btn_data["label"],
                        icon=btn_data["icon"],
                        type=btn_data["type"],
                        url=btn_data["url"],
                        use_container_width=True,
                    )

