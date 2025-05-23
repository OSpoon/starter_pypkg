import os
import re
import shutil
import subprocess
import datetime
import gradio as gr

def replace_in_file(file_path, replacements):
    """在文件中替换内容"""
    if not os.path.exists(file_path):
        print(f"文件不存在: {file_path}")
        return
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        for old, new in replacements:
            content = content.replace(old, new)
        
        # 先写入备份
        with open(f"{file_path}.bak", 'w', encoding='utf-8') as file:
            file.write(content)
        
        # 再替换原文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {e}")

def initialize_project(project_name, display_name, project_description, 
                      author_name, author_email, github_username, 
                      copyright_year, reinit_git):
    """初始化项目"""
    log = []
    
    # 记录日志
    def add_log(msg):
        log.append(msg)
        print(msg)
    
    add_log("开始初始化项目...")
    
    # 转换project_name为合法的Python包名 (小写，下划线替换横杠)
    package_name = project_name.replace('-', '_').lower()
    
    # 使用display_name的默认值
    if not display_name:
        display_name = project_name
    
    # 使用当前年份作为默认版权年份
    if not copyright_year:
        copyright_year = str(datetime.datetime.now().year)
        
    add_log(f"包名称: {package_name}")
    add_log(f"显示名称: {display_name}")
    
    # 替换文件内容
    add_log("更新文件内容...")
    
    # 更新pyproject.toml
    if os.path.exists("pyproject.toml"):
        replacements = [
            ('name = "starter_pypkg"', f'name = "{package_name}"'),
            ('OSpoon', github_username),
            ('zxin088@gmail.com', author_email),
            ('{ name = "OSpoon", email = "zxin088@gmail.com" }', f'{{ name = "{author_name}", email = "{author_email}" }}'),
            ('Add your description here', project_description),
            ('keywords = ["starter_pypkg"]', f'keywords = ["{package_name}"]'),
            ('"Homepage" = "https://github.com/OSpoon/starter_pypkg/"', f'"Homepage" = "https://github.com/{github_username}/{project_name}/"'),
            ('"Bug Tracker" = "https://github.com/OSpoon/starter_pypkg/issues"', f'"Bug Tracker" = "https://github.com/{github_username}/{project_name}/issues"'),
        ]
        replace_in_file("pyproject.toml", replacements)
        add_log("已更新 pyproject.toml")
    
    # 更新README.md
    if os.path.exists("README.md"):
        replacements = [
            ('starter_pypkg', display_name),
            ('OSpoon', github_username),
            ('https://github.com/OSpoon/starter_pypkg', f'https://github.com/{github_username}/{project_name}'),
            ('pip install starter_pypkg', f'pip install {package_name}'),
            ('uv pip install starter_pypkg', f'uv pip install {package_name}'),
            ('from starter_pypkg import add', f'from {package_name} import add'),
            ('python -m starter_pypkg 1 2', f'python -m {package_name} 1 2'),
        ]
        replace_in_file("README.md", replacements)
        add_log("已更新 README.md")
    
    # 更新LICENSE
    if os.path.exists("LICENSE"):
        replacements = [
            ('Copyright (c) 2025 小鑫同学', f'Copyright (c) {copyright_year} {author_name}'),
        ]
        replace_in_file("LICENSE", replacements)
        add_log("已更新 LICENSE")
    
    # 更新其他文件
    github_files = [
        '.github/ISSUE_TEMPLATE/bug_report.yml',
        '.github/ISSUE_TEMPLATE/feature_request.yml',
        '.github/FUNDING.yml',
        '.github/PULL_REQUEST_TEMPLATE.md',
        'CONTRIBUTING.md'
    ]
    
    for file_path in github_files:
        if os.path.exists(file_path):
            replacements = [
                ('OSpoon', github_username),
                ('OSpoon/starter_pypkg', f'{github_username}/{project_name}'),
            ]
            replace_in_file(file_path, replacements)
            add_log(f"已更新 {file_path}")
    
    # 更新workflows
    workflow_files = [
        '.github/workflows/python-package.yml',
        '.github/workflows/pytest.yml',
        '.github/workflows/ruff.yml',
    ]
    
    for file_path in workflow_files:
        if os.path.exists(file_path):
            replacements = [
                ('OSpoon/starter_pypkg', f'{github_username}/{project_name}'),
            ]
            replace_in_file(file_path, replacements)
            add_log(f"已更新 {file_path}")
    
    if os.path.exists('.github/workflows/python-publish.yml'):
        replacements = [
            ('starter_pypkg', package_name),
        ]
        replace_in_file('.github/workflows/python-publish.yml', replacements)
        add_log("已更新 .github/workflows/python-publish.yml")
    
    # 重命名源代码目录
    add_log("重命名源代码目录...")
    if os.path.exists("src/starter_pypkg"):
        # 创建新目录
        if not os.path.exists(f"src/{package_name}"):
            os.makedirs(f"src/{package_name}", exist_ok=True)
            
        # 复制文件
        for item in os.listdir("src/starter_pypkg"):
            src_path = os.path.join("src/starter_pypkg", item)
            dst_path = os.path.join(f"src/{package_name}", item)
            
            if os.path.isfile(src_path):
                shutil.copy2(src_path, dst_path)
            elif os.path.isdir(src_path):
                shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
        
        # 更新__init__.py中的导入
        init_file = f"src/{package_name}/__init__.py"
        if os.path.exists(init_file):
            replacements = [
                ('from .starter_pypkg import add', f'from .{package_name} import add'),
            ]
            replace_in_file(init_file, replacements)
            add_log("已更新 __init__.py")
        
        # 更新__main__.py中的导入
        main_file = f"src/{package_name}/__main__.py"
        if os.path.exists(main_file):
            replacements = [
                ('from .starter_pypkg import cli', f'from .{package_name} import cli'),
            ]
            replace_in_file(main_file, replacements)
            add_log("已更新 __main__.py")
        
        # 重命名源文件
        if os.path.exists(f"src/{package_name}/starter_pypkg.py"):
            os.rename(f"src/{package_name}/starter_pypkg.py", f"src/{package_name}/{package_name}.py")
            add_log(f"已重命名 starter_pypkg.py 为 {package_name}.py")
            
        # 删除旧目录
        shutil.rmtree("src/starter_pypkg")
        add_log("已删除旧源码目录")
    
    # 更新测试文件
    add_log("更新测试文件...")
    if os.path.exists("tests/test_starter_pypkg.py"):
        replacements = [
            ('from src.starter_pypkg import add', f'from src.{package_name} import add'),
        ]
        replace_in_file("tests/test_starter_pypkg.py", replacements)
        os.rename("tests/test_starter_pypkg.py", f"tests/test_{package_name}.py")
        add_log(f"已重命名并更新测试文件")
    
    # 清理备份文件
    add_log("清理临时文件...")
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".bak"):
                os.remove(os.path.join(root, file))
    
    # 初始化git仓库（可选）
    if reinit_git:
        add_log("初始化git仓库...")
        try:
            if os.path.exists(".git"):
                shutil.rmtree(".git")
            subprocess.run(["git", "init"], check=True)
            subprocess.run(["git", "add", "."], check=True)
            # subprocess.run(["git", "commit", "-m", f"初始化项目: {display_name}"], check=True)
            add_log("Git仓库已初始化")
        except subprocess.SubprocessError as e:
            add_log(f"Git初始化失败: {e}")
    
    add_log("项目初始化完成！")
    
    return "\n".join(log)

