import gradio as gr
from transformers import pipeline

# Create model
model = pipeline("summarization")


def predict(prompt):
    """
    Grab model output and summarize the text.
    """
    summary = model(prompt)[0]["summary_text"]
    return summary


with gr.Blocks() as demo:
    # Create a text block
    text_box = gr.Textbox(placeholder="Enter text block to summarize", lines=4)
    gr.Interface(fn=predict, inputs=text_box, outputs="text")

demo.launch()
