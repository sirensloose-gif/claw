# 本地测试指南

## 推荐方式：CMD 命令提示符

### 方法一：双击测试脚本
直接双击 `test.bat` 文件即可运行测试。

### 方法二：手动运行 CMD 命令
1. 按 `Win + R`，输入 `cmd`，回车
2. 输入以下命令：

```cmd
cd /d D:\Projects\CodeBuddy
python -c "from automation import automation_manager; automation_manager.run_task('每日周易推送')"
```

### 方法三：运行完整聊天机器人
```cmd
cd /d D:\Projects\CodeBuddy
python main.py
```

---

## PowerShell 方式

### 方法一：运行测试命令
1. 按 `Win + X`，选择 "Windows PowerShell" 或 "终端"
2. 输入以下命令：

```powershell
cd D:\Projects\CodeBuddy
python -c "from automation import automation_manager; automation_manager.run_task('每日周易推送')"
```

### 方法二：运行完整聊天机器人
```powershell
cd D:\Projects\CodeBuddy
python main.py
```

---

## 常见问题

### Q: 提示 "python 不是内部或外部命令"？
A: Python 未添加到系统 PATH。解决方法：
1. 重新安装 Python，勾选 "Add Python to PATH"
2. 或手动添加：`D:\Python` 到系统环境变量

### Q: 提示 "No module named 'requests'"？
A: 安装依赖：
```cmd
cd /d D:\Projects\CodeBuddy
pip install -r requirements.txt
```

### Q: 提示 "No module named 'dotenv'"？
A: 安装 python-dotenv：
```cmd
pip install python-dotenv
```

### Q: API 调用失败？
A: 检查 `.env` 文件是否存在且配置正确：
```cmd
type .env
```

---

## 测试命令汇总

### 测试周易推送
```cmd
python -c "from automation import automation_manager; automation_manager.run_task('每日周易推送')"
```

### 测试古诗推送
```cmd
python -c "from automation import automation_manager; automation_manager.run_task('每日古诗谚语推送')"
```

### 列出所有任务
```cmd
python -c "from automation import automation_manager; print(automation_manager.list_tasks())"
```

### 运行聊天机器人
```cmd
python main.py
```

---

## 快速测试

最简单的方式：
1. 双击 `test.bat`
2. 等待测试完成
3. 查看输出结果

---

## 注意事项

1. **确保在项目目录下运行**：`D:\Projects\CodeBuddy`
2. **确保已安装依赖**：`pip install -r requirements.txt`
3. **确保 `.env` 文件存在**：包含正确的 API 密钥
4. **网络连接正常**：需要访问 MiMo API

---

测试完成后，如果一切正常，你会看到：
- 周易推送：乾卦的详细解析
- 古诗推送：《静夜思》的赏析内容