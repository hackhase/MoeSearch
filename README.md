# 🔍 MoeSearch

> 一个极简、极速、开箱即用的开源资源搜索引擎。

![Vue.js](https://img.shields.io/badge/Vue.js-3.x-green.svg?style=flat-square&logo=vue.js)
![Django](https://img.shields.io/badge/Django-5.x-darkgreen.svg?style=flat-square&logo=django)
![MySQL](https://img.shields.io/badge/MySQL-8.0-blue.svg?style=flat-square&logo=mysql)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)

<img width="871" height="823" alt="MoeSearch 预览图" src="https://github.com/user-attachments/assets/a0be8d53-7134-4454-9f9a-789f186fa228" />

## ✨ 核心特性

- 🚀 **极速检索**：针对海量数据深度优化，精准锁定标题字段，单表 48 万数据响应耗时控制在百毫秒以内。
- 🎨 **现代极简 UI**：基于 Vue3 + Vite 构建，现代扁平化设计，绝佳视觉体验。
- 🔓 **零鉴权限制**：无需复杂的 API Key 登录，克隆代码、导入数据即可直接运行。
- 📦 **开箱即用**：附带 2000 条真实演示数据，拒绝空壳。

## 🛠️ 技术栈

- **前端**：Vue 3 + Vite + Axios + Vue Router
- **后端**：Python 3.10+ + Django 5.x + Django REST Framework
- **数据库**：MySQL 8.0+

## 🚀 快速启动

### 1. 克隆项目

    git clone https://github.com/hackhase/MoeSearch.git
    cd MoeSearch

### 2. 配置后端 (Django)

    # 创建并激活虚拟环境
    python -m venv venv
    venv\Scripts\activate

    # 安装依赖
    pip install -r requirements.txt

    # 修改数据库配置
    # 打开 backend/settings.py，修改 DATABASES 为你的本地 MySQL 账号密码

    # 导入演示数据 (假设你已经建好了数据库)
    mysql -u root -p 你的数据库名 < demo_data.sql

    # 启动后端
    python manage.py runserver

### 3. 配置前端 (Vue3)

    cd frontend
    pnpm install
    pnpm dev

访问 `http://localhost:5173` 即可看到页面。

---

## 💡 关于作者

如果你觉得这个项目对你有帮助，欢迎点个 **Star ⭐**！

如果你在部署中遇到环境问题，或需要 **48 万条全量真实数据**，可以联系作者提供有偿协助。承接各类 Python 爬虫定制、Vue/Django 全栈开发外包。

<div align="center">
  <h3>📬 作者联系方式</h3>
  <p>扫码添加微信，备注“MoeSearch”</p>
  <img src="https://github.com/user-attachments/assets/c091a504-3908-45de-b9b3-735c4e29708c" width="300" alt="微信二维码" />
</div>
