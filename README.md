# 自动签到脚本

这是一个使用GitHub Actions实现的自动签到脚本。

## 功能特点

- 自动登录获取用户信息
- 执行每日签到
- 显示签到结果
- 支持GitHub Actions自动化执行

## 设置说明

### 1. 设置GitHub Secrets

在您的GitHub仓库中设置以下私密变量：

1. 进入仓库页面
2. 点击 `Settings` 标签
3. 在左侧菜单中选择 `Secrets and variables` → `Actions`
4. 点击 `New repository secret` 添加以下变量：

| 变量名 | 描述 |
|--------|------|
| `USERNAME` | 登录用户名 |
| `PASSWORD` | 登录密码 |

### 2. 执行时间

脚本默认设置为每天北京时间早上8点自动执行（UTC时间0点）。

### 3. 手动执行

您也可以手动触发签到：

1. 进入仓库的 `Actions` 标签
2. 选择 `自动签到` 工作流
3. 点击 `Run workflow` 按钮

## 文件说明

- `login.py` - 主要的签到脚本
- `.github/workflows/auto-qiandao.yml` - GitHub Actions工作流配置

## 本地运行

如果需要在本地测试：

```bash
# 设置环境变量
export USERNAME="你的用户名"
export PASSWORD="你的密码"

# 运行脚本
python main.py
```

## 输出示例

```
NAME: Sorynthia
UID:  100750
MSG:  今天已经签到过了
```
