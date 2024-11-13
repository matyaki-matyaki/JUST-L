"""JUST-L app の UI"""
from pathlib import Path

import streamlit as st

from just_l.generate import generate_input
from just_l.visualize import visualize_input, visualize_output

st.set_page_config(
    page_title="JUST-L",
    layout="wide",
    menu_items={
        'Report a bug': "https://github.com/matyaki-matyaki/JUST-L",
        'About': "https://github.com/matyaki-matyaki/JUST-L"
    }
)
st.title("JUST-L Visualizer")
st.subheader("情報数理学演習I 2024年度 最終課題")
st.write("---")

path_to_in = Path("examples/ex1/in1.txt")
with open(path_to_in) as f:
    lines_in = f.readlines()

path_to_out = Path("examples/ex1/out1-1.txt")
with open(path_to_out) as f:
    lines_out = f.readlines()

col1, vline, col2 = st.columns([10.9, 0.2, 10.9])

with col1:
    st.subheader("入力")
    with st.container(height=280):
        st.text("入力例：")
        st.code("".join(lines_in), language=None)
    str_input = st.text_area("入力を記述してください．", height=200).splitlines()
    if str_input:
        st.text("入力盤面：")
        fig, _ = visualize_input(str_input)
        st.pyplot(fig)
    
with vline:
    st.html(
        '''
            <div class="divider-vertical-line"></div>
            <style>
                .divider-vertical-line {
                    border-left: 1px solid #F0F2F6;
                    height: 200vh;
                    margin: auto;
                }
            </style>
        '''
    )

with col2:
    st.subheader("出力")
    with st.container(height=280):
        st.text("出力例：")        
        st.code("".join(lines_out), language=None)
    str_output = st.text_area("出力を記述してください．", height=200).splitlines()
    if str_output:
        st.text("入力盤面 + ブロック：")
        fig, _ = visualize_output(str_input, str_output)
        st.pyplot(fig)

with st.sidebar:
    st.subheader("入力の生成")
    H = st.slider(label="H", min_value=3, max_value=10, value=7)
    W = st.slider(label="W", min_value=3, max_value=10, value=7)
    N = st.slider(label="N", min_value=2, max_value=5, value=4)
    seed = st.number_input("乱数シード", min_value=0, step=1, value=42)
    input_example = generate_input(H, W, N, seed)
    st.text("生成された入力：")
    st.code(input_example, language=None)
    
    