from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker
from colorama import Fore

if __name__ == "__main__":

    converter = DocumentConverter()
    doc = converter.convert("tm1_dg_dvlpr-10pages.pdf").document
    chunker = HybridChunker()
    chunks = chunker.chunk(dl_doc=doc)

    dataset = {}

    for i, chunk in enumerate(chunks):

        print(Fore.YELLOW + f"Raw text:\n{chunk.text[:150]}..." + Fore.RESET)
        enriched_text = chunker.contextualize(chunk=chunk)
        print(Fore.LIGHTMAGENTA_EX + f"Contextualized text:\n{enriched_text[:150]}..." + Fore.RESET)