import streamlit as st
import os 
import vector
class ChatBox:
    """
    ## Methods

    1. user_chat_bubble -> renders the chat for user in streamlit 
    2. assistant_chat_bubble -> renders the chat for assistant in streamlit 
    3. pdf_mode() -> renders the pdf toggle in streamlit 
    4. vector_search_pdf -> returns context parsers with few shot prompting 
    5. chat -> main function which is called as ChatBox.chat() to render the entire page

    """
    def __init__(self,choose_model,model,image_parts) -> None:
        self.choose_model = choose_model
        self.model=model
        self.image_parts = image_parts
        self.is_active=False
        self.prompt_parts = []
        self.prompt=""
    def user_chat_bubble(self):
        with st.chat_message("user"):
            st.markdown(self.prompt)
        st.session_state.messages.append({"role": "user", "content": self.prompt})
    def assistant_chat_bubble(self):
        with st.chat_message("assistant"):
            message_holder = st.empty()
            message=""
            if self.is_active:
                context_parse=self.vector_search_pdf()
            else:
                context_parse=self.prompt
            self.prompt_parts.append(context_parse)
            if self.choose_model=='gemini-pro-vision':
                self.prompt_parts.append(self.image_parts.data)
            response = self.model.generate_content(self.prompt_parts,stream=True)
            for chunk in response:
                message+=chunk.text+" "
                message_holder.markdown(message+ "▌")
            message_holder.markdown(message)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    def pdf_mode(self):
        get_files = os.listdir("./upload")
        if get_files!=[]: 
                value=True
                if(self.choose_model!="gemini-pro"):value=False
                activated =st.toggle("Pdf Chat Mode",value=value)  
        return activated
    
    def vector_search_pdf(self):
        db = vector.use_cone()
        get_context=db.similarity_search(self.prompt)
        context=""
        for items in get_context:
            context+=items.page_content
        context_parse=f'''
            This is the context that you have to look :
            {context}
            -----------------------------
            This is the prompt that user entered :
            {self.prompt}
            ------------------------------
            You have to first look at the context and then the prompt and 
            give responses accordingly , make it good and convincing
            Give user a good explaination by structuring the context and make it readable 
            While predicting the next token , make sure it is similar to provided context
            The response should contains the points from the context ,
            Do not cover topics other the one provided context
        '''
        print(context_parse)
        return context_parse
    
    def chat(self):
        st.header("Gemini App")
        st.subheader("Free & open source drop-in pdf chat and more")
        st.divider()
        if "messages" not in st.session_state:
            st.session_state.messages=[]
            st.session_state.messages.append({"role": "assistant", "content":"Welcome !,how can i help you today ?"})
            

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        self.is_active = self.pdf_mode()
        self.prompt=st.chat_input("What is up?")
        if self.prompt:

            self.user_chat_bubble()
            self.assistant_chat_bubble()
