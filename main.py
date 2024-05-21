from matplotlib import pyplot as plt
from matplotlib_venn import venn2
import matplotlib_fontja  # noqa
import streamlit as st

st.set_page_config(page_title="ベン図を描くアプリ", page_icon=":bar_chart:")
st.title("ベン図を描こう")
st.markdown(
    "[matplotlib-venn](https://github.com/konstantint/matplotlib-venn) を使ってベン図を描くアプリです。"
)

col1, col2, col3 = st.columns(3)
with col1:
    left = st.number_input("左集合の数", step=1, value=1)
    left_label = st.text_input("左集合のラベル", "Left")
with col2:
    common = st.number_input("共通集合の数", step=1, value=2)
with col3:
    right = st.number_input("右集合の数", step=1, value=3)
    right_label = st.text_input("右集合のラベル", "Right")

with st.expander("詳細設定"):
    colx, coly = st.columns(2)
    with colx:
        x = st.number_input("横幅px", step=1, value=6)

        left_color_pick = st.color_picker("左集合の色", "#FF4000")
        left_color_text = st.text_input("左の英語色名(優先される)", "")
        left_color = left_color_pick if left_color_text == "" else left_color_text
    with coly:
        y = st.number_input("縦幅px", step=1, value=6)

        right_color_pick = st.color_picker("右集合の色", "#0051FF")
        right_color_text = st.text_input("右の英語色名(優先される)", "")
        right_color = right_color_pick if right_color_text == "" else right_color_text

    alpha = st.slider("色の透明度", 0.0, 1.0, 0.5)
    font_size = st.number_input("フォントサイズ", step=1, value=12)
    title = st.text_input("タイトル", "")

# 描画
fig = plt.figure(figsize=(x, y))
plt.rcParams["font.size"] = font_size
plt.title(title)
venn2(
    subsets=[left, right, common],
    set_labels=(left_label, right_label),
    set_colors=(left_color, right_color),
    alpha=0.5,
)
st.pyplot(fig)
