import math
import random
import pandas as pd
import gradio as gr
import numpy as np

LIST_CITY = ["Hà Nội", "Hồ Chí Minh"]

def get_current_data(city):
    if str(city) == "Hà Nội":
        # data from storage
        res = {
            "header_1": random.randint(0, 50),
            "header_2": random.randint(0, 50),
            "header_3": random.randint(0, 50),
            "header_4": random.randint(0, 50),
            "header_5": random.randint(0, 50),
            "header_6": random.randint(0, 50)
        }
    else:
        # data from storage
        res = {
            "header_1": random.randint(50, 100),
            "header_2": random.randint(50, 100),
            "header_3": random.randint(50, 100),
            "header_4": random.randint(50, 100),
            "header_5": random.randint(50, 100),
            "header_6": random.randint(50, 100)
        }
    
    res = pd.DataFrame({k:pd.Series(v) for k,v in res.items()})

    update = gr.DataFrame.update(
        value=res
    )

    return update


def get_plot_future(city):
    if city=="Hà Nội":
        # outputs from model
        sample_list = [] 
        for i in range(4):
            sample_list.append(random.randint(0, 50))
    else:
        # outputs from model
        sample_list = [] 
        for i in range(4):
            sample_list.append(random.randint(50, 100))

    x = ['next 1h', 'next 2h', 'next 3h', 'next 4h']
    y = sample_list
    update = gr.LinePlot.update(
        value=pd.DataFrame({"x": x, "y": y}),
        x="x",
        y="y",
        title="Predicted Future PM",
        width=600,
        height=350,
    )

    return update

    
with gr.Blocks() as demo:
    with gr.Tab("Chỉ số PM hiện tại"):
        city = gr.Dropdown(choices=LIST_CITY, label="City")

        outputs = gr.DataFrame(headers=["Header 1", "Header 2", "Header 3", "Header 4", "Header 5", "Header 6"],
                            datatype=["number", "number", "number", "number", "number", "number"], wrap=True)
        
        city.change(get_current_data, city, outputs, every=5)

    with gr.Tab("Chỉ số PM dự đoán"):
        city = gr.Dropdown(choices=LIST_CITY, label="City", value="Hà Nội")

        plot = gr.LinePlot(show_label=False)

        city.change(get_plot_future, city, plot, every=5)


if __name__ == "__main__":
    demo.queue().launch()