import fitz
def extract_pdf_text(path):
 doc=fitz.open(path); out=[]
 for i,p in enumerate(doc): out.append({'page':i+1,'text':p.get_text()})
 return out