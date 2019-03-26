from notion.client import NotionClient
from notion.block import *

with open('token_v2.txt') as f:
    token_v2 = f.readlines()[0]
client = NotionClient(token_v2=token_v2)
print('Notion logged in successfully.')
print('Notion登录成功')

page = client.get_block(input('Please input your page URL:\n请输入你想要生成目录的页面URL：\n'))

print('Extracting HeaderBlock...')
print('正在提取HeaderBlock...')
headers = []
for block in page.children:
    if block.type in ['header', 'sub_header', 'sub_sub_header']:
        headers.append(block)

print('Analyzing TOC structure...')
print('正在分析目录结构...')
hier_dict = {
    'header': 1,
    'sub_header': 2,
    'sub_sub_header': 3
}

class Node(object):
    def __init__(self, title='_'):
        self.title = title
        self.children = []

prev_h1 = Node()
nodes = [prev_h1]

for header in headers:
    hier = hier_dict[header.type]
    title = f'[{header.title}]({header.get_browseable_url()})'
    node = Node(title)
    if hier == 1:
        nodes.append(node)
        prev_h1 = node
    elif hier == 2:
        prev_h1.children.append(node)

for node in nodes:
    if node.title == '_' and len(node.children) == 0:
        nodes.remove(node)

print('Generating TOC...')
print('正在生成目录...')
first_elem = page.children[0]

tocblock = page.children.add_new(HeaderBlock, title='Table of Contents')
tocblock.move_to(first_elem, 'before')

for node in nodes:
    block = page.children.add_new(TextBlock, title=node.title)
    block.move_to(first_elem, 'before')
    for child in node.children:
        block.children.add_new(TextBlock, title=child.title)

divider = page.children.add_new(DividerBlock)
divider.move_to(first_elem, 'before')

print('Done. Please refresh your page to check it out.')
print('已完成，请刷新页面查看')
