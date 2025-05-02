from streamlit import columns, header, image, info, set_page_config, subheader, title, write
from pandas import read_csv

set_page_config(layout='wide')
col1, col2 = columns(2)

with col1:
    image("images/photo.jpg")

with col2:
    title('Victor Das')
    content = """
    A seasoned software engineer with 15 years of experience building 
    scalable and reliable systems across diverse industries. Passionate 
    about technology and problem-solving, they’ve contributed to global 
    projects while traveling extensively across multiple countries. 
    This international exposure has enriched their perspective, strengthened 
    cross-cultural collaboration skills, and deepened their understanding 
    of user needs in various markets.
    """

    info(content)

subheader("""
Below you can find some cool Python apps
""")

col3, spacer, col4 = columns([1.5, 0.5, 1.5])

df = read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        header(row['title'])
        write(row['description'])
        image(f"images/{row['image']}")
        write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        header(row['title'])
        write(row['description'])
        image(f"images/{row['image']}")
        write(f"[Source Code]({row['url']})")
