import streamlit as st
import streamlit.components.v1 as components

from pathlib import Path

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "files" / "MedelVecinaCV.pdf"

def main():
    # Title
    st.set_page_config(page_title="Resume", page_icon=":memo:", layout="wide")

    # Use local CSS
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style/style.css")

    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
 
    # Photo and Name
    col1, col2 = st.columns([1, 1.5])
    image = "files/meds.png"
    with col1:
        st.image(image, width=530)
    with col2:
        st.markdown("""<span style='font-size:80px;font-family:impact;color:A9A9A9'>MEDS VECINA</span> """, unsafe_allow_html=True)
        st.markdown("<span style='font-size:30px;color:#FFA07A'>Head of QA</span>", unsafe_allow_html=True)
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
        st.write("---") 
        st.markdown("<span style='font-size:30px'>About Me</span>", unsafe_allow_html=True)
        st.markdown("<span style='font-size:30px;font-family:arial;color:#A9A9A9'>More than 17 years of expertise in </span> <span style='font-size:30px;font-family:arial'>SOFTWARE QA & AUTOMATION TESTING, <span style='font-size:30px;font-family:arial;color:#A9A9A9'>and 8 years in a </span>LEADERSHIP ROLE.</span>", unsafe_allow_html=True)
        st.write("---")

        
        # Sidebar
        # st.sidebar.header("Navigation")
        menu = ["Skills", "Get In Touch With Me!"]
        choice = st.sidebar.radio(label="", options=menu, key="navigation",)

        # Main Content
        st.subheader(choice)

        if choice == "Skills":
            st.write("I have designed test automation frameworks and CI/CD pipelines with these automation tools:")
            st.markdown("- IBM Rational Functional Tester | HP Unified Functional Testing")
            st.markdown("- Robot Framework | Appium | Selenium")
            st.markdown("- Nightwatch.js | Cucumber-Gherkin | TestNG")
            st.markdown("- JMeter | Postman | Insomnia")
            st.markdown("- Jenkins | Github Actions | Maven")
        elif choice == "Get In Touch With Me!":
            # st.write("Email: medel.vecina@gmail.com")
            # st.write("Phone: (+63) 917 634 8632")
            # ---- CONTACT ----
            with st.container():

                # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
                contact_form = """
                <form action="https://formsubmit.co/medel.vecina@gmail.com" method="POST">
                    <input type="hidden" name="_captcha" value="false">
                    <input type="text" name="name" placeholder="Your name" required>
                    <input type="email" name="email" placeholder="Your email" required>
                    <textarea name="message" placeholder="Your message here" required></textarea>
                    <button type="submit">Send</button>
                </form>
                """
                left_column, right_column = st.columns(2)
                with left_column:
                    st.markdown(contact_form, unsafe_allow_html=True)
                with right_column:
                    st.empty()


        st.write("---")
        # LinkedIn and GitHub Icons
        st.write("Connect with me on:")
        linkedin_html = '<a href="https://www.linkedin.com/in/medelvecina/"><img src="https://cdn1.iconfinder.com/data/icons/logotypes/32/circle-linkedin-512.png" height="50" width="50"/></a>'
        github_html = '<a href="https://github.com/mvecina25"><img src="https://cdn2.iconfinder.com/data/icons/social-icons-33/128/Github-128.png" height="50" width="50"/></a>'
        # components.html(linkedin_html + github_html, height=70)
        st.markdown(linkedin_html, unsafe_allow_html=True)
        st.markdown(github_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
