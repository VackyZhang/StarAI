import os

def print_directory_structure(path, level=0):
    # 打印当前目录或文件
    indent = "  " * level
    if os.path.isdir(path):
        # 忽略 Git 相关的文件和目录以及 .venv 目录
        if ".git" in os.path.basename(path):
            return
        if "__pycache__" in os.path.basename(path):
            return
        if ".venv" in os.path.basename(path):
            return
        print(f"{indent}[DIR] {os.path.basename(path)}/")
        # 递归打印子目录
        for item in os.listdir(path):
            print_directory_structure(os.path.join(path, item), level + 1)
    else:
        # 忽略 .pyc 文件
        if path.endswith(".pyc"):
            return
        print(f"{indent}[FILE] {os.path.basename(path)}")

if __name__ == "__main__":
    project_root = os.getcwd()  # 获取当前工作目录（即项目根目录）
    print("项目文件夹结构：")
    print_directory_structure(project_root)
