import plotly.express as px

fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])

sample_data = {
    {"name":'a',"value":1},
    {"name":'b',"value":2},
}


fig.write_html(file='first_figure.html')
fig.write_image('this.png')