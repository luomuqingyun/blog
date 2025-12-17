# GitHub 命令及参数详解

## Git 核心命令详解

### 1. git init - 初始化仓库
```bash
git init                    # 在当前目录初始化仓库
git init <directory>        # 在指定目录初始化仓库
git init --bare            # 创建裸仓库（服务器端）
git init --template=<path> # 使用模板目录
```

### 2. git clone - 克隆仓库
```bash
git clone <url>                           # 克隆到当前目录
git clone <url> <directory>               # 克隆到指定目录
git clone --depth <num> <url>            # 浅克隆（只克隆最近的提交）
git clone --branch <branch> <url>        # 克隆指定分支
git clone --single-branch <url>          # 只克隆单个分支
git clone --recursive <url>              # 递归克隆子模块
git clone --mirror <url>                 # 镜像克隆
```

### 3. git add - 添加文件到暂存区
```bash
git add <file>                # 添加指定文件
git add .                     # 添加当前目录所有文件
git add -A                    # 添加所有文件（包括删除的）
git add -u                    # 只添加已跟踪的文件
git add -p                    # 交互式添加
git add -n                    # 预览将要添加的文件
git add --ignore-errors       # 忽略错误继续添加
```

### 4. git commit - 提交更改
```bash
git commit -m "message"       # 提交并添加消息
git commit -am "message"      # 添加已跟踪文件并提交
git commit --amend           # 修改最后一次提交
git commit --amend --no-edit # 修改最后一次提交，不修改提交信息
git commit --amend -m "new"  # 修改最后一次提交消息
git commit --no-verify       # 跳过 pre-commit 钩子
git commit --allow-empty     # 允许空提交
git commit -S                # 使用 GPG 签名提交
git commit --date="date"     # 指定提交日期
```

### 5. git status - 查看状态
```bash
git status                   # 显示工作区状态
git status -s               # 简短格式显示
git status --porcelain      # 机器可读格式
git status -b               # 显示分支信息
git status --ignored        # 显示被忽略的文件
git status -uno             # 不显示未跟踪文件
```

### 6. git log - 查看历史
```bash
git log                      # 显示完整历史
git log --oneline           # 每行一个提交
git log --graph             # 图形化显示
git log --stat              # 显示文件变更统计
git log --patch             # 显示具体更改
git log -p                  # 同 --patch
git log -n <num>            # 显示最近 n 个提交
git log --since="date"      # 指定时间后的提交
git log --until="date"      # 指定时间前的提交
git log --author="name"     # 指定作者的提交
git log --grep="pattern"    # 搜索提交消息
git log --all               # 显示所有分支
git log --decorate          # 显示分支和标签信息
git log --pretty=format:"%h %s" # 自定义格式
```

### 7. git diff - 查看差异
```bash
git diff                    # 工作区与暂存区差异
git diff --staged          # 暂存区与最后提交差异
git diff --cached          # 同 --staged
git diff HEAD              # 工作区与最后提交差异
git diff <commit>          # 与指定提交差异
git diff <commit1> <commit2> # 两个提交间差异
git diff --name-only       # 只显示文件名
git diff --stat            # 显示统计信息
git diff --word-diff       # 按单词显示差异
git diff --color-words     # 彩色显示单词差异
```

### 8. git branch - 分支操作
```bash
git branch                  # 列出本地分支
git branch -r              # 列出远程分支
git branch -a              # 列出所有分支
git branch <name>          # 创建新分支
git branch -d <name>       # 删除分支
git branch -D <name>       # 强制删除分支
git branch -m <old> <new>  # 重命名分支
git branch -u <remote>     # 设置上游分支
git branch --merged        # 显示已合并分支
git branch --no-merged     # 显示未合并分支
git branch -v              # 显示最后一次提交
git branch --contains <commit> # 包含指定提交的分支
```

### 9. git checkout - 切换分支/检出文件
```bash
git checkout <branch>       # 切换分支
git checkout -b <branch>    # 创建并切换分支
git checkout -B <branch>    # 强制创建并切换分支
git checkout -- <file>     # 恢复文件到最后提交状态
git checkout <commit>       # 检出指定提交（分离HEAD）
git checkout <commit> -- <file> # 恢复文件到指定提交状态
git checkout -p            # 交互式检出
git checkout -t <remote/branch> # 创建跟踪分支
```

### 10. git merge - 合并分支
```bash
git merge <branch>          # 合并指定分支
git merge --no-ff <branch>  # 禁用快进合并
git merge --ff-only <branch> # 只允许快进合并
git merge --squash <branch> # 压缩合并
git merge --abort          # 取消合并
git merge --continue       # 继续合并
git merge -s <strategy>    # 指定合并策略
git merge -X <option>      # 指定合并选项
```

### 11. git rebase - 变基操作
```bash
git rebase <branch>         # 变基到指定分支
git rebase -i <commit>      # 交互式变基
git rebase --continue       # 继续变基
git rebase --abort         # 取消变基
git rebase --skip          # 跳过当前提交
git rebase --onto <new> <old> <branch> # 复杂变基
git rebase --preserve-merges # 保留合并提交
```

