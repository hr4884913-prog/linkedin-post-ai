import streamlit as st
import openai

st.title("AI Powered LinkedIn Post Generator")
st.write("Easiest way to create viral, SEO-rich LinkedIn posts in seconds!")

prompt = st.text_area("Describe your topic/idea for LinkedIn post")
btn = st.button("Generate LinkedIn Post")

if btn and prompt:
    with st.spinner("Generating..."):
        response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a professional LinkedIn post writer."},
        {"role": "user", "content": f"Write a 5-sentence LinkedIn post about: {prompt}"}
    ]
)
st.success(response.choices[0].message.content.strip())
        # openai.api_key = "sk-xxxxxxxxxx"
        openai.api_key = "YAHAN-APNI-OPENAI-KEY-PASTE-KARO"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional LinkedIn post writer."},
                {"role": "user", "content": f"Write a 5-sentence LinkedIn post about: {prompt}"}
            ]
        )
        st.success(response.choices[0].message.content.strip())

st.markdown(
    'Upgrade to access advanced features or custom branding. [Buy here](https://example.com)',
    unsafe_allow_html=True
)
st.caption("Powered by OpenAI")