def create_ui():
    """创建Gradio界面"""
    with gr.Blocks(title="项目模板初始化工具") as app:
        gr.Markdown("# 项目模板初始化工具")
        gr.Markdown("使用此工具将 starter_pypkg 模板转换为您的项目")
        
        with gr.Row():
            with gr.Column():
                project_name = gr.Textbox(label="项目名称 (python包名, 例如: my_package)", 
                                         value=os.path.basename(os.getcwd()))
                display_name = gr.Textbox(label="项目显示名称 (用于README等文档)", 
                                          info="留空将使用项目名称")
                project_description = gr.Textbox(label="项目描述")
                author_name = gr.Textbox(label="您的名字")
                author_email = gr.Textbox(label="您的邮箱")
                github_username = gr.Textbox(label="GitHub用户名")
                copyright_year = gr.Textbox(label="版权年份", 
                                           value=str(datetime.datetime.now().year))
                reinit_git = gr.Checkbox(label="初始化Git仓库", value=False)
                
                submit_button = gr.Button("初始化项目", variant="primary")
            
            with gr.Column():
                output = gr.Textbox(label="日志输出", lines=20)
        
        submit_button.click(
            fn=initialize_project, 
            inputs=[project_name, display_name, project_description, 
                   author_name, author_email, github_username, 
                   copyright_year, reinit_git],
            outputs=output
        )
        
    return app

if __name__ == "__main__":
    app = create_ui()
    app.launch(inbrowser=True)