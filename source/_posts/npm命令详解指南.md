# npm命令详解指南

## 1. 安装命令 (install)

### 基本语法
```bash
npm install [<@scope>/]<package>[@<version>] [options]
```

### 详细用法

#### 安装所有依赖
```bash
npm install
npm i  # 简写
```
- 读取package.json中的dependencies和devDependencies
- 生成或更新package-lock.json
- 创建node_modules文件夹

#### 安装指定包
```bash
# 安装最新版本
npm install lodash

# 安装指定版本
npm install lodash@4.17.21

# 安装版本范围
npm install lodash@^4.0.0  # 兼容版本
npm install lodash@~4.17.0 # 近似版本
npm install lodash@latest  # 最新版本
```

#### 安装选项详解
```bash
# 保存到dependencies（默认行为）
npm install express --save
npm install express -S

# 保存到devDependencies
npm install webpack --save-dev
npm install webpack -D

# 全局安装
npm install -g nodemon

# 只安装生产依赖
npm install --production
npm install --only=production

# 不保存到package.json
npm install express --no-save

# 强制重新安装
npm install --force

# 忽略scripts
npm install --ignore-scripts
```

### 实际应用场景
```bash
# 新项目初始化后安装依赖
npm install

# 添加生产依赖
npm install express mongoose cors

# 添加开发依赖
npm install -D webpack babel-loader eslint

# 安装特定版本解决兼容性问题
npm install react@17.0.2 react-dom@17.0.2
```

## 2. 初始化命令 (init)

### 基本语法
```bash
npm init [options]
npm init <package-spec> [options]
```

### 详细用法

#### 交互式初始化
```bash
npm init
```
会提示输入：
- package name: 包名
- version: 版本号
- description: 描述
- entry point: 入口文件
- test command: 测试命令
- git repository: Git仓库
- keywords: 关键词
- author: 作者
- license: 许可证

#### 快速初始化
```bash
npm init -y
npm init --yes
```
使用默认值快速创建package.json

#### 使用模板初始化
```bash
# 创建React应用
npm init react-app my-app

# 创建Vue应用
npm init vue@latest my-vue-app

# 创建Express应用
npm init express-generator my-express-app
```

### 自定义默认值
```bash
# 设置默认作者
npm config set init-author-name "Your Name"
npm config set init-author-email "your.email@example.com"
npm config set init-license "MIT"

# 查看当前配置
npm config list
```

## 3. 脚本运行命令 (run)

### 基本语法
```bash
npm run <script> [-- <args>]
npm run-script <script> [-- <args>]
```

### 详细用法

#### package.json脚本配置
```json
{
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js",
    "build": "webpack --mode=production",
    "test": "jest",
    "lint": "eslint src/",
    "lint:fix": "eslint src/ --fix",
    "clean": "rm -rf dist/",
    "prebuild": "npm run clean",
    "postbuild": "echo 'Build completed'"
  }
}
```

#### 运行脚本
```bash
# 运行自定义脚本
npm run dev
npm run build
npm run lint

# 内置脚本可省略run
npm start  # 等同于 npm run start
npm test   # 等同于 npm run test

# 传递参数
npm run build -- --watch
npm run lint -- --fix

# 查看所有可用脚本
npm run
```

#### 生命周期脚本
```bash
# pre和post钩子
npm run prebuild  # 自动在build前运行
npm run build     # 主要构建命令
npm run postbuild # 自动在build后运行
```

## 4. 信息查询命令

### list - 列出已安装包
```bash
# 列出当前项目依赖
npm list
npm ls

# 只显示顶级依赖
npm ls --depth=0

# 列出全局包
npm ls -g --depth=0

# 列出特定包
npm ls lodash

# 以JSON格式输出
npm ls --json
```

### view - 查看包信息
```bash
# 查看包的详细信息
npm view react

# 查看特定字段
npm view react version
npm view react versions --json
npm view react dependencies
npm view react repository.url

# 查看包的所有版本
npm view react versions
```

