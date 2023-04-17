import os
import streamlit as st
import base64
import sys

sys.path.insert(0, '../')

import src.config as config

st.header('师兄带你学习🤗🤗🤗')
st.write('''
    本页面是面向CPG或者小新们的学习资料，希望能够帮助到大家。
    ''')


# load all video url
@st.cache_data
def load_video_url():
    url_tmp = []
    for file in os.listdir(config.static_source['class_video']):
        if file.endswith('.mp4'):
            url_tmp.append(os.path.join(config.static_source['class_video'], file))
    return url_tmp


video_url = load_video_url()
video_name = [os.path.basename(i) for i in video_url]
video_name = [i.split('.')[0] for i in video_name]

seleted_video_name = st.selectbox('选择课程', video_name)


def load_video(url_tmp):
    st.video(url_tmp)


# 检测按钮更新
load_video(video_url[video_name.index(seleted_video_name)])

st.download_button(
    label='下载视频',
    data=open(video_url[video_name.index(seleted_video_name)], 'rb'),
    file_name=seleted_video_name + '.mp4',
    mime='video/mp4'
)


# # load all ppt url
# @st.cache_data
# def load_ppt_url():
#     url_tmp = []
#     for file in os.listdir(config.static_source['class_ppt']):
#         if file.endswith('.pptx'):
#             url_tmp.append(os.path.join(config.static_source['class_ppt'], file))
#     return url_tmp
#
#
#     # 下拉框
# ppt_url = load_ppt_url()
# ppt_name = [os.path.basename(i) for i in ppt_url]
# ppt_name = [i.split('.')[0] for i in ppt_name]
#
# seleted_name = st.selectbox('选择PPT', ppt_name)
#
# ppt_seleted_url = ppt_url[ppt_name.index(seleted_name)]
#
# # download button
# st.download_button(
#     label='下载PPT',
#     data=open(ppt_seleted_url, 'rb'),
#     file_name=seleted_name + '.pptx',
#     mime='application/vnd.openxmlformats-officedocument.presentationml.presentation'
# )
#
#
