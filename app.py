import streamlit as st
import openai

st.title("AI Powered LinkedIn Post Generator")

st.write("Easiest way to create viral, SEO-rich LinkedIn posts in seconds!")

prompt = st.text_area("Describe your topic/idea for LinkedIn post", height=100)
bt = st.button("Generate LinkedIn Post")

if bt and prompt:
    with st.spinner("Generating..."):
        # Replace "your-openai-key-here" with your real OPENAI key
        openai.api_key = "your-openai-key-here"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Write a 5-sentence LinkedIn post about: {prompt}. Make it engaging, professional, and include a call to action.",
            temperature=0.7,
            max_tokens=150
        )
        st.success(response.choices[0].text.strip())
        st.caption("Powered by OpenAI")

st.markdown("---")
st.info("Upgrade to access advanced features or custom branding. [Buy here](https://your-lemonsqueezy-link)")
