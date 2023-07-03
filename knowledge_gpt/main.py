import streamlit as st
from openai.error import OpenAIError

from knowledge_gpt.components.sidebar import sidebar
from knowledge_gpt.utils.QA import (
    embed_docs,
    get_answer,
    get_sources,
    parse_file,
    text_to_docs,
)

from knowledge_gpt.utils.UI import wrap_text_in_html, is_valid


def clear_submit():
    st.session_state["submit"] = False


st.set_page_config(page_title="ONARB-GPT", page_icon="📖", layout="wide")
st.header("💸ONARB-GPT")

sidebar()

uploaded_file = st.file_uploader(
    "Upload a pdf, docx, or txt file",
    type=["pdf", "docx", "txt"],
    help="Scanned documents are not supported yet!",
    on_change=clear_submit,
)

index = None
texts = None
if uploaded_file is not None:
    texts = parse_file(uploaded_file)
    docs = text_to_docs(texts)

    try:
        with st.spinner("Indexing document... This may take a while⏳"):
            index = embed_docs(docs)
    except OpenAIError as e:
        st.error(e._message)

query = st.text_area("Ask a question about the document", on_change=clear_submit)

with st.expander("Advanced Options"):
    show_all_chunks = st.checkbox("Show all chunks retrieved from vector search")
    show_full_doc = st.checkbox("Show parsed contents of the document")

if show_full_doc and texts:
    with st.expander("Document"):
        # Hack to get around st.markdown rendering LaTeX
        st.markdown(f"<p>{wrap_text_in_html(texts)}</p>", unsafe_allow_html=True)

button = st.button("Submit")
if button or st.session_state.get("submit"):
    if not is_valid(index, query):
        st.stop()

    st.session_state["submit"] = True
    # Output Columns
    answer_col, sources_col = st.columns(2)
    sources = index.similarity_search(query, k=5)  # type: ignore

    try:
        answer = get_answer(sources, query)
        if not show_all_chunks:
            # Get the sources for the answer
            sources = get_sources(answer, sources)

        with answer_col:
            st.markdown("#### Answer")
            st.markdown(answer["output_text"].split("SOURCES: ")[0])

        with sources_col:
            st.markdown("#### Sources")
            for source in sources:
                st.markdown(source.page_content)
                st.markdown(source.metadata["source"])
                st.markdown("---")

    except OpenAIError as e:
        st.error(e._message)
