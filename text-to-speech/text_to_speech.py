import gradio as gr
import tempfile
from openai import OpenAI


def tts(text, model, voice, api_key):
    """
    Convert input text to speech using the specified model and voice.
    
    Parameters:
    - text (str): The text to convert to speech.
    - model (str): The name of the TTS model to use.
    - voice (str): The voice option to use.
    - api_key (str): The API key for authenticating with OpenAI.
    
    Returns:
    - str: The filename (path) of the generated audio file.
    """
    # check if the API key was provided, if not raise an error
    if not api_key:
      raise gr.Error("Please enter your OpenAi API key")
    
    try:
        # create a client object using the provided API key
        client = OpenAI(api_key=api_key)

        # generate the audio file using the provided text, model, and voice
        response = client.audio.speech.create(
            model=model,
            voice=voice,
            input=text
        )

    except Exception as error:
        print(str(error))
        raise gr.Error("An error occurred while generating the audio file")
    
    # create a temporary file to store the audio file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
       temp_file.write(response.content)

    # return the name (path) of the temporary file containing the audio
    return temp_file.name



def gradio_interface():
    """
        Create and launch a Gradio interface for the text-to-speech application
    """
    with gr.Blocks() as demo:
        # display the input text field
        gr.Markdown("# <center>OpenAI Text to Speech </center>")

        with gr.Row():
            # A password textbox for the API key
            api_key = gr.Textbox(label="API Key", type="password", placeholder="Enter your OpenAI API key")

            # A dropdown to select text-to-speech model
            model = gr.Dropdown(choices=["tts-1", "tts-1-hd"], label="Model", value="tts-1")

            # A dropdown to select the voice
            voice = gr.Dropdown(choices=['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer'], label='Voice Options', value='alloy')

        # A textbox to enter the text to convert to speech
        text = gr.Textbox(label="Enter the text to convert to speech", placeholder="Enter the text here and click the 'Generate' to convert to speech")

        # A button to generate the speech
        btn = gr.Button("Generate Speech")

        # An audio output to play the generated speech
        output_audio = gr.Audio(label="Speech Output")

        # Set up the text submission so that pressing enter triggers the TTs function
        text.submit(fn=tts, inputs=[text, model, voice, api_key], outputs=output_audio, api_name="tts_enter_key", concurrency_limit=None)

        # Set up the button to trigger the TTs function
        btn.click(fn=tts, inputs=[text, model, voice, api_key], outputs=output_audio, api_name="tts_button", concurrency_limit=None)


    demo.launch(share=True)



if __name__ == "__main__":
    gradio_interface()