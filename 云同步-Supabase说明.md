# 云同步部署（Supabase）

进度同步从 JSONBin 换成了 **Supabase**：一个项目、一张表搞定，不会再冒出一堆乱七八糟的 bin。

## 三步走

### 1. 建项目
到 [supabase.com](https://supabase.com) 注册，New project，记下密码，等它初始化好（约 1～2 分钟）。

### 2. 建表（粘 SQL 即可）
左侧 **SQL Editor** → New query，把下面整段贴进去 Run：

```sql
create table if not exists checkin (
  id text primary key,
  kind text not null default 'main',
  label text,
  data jsonb,
  created_at timestamptz not null default now()
);
-- 把表权限授予 anon 角色，否则会 permission denied(42501)
grant all on table public.checkin to anon, authenticated;
-- 开启 RLS 并加一条「全放行」策略（个人自用、key 只存自己浏览器）
alter table public.checkin enable row level security;
drop policy if exists "checkin all" on public.checkin;
create policy "checkin all" on public.checkin
  for all to anon, authenticated
  using (true) with check (true);
```

### 3. 拿 URL + key 填进网页
- **Project URL**：左侧 **Data API** 页顶部，或顶部绿色 **Connect** 按钮里，形如 `https://xxxx.supabase.co`。
- **key**（两种任选其一，代码都兼容）：
  - **Settings → API Keys → Publishable key**：`sb_publishable_...`（新版，可公开）。
  - 或点 **Legacy anon, service_role API keys** 标签里的 `anon` key：`eyJ...` 开头。

打开网页 → 「☁️ 云同步设置」→ 填 Project URL + key → 保存并同步。每台设备填一次就互通。

## 说明
- 主进度存在表里 `id='main'` 这一行；每次改动自动 upsert 覆盖。
- 云端备份各占一行（`kind='backup'`），删除备份会真删除那一行，不再像以前那样堆 bin。
- anon key 只保存在你自己浏览器的 localStorage，不写进公开的 HTML。配合上面「关闭 RLS」，等于这把 key 能读写该表——个人自用没问题；若担心，可改成带 RLS 的策略。
