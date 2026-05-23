# CodeBuddy/Claw 项目部署指南

## 第一步：准备 GitHub 账户

1. 如果没有 GitHub 账户，去 [github.com](https://github.com) 注册
2. 记下你的 GitHub 用户名和邮箱

## 第二步：创建 GitHub 仓库

1. 登录 GitHub，点击右上角 "+" → "New repository"
2. 填写信息：
   - **Repository name**: `claw`（或你喜欢的名字）
   - **Description**: 基于 MiMo API 的 AI 聊天机器人
   - **Public**（免费）或 **Private**
   - **不要**勾选 "Initialize this repository with a README"
3. 点击 "Create repository"

## 第三步：配置 Git 认证

### 方式一：SSH 密钥（推荐，一劳永逸）

1. 打开终端（Git Bash 或 PowerShell）
2. 生成 SSH 密钥：
   ```bash
   ssh-keygen -t ed25519 -C "你的邮箱@example.com"
   ```
   - 一路回车使用默认设置
3. 查看公钥：
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```
4. 复制公钥内容
5. 到 GitHub → Settings → SSH and GPG keys → New SSH key
6. 粘贴公钥，保存

### 方式二：个人访问令牌（简单但需定期更新）

1. GitHub → Settings → Developer settings → Personal access tokens → Generate new token
2. 勾选 `repo` 权限
3. 生成并复制令牌

## 第四步：初始化本地仓库并推送

在项目目录下运行：

```bash
# 初始化 Git 仓库
git init

# 添加所有文件
git add .

# 第一次提交
git commit -m "Initial commit: CodeBuddy/Claw 项目初始化"

# 设置主分支名
git branch -M main

# 添加远程仓库（替换成你的 GitHub 用户名和仓库名）
git remote add origin https://github.com/你的用户名/claw.git

# 推送
git push -u origin main
```

如果使用个人访问令牌，推送时用令牌代替密码。

## 第五步：配置 GitHub Actions Secrets

1. 进入你的 GitHub 仓库
2. 点击 Settings → Secrets and variables → Actions
3. 点击 "New repository secret"
4. 添加以下 Secrets：

| 名称 | 说明 | 示例 |
|------|------|------|
| `MIMO_API_KEY` | MiMo API 密钥 | `your-api-key-here` |
| `MIMO_API_BASE` | API 基础地址（可选） | `https://api.mimo.com/v1` |
| `PUSH_METHOD` | 推送方式 | `console` |
| `WEBHOOK_URL` | Webhook 地址（可选） | `https://your-webhook-url.com` |
| `EMAIL_TO` | 接收邮箱（可选） | `your@email.com` |

## 第六步：启用 GitHub Actions

1. 进入仓库的 Actions 页面
2. 点击 "I understand my workflows, go ahead and enable them"
3. 工作流将每天自动运行：
   - 早上 8:00（北京时间）推送周易
   - 早上 9:00（北京时间）推送古诗

## 第七步：测试运行

### 本地测试

```bash
# 安装依赖
pip install -r requirements.txt

# 设置环境变量
export MIMO_API_KEY="你的API密钥"

# 测试聊天机器人
python main.py

# 测试自动化任务
python -c "from automation import automation_manager; automation_manager.run_task('每日周易推送')"
```

### GitHub Actions 手动测试

1. 在 Actions 页面选择 "Daily Push Automation"
2. 点击 "Run workflow"
3. 选择分支（main）
4. 点击 "Run workflow" 按钮

## 第八步：查看运行结果

1. 在 Actions 页面可以看到运行状态
2. 点击具体的运行可以查看日志
3. 如果推送方式设置为 `console`，日志中会显示推送内容

## 常见问题

### Q: 没有 MiMo API 密钥怎么办？
A: 可以先使用模拟数据测试。修改 `config.py` 中的 `mimo_api_key` 为空字符串，系统会使用默认回复。

### Q: GitHub Actions 不运行？
A: 检查以下几点：
1. 确保仓库是公开的（私有仓库有免费额度限制）
2. 检查 Secrets 是否正确设置
3. 查看 Actions 页面的运行日志

### Q: 如何修改推送时间？
A: 修改 `.github/workflows/daily-push.yml` 中的 cron 表达式：
```yaml
- cron: '0 0 * * *'  # 周易推送（UTC 0点，北京时间8点）
- cron: '0 1 * * *'  # 古诗推送（UTC 1点，北京时间9点）
```

### Q: 如何添加新的推送渠道？
A: 在 `automation.py` 中实现新的推送方法，并在 `config.py` 中添加配置。

## 项目结构说明

```
Claw/
├── main.py              # 主程序入口
├── config.py            # 配置管理
├── automation.py        # 自动化任务模块
├── requirements.txt     # Python 依赖
├── .github/
│   └── workflows/
│       └── daily-push.yml  # GitHub Actions 工作流
├── data/                # 数据存储目录（自动生成）
├── tests/               # 测试文件
├── README.md            # 项目说明
└── SETUP.md             # 部署指南（本文件）
```

## 下一步

1. 推送代码到 GitHub
2. 配置 Secrets
3. 测试运行
4. 根据需要调整配置
5. 开始使用！

---

如有问题，可以查看 GitHub Issues 或联系开发者。