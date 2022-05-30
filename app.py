from transformers import pipeline
import gradio as gr

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
    text_box = gr.TextBox(
        placeholder="Enter text block to summarize",
        lines=4
    )
    gr.Interface(
        fn=predict,
        inputs=text_box,
        outputs="text"
    )

demo.launch()