from distutils.core import setup

setup(
    name="azureml-copilot",
    version="0.0.1",
    author="Zhengfei Wang",
    author_email="wangzhengfei.chn@outlook.com",
    python_requires="<4.0,>=3.8",
    entry_points={
        "console_scripts": [
            "acl=azureml_copilot._cli.api:list_workspace_api",
            "acg=azureml_copilot._cli.api:get_workspace_api",
        ]
    },
)
