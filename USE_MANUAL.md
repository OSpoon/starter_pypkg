## 使用手册

### 1. 创建新项目

有两种方式可以使用此模板:

1. 点击 GitHub 仓库页面上的 "Use this template" 按钮创建新仓库
2. 手动克隆并重置:
```bash
# 克隆仓库
git clone https://github.com/OSpoon/starter_pypkg.git your-project-name
cd your-project-name

# 删除原有的 git 历史
rm -rf .git
git init
```

### 2. 修改项目信息

1. 修改 `pyproject.toml`:
```toml
[project]
name = "your-project-name"  # 修改包名
version = "0.1.0"           # 修改版本号
authors = [
    { name = "Your Name", email = "your.email@example.com" }  # 修改作者信息
]
description = "Your project description"  # 修改项目描述
```

2. 重命名包目录:
```bash
mv src/starter_pypkg src/your_project_name
```

3. 修改导入路径:
- 更新 `src/your_project_name/__init__.py` 中的导入语句
- 更新 `tests/test_your_project_name.py` 中的导入语句

4. 更新 README.md:
- 修改项目名称和描述
- 更新示例代码
- 修改仓库链接

5. 更新其他文件:
- `.github/workflows/*.yml`: 修改 CI/CD 配置
- `LICENSE`: 更新版权信息
- `CONTRIBUTING.md`: 更新贡献指南
- `.github/*`: 更新 Issue 和 PR 模板

### 3. 开发工作流程

1. 安装开发依赖:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# 或
.venv\Scripts\activate     # Windows

pip install -e ".[dev]"   # 安装所有开发依赖
pre-commit install        # 安装 git hooks
```

2. 开发新功能:
```bash
git checkout -b feature/your-feature  # 创建功能分支
# 编写代码和测试
pytest                               # 运行测试
git commit -m "feat: your feature"   # 提交代码
```

3. 代码质量检查:
```bash
mypy src/                  # 类型检查
ruff check .               # 代码风格检查
ruff format .              # 代码格式化
coverage run -m pytest     # 运行测试并收集覆盖率
coverage report            # 查看覆盖率报告
```

### 4. 发布流程

1. 更新版本号:
- 修改 `pyproject.toml` 中的 `version`

2. 创建 Release:
- 在 GitHub 上创建新的 Release
- CI 将自动构建并发布到 PyPI

3. 手动发布到 PyPI (如需要):
```bash
python -m build           # 构建分发包
twine upload dist/*       # 上传到 PyPI
```

### 5. VS Code 开发环境

1. 安装推荐的扩展:
- Python
- Pylance
- Ruff
- mypy Type Checker

2. 工作区设置已配置好:
- 保存时自动格式化
- 类型检查
- 代码质量检查
- 测试集成
