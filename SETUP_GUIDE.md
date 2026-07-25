# GitHub 仓库设置指南

由于系统未安装 GitHub CLI，请按照以下步骤手动设置 GitHub 仓库。

## 步骤 1：在 GitHub 上创建仓库

1. 访问 https://github.com/new
2. 仓库名称输入：`pebble.github.io`
3. 设置为 **Public**（GitHub Pages 需要公开仓库）
4. **不要**勾选 "Add a README file"（我们已经有了）
5. **不要**添加 .gitignore 或 license（我们已经有了）
6. 点击 "Create repository"

## 步骤 2：连接并推送代码

在项目目录中运行以下命令：

```bash
cd /Users/xinwenfan/Downloads/pebble/pebble.github.io

# 添加 GitHub 远程仓库（请替换 YOUR_USERNAME）
git remote add origin https://github.com/YOUR_USERNAME/pebble.github.io.git

# 或者使用 SSH：
# git remote add origin git@github.com:YOUR_USERNAME/pebble.github.io.git

# 推送代码到 GitHub
git branch -M main
git push -u origin main
```

## 步骤 3：启用 GitHub Pages

1. 访问你的仓库页面：https://github.com/YOUR_USERNAME/pebble.github.io
2. 点击 **Settings** 标签
3. 在左侧菜单中找到 **Pages**
4. 在 "Source" 下选择：
   - **Branch**: `main`
   - **Folder**: `/root`
5. 点击 **Save**

## 步骤 4：等待部署

- GitHub 会自动构建和部署你的网站
- 通常需要 1-5 分钟
- 在 GitHub Actions 标签可以看到构建进度
- 构建完成后，访问：`https://YOUR_USERNAME.github.io/`

## 步骤 5：邀请团队成员（可选）

如果你想邀请团队成员贡献内容：

1. 在 GitHub 仓库页面点击 **Settings**
2. 点击 **Collaborators**
3. 点击 **Add people**
4. 输入团队成员的 GitHub 用户名
5. 设置权限为 **Admin** 或 **Maintain**

## 快速命令参考

```bash
# 进入项目目录
cd /Users/xinwenfan/Downloads/pebble/pebble.github.io

# 查看状态
git status

# 添加新文件
git add .

# 提交更改
git commit -m "Add your message here"

# 推送到 GitHub
git push

# 拉取最新更改
git pull
```

## 团队成员如何添加内容

### 方法 1：直接在 GitHub 网页上编辑

1. 访问仓库中的文件
2. 点击铅笔图标编辑
3. 在页面底部提交更改

### 方法 2：克隆仓库本地编辑

```bash
# 克隆仓库
git clone https://github.com/YOUR_USERNAME/pebble.github.io.git

# 编辑文件后提交
git add .
git commit -m "Add new method"
git push
```

## 常见问题

**Q: 网站显示 404？**
A: 等待几分钟让 GitHub Pages 部署完成，或者检查 GitHub Actions 是否有错误。

**Q: 如何添加自定义域名？**
A: 在 GitHub Pages 设置中可以配置自定义域名。

**Q: 如何添加更多协作者？**
A: 在仓库 Settings > Collaborators 中添加。

---

*创建完成后，团队就可以开始添加内容了！*
