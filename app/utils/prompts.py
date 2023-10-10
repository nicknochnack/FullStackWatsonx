def ragprompt(question, documents): 
    return   f"""Use the following pieces of context to answer the question at the end. 
            If you don't know the answer, just say that you don't know, don't try to make up an answer.
            {documents}
            Question: {question}
            Helpful Answer:"""