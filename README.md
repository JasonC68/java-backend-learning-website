# 秋招后端 + AI Agent 八股背诵打卡站

一个面向**国内秋招（后端 + AI Agent 方向）**的八股复习工具：把高频面试题按板块整理成打卡清单，配合艾宾浩斯遗忘曲线安排复习，支持自己写答案、跨设备云同步。

题目精选自[小林 coding](https://www.xiaolincoding.com/) 与[小林大模型面试题](https://xiaolinnote.com/ai/)，按「抓主干、避免背太多」的原则做了筛选与分档。

---

## 📄 网页效果

<img width="1097" height="709" alt="image" src="https://github.com/user-attachments/assets/fb917f0d-0ad1-4d26-bdcf-e207765a97fe" />

---

## ✨ 主要功能

- **175 道精选必背题**，分 14 个板块：集合、并发、MySQL、JVM、Spring、计算机网络、Redis、扩展(MyBatis/MQ/分布式)、操作系统、Java 基础，以及 4 个 AI 板块（Agent / RAG / 工具调用 / 大模型基础），外加算法板块（CodeTop 高频 Top 100）。
- **每天约 8 题的学习计划**：自动排好建议日期；数据库（MySQL/Redis）与 AI 题打散并交替贯穿每一天，其余板块成块推进，便于配合复习不遗忘。日期可随时手动改期，也可一键清空为「未分配」。
- **掌握程度打卡**：未开始 / 眼熟 / 能讲框架 / 能扛追问，四档点击切换、自动统计完成率。
- **艾宾浩斯复习**：每次点「复习 +1」按 1/2/4/7/15/30/60 天自动排下次复习，到期标红。
- **今天还没开始的题会标红点**：序号前的小红点提示当天该新学/该复习但还没点过「＋」的题，完成后自动消失。
- **多维筛选**：按板块、掌握程度、收藏；日期维度有「今天任务 / 今天打卡 / 明天 / 今日复习」，以及带小红点的自定义日历选任意一天。
- **⭐ 收藏**：给题目加星，一键筛出所有收藏。
- **手动调整题目顺序**：每题旁的 ▲▼ 可在同板块内上移/下移，序号自动重新编号，顺序会随进度一起同步/备份。
- **今日任务剩余时间估算**：按「八股新学/复习」「算法新学/复习」各自的单题耗时，实时算出完成今天剩余任务大约还需多久（八股、算法分开显示 + 合计），每完成一题自动减少对应时间。
- **🎯 专注模式**：点一下从今日任务里挑一题（复习优先、按建议时长）开始计时；到时会弹窗提醒，可选「继续本题」「复习下一题」或「停止复习」；期间可暂停/跳过，随时点「完成本题」直接过（等效于点该题的「＋」，也会自动跳到下一题）；点面板里的题目标题可直接跳转到该题并展开、自动切换到对应模式（八股/算法）。八股和算法的专注互不干扰，切换模式不会打断进行中的专注。当天没有待办任务时按钮自动置灰。
- **⏱ 学习计时器**：独立于专注模式的手动正计时秒表，随时开始/暂停/重置，方便统计整体学习时长。
- **所见即所得 Markdown 编辑器**（基于 ProseMirror，离线内嵌）：展开任意题写自己的答案，`- `→列表、`# `→标题、`> `→引用，边打边渲染；支持粘贴 markdown 自动解析、Tab 缩进、Cmd±调标题级别、插图。选中文字按 **⌘/Ctrl+E** 可高亮，再按取消。
- **💡 助记框 + 代码框**：答案区可加助记口诀框、多个可独立折叠/删除的代码框（语法高亮）；助记、代码、答案三类框的折叠/删除按钮都在框右上角，折叠后点击该区域任意位置即可展开。
- **隐藏答案自测**：把答案框折叠起来只看助记背诵，记不住再点开。
- **今天任务剩余计数**：「📌 今天任务」实时显示当天还剩多少题没完成，完成一题数字减一；可一键「✂️ 缩减」把当天部分任务挪到未来。
- **🗑 回收站 + 💾 备份**：删除可恢复；进度可存多份本地与云端备份，随时恢复/导出/导入。
- **暗色模式**：跟随系统 / 亮 / 暗三档。
- **自建题目**：每个板块可随时添加自己的问题。
- **跨设备云同步**：进度与笔记通过 **Supabase** 在所有设备间自动同步（打开/切回/每 60 秒自动拉取，失败每 10 秒重试）；图片可选填 ImgBB 图床自动上传。

---

## 📁 文件说明

| 文件 | 说明 |
|------|------|
| `秋招必背打卡表-云同步.html` | **主程序**。单文件、自包含（编辑器内核已内嵌），浏览器打开即用，可直接部署 |
| `generate_html_sync.py` | 生成上面 HTML 的脚本（题库、计划、功能都在这里改） |
| `秋招后端八股「必背清单」（基于小林coding）.md` | 分档清单（⭐必背 / 🔸次要 / ⬜可跳过） |
| `云同步-Supabase说明.md` | 跨设备同步的部署步骤（含建表 SQL） |
| `秋招必背打卡表.xlsx` | Excel 版打卡表（早期版本，可离线用） |
| `build_checklist.py` | 生成 Excel 打卡表的脚本 |

> 主程序是自包含的，备份/部署只需要 `秋招必背打卡表-云同步.html` 这一个文件。

---

## 🚀 使用 / 部署

直接双击 `秋招必背打卡表-云同步.html` 用浏览器打开即可本地使用（进度存在本浏览器）。

要**跨设备同步**，按 `云同步-Supabase说明.md` 三步走（约 10 分钟，全免费）：

1. 在 [Supabase](https://supabase.com) 建一个项目，用 SQL Editor 跑一段建表 SQL（见说明文件，含 `checkin` 表 + 授权 + 全放行策略）；
2. 把 HTML 部署到任意静态托管拿一个网址（Netlify Drop / GitHub Pages / Cloudflare Pages 均可）；
3. 每台设备打开网址 → 「☁️ 云同步设置」填入 **Project URL** + **anon/publishable key**。

### 用 GitHub Pages 托管（可选）

本仓库可直接开 GitHub Pages：仓库 Settings → Pages → Source 选 `main` 分支根目录，保存后用 `https://<用户名>.github.io/java-backend-learning-website/秋招必背打卡表-云同步.html` 访问。

---

## 🛠 重新生成 HTML（开发者）

编辑器内核基于 ProseMirror，代码语法高亮基于 highlight.js，均用 esbuild 打包成自包含文件后内嵌进 HTML。`generate_html_sync.py` 会读取打包产物（`/tmp/tui/md.bundle.js`、`/tmp/tui/hl.bundle.js` 与 prosemirror 的 CSS）。如需改题库或功能后重新生成：

```bash
# 1) 准备编辑器内核（首次或临时环境被清空后）
cd /tmp && mkdir -p tui && cd tui && npm init -y
npm install prosemirror-model prosemirror-state prosemirror-view prosemirror-markdown \
  prosemirror-example-setup prosemirror-keymap prosemirror-commands prosemirror-schema-list \
  prosemirror-gapcursor highlight.js esbuild
# 写入 mdentry.js（编辑器入口：在 prosemirror-markdown schema 上加 highlight 高亮 mark + ⌘/Ctrl+E 快捷键、
#   标题快捷键、粘贴 markdown 解析、Tab 缩进、图片粘贴/拖入；笔记存 HTML），再打包：
./node_modules/.bin/esbuild mdentry.js --bundle --format=iife --outfile=md.bundle.js
# 写入 hlentry.js（import hljs from 'highlight.js/lib/common'; window.hljs=hljs;），打包代码高亮：
./node_modules/.bin/esbuild hlentry.js --bundle --format=iife --outfile=hl.bundle.js

# 2) 生成 HTML
python3 generate_html_sync.py
```

> 已生成的 `秋招必背打卡表-云同步.html` 是自包含的，仅做备份/部署时无需重新构建。

---

