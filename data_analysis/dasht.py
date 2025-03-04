import dash
import dash_cytoscape as cyto
from dash import html

app = dash.Dash(__name__)

# 定义节点和边
nodes = [
    {'data': {'id': '不良类型', 'label': '不良类型'}, 'position': {'x': 0, 'y': 0}},
    {'data': {'id': '元件歪斜(指向上偏斜)', 'label': '元件歪斜(指向上偏斜)'}, 'position': {'x': 100, 'y': 100}},
    {'data': {'id': 'Others', 'label': 'Others'}, 'position': {'x': 200, 'y': 100}},
    {'data': {'id': '少锡', 'label': '少锡'}, 'position': {'x': 300, 'y': 100}},
    {'data': {'id': '螺丝不良', 'label': '螺丝不良'}, 'position': {'x': 400, 'y': 100}},
    {'data': {'id': '误报', 'label': '误报'}, 'position': {'x': 500, 'y': 100}},
    {'data': {'id': '无引脚（插件反面不见引脚）', 'label': '无引脚（插件反面不见引脚）'}, 'position': {'x': 600, 'y': 100}},
    {'data': {'id': '松香污染', 'label': '松香污染'}, 'position': {'x': 700, 'y': 100}},
    {'data': {'id': '短路/连锡', 'label': '短路/连锡'}, 'position': {'x': 800, 'y': 100}},
    {'data': {'id': '外来物', 'label': '外来物'}, 'position': {'x': 900, 'y': 100}},
    {'data': {'id': '漏件/少件', 'label': '漏件/少件'}, 'position': {'x': 1000, 'y': 100}},
    {'data': {'id': '位置不正确', 'label': '位置不正确'}, 'position': {'x': 1100, 'y': 100}},
    {'data': {'id': '元件一端放置（竖立90度）', 'label': '元件一端放置（竖立90度）'}, 'position': {'x': 1200, 'y': 100}},
    {'data': {'id': '元件升高', 'label': '元件升高'}, 'position': {'x': 1300, 'y': 100}},
    {'data': {'id': '变形', 'label': '变形'}, 'position': {'x': 1400, 'y': 100}},
    {'data': {'id': '破损', 'label': '破损'}, 'position': {'x': 1500, 'y': 100}},
    {'data': {'id': '锡珠', 'label': '锡珠'}, 'position': {'x': 1600, 'y': 100}},
    {'data': {'id': '多锡', 'label': '多锡'}, 'position': {'x': 1700, 'y': 100}},
    {'data': {'id': '焊盘设计不合理', 'label': '焊盘设计不合理'}, 'position': {'x': 1800, 'y': 100}},
    {'data': {'id': '焊锡膏印刷不均匀', 'label': '焊锡膏印刷不均匀'}, 'position': {'x': 1900, 'y': 100}},
    {'data': {'id': '回流焊温度不均匀', 'label': '回流焊温度不均匀'}, 'position': {'x': 2000, 'y': 100}},
    {'data': {'id': '具体原因不明确', 'label': '具体原因不明确'}, 'position': {'x': 2100, 'y': 100}},
    {'data': {'id': '焊锡膏印刷量不足', 'label': '焊锡膏印刷量不足'}, 'position': {'x': 2200, 'y': 100}},
    {'data': {'id': '焊接温度不够', 'label': '焊接温度不够'}, 'position': {'x': 2300, 'y': 100}},
    {'data': {'id': '螺丝质量问题', 'label': '螺丝质量问题'}, 'position': {'x': 2400, 'y': 100}},
    {'data': {'id': '安装不当', 'label': '安装不当'}, 'position': {'x': 2500, 'y': 100}},
    {'data': {'id': '扭矩不合适', 'label': '扭矩不合适'}, 'position': {'x': 2600, 'y': 100}},
    {'data': {'id': '检测设备误判', 'label': '检测设备误判'}, 'position': {'x': 2700, 'y': 100}},
    {'data': {'id': '程序设置不当', 'label': '程序设置不当'}, 'position': {'x': 2800, 'y': 100}},
    {'data': {'id': '插件安装不当', 'label': '插件安装不当'}, 'position': {'x': 2900, 'y': 100}},
    {'data': {'id': '焊接不良', 'label': '焊接不良'}, 'position': {'x': 3000, 'y': 100}},
    {'data': {'id': '焊接过程中松香残留过多', 'label': '焊接过程中松香残留过多'}, 'position': {'x': 3100, 'y': 100}},
    {'data': {'id': '焊锡膏印刷过多', 'label': '焊锡膏印刷过多'}, 'position': {'x': 3200, 'y': 100}},
    {'data': {'id': '焊接温度过高', 'label': '焊接温度过高'}, 'position': {'x': 3300, 'y': 100}},
    {'data': {'id': '生产环境不洁净', 'label': '生产环境不洁净'}, 'position': {'x': 3400, 'y': 100}},
    {'data': {'id': '操作不当', 'label': '操作不当'}, 'position': {'x': 3500, 'y': 100}},
    {'data': {'id': '元件未正确安装', 'label': '元件未正确安装'}, 'position': {'x': 3600, 'y': 100}},
    {'data': {'id': '贴片机故障', 'label': '贴片机故障'}, 'position': {'x': 3700, 'y': 100}},
    {'data': {'id': '贴片机精度不够', 'label': '贴片机精度不够'}, 'position': {'x': 3800, 'y': 100}},
    {'data': {'id': '焊锡膏质量问题', 'label': '焊锡膏质量问题'}, 'position': {'x': 3900, 'y': 100}},
    {'data': {'id': '元件质量问题', 'label': '元件质量问题'}, 'position': {'x': 4000, 'y': 100}}
]

edges = [
    {'data': {'source': '不良类型', 'target': '元件歪斜(指向上偏斜)', 'weight': 0.1}},
    {'data': {'source': '不良类型', 'target': 'Others', 'weight': 0.1}},
    {'data': {'source': '不良类型', 'target': '少锡', 'weight': 0.1}},
    {'data': {'source': '不良类型', 'target': '螺丝不良', 'weight': 0.1}},
    {'data': {'source': '不良类型', 'target': '误报', 'weight': 0.1}},
    {'data': {'source': '不良类型', 'target': '无引脚（插件反面不见引脚）', 'weight': 0.1}},
    {'data': {'source': '不良类型', 'target': '松香污染', 'weight': 0.1}},
    {'data': {'source': '不良类型', 'target': '短路/连锡', 'weight': 0.1}},
    {'data': {'source': '不良类型', 'target': '外来物', 'weight': 0.1}},
    {'data': {'source': '不良类型', 'target': '漏件/少件', 'weight': 0.1}},
    {'data': {'source': '不良类型', 'target': '位置不正确', 'weight': 0.1}},]

elements = nodes + edges

app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape',
        elements=elements,
        style={'width': '100%', 'height': '400px'},
        layout={'name': 'preset'},
        stylesheet=[
            {
                'selector': 'node',
                'style': {
                    'label': 'data(label)',
                    'width': '60px',
                    'height': '60px',
                    'background-color': '#0074D9',
                    'color': 'white',
                    'font-size': '20px',
                    'text-valign': 'center',
                    'text-halign': 'center',
                }
            },
            {
                'selector': 'edge',
                'style': {
                    'label': 'data(weight)',
                    'width': 2,
                    'line-color': '#0074D9',
                    'target-arrow-color': '#0074D9',
                    'target-arrow-shape': 'triangle',
                    'curve-style': 'bezier',
                }
            }
        ]
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)