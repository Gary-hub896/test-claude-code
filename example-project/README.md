# 任务管理器示例项目

这是一个由 **Claude Code 网页版**自动创建的完整 Flask Web 应用，用于展示网页版的强大功能。

## 项目特点

- ✅ 完整的 Flask Web 应用
- ✅ RESTful API 设计
- ✅ 现代化的前端界面
- ✅ 响应式设计，支持移动设备
- ✅ 包含完整的项目结构

## 项目结构

```
example-project/
├── app.py              # Flask 应用主文件
├── templates/          # HTML 模板目录
│   └── index.html     # 主页面
├── requirements.txt    # Python 依赖
└── README.md          # 项目说明
```

## 功能特性

### 后端 API (app.py)

- `GET /` - 主页
- `GET /api/tasks` - 获取所有任务
- `POST /api/tasks` - 创建新任务
- `PUT /api/tasks/<id>` - 更新任务状态
- `DELETE /api/tasks/<id>` - 删除任务
- `GET /health` - 健康检查

### 前端界面 (index.html)

- 任务列表展示
- 添加新任务
- 标记任务完成/未完成
- 删除任务
- 统计已完成任务数量
- 美观的渐变色背景
- 流畅的动画效果

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行应用

```bash
python app.py
```

### 3. 访问应用

在浏览器中打开：http://localhost:5000

## 技术栈

- **后端**: Python 3.x + Flask
- **前端**: HTML5 + CSS3 + JavaScript (原生)
- **API**: RESTful 风格

## 这个项目展示了什么？

### 1. 快速创建完整项目

Claude Code 网页版可以在几秒钟内创建包含多个文件的完整项目结构，包括：
- Python 后端代码
- HTML 前端模板
- 项目配置文件
- 说明文档

### 2. 自动化的 Git 操作

所有文件的创建和修改都会自动：
- 在专用分支上进行
- 提交到 Git
- 推送到 GitHub

### 3. 团队协作友好

- 代码在 GitHub 上可见
- 其他人可以直接 clone 和运行
- 方便进行代码审查

### 4. 跨设备访问

- 无需本地环境配置
- 任何浏览器都能访问
- 代码云端存储

## 扩展建议

这个示例项目可以轻松扩展：

1. **添加数据库**: 使用 SQLite 或 PostgreSQL
2. **用户认证**: 添加登录/注册功能
3. **部署**: 部署到 Heroku、Vercel 等平台
4. **测试**: 添加单元测试和集成测试
5. **前端框架**: 迁移到 React、Vue 等框架

## 下一步

尝试对这个项目进行修改：

- 要求 Claude 添加新功能
- 修改样式和布局
- 添加新的 API 端点
- 优化代码结构

所有修改都会自动提交和推送到 GitHub！

---

**由 Claude Code 网页版创建** - 2025-11-05
