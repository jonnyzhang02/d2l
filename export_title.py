import markdown
import re

def headers_to_list(md_text):
    html = markdown.markdown(md_text)
    
    # 使用正则表达式提取所有h1-h6标题
    headers = re.findall(r'<h([1-6])>(.*?)</h\1>', html)
    
    outlines = []
    for level, title in headers:
        # 将标题级别转换为列表层级
        level = int(level) 
        outlines.append('  ' * (level-1) + '- ' + title)
    
    return '\n'.join(outlines)

with open('./chapters/chapter_convolutional-modern/.md', 'r', encoding='utf-8') as f:
    md_text = f.read()

outlines = headers_to_list(md_text)
print(outlines)