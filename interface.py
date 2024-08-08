import gradio as gr
from main_func import line_offer


def Which_lines_turn_off(Hours):
    return line_offer(int(Hours))


demo = gr.Interface(
    fn=Which_lines_turn_off,
    inputs=["text"],
    outputs=["text"],
)
demo.launch()  # Share your demo with just 1 extra parameter 🚀
