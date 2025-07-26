# this converts the text into chunks into characters, 
# tomorrow i will convert them to chunks of tokens
def chunk_text(text: str, chunkSize:int = 1000, overlap:int = 100):
    chunk=[]
    start = 0
    n = len(text)
    while(start < n):
        end = start + chunkSize
        txt = text[start:end]
        chunk.append(txt)
        start = start + chunkSize - overlap
    return chunk

