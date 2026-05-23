# CodeBuddy/Claw

基于 MiMo API 的 AI 聊天机器人 Agent，支持自动化内容推送。

## 功能特性

- 🤖 **智能聊天**：基于 MiMo API 的对话能力
- 📚 **每日周易**：自动推送周易卦象解析
- 🎭 **每日古诗**：自动推送经典古诗赏析
- ⏰ **定时推送**：支持 GitHub Actions 定时执行
- 🔧 **可扩展**：模块化设计，易于添加新功能

## 项目结构

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
└── tests/               # 测试文件
```

## 快速开始

### 1. 本地运行

```bash
# 克隆仓库
git clone https://github.com/你的用户名/claw.git
cd claw

# 安装依赖
pip install -r requirements.txt

# 设置环境变量
export MIMO_API_KEY="你的API密钥"

# 运行聊天机器人
python main.py
```

### 2. GitHub Actions 部署

1. **Fork 或克隆本仓库到你的 GitHub**

2. **设置 Secrets**：
   - 进入仓库 Settings → Secrets and variables → Actions
   - 添加以下 Secrets：
     - `MIMO_API_KEY`: 你的 MiMo API 密钥
     - `MIMO_API_BASE`: API 基础地址（可选）
     - `PUSH_METHOD`: 推送方式（console/email/webhook）
     - `WEBHOOK_URL`: Webhook 地址（可选）
     - `EMAIL_TO`: 接收邮箱（可选）

3. **启用 GitHub Actions**：
   - 进入仓库 Actions 页面
   - 点击 "I understand my workflows, go ahead and enable them"
   - 工作流将每天自动运行

4. **手动触发**：
   - 在 Actions 页面选择 "Daily Push Automation"
   - 点击 "Run workflow" 手动测试

## 配置说明

### 环境变量

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `MIMO_API_KEY` | MiMo API 密钥 | （必填） |
| `MIMO_API_BASE` | API 基础地址 | `https://api.mimo.com/v1` |
| `AUTOMATION_ENABLED` | 是否启用自动化 | `true` |
| `ZHOUYI_PUSH_HOUR` | 周易推送小时（24小时制） | `8` |
| `ZHOUYI_PUSH_MINUTE` | 周易推送分钟 | `0` |
| `POETRY_PUSH_HOUR` | 古诗推送小时 | `9` |
| `POETRY_PUSH_MINUTE` | 古诗推送分钟 | `0` |
| `PUSH_METHOD` | 推送方式 | `console` |
| `WEBHOOK_URL` | Webhook 地址 | （可选） |
| `EMAIL_TO` | 接收邮箱 | （可选） |
| `DATA_DIR` | 数据目录 | `./data` |

### 推送方式

1. **console**：控制台输出（默认，适合本地测试）
2. **webhook**：发送到指定 URL（如企业微信、钉钉机器人）
3. **email**：发送邮件通知

## 自动化任务

### 周易推送
- 每天推送一章周易内容
- 包含卦名、卦辞、爻辞和简要解释
- 自动记录进度，从第1卦开始循环

### 古诗推送
- 每天推送一首经典古诗
- 包含原文、释义和背景故事
- 自动记录进度，按顺序推送

## 开发指南

### 添加新的自动化任务

1. 在 `automation.py` 中创建新的任务类：
```python
class NewTask(AutomationTask):
    def __init__(self):
        super().__init__(
            name="任务名称",
            description="任务描述",
            schedule="执行时间"
        )
    
    def run(self):
        # 实现任务逻辑
        pass
```

2. 在 `AutomationManager.register_default_tasks()` 中注册任务

3. 更新 GitHub Actions 工作流（如需要）

### 本地测试

```bash
# 测试周易推送
python -c "from automation import automation_manager; automation_manager.run_task('每日周易推送')"

# 测试古诗推送
python -c "from automation import automation_manager; automation_manager.run_task('每日古诗谚语推送')"

# 列出所有任务
python -c "from automation import automation_manager; print(automation_manager.list_tasks())"
```

## 常见问题

### Q: GitHub Actions 不运行怎么办？
A: 检查以下几点：
1. 确保仓库是公开的（私有仓库有免费额度限制）
2. 检查 Secrets 是否正确设置
3. 查看 Actions 页面的运行日志

### Q: 如何修改推送时间？
A: 修改环境变量 `ZHOUYI_PUSH_HOUR`、`ZHOUYI_PUSH_MINUTE`、`POETRY_PUSH_HOUR`、`POETRY_PUSH_MINUTE`

### Q: 如何添加新的推送渠道？
A: 在 `automation.py` 中实现新的推送方法，并在 `config.py` 中添加配置

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！