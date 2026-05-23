# 项目已迁移

## 新位置
项目已从 C 盘迁移到 D 盘：

**原位置**: `C:\Users\xiaowuya\WorkBuddy\Claw`
**新位置**: `D:\Projects\CodeBuddy`

## 如何访问

### 方式一：直接访问
```bash
cd D:\Projects\CodeBuddy
```

### 方式二：使用快捷脚本
双击运行 `C:\Users\xiaowuya\WorkBuddy\Claw\go-to-project.bat`

### 方式三：创建符号链接（可选）
以管理员身份运行：
```bash
mklink /D "C:\Users\xiaowuya\WorkBuddy\Claw\project" "D:\Projects\CodeBuddy"
```

## 注意事项

1. **Git 仓库**：项目已完整复制，Git 历史保留
2. **配置文件**：所有配置使用相对路径，无需修改
3. **GitHub Actions**：远程仓库不受影响
4. **WorkBuddy 配置**：`.workbuddy` 目录仍在原位置

## 迁移原因
- C 盘空间不足
- D 盘有更多可用空间
- 项目文件与系统文件分离

## 下一步
1. 在新位置测试项目运行
2. 更新 Git 远程仓库地址（如需要）
3. 继续开发和使用

---

迁移时间：2026-05-23 18:05