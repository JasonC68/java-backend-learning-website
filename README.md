# 秋招后端 + AI Agent 八股背诵打卡站

一个面向**国内秋招（后端 + AI Agent 方向）**的八股复习工具：把高频面试题按板块整理成打卡清单，配合艾宾浩斯遗忘曲线安排复习，支持自己写答案、跨设备云同步。

题目精选自[小林 coding](https://www.xiaolincoding.com/) 与[小林大模型面试题](https://xiaolinnote.com/ai/)，按「抓主干、避免背太多」的原则做了筛选与分档。

---

## ✨ 主要功能

- **175 道精选必背题**，分 14 个板块：集合、并发、MySQL、JVM、Spring、计算机网络、Redis、扩展(MyBatis/MQ/分布式)、操作系统、Java 基础，以及 4 个 AI 板块（Agent / RAG / 工具调用 / 大模型基础）。
- **每天约 8 题的学习计划**：自动排好建议日期，AI 题打散到每一天。
- **掌握程度打卡**：未开始 / 眼熟 / 能讲框架 / 能扛追问，四档点击切换、自动统计完成率。
- **艾宾浩斯复习**：每次点「复习 +1」按 1/2/4/7/15/30/60 天自动排下次复习，到期标红。
- **多维筛选**：按板块、掌握程度、收藏；日期维度有「今天任务 / 今天打卡 / 明天 / 今日复习」，以及带小红点的自定义日历选任意一天。
- **⭐ 收藏**：给题目加星，一键筛出所有收藏。
- **所见即所得 Markdown 编辑器**（基于 ProseMirror，离线内嵌）：展开任意题写自己的答案，`- `→列表、`# `→标题、`> `→引用，边打边渲染；支持粘贴 markdown 自动解析、Tab 缩进、Cmd±调标题级别、插图。
- **自建题目**：每个板块可随时添加自己的问题。
- **跨设备云同步**：进度与笔记通过 JSONBin 在所有设备间自动同步（打开/切回/每 60 秒自动拉取，失败每 10 秒重试）。

---

## 📁 文件说明

| 文件 | 说明 |
|------|------|
| `秋招必背打卡表-云同步.html` | **主程序**。单文件、自包含（编辑器内核已内嵌），浏览器打开即用，可直接部署 |
| `generate_html_sync.py` | 生成上面 HTML 的脚本（题库、计划、功能都在这里改） |
| `秋招后端八股「必背清单」（基于小林coding）.md` | 分档清单（⭐必背 / 🔸次要 / ⬜可跳过） |
| `云同步-部署说明.md` | 跨设备同步的部署步骤 |
| `打卡表-按钮设置说明.md` | Excel 版打卡表的宏按钮设置说明 |
| `秋招必背打卡表.xlsx` | Excel 版打卡表（早期版本，可离线用） |
| `build_checklist.py` | 生成 Excel 打卡表的脚本 |

> 主程序是自包含的，备份/部署只需要 `秋招必背打卡表-云同步.html` 这一个文件。

---

## 🚀 使用 / 部署

直接双击 `秋招必背打卡表-云同步.html` 用浏览器打开即可本地使用（进度存在本浏览器）。

要**跨设备同步**，按 `云同步-部署说明.md` 三步走（约 10 分钟，全免费）：

1. 在 [JSONBin](https://jsonbin.io) 建一个 Bin 存进度，拿到 Bin ID + Master Key；
2. 把 HTML 部署到任意静态托管拿一个网址（Netlify Drop / GitHub Pages / Cloudflare Pages 均可）；
3. 每台设备打开网址 → 「☁️ 云同步设置」填入 Bin ID + Master Key。

### 用 GitHub Pages 托管（可选）

本仓库可直接开 GitHub Pages：仓库 Settings → Pages → Source 选 `main` 分支根目录，保存后用 `https://<用户名>.github.io/java-backend-learning-website/秋招必背打卡表-云同步.html` 访问。

---

## 🛠 重新生成 HTML（开发者）

编辑器内核基于 ProseMirror，用 esbuild 打包成自包含文件后内嵌进 HTML。`generate_html_sync.py` 会读取打包产物（`/tmp/tui/md.bundle.js` 与 prosemirror 的 CSS）。如需改题库或功能后重新生成：

```bash
# 1) 准备编辑器内核（首次或临时环境被清空后）
cd /tmp && mkdir -p tui && cd tui && npm init -y
npm install prosemirror-model prosemirror-state prosemirror-view prosemirror-markdown \
  prosemirror-example-setup prosemirror-keymap prosemirror-commands prosemirror-schema-list esbuild
# 写入 mdentry.js（编辑器入口，含标题快捷键/粘贴解析/Tab 缩进），再打包：
./node_modules/.bin/esbuild mdentry.js --bundle --format=iife --outfile=md.bundle.js

# 2) 生成 HTML
python3 generate_html_sync.py
```

> 已生成的 `秋招必背打卡表-云同步.html` 是自包含的，仅做备份/部署时无需重新构建。

---

## 📌 复习优先级建议

集合 ≈ 并发 ＞ MySQL ≈ JVM ＞ Spring ＞ 网络 ＞ Redis ＞ 扩展 ＞ 操作系统 ＞ Java 基础；AI 板块按投递方向穿插。八股保证不被基础轮刷掉，**项目与 AI Agent 经验决定能否拿 offer**。
