import sys
from typing import List, Dict
from pathlib import Path
import argparse


try:
    from PyPDF2 import PdfReader
except ImportError:
    print("PyPDF2 未安装，请先运行 pip install PyPDF2")
    sys.exit(1)


def extract_sections_with_keyword(pdf_path: str, keyword: str) -> List[Dict]:
    reader = PdfReader(pdf_path)
    num_pages = len(reader.pages)
    results = []
    # 合并所有文本
    page_texts = []
    for i in range(num_pages):
        text = reader.pages[i].extract_text() or ""
        page_texts.append(text)
    # 以每页为单位查找关键字所在页
    for i, text in enumerate(page_texts):
        if keyword in text:
            results.append({
                'pdf_name': Path(pdf_path).name,
                'section_text': text.strip(),
                'page_range': (i + 1, i + 1)
            })
    return results


def extract_text_by_page_range(
        pdf_path: str, start_page: int, end_page: int
) -> Dict:
    """
    读取PDF指定页码范围的所有文本。
    页码从1开始，包含start_page和end_page。
    """
    reader = PdfReader(pdf_path)
    num_pages = len(reader.pages)
    # 校验页码范围
    if start_page < 1 or end_page > num_pages or start_page > end_page:
        raise ValueError(f"页码范围无效，有效范围为1-{num_pages}")
    texts = []
    for i in range(start_page - 1, end_page):
        text = reader.pages[i].extract_text() or ""
        texts.append(text)
    return {
        'pdf_name': Path(pdf_path).name,
        'page_range': (start_page, end_page),
        'text': '\n'.join(texts)
    }


def main():
    parser = argparse.ArgumentParser(description="PDF章节与页码文本提取工具")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # search 子命令
    parser_search = subparsers.add_parser("search", help="按关键字查找章节")
    parser_search.add_argument("pdf_path", help="PDF文件路径")
    parser_search.add_argument("keyword", help="要查找的关键字")
    parser_search.add_argument("--max-chars", type=int, default=None,
                               help="限制返回内容的最大字符数（可选）")

    # range 子命令
    parser_range = subparsers.add_parser("range", help="读取指定页码范围文本")
    parser_range.add_argument("pdf_path", help="PDF文件路径")
    parser_range.add_argument("start_page", type=int, help="起始页码(从1开始)")
    parser_range.add_argument("end_page", type=int, help="结束页码(从1开始)")
    parser_range.add_argument("--max-chars", type=int, default=None,
                              help="限制返回内容的最大字符数（可选）")

    args = parser.parse_args()

    if args.command == "search":
        results = extract_sections_with_keyword(args.pdf_path, args.keyword)
        max_chars = args.max_chars
        # 获取真实title
        reader = PdfReader(args.pdf_path)
        title = getattr(getattr(reader, "metadata", None), "title", None)
        if not results:
            print(f"未找到包含关键字 '{args.keyword}' 的内容。")
        else:
            for r in results:
                content = r['section_text']
                if max_chars is not None:
                    content = content[:max_chars]
                    if len(content) > max_chars:
                        content += "..."
                print(f"PDF文件: {r['pdf_name']}")
                if title:
                    print(f"PDF标题: {title}")
                print(f"页码范围: {r['page_range'][0]} - {r['page_range'][1]}")
                print(f"内容:\n{content}\n{'-'*40}")
    elif args.command == "range":
        try:
            result = extract_text_by_page_range(
                args.pdf_path, args.start_page, args.end_page
            )
            content = result['text']
            max_chars = args.max_chars
            if max_chars is not None:
                content = content[:max_chars] + (
                    "..." if len(content) > max_chars else ""
                )
            print(f"PDF文件: {result['pdf_name']}")
            print("页码范围: "
                  f"{result['page_range'][0]} - {result['page_range'][1]}")
            print(f"文本内容:\n{content}\n{'-'*40}")
        except Exception as e:
            print(f"读取失败: {e}")


if __name__ == "__main__":
    main()

