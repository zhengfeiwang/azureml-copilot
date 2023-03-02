from distutils.core import setup

setup(
    name="azureml-copilot",
    version="0.0.1",
    author="Zhengfei Wang",
    author_email="wangzhengfei.chn@outlook.com",
    python_requires="<4.0,>=3.8",
    entry_points={
        "console_scripts": [
            "azureml-copilot=azureml_copilot._cli.commands:main",
            "acw=azureml_copilot._cli.commands:_workspace_parser"
        ]
    },
)
