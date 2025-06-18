import pdfplumber
import fugashi
import pykakasi

tagger = fugashi.Tagger()
kks = pykakasi.kakasi()


def is_hiragana(text):
    return all('\u3040' <= ch <= '\u309F' for ch in text)


def word_with_ruby(word):
    surface = word.surface.strip()
    if not surface:
        return ''
    converted = kks.convert(surface)
    if not converted:
        return surface
    hira = converted[0].get('hira', surface)
    if surface != hira and not is_hiragana(surface):
        return f"<ruby>{surface}<rt>{hira}</rt></ruby>"
    else:
        return surface


def convert_text_to_html(text):
    result = []
    for word in tagger(text):
        result.append(word_with_ruby(word))
    return ''.join(result)


# 提取 PDF 文本
all_html = []
with pdfplumber.open("/Users/zhanglei/Desktop/thesis202103.pdf") as pdf:
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            for line in page_text.split("\n"):
                ruby_line = convert_text_to_html(line.strip())
                if ruby_line:
                    all_html.append(f"<p>{ruby_line}</p>")

# 包装成完整 HTML
html_output = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>ふりがな付きPDF</title>
<style>
  body {{ font-family: 'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif; line-height: 1.8; padding: 2em; }}
  ruby rt {{ font-size: 0.6em; color: #666; }}
</style>
</head>
<body>
{''.join(all_html)}
</body>
</html>
"""

# 保存为 HTML 文件
with open("output_with_furigana.html", "w", encoding="utf-8") as f:
    f.write(html_output)

print("✅ HTML 已生成：output_with_furigana.html")
