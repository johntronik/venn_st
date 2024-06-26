from matplotlib import pyplot as plt
from matplotlib_venn import venn2
import matplotlib_fontja  # noqa
import streamlit as st

st.set_page_config(page_title="ベン図を描くアプリ", page_icon=":bar_chart:")
st.title("ベン図描く")
st.markdown(
    "[matplotlib-venn](https://github.com/konstantint/matplotlib-venn) を使ってベン図を描くアプリです。"
)

col1, col2, col3 = st.columns(3)
with col1:
    left_input = st.number_input("←左集合の数", step=1, value=3)
    left_label = st.text_input("左集合のラベル", "Left")
with col2:
    common = st.number_input("共通集合の数", step=1, value=2)
with col3:
    right_input = st.number_input("右集合の数→", step=1, value=5)
    right_label = st.text_input("右集合のラベル", "Right")

is_subset = st.toggle("共通部分を左右の集合から引く", value=True)
left = left_input - common * is_subset
right = right_input - common * is_subset

with st.expander("詳細設定"):
    colx, coly = st.columns(2)
    with colx:
        x = st.number_input("横幅px", step=1, value=6)
        left_color = st.color_picker("左集合の色指定", "#FF4000")
    with coly:
        y = st.number_input("縦幅px", step=1, value=6)
        right_color = st.color_picker("右集合の色指定", "#0051FF")

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
    alpha=alpha,
)
st.pyplot(fig)
