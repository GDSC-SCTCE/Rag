"""
Gemini PDF Chat
by Google Developer Student Clubs , SCTCE

## Project Information

- **License:** MIT License
- **Project Documentation:** [GDSC SCTCE](https://ai.google.dev/tutorials/python_quickstart)

## Usage

1. Choose the Gemini Pro model from the sidebar.
2. Upload PDF documents or images for chat interactions.
3. Enjoy conversational experiences with the underlying model.

"""
import google.generativeai as genai 
from apikey import GetKey
from gemini_components.side_bar import SideBar
from gemini_components.chat_box import ChatBox
from gemini_components.get_the_freaking_watermark_out import GetTheFreakingWatermarkOut

class App:
    def main():
        genai.configure(api_key=GetKey().api_key)
        generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
        }
        choose_model = SideBar.GetModels()
        SideBar.PdfUploadForm()
        image_parts=None
        if choose_model=="gemini-pro-vision": 
            image_parts = SideBar.ImageUploadForm()

        model = genai.GenerativeModel(
            model_name=choose_model,
            generation_config=generation_config
        )
        window= ChatBox(choose_model=choose_model,
                        model=model,
                        image_parts=image_parts)
        window.chat()

if __name__=="__main__":
    GetTheFreakingWatermarkOut()
    app = App.main()


  