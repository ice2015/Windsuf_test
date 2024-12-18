import os

def create_project_structure():
    base_dir = "Code"
    
    # 创建主项目目录结构
    directories = [
        os.path.join(base_dir, "src"),
        os.path.join(base_dir, "tests"),
        os.path.join(base_dir, "docs"),
        os.path.join(base_dir, "data"),
        os.path.join(base_dir, "config"),
        os.path.join(base_dir, "logs"),
    ]
    
    # 创建所有目录
    for dir_path in directories:
        os.makedirs(dir_path, exist_ok=True)
    
    # 创建基本文件
    files = {
        os.path.join(base_dir, "README.md"): "# Project Name\n\nProject description goes here.",
        os.path.join(base_dir, "requirements.txt"): "# Core dependencies\nnumpy\n",
        os.path.join(base_dir, ".gitignore"): "*.pyc\n__pycache__/\n*.log\n.env\n",
        os.path.join(base_dir, "src", "__init__.py"): "",
        os.path.join(base_dir, "src", "main.py"): "def main():\n    pass\n\nif __name__ == '__main__':\n    main()",
        os.path.join(base_dir, "tests", "__init__.py"): "",
        os.path.join(base_dir, "tests", "test_main.py"): "def test_example():\n    assert True",
        os.path.join(base_dir, "config", "config.yaml"): "# Configuration settings\n",
    }
    
    # 创建所有文件
    for file_path, content in files.items():
        with open(file_path, 'w') as f:
            f.write(content)

if __name__ == "__main__":
    create_project_structure()
