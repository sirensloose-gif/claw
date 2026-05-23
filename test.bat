@echo off
echo ========================================
echo CodeBuddy/Claw 本地测试
echo ========================================
echo.

cd /d D:\Projects\CodeBuddy

echo 1. 测试周易推送
echo -------------------
python -c "from automation import automation_manager; automation_manager.run_task('每日周易推送')"
echo.

echo 2. 测试古诗推送
echo -------------------
python -c "from automation import automation_manager; automation_manager.run_task('每日古诗谚语推送')"
echo.

echo ========================================
echo 测试完成！
echo ========================================
pause