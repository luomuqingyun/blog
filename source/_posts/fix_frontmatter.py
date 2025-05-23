#!/usr/bin/env python
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

def get_file_creation_date(file_path):
    """获取文件创建时间"""
    try:
        # Windows系统使用st_ctime，Linux/Mac使用st_birthtime（如果支持）
        if os.name == 'nt':  # Windows
            creation_time = os.path.getctime(file_path)
        else:  # Linux/Mac
            stat = os.stat(file_path)
            # 尝试获取创建时间，如果不支持则使用修改时间
            try:
                creation_time = stat.st_birthtime
            except AttributeError:
                creation_time = stat.st_mtime
        
        return datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
    except:
        # 如果获取失败，使用当前时间
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def process_file(file_path):
    """处理单个Markdown文件，添加或补充元数据"""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 检查文件是否已经有YAML元数据
    yaml_pattern = r'^---\s*\n(.*?)\n---\s*\n'
    yaml_match = re.search(yaml_pattern, content, re.DOTALL)
    
    title = get_title_from_filename(file_path)
    # 使用文件创建时间而不是当前时间
    file_date = get_file_creation_date(file_path)
    
    if yaml_match:
        # 已有元数据，检查是否需要补充
        yaml_content = yaml_match.group(1)
        new_yaml = yaml_content
        
        # 检查并补充各个字段（只添加不存在的字段，不修改已有内容）
        if not re.search(r'title:', yaml_content):
            new_yaml += f'\ntitle: {title}'
        
        if not re.search(r'date:', yaml_content):
            new_yaml += f'\ndate: {file_date}'
        
        if not re.search(r'author:', yaml_content):
            new_yaml += '\nauthor: luomuqingyun'
        
        if not re.search(r'index_img:', yaml_content):
            new_yaml += '\nindex_img: /img/index_img/default.jpg'
        
        if not re.search(r'banner_img:', yaml_content):
            new_yaml += '\nbanner_img: /img/banner_img/default.jpg'
        
        if not re.search(r'comments:', yaml_content):
            new_yaml += '\ncomments: true'
        
        if not re.search(r'math:', yaml_content):
            new_yaml += '\nmath: true'
        
        if not re.search(r'mermaid:', yaml_content):
            new_yaml += '\nmermaid: true'
        
        if not re.search(r'hide:', yaml_content):
            new_yaml += '\nhide: false'
        
        if not re.search(r'archive:', yaml_content):
            new_yaml += '\narchive: false'
        
        if not re.search(r'category_bar:', yaml_content):
            new_yaml += '\ncategory_bar: true'
        
        # 对于category和tags，如果不存在则添加空数组，如果存在则保持原样
        if not re.search(r'category:', yaml_content):
            new_yaml += '\ncategory: []'
        
        if not re.search(r'tags:', yaml_content):
            new_yaml += '\ntags: []'
        
        # 对于excerpt，如果不存在则添加空的，如果存在则保持原样
        if not re.search(r'excerpt:', yaml_content):
            new_yaml += '\nexcerpt:\n    - '
        
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
# 注意：注释内容并不会在新建文档中出现！！！
title: {title}
date: {file_date}
author: luomuqingyun
# 文章在首页的封面图
index_img: /img/index_img/default.jpg
# 文章页顶部大图
banner_img: /img/banner_img/default.jpg
comments: true
# mathjax可以不用设置，设置math即可
# mathjax: true 
math: true
mermaid: true
# 设置不在首页和其他归档分类页里展示
hide: false 
# 不想隐藏，只是不想在首页显示，设置archive
archive: false
# 安装 hexo-generator-index >= 2.0.0 版本时可设置首页排序等级
# sticky: 100
# 侧边栏展示当前分类下的文章
category_bar: true
# 分类
category: []
# 标签
tags: []
excerpt:
    - 
---
"""
        new_content = metadata + content
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"已添加元数据: {file_path}")

def main():
    """主函数，处理Markdown文件"""
    if len(sys.argv) > 1:
        target = sys.argv[1]
        
        # 检查是单个文件还是目录
        if os.path.isfile(target) and target.endswith('.md'):
            # 处理单个文件
            process_file(target)
            print(f"处理完成，处理了 1 个Markdown文件")
        elif os.path.isdir(target):
            # 处理目录下的所有文件
            count = 0
            for root, _, files in os.walk(target):
                for file in files:
                    if file.endswith('.md'):
                        file_path = os.path.join(root, file)
                        process_file(file_path)
                        count += 1
            print(f"处理完成，共处理了 {count} 个Markdown文件")
        else:
            print(f"错误：'{target}' 不是有效的Markdown文件或目录")
    else:
        # 没有参数，处理当前目录下的所有文件
        directory = os.getcwd()
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