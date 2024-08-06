import gradio as gr

import data_processing


def greet(Hours):
    return data_processing.alghorithm


demo = gr.Interface(
    fn=greet,
    inputs=["text"],
    outputs=["text"],
)
demo.launch()  # Share your demo with just 1 extra parameter 🚀
