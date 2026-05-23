@echo off
echo ========================================
echo CodeBuddy/Claw 项目 Git 配置脚本
echo ========================================
echo.

echo 请提供以下信息：
echo.

set /p GITHUB_USERNAME="GitHub 用户名: "
set /p GITHUB_EMAIL="GitHub 邮箱: "
set /p REPO_NAME="仓库名 (默认: claw): "

if "%REPO_NAME%"=="" set REPO_NAME=claw

echo.
echo 正在配置 Git...
echo.

:: 设置 Git 用户信息
git config --global user.name "%GITHUB_USERNAME%"
git config --global user.email "%GITHUB_EMAIL%"

:: 初始化仓库
git init
git add .
git commit -m "Initial commit: CodeBuddy/Claw 项目初始化"
git branch -M main

:: 添加远程仓库
git remote add origin https://github.com/%GITHUB_USERNAME%/%REPO_NAME%.git

echo.
echo ========================================
echo 配置完成！
echo ========================================
echo.
echo 下一步：
echo 1. 生成 SSH 密钥：
echo    ssh-keygen -t ed25519 -C "%GITHUB_EMAIL%"
echo.
echo 2. 查看公钥：
echo    cat ~/.ssh/id_ed25519.pub
echo.
echo 3. 将公钥添加到 GitHub：
echo    GitHub → Settings → SSH and GPG keys → New SSH key
echo.
echo 4. 推送代码：
echo    git push -u origin main
echo.
echo ========================================
pause