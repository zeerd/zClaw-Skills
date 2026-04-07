"""将PDF文件转换为Markdown格式的文本。
使用方法:
    python pdf2md.py input.pdf output.md
"""
import pymupdf4llm


def pdf_to_markdown(pdf_path, output_md):
    markdown_text = pymupdf4llm.to_markdown(pdf_path)
    markdown_text = markdown_text.replace('�', ' ')

    with open(output_md, "w", encoding="utf-8") as f:
        f.write(markdown_text)
    print(f"转换完成，已保存至 {output_md}")


if __name__ == "__main__":
    import sys
    pdf_to_markdown(sys.argv[1], sys.argv[2])
