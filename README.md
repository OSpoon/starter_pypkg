# starter_pypkg

[![Python package](https://github.com/OSpoon/starter_pypkg/actions/workflows/python-package.yml/badge.svg)](https://github.com/OSpoon/starter_pypkg/actions/workflows/python-package.yml)
[![Pytest and Coverage](https://github.com/OSpoon/starter_pypkg/actions/workflows/pytest.yml/badge.svg)](https://github.com/OSpoon/starter_pypkg/actions/workflows/pytest.yml)
[![PyPI version](https://badge.fury.io/py/starter_pypkg.svg)](https://badge.fury.io/py/starter_pypkg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一个现代Python包开发模板，集成了以下特性：

- ✨ 使用 `pyproject.toml` 进行项目配置
- 🎯 严格的类型检查 (`mypy`)
- 🔍 代码质量检查 (`ruff`)
- ✅ 单元测试 (`pytest`)
- 📊 代码覆盖率检查 (`coverage`)
- 🔄 CI/CD 支持 (GitHub Actions)
- 📦 自动发布到 PyPI
- 💡 VS Code 开发环境支持

## 安装

使用 pip 安装:

```bash
pip install starter_pypkg
```

或使用 uv 安装:

```bash
uv pip install starter_pypkg
```

## 使用示例

```python
from starter_pypkg import add

# 基础使用
result = add(1, 2)  # 返回 3

# CLI 方式使用
python -m starter_pypkg 1 2  # 输出: Result: 3
```

## 开发指南

1. 克隆仓库:

```bash
git clone https://github.com/OSpoon/starter_pypkg.git
cd starter_pypkg
```

2. 创建虚拟环境:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# 或
.venv\Scripts\activate  # Windows
```

3. 安装开发依赖:

```bash
pip install -e ".[dev]"
```

4. 安装 pre-commit hooks:

```bash
pre-commit install
```

### 运行测试

```bash
pytest
```

### 检查代码覆盖率

```bash
coverage run -m pytest
coverage report
```

## VS Code 配置

本项目包含推荐的 VS Code 配置，安装以下推荐的扩展以获得最佳开发体验：

- Python
- Pylance
- Ruff
- mypy Type Checker

## 贡献指南

欢迎贡献! 请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详细信息。

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详细信息。

## 支持

如果这个项目对您有帮助，请考虑给它一个星标 ⭐️

您也可以通过以下方式支持本项目：
- 报告 Issues
- 提交 Pull Requests
- 分享给其他开发者

## 相关链接

- [项目主页](https://github.com/OSpoon/starter_pypkg/)
- [问题反馈](https://github.com/OSpoon/starter_pypkg/issues)