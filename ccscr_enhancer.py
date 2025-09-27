import streamlit as st

st.set_page_config(page_title="CC SC R Prompt Enhancer", page_icon="✨")
st.title("✨ Prompt Engineer — CC SC R Framework")
st.caption("Demo Mode - Learn how to structure better prompts with Context, Constraints, System, Content, and Role!")

st.subheader("Enter CC SC R Framework Details")

# Context - What's the situation/background?
context = st.text_area("Context (CC)", 
                      value="Working on a marketing campaign for a tech startup")
st.markdown("*Describe the situation, background, or setting*")

# Constraints - What are the limits/requirements?
constraints = st.text_area("Constraints (CC)", 
                          value="Must be under 100 words, professional tone, target millennials")
st.markdown("*Specify any limitations, requirements, or rules*")

# System - How should the AI behave?
system = st.text_input("System (S)", 
                      value="Act as a creative marketing expert")
st.markdown("*Define how the AI should behave or what role it should take*")

# Content - What specific content/task?
content = st.text_area("Content (C)", 
                      value="Write a social media post announcing our new app feature")
st.markdown("*Describe the specific task or content needed*")

# Role - Who is the target audience/perspective?
role = st.text_input("Role (R)", 
                    value="Target audience: Tech-savvy millennials aged 25-35")
st.markdown("*Define the target audience or perspective*")

st.subheader("Paste your rough prompt")
draft = st.text_area("Your Draft Prompt:", 
                    height=140,
                    placeholder="Enter your initial prompt idea here...")

if st.button("Enhance Prompt with CC SC R"):
    if not draft.strip():
        st.warning("Please enter your draft prompt.")
    else:
        # Demo output - shows structured CC SC R approach
        instruction = (
            "Generate an enhanced, structured prompt using CC SC R framework.\n"
            "1) Improve clarity and structure\n"
            "2) Follow CC SC R format\n"
            "3) Ask TWO clarifying questions\n"
            "4) Specify clear output format\n"
        )
        
        demo_output = (
            f"CONTEXT: {context}\n"
            f"CONSTRAINTS: {constraints}\n"
            f"SYSTEM: {system}\n"
            f"CONTENT: {content}\n"
            f"ROLE: {role}\n\n"
            f"USER DRAFT:\n{draft}\n\n"
            "OUTPUT FORMAT:\n- Clear, actionable response\n- 2 follow-up questions for refinement"
        )
        
        st.success("Enhanced Prompt (Demo Mode)")
        st.code(instruction + "\n" + demo_output, language="markdown")
        
        st.info("💡 This is demo mode showing the CC SC R structure. In live mode, AI would generate the actual enhanced prompt!")

# Add helpful information about the framework
st.markdown("---")
st.subheader("About CC SC R Framework")
st.markdown("""
**CC SC R** stands for:
- **Context (CC)**: Background information and situation
- **Constraints (CC)**: Limitations, requirements, and rules
- **System (S)**: How the AI should behave or act
- **Content (C)**: The specific task or content needed  
- **Role (R)**: Target audience or perspective

This framework helps create more structured and effective prompts!
""")