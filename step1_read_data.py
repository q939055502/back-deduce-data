import os
from typing import List, Dict, Any


def read_txt_file(file_path: str) -> List[List[str]]:
    data: List[List[str]] = []
    encodings = ['utf-8', 'utf-16-le', 'gbk']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split('\t')
                    cleaned_parts = []
                    for part in parts:
                        part = part.strip()
                        if part.startswith('\ufeff'):
                            part = part[1:]
                        cleaned_parts.append(part)
                    data.append(cleaned_parts)
            return data
        except (UnicodeDecodeError, UnicodeError):
            continue
        except FileNotFoundError:
            print(f"文件不存在: {file_path}")
            return data
        except Exception as e:
            print(f"读取文件失败: {file_path}, 错误: {e}")
            return data
    print(f"所有编码都无法读取文件: {file_path}")
    return data


def read_all_txt_files() -> tuple[List[List[str]], List[List[str]], List[List[str]]]:
    project_dir = os.path.dirname(os.path.abspath(__file__))
    
    nane_and_data: List[List[str]] = []
    tan_hua: List[List[str]] = []
    tan_hua_re: List[List[str]] = []
    
    file_path1 = os.path.join(project_dir, '碳化转换.txt')
    file_path2 = os.path.join(project_dir, '碳化反转.txt')
    file_path3 = os.path.join(project_dir, '构件数据.txt')

    tan_hua = read_txt_file(file_path1)
    tan_hua_re = read_txt_file(file_path2)
    nane_and_data = read_txt_file(file_path3)
    
    return nane_and_data, tan_hua, tan_hua_re


if __name__ == '__main__':
    nane_and_data, tan_hua, tan_hua_re = read_all_txt_files()
    