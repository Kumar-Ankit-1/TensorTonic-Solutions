def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    chunks=[]
    start=0
    while start<len(tokens):
        end=start+chunk_size
        chunks.append(tokens[start:end])
        start=end-overlap
        if end==len(tokens):
                break
    return (chunks)