from pyecharts import options as opts
from pyecharts.charts import Graph

# 定义节点和边
nodes = [
    {"name": "不良类型", "symbolSize": 60},
    {"name": "元件歪斜(指向上偏斜)", "symbolSize": 50},
    {"name": "Others", "symbolSize": 50},
    {"name": "少锡", "symbolSize": 50},
    {"name": "螺丝不良", "symbolSize": 50},
    {"name": "误报", "symbolSize": 50},
    {"name": "无引脚（插件反面不见引脚）", "symbolSize": 50},
    {"name": "松香污染", "symbolSize": 50},
    {"name": "短路/连锡", "symbolSize": 50},
    {"name": "外来物", "symbolSize": 50},
    {"name": "漏件/少件", "symbolSize": 50},
    {"name": "位置不正确", "symbolSize": 50},
    {"name": "元件一端放置（竖立90度）", "symbolSize": 50},
    {"name": "元件升高", "symbolSize": 50},
    {"name": "变形", "symbolSize": 50},
    {"name": "破损", "symbolSize": 50},
    {"name": "锡珠", "symbolSize": 50},
    {"name": "多锡", "symbolSize": 50},
    {"name": "焊盘设计不合理", "symbolSize": 30},
    {"name": "焊锡膏印刷不均匀", "symbolSize": 30},
    {"name": "回流焊温度不均匀", "symbolSize": 30},
    {"name": "具体原因不明确", "symbolSize": 30},
    {"name": "焊锡膏印刷量不足", "symbolSize": 30},
    {"name": "焊接温度不够", "symbolSize": 30},
    {"name": "螺丝质量问题", "symbolSize": 30},
    {"name": "安装不当", "symbolSize": 30},
    {"name": "扭矩不合适", "symbolSize": 30},
    {"name": "检测设备误判", "symbolSize": 30},
    {"name": "程序设置不当", "symbolSize": 30},
    {"name": "插件安装不当", "symbolSize": 30},
    {"name": "焊接不良", "symbolSize": 30},
    {"name": "焊接过程中松香残留过多", "symbolSize": 30},
    {"name": "焊锡膏印刷过多", "symbolSize": 30},
    {"name": "焊接温度过高", "symbolSize": 30},
    {"name": "生产环境不洁净", "symbolSize": 30},
    {"name": "操作不当", "symbolSize": 30},
    {"name": "元件未正确安装", "symbolSize": 30},
    {"name": "贴片机故障", "symbolSize": 30},
    {"name": "贴片机精度不够", "symbolSize": 30},
    {"name": "焊锡膏质量问题", "symbolSize": 30},
    {"name": "元件质量问题", "symbolSize": 30}
]

edges = [
    {"source": "不良类型", "target": "元件歪斜(指向上偏斜)", "value": 0.1},
    {"source": "不良类型", "target": "Others", "value": 0.1},
    {"source": "不良类型", "target": "少锡", "value": 0.1},
    {"source": "不良类型", "target": "螺丝不良", "value": 0.1},
    {"source": "不良类型", "target": "误报", "value": 0.1},
    {"source": "不良类型", "target": "无引脚（插件反面不见引脚）", "value": 0.1},
    {"source": "不良类型", "target": "松香污染", "value": 0.1},
    {"source": "不良类型", "target": "短路/连锡", "value": 0.1},
    {"source": "不良类型", "target": "外来物", "value": 0.1},
    {"source": "不良类型", "target": "漏件/少件", "value": 0.1},
    {"source": "不良类型", "target": "位置不正确", "value": 0.1},
    {"source": "不良类型", "target": "元件一端放置（竖立90度）", "value": 0.1},
    {"source": "不良类型", "target": "元件升高", "value": 0.1},
    {"source": "不良类型", "target": "变形", "value": 0.1},
    {"source": "不良类型", "target": "破损", "value": 0.1},
    {"source": "不良类型", "target": "锡珠", "value": 0.1},
    {"source": "不良类型", "target": "多锡", "value": 0.1},

    {"source": "元件歪斜(指向上偏斜)", "target": "焊盘设计不合理", "value": 0.1},
    {"source": "元件歪斜(指向上偏斜)", "target": "焊锡膏印刷不均匀", "value": 0.1},
    {"source": "元件歪斜(指向上偏斜)", "target": "回流焊温度不均匀", "value": 0.1},

    {"source": "Others", "target": "具体原因不明确", "value": 0.1},

    {"source": "少锡", "target": "焊锡膏印刷量不足", "value": 0.1},
    {"source": "少锡", "target": "焊盘设计不合理", "value": 0.1},
    {"source": "少锡", "target": "焊接温度不够", "value": 0.1},

    {"source": "螺丝不良", "target": "螺丝质量问题", "value": 0.1},
    {"source": "螺丝不良", "target": "安装不当", "value": 0.1},
    {"source": "螺丝不良", "target": "扭矩不合适", "value": 0.1},

    {"source": "误报", "target": "检测设备误判", "value": 0.1},
    {"source": "误报", "target": "程序设置不当", "value": 0.1},

    {"source": "无引脚（插件反面不见引脚）", "target": "插件安装不当", "value": 0.1},
    {"source": "无引脚（插件反面不见引脚）", "target": "焊接不良", "value": 0.1},

    {"source": "松香污染", "target": "焊接过程中松香残留过多", "value": 0.1},

    {"source": "短路/连锡", "target": "焊锡膏印刷过多", "value": 0.1},
    {"source": "短路/连锡", "target": "焊盘设计不合理", "value": 0.1},
    {"source": "短路/连锡", "target": "焊接温度过高", "value": 0.1},

    {"source": "外来物", "target": "生产环境不洁净", "value": 0.1},
    {"source": "外来物", "target": "操作不当", "value": 0.1},

    {"source": "漏件/少件", "target": "元件未正确安装", "value": 0.1},
    {"source": "漏件/少件", "target": "贴片机故障", "value": 0.1},

    {"source": "位置不正确", "target": "贴片机精度不够", "value": 0.1},
    {"source": "位置不正确", "target": "焊盘设计不合理", "value": 0.1},

    {"source": "元件一端放置（竖立90度）", "target": "焊盘设计不合理", "value": 0.1}]

# 创建图表
graph = (
    Graph()
    .add("", nodes, edges, repulsion=8000, edge_label=opts.LabelOpts(is_show=True, position="middle", formatter="{c}"))
    .set_global_opts(title_opts=opts.TitleOpts(title="交互式网络图"))
)

# 渲染图表
graph.render("interactive_network.html")