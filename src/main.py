import streamlit as st
import time
import webbrowser

st.balloons()

# 设置网页标题
st.markdown('<style>h1{color: #FFA500;}</style>', unsafe_allow_html=True)
st.title('Hello, Wecome to MlStreamlit🤗🤗')

# 设置header文字颜色
# st.markdown('<style>h2{color: #FFA500;}</style>', unsafe_allow_html=True)
st.header('Information💡')
st.markdown('''
    本项目是基于Streamlit的机器学习项目，主要用于展示机器学习的一些算法，以及一些机器学习的应用。
    
    This project is based on Streamlit machine learning project, mainly used to show some machine learning algorithms, and some machine learning applications.
    ''')


def to_github():
    url = 'https://github.com/Szc-coder/MlStreamlit.git'
    webbrowser.open_new_tab(url)


# button go to use
st.header('Usage🏄️')
st.markdown('''
    1. 一般情况下，您需要在左侧的Step1 Feat中上传数据集，您可以在该页面中进行数据分析和数据预处理。
    2. 在Step2 Model中，您可以选择模型，进行模型训练，模型评估，模型预测等操作。
    3. 在Step3 Vis中，您可以进行模型可视化，以及模型的保存和加载。
    4. 在Step4 Real中，您可以进行模型的部署，以及模型的实时预测。
    ''')

st.header('Code with ❤️ by Szc-coder')
st.button('Go to github', on_click=to_github)
