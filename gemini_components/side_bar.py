import streamlit as st
import os 
from IPython.display import Image
from vector import cone_vector,add_document_tovector
class SideBar:
    """
    ## Methods

    1. GetModels -> creates a dropdown menu in sidebar 
    2. PdfUploadForm -> Form in sidebar 
    3. ImageUploadForm() -> Form in sidebar
    """
    def GetModels():
        '''
        Currently, only support for text model gemini pro is implemented \n
        Gemin pro vision image upload needs a PR to fix the error in sending image 
        over Http
        '''
        choose_model = st.sidebar.selectbox("Choose Model",['gemini-pro'])
        return choose_model
    
    def PdfUploadForm():
        '''
        Display a file uploader for PDFs in the sidebar. \n
        Files are uploaded to dir -> upload \n
        While form submition vector db is initiated \n
        Returns:
            None
        '''
        filename=""
        with st.sidebar.form(key="File",clear_on_submit=True):
            upload_file = st.file_uploader("Upload your pdfs",type='pdf',accept_multiple_files=True)
            for file in upload_file:
                data = file.read()
                filename=file.name
                st.write("Name",filename)
            submit = st.form_submit_button(label="Upload")
        if submit:
            st.toast("File uploaded , now you can chat with it !")
            with open(os.path.join('upload',filename),"wb") as filestream:
                filestream.write(data)
            cone_vector(filename)
    def ImageUploadForm():
        '''
        Display a Image uploader for Gemini Pro Vision model . \n
        Images are uploaded to dir -> pics \n
        
        Returns:
            blob image
        '''
        with st.sidebar.form(key="Image",clear_on_submit=True):
            image_upload = st.file_uploader("Upload the image",type=["jpg","png","jpeg"],accept_multiple_files=True)
            for image in image_upload:
                name = image.name
                st.write(name)
            image_submit = st.form_submit_button(label="Upload Image")
            
            if image_submit:
                st.toast("Image uploaded , now you can chat with it !")
                with open(os.path.join('pics',name),"wb") as imagestream:
                    imagestream.write(image.getbuffer())        
                image_parts=Image(os.path.join("pics",name))
                return image_parts