### 12. git reset - 重置操作
```bash
git reset                   # 取消暂存所有文件
git reset <file>           # 取消暂存指定文件
git reset --soft <commit>  # 软重置（保留更改）
git reset --mixed <commit> # 混合重置（默认）
git reset --hard <commit>  # 硬重置（丢弃更改）
git reset HEAD~1           # 重置到上一个提交
git reset --merge          # 重置合并状态
```

### 13. git remote - 远程仓库管理
```bash
git remote                  # 列出远程仓库
git remote -v              # 显示详细信息
git remote add <name> <url> # 添加远程仓库
git remote remove <name>    # 删除远程仓库
git remote rename <old> <new> # 重命名远程仓库
git remote set-url <name> <url> # 修改远程仓库URL
git remote show <name>     # 显示远程仓库详情
git remote prune <name>    # 清理远程分支引用
```

### 14. git push - 推送到远程
```bash
git push                    # 推送当前分支
git push <remote> <branch>  # 推送到指定远程分支
git push -u <remote> <branch> # 推送并设置上游
git push --all             # 推送所有分支
git push --tags            # 推送所有标签
git push --force           # 强制推送
git push --force-with-lease # 安全的强制推送
git push --delete <remote> <branch> # 删除远程分支
git push --set-upstream <remote> <branch> # 设置上游分支
```

### 15. git pull - 拉取远程更新
```bash
git pull                    # 拉取并合并
git pull <remote> <branch>  # 从指定远程分支拉取
git pull --rebase          # 拉取并变基
git pull --no-rebase       # 拉取并合并
git pull --ff-only         # 只允许快进
git pull --all             # 拉取所有远程分支
git pull --tags            # 拉取标签
```

### 16. git fetch - 获取远程更新
```bash
git fetch                   # 获取默认远程更新
git fetch <remote>         # 获取指定远程更新
git fetch --all            # 获取所有远程更新
git fetch --tags           # 获取标签
git fetch --prune          # 清理本地远程分支引用
git fetch --depth=<n>      # 浅获取
```

### 17. git tag - 标签操作
```bash
git tag                     # 列出所有标签
git tag <tagname>          # 创建轻量标签
git tag -a <tagname> -m "message" # 创建带注释标签
git tag -d <tagname>       # 删除本地标签
git tag -l "pattern"       # 按模式列出标签
git show <tagname>         # 显示标签信息
git push origin <tagname>  # 推送标签
git push origin --tags     # 推送所有标签
```

### 18. git stash - 暂存工作区
```bash
git stash                   # 暂存当前更改
git stash save "message"   # 暂存并添加消息
git stash list             # 列出所有暂存
git stash show             # 显示最新暂存内容
git stash apply            # 应用最新暂存
git stash pop              # 应用并删除最新暂存
git stash drop             # 删除最新暂存
git stash clear            # 清空所有暂存
git stash branch <branch>  # 从暂存创建分支
```

## GitHub CLI (gh) 命令详解

### 安装和认证
```bash
# 安装 (macOS)
brew install gh

# 安装 (Ubuntu/Debian)
sudo apt install gh

# 认证
gh auth login              # 登录 GitHub
gh auth logout             # 登出
gh auth status             # 查看认证状态
gh auth refresh            # 刷新认证
gh auth setup-git          # 设置 Git 认证
```

### 1. gh repo - 仓库操作
```bash
gh repo create <name>       # 创建仓库
gh repo create --private    # 创建私有仓库
gh repo create --public     # 创建公开仓库
gh repo create --clone      # 创建并克隆
gh repo create --template <template> # 使用模板创建

gh repo clone <repo>        # 克隆仓库
gh repo fork <repo>         # Fork 仓库
gh repo fork --clone        # Fork 并克隆

gh repo view               # 查看当前仓库
gh repo view <repo>        # 查看指定仓库
gh repo view --web         # 在浏览器中查看

gh repo list               # 列出用户仓库
gh repo list <owner>       # 列出指定用户仓库
gh repo list --limit <n>   # 限制显示数量
gh repo list --public      # 只显示公开仓库
gh repo list --private     # 只显示私有仓库

gh repo delete <repo>      # 删除仓库
gh repo archive <repo>     # 归档仓库
gh repo edit              # 编辑仓库设置
```

