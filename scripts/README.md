## 使用手册

### 1. 创建新项目

点击 GitHub 仓库页面上的 "Use this template" 按钮创建新仓库

### 2. 初始化项目信息

使用内置的初始化工具可以快速替换所有项目信息：

```bash
# 运行初始化工具
uv run scripts/init.py
```

此工具提供友好的图形界面，帮助您：
- 设置项目名称和描述
- 更新作者信息和GitHub用户名
- 重命名源码目录和相关文件
- 更新所有文件中的引用
- 初始化Git仓库(可选)

工具会自动处理以下文件的更新：
- `pyproject.toml`：包名称、版本号、作者信息等
- `README.md`：项目名称、描述和示例代码
- `LICENSE`：版权信息
- GitHub相关配置文件和工作流程
- 源代码文件和目录结构

### 3. 开发工作流程

1. 安装开发依赖:
```bash
uv venv

source .venv/bin/activate    # Linux/macOS
# 或
.venv\Scripts\activate       # Windows

uv sync                      # 同步项目依赖
pre-commit install           # 安装 git hooks
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