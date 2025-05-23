#!/usr/bin/env python3
import os
import re
from datetime import datetime
import sys

def get_title_from_filename(filename):
    """从文件名获取标题，移除扩展名并将连字符和下划线替换为空格"""
    base_name = os.path.basename(filename)
    name_without_ext = os.path.splitext(base_name)[0]
    # 将连字符和下划线替换为空格，并将首字母大写
    title = name_without_ext.replace('-', ' ').replace('_', ' ').title()
    return title

def process_file(file_path):
    """处理单个Markdown文件，添加或补充元数据"""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 检查文件是否已经有YAML元数据
    yaml_pattern = r'^---\s*\n(.*?)\n---\s*\n'
    yaml_match = re.search(yaml_pattern, content, re.DOTALL)
    
    title = get_title_from_filename(file_path)
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    if yaml_match:
        # 已有元数据，检查是否需要补充
        yaml_content = yaml_match.group(1)
        new_yaml = yaml_content
        
        # 检查并补充title
        if not re.search(r'title:', yaml_content):
            new_yaml += f'\ntitle: {title}'
        
        # 检查并补充author
        if not re.search(r'author:', yaml_content):
            new_yaml += '\nauthor: luomuqingyun'
        
        # 检查并补充date
        if not re.search(r'date:', yaml_content):
            new_yaml += f'\ndate: {current_date}'
        
        # 检查并补充comments
        if not re.search(r'comments:', yaml_content):
            new_yaml += '\ncomments: true'
        
        # 检查并补充category
        if not re.search(r'category:', yaml_content):
            new_yaml += '\ncategory:\n  - 编程'
        
        # 检查并补充tags
        if not re.search(r'tags:', yaml_content):
            new_yaml += '\ntags:\n  - 编程经验'
        
        # 检查并补充excerpt
        if not re.search(r'excerpt:', yaml_content):
            new_yaml += '\nexcerpt:\n  - 详见完整内容'
        
        # 如果有任何变化，更新文件
        if new_yaml != yaml_content:
            new_content = re.sub(yaml_pattern, f'---\n{new_yaml}\n---\n', content, count=1, flags=re.DOTALL)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"已更新元数据: {file_path}")
        else:
            print(f"元数据已完整: {file_path}")
    else:
        # 没有元数据，添加完整的元数据
        metadata = f"""---
title: {title}
author: luomuqingyun
date: {current_date}
comments: true
category:
  - 编程
tags:
  - 编程经验
excerpt:
  - 详见完整内容
---
"""
        new_content = metadata + content
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"已添加元数据: {file_path}")

def main():
    """主函数，处理当前目录下的所有Markdown文件"""
    directory = os.getcwd()  # 获取当前工作目录
    
    # 如果提供了命令行参数，使用它作为目录
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    
    count = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                process_file(file_path)
                count += 1
    
    print(f"处理完成，共处理了 {count} 个Markdown文件")

if __name__ == "__main__":
    main()