### search - 搜索包
```bash
# 搜索包
npm search react
npm search "react component"

# 限制搜索结果
npm search react --searchlimit=10
```

## 5. 更新和维护命令

### update - 更新包
```bash
# 更新所有包
npm update

# 更新特定包
npm update lodash

# 全局更新
npm update -g

# 检查过时的包
npm outdated

# 检查全局过时包
npm outdated -g
```

### audit - 安全审计
```bash
# 检查安全漏洞
npm audit

# 自动修复
npm audit fix

# 强制修复（可能破坏性更改）
npm audit fix --force

# 生产环境审计
npm audit --production

# 输出JSON格式
npm audit --json
```

## 6. 配置管理命令 (config)

### 基本语法
```bash
npm config set <key> <value>
npm config get <key>
npm config delete <key>
npm config list
```

### 常用配置
```bash
# 设置registry镜像源
npm config set registry https://registry.npmmirror.com/

# 设置代理
npm config set proxy http://proxy.company.com:8080
npm config set https-proxy http://proxy.company.com:8080

# 设置用户信息
npm config set init-author-name "Your Name"
npm config set init-author-email "your@email.com"

# 查看所有配置
npm config list

# 查看特定配置
npm config get registry

# 删除配置
npm config delete proxy
```

### 配置文件位置
- 用户配置：`~/.npmrc`
- 项目配置：`项目根目录/.npmrc`
- 系统配置：`/etc/npmrc`

## 7. 缓存管理命令 (cache)

### 基本操作
```bash
# 清理缓存
npm cache clean --force

# 验证缓存
npm cache verify

# 查看缓存路径
npm config get cache

# 设置缓存路径
npm config set cache /path/to/cache
```

## 8. 发布管理命令

### 账户管理
```bash
# 登录npm
npm login

# 查看当前用户
npm whoami

# 登出
npm logout
```

### 发布包
```bash
# 发布包
npm publish

# 发布beta版本
npm publish --tag beta

# 发布私有包
npm publish --access=public

# 撤销发布（24小时内）
npm unpublish package-name@version

# 标记废弃
npm deprecate package-name@version "reason"
```

## 9. 执行命令 (npx)

### 基本用法
```bash
# 执行本地包命令
npx webpack

# 执行远程包（不安装）
npx create-react-app my-app

# 指定版本执行
npx webpack@4

# 强制使用远程版本
npx --ignore-existing webpack

# 静默模式
npx --quiet create-react-app my-app
```

## 10. 常用组合命令

### 项目初始化流程
```bash
# 1. 创建项目目录
mkdir my-project && cd my-project

# 2. 初始化package.json
npm init -y

# 3. 安装依赖
npm install express
npm install -D nodemon

# 4. 创建启动脚本
# 在package.json中添加scripts

# 5. 运行项目
npm run dev
```

### 依赖管理最佳实践
```bash
# 安装前检查过时包
npm outdated

# 安装依赖
npm install

# 安全检查
npm audit

# 修复安全问题
npm audit fix

# 清理无用依赖
npm prune
```

### 性能优化命令
```bash
# 使用淘宝镜像
npm config set registry https://registry.npmmirror.com/

# 并行安装（npm v7+默认）
npm install --maxsockets 10

# 跳过可选依赖
npm install --no-optional

# 离线安装
npm install --offline
```

## 11. 故障排除命令

### 清理和重置
```bash
# 删除node_modules和package-lock.json
rm -rf node_modules package-lock.json

# 清理npm缓存
npm cache clean --force

# 重新安装
npm install

# 修复权限问题（macOS/Linux）
sudo chown -R $(whoami) ~/.npm
```

### 调试命令
```bash
# 详细输出
npm install --verbose

# 调试模式
npm install --loglevel=verbose

# 检查npm配置
npm doctor

# 查看npm版本信息
npm version
```

这个详细指南涵盖了npm的主要命令和实际使用场景，可以作为日常开发的参考手册。