### 2. gh pr - Pull Request 操作
```bash
gh pr create               # 创建 PR
gh pr create --title "title" # 指定标题
gh pr create --body "body" # 指定描述
gh pr create --draft      # 创建草稿 PR
gh pr create --assignee <user> # 指定负责人
gh pr create --reviewer <user> # 指定审查者
gh pr create --label <label> # 添加标签
gh pr create --milestone <milestone> # 指定里程碑

gh pr list                # 列出 PR
gh pr list --state open   # 只显示开放的 PR
gh pr list --state closed # 只显示关闭的 PR
gh pr list --state merged # 只显示已合并的 PR
gh pr list --author <user> # 指定作者
gh pr list --assignee <user> # 指定负责人
gh pr list --label <label> # 指定标签
gh pr list --limit <n>    # 限制显示数量

gh pr view <number>       # 查看 PR 详情
gh pr view --web          # 在浏览器中查看
gh pr view --comments     # 显示评论

gh pr checkout <number>   # 检出 PR 分支
gh pr diff <number>       # 查看 PR 差异
gh pr status             # 查看 PR 状态

gh pr merge <number>      # 合并 PR
gh pr merge --merge      # 使用合并提交
gh pr merge --squash     # 压缩合并
gh pr merge --rebase     # 变基合并
gh pr merge --delete-branch # 合并后删除分支

gh pr close <number>      # 关闭 PR
gh pr reopen <number>     # 重新打开 PR
gh pr ready <number>      # 将草稿标记为就绪
gh pr review <number>     # 审查 PR
gh pr review --approve    # 批准 PR
gh pr review --request-changes # 请求更改
```

### 3. gh issue - Issue 操作
```bash
gh issue create           # 创建 Issue
gh issue create --title "title" # 指定标题
gh issue create --body "body" # 指定描述
gh issue create --assignee <user> # 指定负责人
gh issue create --label <label> # 添加标签
gh issue create --milestone <milestone> # 指定里程碑

gh issue list             # 列出 Issues
gh issue list --state open # 只显示开放的 Issues
gh issue list --state closed # 只显示关闭的 Issues
gh issue list --author <user> # 指定作者
gh issue list --assignee <user> # 指定负责人
gh issue list --label <label> # 指定标签
gh issue list --limit <n> # 限制显示数量

gh issue view <number>    # 查看 Issue 详情
gh issue view --web       # 在浏览器中查看
gh issue view --comments  # 显示评论

gh issue close <number>   # 关闭 Issue
gh issue reopen <number>  # 重新打开 Issue
gh issue edit <number>    # 编辑 Issue
gh issue comment <number> # 添加评论
gh issue pin <number>     # 固定 Issue
gh issue unpin <number>   # 取消固定 Issue
```

### 4. gh release - Release 操作
```bash
gh release create <tag>   # 创建 Release
gh release create --title "title" # 指定标题
gh release create --notes "notes" # 指定说明
gh release create --draft # 创建草稿
gh release create --prerelease # 创建预发布
gh release create --generate-notes # 自动生成说明

gh release list           # 列出 Releases
gh release list --limit <n> # 限制显示数量

gh release view <tag>     # 查看 Release 详情
gh release view --web     # 在浏览器中查看

gh release download <tag> # 下载 Release 资源
gh release download --pattern "*.zip" # 按模式下载
gh release download --dir <dir> # 下载到指定目录

gh release delete <tag>   # 删除 Release
gh release edit <tag>     # 编辑 Release
gh release upload <tag> <file> # 上传文件到 Release
```

### 5. gh workflow - GitHub Actions 工作流
```bash
gh workflow list          # 列出工作流
gh workflow view <name>   # 查看工作流详情
gh workflow run <name>    # 运行工作流
gh workflow enable <name> # 启用工作流
gh workflow disable <name> # 禁用工作流

gh run list              # 列出工作流运行
gh run view <id>         # 查看运行详情
gh run rerun <id>        # 重新运行
gh run cancel <id>       # 取消运行
gh run logs <id>         # 查看运行日志
gh run download <id>     # 下载运行产物
```

### 6. gh secret - 密钥管理
```bash
gh secret list           # 列出密钥
gh secret set <name>     # 设置密钥
gh secret remove <name>  # 删除密钥
```

### 7. gh alias - 别名管理
```bash
gh alias list            # 列出别名
gh alias set <alias> <command> # 设置别名
gh alias delete <alias>  # 删除别名
```

## 配置和高级功能

### Git 配置
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
git config --global init.defaultBranch main
git config --global core.editor vim
git config --global merge.tool vimdiff
git config --global color.ui auto
git config --global push.default simple
git config --global pull.rebase false
git config --global core.autocrlf input  # Linux/Mac
git config --global core.autocrlf true   # Windows
```

### 常用别名配置
```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.df diff
git config --global alias.lg "log --oneline --graph --decorate --all"
git config --global alias.unstage "reset HEAD --"
git config --global alias.last "log -1 HEAD"
git config --global alias.visual "!gitk"
```

### .gitignore 文件
```bash
# 查看忽略文件
git ls-files --others --ignored --exclude-standard

# 常见忽略模式
*.log
*.tmp
/build/
/node_modules/
.env
.DS_Store
```

### Git Hooks 示例
```bash
# pre-commit hook 示例
#!/bin/sh
# 在提交前检查代码风格
npm run lint
if [ $? -ne 0 ]; then
    echo "Linting failed. Please fix errors before committing."
    exit 1
fi
```

这些命令和参数覆盖了 Git 和 GitHub CLI 的大部分功能。建议从基础命令开始学习，逐步掌握高级功能。每个命令都有更多选项，可以通过 `git help <command>` 或 `gh <command> --help` 查看完整文档。