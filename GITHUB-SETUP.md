# GitHub 推送指南

## 第一步：配置 Git 用户信息

在终端中运行以下命令（替换为你的信息）：

```bash
git config --global user.name "你的GitHub用户名"
git config --global user.email "你的GitHub邮箱"
```

## 第二步：初始化本地仓库并提交

```bash
cd D:\Projects\CodeBuddy
git init
git add .
git commit -m "Initial commit: CodeBuddy/Claw 项目初始化"
git branch -M main
```

## 第三步：添加远程仓库

```bash
git remote add origin https://github.com/你的用户名/你的仓库名.git
```

例如：
```bash
git remote add origin https://github.com/xiaowuya/claw.git
```

## 第四步：配置 SSH 密钥（推荐）

### 4.1 生成 SSH 密钥
```bash
ssh-keygen -t ed25519 -C "你的GitHub邮箱"
```
- 一路回车使用默认设置

### 4.2 查看公钥
```bash
cat ~/.ssh/id_ed25519.pub
```

### 4.3 将公钥添加到 GitHub
1. 复制公钥内容
2. 打开 GitHub → Settings → SSH and GPG keys → New SSH key
3. 粘贴公钥，保存

## 第五步：推送代码

```bash
git push -u origin main
```

---

## 常见问题

### Q: 推送时提示认证失败？
A: 如果使用 HTTPS 方式，需要输入 GitHub 用户名和个人访问令牌（不是密码）。

### Q: 如何生成个人访问令牌？
A: 
1. GitHub → Settings → Developer settings → Personal access tokens → Generate new token
2. 勾选 `repo` 权限
3. 生成并复制令牌
4. 推送时用令牌代替密码

### Q: 如何检查远程仓库是否添加成功？
A: 运行 `git remote -v`

### Q: 如何查看当前配置？
A: 运行 `git config --list`

---

## 快速配置脚本

双击运行 `setup-git.bat` 可以自动完成部分配置。

---

## 推送完成后

1. **配置 GitHub Actions Secrets**：
   - 进入仓库 Settings → Secrets and variables → Actions
   - 添加 `MIMO_API_KEY`（你的 MiMo API 密钥）
   - 添加 `PUSH_METHOD`（值为 `console`）

2. **启用 GitHub Actions**：
   - 进入仓库 Actions 页面
   - 点击 "I understand my workflows, go ahead and enable them"

3. **测试运行**：
   - 在 Actions 页面选择 "Daily Push Automation"
   - 点击 "Run workflow" 手动测试

---

## 需要帮助？

如果遇到问题，可以：
1. 查看 GitHub 官方文档
2. 搜索错误信息
3. 告诉我具体错误，我帮你解决