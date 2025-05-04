import os

def print_directory_structure(root_dir, level=0):
    """
    打印指定目录下的文件和子目录结构，排除指定的目录和文件
    :param root_dir: 根目录路径
    :param level: 当前目录的层级，用于打印缩进
    """
    # 屏蔽的目录和文件类型
    excluded_dirs = {
        '.pytest_cache',
        '.venv',
        '.git',
        '__pycache__',
        'starai.egg-info',
        'notebooks'
    }
    excluded_files = {
        '.gitmodules'
    }

    try:
        for item in sorted(os.listdir(root_dir)):
            item_path = os.path.join(root_dir, item)

            if os.path.isdir(item_path):
                # 忽略排除列表中的目录
                if item in excluded_dirs:
                    continue
                print("  " * level + f"[DIR]  {item}/")
                print_directory_structure(item_path, level + 1)

            elif os.path.isfile(item_path):
                # 忽略排除列表中的文件
                if item in excluded_files:
                    continue
                print("  " * level + f"[FILE] {item}")

    except PermissionError:
        print("  " * level + "[ERROR] 权限不足，无法访问此目录")

if __name__ == "__main__":
    root_directory = os.getcwd()
    print("项目目录结构：\n")
    print_directory_structure(root_directory)
