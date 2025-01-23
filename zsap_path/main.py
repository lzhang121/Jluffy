import plotly.graph_objects as go

# NODES = dict(
#     label=['美国', '中国', '日本', '英国', '俄罗斯', '金牌', '银牌', '铜牌', '五常国家', '非五常国家'],
#     color=['#440154', '#482677', '#414487', '#355f8d', '#2a788e',
#            '#e8c705', '#00a087', '#5f4a8b', '#ff7f0e', '#1f77b4']
# )

NODES = dict(
    label=['SPRO', '行政机构管理', '基本设置', '激活全局基金管理功能', '资金管理部门', '激活预算控制系统全局功能'],
    color=['#440154', '#482677', '#414487', '#355f8d', '#482677', '#414487']
)


# LINKS = dict(
#     source=[0, 1, 2, 3, 1, 4, 2],
#     target=[1, 2, 3, 4, 4, 2, 5],
#     value=[1, 2, 2, 1, 1, 1, 1],
#     color=[
#         'lightgreen',  # 节点0美国
#         'lightskyblue',  # 节点1中国
#         'bisque',  # 节点2日本
#         'lightcoral',
#         'lightpink',
#         'bisque'
#     ]
# )

LINKS = dict(
    source=[0, 1, 2, 3, 1, 4, 2],
    target=[1, 2, 3, 4, 4, 2, 5],
    value=[1, 2, 2, 1, 1, 1, 1],
    color=[
        'lightgreen',
        'lightgreen',
        'lightgreen',
        'lightgreen',
        'lightpink',
        'lightpink',
        'lightpink'
    ]
)


data = go.Sankey(node=NODES, link=LINKS)
fig = go.Figure(data)
# fig.update_layout(title='202东京奥运会奖牌榜前五', font_size=16)
fig.update_layout(title='SAP-FM激活全局基金管理功能', font_size=16)
fig.show()
