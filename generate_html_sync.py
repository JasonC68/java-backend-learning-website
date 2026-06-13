# -*- coding: utf-8 -*-
import json
from datetime import date, timedelta

data = {
    "集合": ["HashMap 实现原理","HashMap 的 put / get 过程","HashMap 扩容机制","为什么容量是 2 的 n 次方 / 负载因子","为什么链表转红黑树（而非 AVL）","哈希冲突的解决方法","HashMap 线程安全吗 / 多线程下的问题","重写 equals / hashCode 的注意点","HashMap 用什么做 Key / 为什么 String 合适","HashMap vs Hashtable vs ConcurrentHashMap","ConcurrentHashMap 怎么实现的","用了 synchronized 为什么还要 CAS","ArrayList vs LinkedList","ArrayList 扩容机制","ArrayList 为什么线程不安全 / 怎么变安全","List vs Set"],
    "并发/多线程": ["JMM（Java 内存模型）+ 三大问题","线程的创建方式","线程的六种状态","sleep vs wait","notify vs notifyAll","怎么保证多线程安全","volatile 作用与原理","synchronized 原理 + 锁升级","CAS 原理 + ABA 问题","ReentrantLock vs synchronized + AQS","线程池原理（核心参数/流程/拒绝策略）","BLOCKED vs WAITING / 如何停止线程"],
    "MySQL": ["索引为什么用 B+ 树（vs B树/跳表/哈希）","聚簇索引 vs 非聚簇索引","联合索引 + 最左匹配原则","索引失效的场景","回表 / 覆盖索引","事务的 ACID 及实现","事务隔离级别 + 默认级别","RR 怎么（部分）解决幻读","MVCC 实现原理","redo log / undo log / binlog","binlog 两阶段提交","一条 SQL 的执行过程","InnoDB vs MyISAM","MySQL 有哪些锁","explain 怎么看","慢查询怎么优化"],
    "JVM": ["JVM 内存模型（运行时数据区）","堆和栈的区别 / 堆怎么分代","程序计数器为什么线程私有","创建对象的过程","类加载过程","双亲委派模型是什么 / 有什么用","类加载器有哪些","判断垃圾的方法","垃圾回收算法","垃圾回收器 / CMS vs G1","MinorGC / MajorGC / FullGC","四种引用类型","内存泄漏 vs 内存溢出"],
    "Spring": ["IoC / DI 是什么","Bean 的生命周期","Bean 的作用域","三级缓存如何解决循环依赖","AOP 原理（JDK 代理 vs CGLIB）","@Transactional 事务原理","事务的传播行为","事务失效的场景","Spring MVC 请求处理流程","Spring Boot 自动装配原理","常用注解区别（@Autowired vs @Resource 等）"],
    "计算机网络": ["TCP 三次握手 + 为什么三次","TCP 四次挥手 + 为什么四次 + 2MSL","TCP vs UDP","TCP 为什么可靠","TCP 拥塞控制","GET vs POST","HTTP 常用状态码（含 502/504）","HTTP vs HTTPS","HTTPS 握手过程","HTTP/1.1 vs 2.0","HTTP 无状态 / Cookie 和 Session","Cookie / Session / Token(JWT)","输入 URL 到页面展示发生了什么","DNS 解析流程 / TCP 还是 UDP","HTTP 长连接 vs WebSocket"],
    "Redis": ["Redis 为什么快","五种数据类型及底层实现","ZSet 底层 / 跳表 / 为什么不用 B+ 树","RDB vs AOF","内存淘汰策略","过期删除策略","缓存雪崩 / 击穿 / 穿透","布隆过滤器原理","Redis 和 MySQL 缓存一致性","Redis 分布式锁","大 Key / 热 Key 问题","主从复制","哨兵机制","怎么保证 Redis 操作原子性"],
    "扩展(MyBatis/MQ/分布式)": ["MyBatis #{} 和 ${} 的区别","MyBatis 一级/二级缓存","MQ 的作用（解耦/异步/削峰）","MQ 如何保证消息不丢失","MQ 如何保证不重复消费（幂等）","MQ 消息积压怎么处理","CAP / BASE 理论","分布式事务方案（2PC/TCC/本地消息表）","分布式 ID 生成方案（雪花算法）","限流算法（漏桶/令牌桶等）"],
    "操作系统": ["进程 vs 线程 vs 协程","进程的五种状态","进程间通信方式（IPC）","线程间通信方式","进程切换 vs 线程切换，为什么线程快","用户态 vs 内核态","死锁四条件 + 如何避免","乐观锁 vs 悲观锁 / 自旋锁","虚拟内存 / 地址转换","程序的内存布局 / 堆栈区别","页面置换算法","IO 多路复用 / select-poll-epoll","epoll 的 LT vs ET","零拷贝"],
    "Java基础": ["值传递 vs 引用传递","装箱拆箱 + Integer 缓存（-128~127）","为什么用 BigDecimal 不用 double","重载 vs 重写","抽象类 vs 接口","final / static 的作用","深拷贝 vs 浅拷贝 + 实现方式","JVM / JDK / JRE 三者关系","八种基本数据类型及字节数","封装/继承/多态，多态的体现","泛型是什么 + 类型擦除"],
    "AI·Agent": ["什么是 Agent？与大模型有什么本质不同？","Agent 的基本架构由哪些核心组件构成？","Workflow / Agent / Tools 的概念和区别？","Agent 推理模式有哪些？ReAct 是什么、怎么实现？","ReAct / Plan-and-Execute / Reflection 的区别与选型？","复杂任务怎么做任务拆分？为什么要拆分？","Agent 的记忆机制 / 记忆模块怎么设计？","长短期记忆怎么存？粒度多大？怎么用？","Agent 记忆压缩有哪些方法？","如何赋予 LLM 规划能力？","Agent 的反思机制？为什么用、怎么实现？","什么是 Multi-Agent？Single vs Multi 怎么选？","多 Agent 的协作、通信与动态路由怎么设计？","为什么有时手搓 Agent 而不用框架？"],
    "AI·RAG": ["什么是 RAG？完整工作流程是怎样的？","RAG 解决了什么问题？RAG vs 微调如何选型？","文档切割（Chunking）策略 / 粒度？","怎么规避语义被切断的问题？","Embedding 是什么？怎么选和评估？","向量数据库是什么？怎么对比选型？","向量检索 vs 关键词检索的区别？","Query Rewrite 是什么？目的是什么？","什么是多路召回？怎么做？检索优化策略有哪些？","进阶 RAG 范式（Self-RAG / Corrective RAG）了解哪些？","如何规避 RAG 幻觉？怎么量化 RAG 效果？","RAG 知识库如何动态与持续更新？"],
    "AI·工具调用": ["什么是 Function Calling？原理是什么？","LLM 如何学会调用工具 / FC 能力怎么训练？","什么是 MCP？由哪几部分组成？","MCP 和 Function Calling 的区别？什么场景用哪个？","Skill 是什么？和 MCP 有什么区别？","Function Calling / Skill / MCP 三者的关系与区别？","什么是 A2A 协议？和 MCP 的区别？","MCP 通信方式 / SSE vs WebSocket 区别？","LLM 网关解决了什么问题？"],
    "AI·大模型基础": ["什么是大语言模型？和传统 NLP 模型有什么区别？","Transformer 架构基本原理（Encoder/Decoder）？","KV Cache 是什么？Prompt Caching 原理（省 token）？","如何写好 Prompt？Prompt 工程实践经验？","什么是 CoT？为什么有效？有什么局限？","大模型为什么会幻觉？怎么缓解？","温度值 / Top-P / Top-K 是什么？怎么设置？","项目中如何做模型选型？为什么选这个模型？"],
}
START = date(2026, 6, 10); PER_DAY = 10; WK = ["一","二","三","四","五","六","日"]
def fmt(idx):
    d = START + timedelta(days=idx // PER_DAY)
    return f"{d.month:02d}-{d.day:02d} 周{WK[d.weekday()]}"
def fmt_d(d):
    return f"{d.month:02d}-{d.day:02d} 周{WK[d.weekday()]}"
AI="AI·"
DAILY=8   # 每天总题量约 8
SPREAD_SECS={"MySQL","Redis"}   # 数据库题与 AI 题一起打散到每一天
def is_spread(s): return s.startswith(AI) or s in SPREAD_SECS
spread_total=max(1,sum(len(qs) for s,qs in data.items() if is_spread(s)))
seq_total=sum(len(qs) for s,qs in data.items() if not is_spread(s))
total=spread_total+seq_total
num_days=max(1,(total+DAILY-1)//DAILY)
seq_per_day=max(1,(seq_total+num_days-1)//num_days)
# 先按字典顺序定 id，并分流到「成块」与「打散」两组
items=[]; gid=0
seq_items=[]; spread_by_sec={}
for sec,qs in data.items():
    for i,q in enumerate(qs,1):
        rec={"id":gid,"sec":sec,"idx":i,"q":q}; items.append(rec)
        (spread_by_sec.setdefault(sec,[]).append(rec) if is_spread(sec) else seq_items.append(rec))
        gid+=1
# 成块组：顺序占天
for k,rec in enumerate(seq_items): rec["_day"]=k//seq_per_day
# 打散组：各板块轮流交错，再均匀铺到所有天（数据库 + AI 交替贯穿全程）
spread_order=[]; secs=list(spread_by_sec.keys()); pos={s:0 for s in secs}; left=sum(len(v) for v in spread_by_sec.values())
while left>0:
    for s in secs:
        if pos[s]<len(spread_by_sec[s]): spread_order.append(spread_by_sec[s][pos[s]]); pos[s]+=1; left-=1
for rank,rec in enumerate(spread_order): rec["_day"]=rank*num_days//spread_total
for rec in items:
    d=START+timedelta(days=rec.pop("_day"))
    rec["date"]=fmt_d(d); rec["iso"]=d.isoformat()
JS=json.dumps(items,ensure_ascii=False); SEC=json.dumps(list(data.keys()),ensure_ascii=False)

html = '''<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>秋招必背打卡表 · 云同步</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,"Microsoft YaHei","PingFang SC",sans-serif;background:#f5f6f8;color:#1f2937;padding:16px;max-width:1100px;margin:0 auto}
h1{font-size:20px}
.row1{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.sub{color:#6b7280;font-size:13px;margin:4px 0 12px}
.pill{font-size:12px;padding:3px 10px;border-radius:12px;background:#e5e7eb;color:#374151}
.pill.ok{background:#d1fae5;color:#065f46}.pill.warn{background:#fee2e2;color:#991b1b}.pill.busy{background:#dbeafe;color:#1e40af}
.bar{height:14px;background:#e5e7eb;border-radius:8px;overflow:hidden;margin:8px 0}
.bar>i{display:block;height:100%;background:linear-gradient(90deg,#34d399,#059669);width:0;transition:width .3s}
.statline{font-size:13px;margin-bottom:12px}.statline b{color:#059669}
.toolbar{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px;align-items:center}
.chip{border:1px solid #d1d5db;background:#fff;border-radius:16px;padding:4px 12px;font-size:13px;cursor:pointer;user-select:none}
.chip.active{background:#2563eb;color:#fff;border-color:#2563eb}
.spacer{flex:1}
.btn{border:1px solid #d1d5db;background:#fff;border-radius:8px;padding:5px 10px;font-size:12px;cursor:pointer}
.btn:hover{background:#f3f4f6}.btn.pri{background:#2563eb;color:#fff;border-color:#2563eb}
table{width:100%;border-collapse:collapse;background:#fff;border-radius:10px;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,.08)}
th,td{padding:9px 8px;font-size:13px;text-align:left;border-bottom:1px solid #f0f0f0}
th{background:#2f5597;color:#fff;font-weight:600;position:sticky;top:0;z-index:2}
td.c,th.c{text-align:center;white-space:nowrap}
tr.sec-row td{background:#eef2ff;font-weight:700;color:#3730a3}
th:nth-child(2){width:120px}
td.date{width:120px;min-width:120px;max-width:120px;color:#6b7280;font-size:12px;white-space:nowrap;cursor:pointer;border-radius:4px;overflow:hidden}
td.date:hover{background:#eef2ff}
td.date input[type=date]{width:108px;box-sizing:border-box;font-size:12px;padding:1px 2px}
.add-row td{background:#fff;padding:6px 14px}
.addq{border:1px dashed #93c5fd;background:#f8fbff;color:#2563eb;border-radius:6px;padding:5px 14px;font-size:12px;cursor:pointer}
.addq:hover{background:#eff6ff}
.del{float:right;margin-right:8px;border:1px solid #fca5a5;background:#fff;color:#b91c1c;border-radius:6px;padding:2px 10px;font-size:12px;cursor:pointer}
.del:hover{background:#fef2f2}
.pickwrap{position:relative;display:inline-block}
.pickbtn{font-size:12px;padding:4px 10px;border:1px solid #d1d5db;border-radius:16px;background:#fff;cursor:pointer}
.pickbtn:hover{background:#f3f4f6}
.cal{position:fixed;z-index:50;background:#fff;border:1px solid #e5e7eb;border-radius:10px;box-shadow:0 8px 24px rgba(0,0,0,.14);padding:10px;width:252px;display:none}
.cal.show{display:block}
.cal-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;font-size:13px;font-weight:600}
.cal-head button{border:none;background:#f3f4f6;border-radius:6px;width:26px;height:26px;cursor:pointer;font-size:14px}
.cal-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:2px}
.cal-grid .wd{font-size:11px;color:#9ca3af;text-align:center;padding:2px 0}
.cal-day{position:relative;text-align:center;font-size:12px;padding:7px 0;border-radius:6px;cursor:pointer}
.cal-day:hover{background:#eff6ff}
.cal-day.other{visibility:hidden}
.cal-day.today{outline:1px solid #93c5fd}
.cal-day.sel{background:#2563eb;color:#fff}
.cal-day .dot{position:absolute;left:50%;transform:translateX(-50%);bottom:2px;width:5px;height:5px;border-radius:50%;background:#dc2626}
.cal-day.sel .dot{background:#fff}
.cal-foot{display:flex;justify-content:space-between;margin-top:8px}
.cal-foot button{font-size:11px;border:1px solid #d1d5db;background:#fff;border-radius:6px;padding:3px 10px;cursor:pointer}
.cal-foot button:hover{background:#f3f4f6}
.addform{display:flex;gap:6px;align-items:center}
.addform .ai{flex:1;max-width:520px;padding:6px 9px;border:1px solid #93c5fd;border-radius:6px;font-size:13px}
.addform .ok{border:1px solid #2563eb;background:#2563eb;color:#fff;border-radius:6px;padding:6px 14px;font-size:12px;cursor:pointer}
.addform .ca{border:1px solid #d1d5db;background:#fff;border-radius:6px;padding:6px 12px;font-size:12px;cursor:pointer}
.lvl{border:none;border-radius:14px;padding:4px 10px;font-size:12px;cursor:pointer;font-weight:600;min-width:74px}
.l0{background:#fde2e2;color:#b91c1c}.l1{background:#fdebc8;color:#b45309}.l2{background:#d9ead3;color:#256029}.l3{background:#a9d08e;color:#14532d}
.cnt{display:inline-flex;align-items:center;gap:6px}
.cnt button{width:24px;height:24px;border-radius:6px;border:1px solid #d1d5db;background:#fff;font-size:15px;line-height:1;cursor:pointer}
.cnt button:hover{background:#eef2ff}.cnt b{min-width:18px;text-align:center;display:inline-block}
.last{color:#6b7280;font-size:12px;white-space:nowrap}.q{line-height:1.4}
.modal{position:fixed;inset:0;background:rgba(0,0,0,.4);display:none;align-items:center;justify-content:center;z-index:9}
.modal.show{display:flex}
.card{background:#fff;border-radius:12px;padding:20px;max-width:440px;width:92%}
.card h3{font-size:16px;margin-bottom:8px}.card p{font-size:13px;color:#4b5563;margin-bottom:10px;line-height:1.5}
.card label{font-size:12px;color:#374151;display:block;margin:8px 0 3px}
.card input{width:100%;padding:8px;border:1px solid #d1d5db;border-radius:6px;font-size:13px}
.card .acts{display:flex;gap:8px;justify-content:flex-end;margin-top:14px}
.star{cursor:pointer;color:#d1d5db;margin-right:7px;font-size:15px;user-select:none}
.star.on{color:#f59e0b}
.star:hover{color:#f59e0b}
.qbtn{cursor:pointer;display:inline-block}
.qbtn:hover{color:#2563eb}
.qbtn .arw{display:inline-block;width:14px;color:#9ca3af;font-size:11px}
.qbtn.has::after{content:"📝";margin-left:5px;font-size:12px}
tr.ed-row td{background:#f8f9ff;padding:10px 14px}
.ehint{font-size:12px;color:#6b7280;margin-bottom:6px;overflow:hidden}
.tgl{float:right;border:1px solid #d1d5db;background:#fff;border-radius:6px;padding:2px 12px;font-size:12px;cursor:pointer}
.tgl:hover{background:#eef2ff}
.tui{margin-top:4px;background:#fff;border-radius:6px}
.fa{width:100%;min-height:200px;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13px;line-height:1.6;padding:10px;border:1px solid #d1d5db;border-radius:6px;resize:vertical}
.editor textarea{width:100%;min-height:220px;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13px;line-height:1.6;padding:10px;border:1px solid #d1d5db;border-radius:6px;resize:vertical}
.preview{min-height:120px;max-height:460px;overflow:auto;padding:8px 14px;border:1px solid #eee;border-radius:6px;background:#fff;font-size:13px;line-height:1.7}
.preview:empty::before{content:"还没有内容，点 ✏️ 编辑开始写…";color:#bbb}
.preview h1,.preview h2,.preview h3{font-size:14px;margin:8px 0 4px}
.preview p{margin:5px 0}.preview ul,.preview ol{margin:5px 0 5px 20px}
.preview code{background:#f3f4f6;padding:1px 4px;border-radius:3px;font-size:12px}
.preview pre{background:#f3f4f6;padding:8px;border-radius:6px;overflow:auto}
.preview pre code{background:none;padding:0}
.preview blockquote{border-left:3px solid #d1d5db;margin:5px 0;padding-left:10px;color:#4b5563}
.preview table{border:1px solid #e5e7eb;box-shadow:none;margin:5px 0}.preview th{position:static}
@media(max-width:640px){.hide-sm{display:none}th,td{padding:7px 5px;font-size:12px}.editor{flex-direction:column}}
</style>
<style>__PM_CSS__</style>
<style>
.tui{border:1px solid #e5e7eb;border-radius:8px;background:#fff;overflow:hidden}
.tui .ProseMirror{outline:none;min-height:180px;padding:12px 16px;font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;font-size:15px;line-height:1.85;color:#1f2937;overflow-wrap:break-word;word-break:break-word}
.ProseMirror img{max-width:100%;height:auto;border-radius:6px}
.ProseMirror:focus{outline:none}
.ProseMirror>:first-child{margin-top:0}
.ProseMirror p{margin:7px 0}
.ProseMirror h1{font-size:21px;font-weight:700;margin:14px 0 8px}
.ProseMirror h2{font-size:18px;font-weight:700;margin:12px 0 6px}
.ProseMirror h3{font-size:16px;font-weight:600;margin:10px 0 5px}
.ProseMirror ul{list-style:disc outside;padding-left:24px;margin:6px 0}
.ProseMirror ol{list-style:decimal outside;padding-left:26px;margin:6px 0}
.ProseMirror ul ul{list-style:circle outside}
.ProseMirror li{margin:3px 0}
.ProseMirror li::marker{color:#374151}
.ProseMirror code{background:#f3f4f6;color:#be123c;padding:1px 6px;border-radius:4px;font-size:13px}
.ProseMirror pre{background:#f6f8fa;border-radius:8px;padding:12px;white-space:pre-wrap}
.ProseMirror pre code{background:none;color:#24292e;padding:0}
.ProseMirror blockquote{border-left:3px solid #c7d2fe;background:#f8faff;color:#475569;padding:4px 12px;margin:8px 0}
.ProseMirror strong{color:#111827}
.ProseMirror a{color:#2563eb}
.ProseMirror hr{border:none;border-top:1px solid #e5e7eb;margin:12px 0}
</style>
<script>__PM_JS__</script>
</head><body>
<div class="row1"><h1>秋招后端必背 · 打卡表</h1><span class="pill" id="syncPill">未配置云同步</span></div>
<div class="sub"><span style="color:#9ca3af">v2.1.3</span></div>
<div class="bar"><i id="pbar"></i></div>
<div class="statline" id="stat"></div>
<div class="toolbar" id="filters"></div>
<div class="toolbar">
  <span style="font-size:12px;color:#6b7280">按日期：</span>
  <span class="chip active" data-date="all">全部</span>
  <span class="chip" data-date="todayall" title="今天要打卡的 + 之前没完成顺延的 + 今天到期/逾期要复习的">📌 今天任务</span>
  <span class="chip" data-date="today">📅 今天打卡</span>
  <span class="chip" data-date="tomorrow">明天</span>
  <span class="chip" data-date="review" title="按艾宾浩斯遗忘曲线，到期/逾期需复习的题">🔁 今日复习</span>
  <span style="font-size:12px;color:#6b7280;margin-left:8px">或指定日期：</span>
  <span class="pickwrap"><button class="pickbtn" id="pickBtn">📅 选择日期</button></span>
</div>
<div class="toolbar">
  <span style="font-size:12px;color:#6b7280">按掌握程度：</span>
  <span class="chip active" data-lvl="all">全部</span>
  <span class="chip" data-lvl="0">未开始</span><span class="chip" data-lvl="1">眼熟</span>
  <span class="chip" data-lvl="2">能讲框架</span><span class="chip" data-lvl="3">能扛追问</span>
  <span class="chip" id="starFilter" style="margin-left:8px">⭐ 仅看收藏</span>
  <span class="spacer"></span>
  <button class="btn pri" id="cfgBtn">☁️ 云同步设置</button>
  <button class="btn" id="pull">⬇️ 手动拉取</button>
  <button class="btn" id="push">⬆️ 手动上传</button>
  <button class="btn" id="reset">清空</button>
</div>
<table><thead><tr>
<th class="c">序号</th><th class="c hide-sm">建议日期</th><th>面试问题</th>
<th class="c">掌握程度</th><th class="c">复习次数</th><th class="c hide-sm">上次复习</th>
</tr></thead><tbody id="tb"></tbody></table>

<div class="cal" id="cal"></div>
<div class="modal" id="modal"><div class="card">
  <h3>云同步设置</h3>
  <p>用免费的 <b>JSONBin.io</b> 存进度：注册后新建一个 Bin（内容填 <code>{}</code>），把 <b>Bin ID</b> 和 <b>Master Key</b> 填到下面。每台设备填一次即可互通。详见配套说明文件。</p>
  <label>Bin ID</label><input id="binId" placeholder="例如 6650a1b2ac...">
  <label>Master Key（$2a$10$... 开头）</label><input id="binKey" placeholder="X-Master-Key">
  <div class="acts">
    <button class="btn" id="cfgClear">清除配置</button>
    <button class="btn" id="cfgCancel">取消</button>
    <button class="btn pri" id="cfgSave">保存并同步</button>
  </div>
</div></div>
<script>
const ITEMS=__ITEMS__, SECTIONS=__SEC__;
const KEY="review_tracker_v2", CFGKEY="sync_cfg_v1";
const LVLS=["未开始","眼熟","能讲框架","能扛追问"];
let state=JSON.parse(localStorage.getItem(KEY)||"{}");
let cfg=JSON.parse(localStorage.getItem(CFGKEY)||"null");
let secFilter="all",lvlFilter="all",dateFilter="all",pickedDate="",starOnly=false,timer=null,openIds=new Set(),editors=[],dirty=false,retryTimer=null;
function isoOf(dt){return dt.getFullYear()+"-"+String(dt.getMonth()+1).padStart(2,"0")+"-"+String(dt.getDate()).padStart(2,"0");}
function todayIso(){return isoOf(new Date());}
function tomorrowIso(){const d=new Date();d.setDate(d.getDate()+1);return isoOf(d);}
const EBB=[1,2,4,7,15,30,60];   // 艾宾浩斯遗忘曲线间隔（天）
function addDays(iso,n){const d=new Date((iso||todayIso())+"T00:00:00");d.setDate(d.getDate()+n);return isoOf(d);}
function schedNext(cnt){const n=EBB[Math.min(Math.max(cnt,1)-1,EBB.length-1)];return addDays(todayIso(),n);}
function get(id){return state[id]||(state[id]={lvl:0,cnt:0,last:""});}
function esc(s){return (s||"").replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c]));}
function md(t){return (window.marked?marked.parse(t||""):"<pre>"+esc(t)+"</pre>");}
function fmtIso(iso){if(!iso)return"";const d=new Date(iso+"T00:00:00");if(isNaN(d))return iso;const wk=["日","一","二","三","四","五","六"];return (d.getMonth()+1+"").padStart(2,"0")+"-"+(d.getDate()+"").padStart(2,"0")+" 周"+wk[d.getDay()];}
function today(){const d=new Date();return (d.getMonth()+1+"").padStart(2,"0")+"-"+(d.getDate()+"").padStart(2,"0");}
function nowt(){const d=new Date();return (d.getHours()+"").padStart(2,"0")+":"+(d.getMinutes()+"").padStart(2,"0");}
function setPill(t,cls){const p=document.getElementById("syncPill");p.textContent=t;p.className="pill"+(cls?" "+cls:"");}
function url(){return "https://api.jsonbin.io/v3/b/"+cfg.bin;}
async function cloudGet(){const r=await fetch(url()+"/latest",{headers:{"X-Master-Key":cfg.key}});if(!r.ok)throw 0;return (await r.json()).record;}
async function cloudPut(){const r=await fetch(url(),{method:"PUT",headers:{"Content-Type":"application/json","X-Master-Key":cfg.key},body:JSON.stringify(state)});if(!r.ok)throw 0;}
function scheduleRetry(){if(retryTimer)return;retryTimer=setTimeout(()=>{retryTimer=null;autoSync();},10000);}
function clearRetry(){if(retryTimer){clearTimeout(retryTimer);retryTimer=null;}}
function save(){localStorage.setItem(KEY,JSON.stringify(state));if(cfg){dirty=true;setPill("待同步…","busy");clearTimeout(timer);timer=setTimeout(push,1200);} }
async function push(){if(!cfg)return;try{setPill("同步中…","busy");await cloudPut();dirty=false;clearRetry();setPill("已同步 "+nowt(),"ok");}catch(e){setPill("同步失败，10秒后重试","warn");scheduleRetry();}}
function isEditing(){const a=document.activeElement;return !!(a&&(a.isContentEditable||a.tagName==="INPUT"||a.tagName==="TEXTAREA"));}
function autoSync(){if(!cfg)return;if(dirty){push();return;}if(isEditing()){scheduleRetry();return;}pull();}
async function pull(){if(!cfg){alert("请先配置云同步");return;}if(isEditing()){scheduleRetry();return;}try{setPill("拉取中…","busy");const c=await cloudGet();if(c&&typeof c==="object"){state=c;localStorage.setItem(KEY,JSON.stringify(state));render();}clearRetry();setPill("已拉取 "+nowt(),"ok");}catch(e){setPill("拉取失败，10秒后重试","warn");scheduleRetry();}}
function buildFilters(){const f=document.getElementById("filters");f.innerHTML='<span style="font-size:12px;color:#6b7280">板块：</span>';
  const mk=(t,v)=>{const s=document.createElement("span");s.className="chip"+(v===secFilter?" active":"");s.textContent=t;s.onclick=()=>{secFilter=v;buildFilters();render();};return s;};
  f.appendChild(mk("全部","all"));SECTIONS.forEach(s=>f.appendChild(mk(s,s)));}
document.querySelectorAll('[data-lvl]').forEach(c=>c.onclick=()=>{document.querySelectorAll('[data-lvl]').forEach(x=>x.classList.remove("active"));c.classList.add("active");lvlFilter=c.dataset.lvl;render();});
const pickBtn=document.getElementById("pickBtn"),calBox=document.getElementById("cal");
let calRef=new Date(),calCtx=null;
function updatePickBtn(){pickBtn.textContent=pickedDate?("📅 "+pickedDate.slice(5)):"📅 选择日期";}
function studyDateSet(){const s=new Set();ITEMS.forEach(it=>{const o=get(it.id);s.add((o.date&&o.date!=="")?o.date:it.iso);});customList().forEach(c=>{const o=get(c.id);if(o.date)s.add(o.date);});return s;}
function renderCal(){
  const sset=(calCtx&&calCtx.dot)?studyDateSet():new Set();
  const sel=calCtx?calCtx.selected:"";
  const y=calRef.getFullYear(),m=calRef.getMonth();
  const startW=new Date(y,m,1).getDay(),days=new Date(y,m+1,0).getDate(),WD=["日","一","二","三","四","五","六"];
  let html='<div class="cal-head"><button id="calPrev">‹</button><span>'+y+'年'+(m+1)+'月</span><button id="calNext">›</button></div><div class="cal-grid">';
  WD.forEach(w=>html+='<div class="wd">'+w+'</div>');
  for(let i=0;i<startW;i++)html+='<div class="cal-day other"></div>';
  for(let d=1;d<=days;d++){const iso=isoOf(new Date(y,m,d));
    html+='<div class="cal-day'+(iso===todayIso()?" today":"")+(iso===sel?" sel":"")+'" data-iso="'+iso+'">'+d+(sset.has(iso)?'<span class="dot"></span>':'')+'</div>';}
  html+='</div><div class="cal-foot"><button id="calToday">今天</button>'+((calCtx&&calCtx.onClear)?'<button id="calClear">'+(calCtx.clearLabel||"清除")+'</button>':'<span></span>')+'</div>';
  calBox.innerHTML=html;
  calBox.querySelector("#calPrev").onclick=e=>{e.stopPropagation();calRef=new Date(y,m-1,1);renderCal();};
  calBox.querySelector("#calNext").onclick=e=>{e.stopPropagation();calRef=new Date(y,m+1,1);renderCal();};
  calBox.querySelector("#calToday").onclick=e=>{e.stopPropagation();calRef=new Date();renderCal();};
  const cc=calBox.querySelector("#calClear");if(cc)cc.onclick=e=>{e.stopPropagation();calBox.classList.remove("show");calCtx.onClear();};
  calBox.querySelectorAll(".cal-day[data-iso]").forEach(el=>el.onclick=e=>{e.stopPropagation();const iso=el.dataset.iso;calBox.classList.remove("show");calCtx.onPick(iso);});
}
function openCal(anchor,ctx){calCtx=ctx;calRef=ctx.selected?new Date(ctx.selected+"T00:00:00"):new Date();renderCal();
  const r=anchor.getBoundingClientRect();
  calBox.style.left=Math.max(6,Math.min(r.left,window.innerWidth-260))+"px";
  calBox.style.top=Math.min(r.bottom+4,window.innerHeight-340)+"px";
  calBox.classList.add("show");}
pickBtn.onclick=e=>{e.stopPropagation();if(calBox.classList.contains("show")){calBox.classList.remove("show");return;}
  openCal(pickBtn,{selected:pickedDate,dot:true,clearLabel:"清除筛选",
    onPick:iso=>{pickedDate=iso;dateFilter="pick";document.querySelectorAll('[data-date]').forEach(x=>x.classList.remove("active"));updatePickBtn();render();},
    onClear:()=>{pickedDate="";dateFilter="all";document.querySelectorAll('[data-date]').forEach(x=>x.classList.remove("active"));document.querySelector('[data-date="all"]').classList.add("active");updatePickBtn();render();}});};
document.addEventListener("click",e=>{if(!calBox.contains(e.target)&&e.target!==pickBtn)calBox.classList.remove("show");});
document.querySelectorAll('[data-date]').forEach(c=>c.onclick=()=>{document.querySelectorAll('[data-date]').forEach(x=>x.classList.remove("active"));c.classList.add("active");dateFilter=c.dataset.date;pickedDate="";updatePickBtn();render();});
document.getElementById("starFilter").onclick=function(){starOnly=!starOnly;this.classList.toggle("active",starOnly);render();};
function passDate(it){if(dateFilter==="all")return true;if(dateFilter==="todayall"){const o=get(it.id);const d=itemDate(it);const studyDue=!!d&&d<=todayIso()&&!(o.lvl>0||o.cnt>0);const reviewDue=!!o.next&&o.next<=todayIso();return studyDue||reviewDue;}if(dateFilter==="review"){const nx=get(it.id).next;return !!nx&&nx<=todayIso();}if(dateFilter==="pick"){const d=itemDate(it),nx=get(it.id).next;return d===pickedDate||nx===pickedDate;}const d=itemDate(it);if(!d)return false;return d===(dateFilter==="today"?todayIso():tomorrowIso());}
function customList(){return state.__custom||(state.__custom=[]);}
function sectionMap(){const map={};SECTIONS.forEach(s=>map[s]=[]);
  ITEMS.forEach(it=>{(map[it.sec]||(map[it.sec]=[])).push({id:it.id,sec:it.sec,q:it.q,baseIso:it.iso});});
  customList().forEach(c=>{(map[c.sec]||(map[c.sec]=[])).push({id:c.id,sec:c.sec,q:c.q,baseIso:"",custom:true});});
  Object.keys(map).forEach(s=>map[s].forEach((it,i)=>it.idx=i+1));return map;}
function itemDate(it){const o=get(it.id);return (o.date!==undefined&&o.date!=="")?o.date:(it.baseIso||"");}
function render(){const tb=document.getElementById("tb");
  const _sy=window.scrollY;
  editors.forEach(e=>{try{e.destroy();}catch(_){}});editors=[];
  tb.innerHTML="";
  const map=sectionMap();
  const secs=Object.keys(map).filter(s=>secFilter==="all"||s===secFilter);
  secs.forEach(s=>{
    const list=map[s].filter(it=>(lvlFilter==="all"||get(it.id).lvl==lvlFilter)&&passDate(it)&&(!starOnly||get(it.id).star));
    if(list.length===0&&(lvlFilter!=="all"||dateFilter!=="all"||starOnly))return;
    const sr=document.createElement("tr");sr.className="sec-row";sr.innerHTML='<td colspan="6">'+esc(s)+'</td>';tb.appendChild(sr);
    list.forEach(it=>{const st=get(it.id);
      const opened=openIds.has(it.id), hasNote=st.note&&st.note.trim();
      const tr=document.createElement("tr");
      tr.innerHTML='<td class="c">'+it.idx+'</td>'+
        '<td class="c hide-sm date">'+(fmtIso(itemDate(it))||'<span style="color:#bbb">＋日期</span>')+'</td>'+
        '<td class="q"><span class="star'+(st.star?' on':'')+'" title="收藏">'+(st.star?'★':'☆')+'</span><span class="qbtn'+(hasNote?' has':'')+'"><span class="arw">'+(opened?'▾':'▸')+'</span>'+esc(it.q)+(it.custom?' <span style="color:#9333ea;font-size:11px">·自建</span>':'')+'</span></td>'+
        '<td class="c"><button class="lvl l'+st.lvl+'">'+LVLS[st.lvl]+'</button></td>'+
        '<td class="c"><span class="cnt"><button class="minus">−</button><b>'+st.cnt+'</b><button class="plus">＋</button></span></td>'+
        '<td class="c hide-sm last">'+(st.last||"—")+(st.next?' <span style="font-size:11px;color:'+(st.next<=todayIso()?"#dc2626":"#9ca3af")+'">↻'+st.next.slice(5)+'</span>':'')+'</td>';
      const dc=tr.querySelector(".date");
      dc.onclick=e=>{e.stopPropagation();openCal(dc,{selected:itemDate(it),dot:true,clearLabel:"恢复默认",
        onPick:iso=>{get(it.id).date=iso;save();render();},
        onClear:()=>{delete get(it.id).date;save();render();}});};
      tr.querySelector(".star").onclick=e=>{e.stopPropagation();st.star=!st.star;save();render();};
      tr.querySelector(".qbtn").onclick=()=>{opened?openIds.delete(it.id):openIds.add(it.id);render();};
      tr.querySelector(".lvl").onclick=()=>{st.lvl=(st.lvl+1)%4;save();render();};
      tr.querySelector(".plus").onclick=()=>{st.cnt++;st.last=today();st.next=schedNext(st.cnt);save();render();};
      tr.querySelector(".minus").onclick=()=>{if(st.cnt>0){st.cnt--;if(st.cnt>0)st.next=schedNext(st.cnt);else delete st.next;}save();render();};
      tb.appendChild(tr);
      if(opened){
        const er=document.createElement("tr");er.className="ed-row";
        const td=document.createElement("td");td.colSpan=6;
        td.innerHTML=(it.custom?'<div class="ehint"><button class="del">🗑 删除此题</button></div>':'')+'<div class="tui"></div>';
        const host=td.querySelector(".tui");
        const del=td.querySelector(".del");
        if(del)del.onclick=()=>{if(confirm("删除这道自建题？")){state.__custom=customList().filter(c=>c.id!==it.id);delete state[it.id];openIds.delete(it.id);save();render();}};
        er.appendChild(td);tb.appendChild(er);
        if(window.MDEditor){
          const ed=window.MDEditor(host, st.note||"", (mdstr)=>{st.note=mdstr;save();});
          editors.push(ed);
        }else{
          host.innerHTML='<textarea class="fa" placeholder="# 在这里写你总结的答案…"></textarea>';
          const ta=host.querySelector(".fa");ta.value=st.note||"";ta.oninput=()=>{st.note=ta.value;save();};
        }
      }});
    if(lvlFilter==="all"&&dateFilter==="all"&&!starOnly){
      const ar=document.createElement("tr");ar.className="add-row";const td=document.createElement("td");td.colSpan=6;
      td.innerHTML='<button class="addq">＋ 添加问题到「'+esc(s)+'」</button>';
      td.querySelector(".addq").onclick=()=>{
        td.innerHTML='<div class="addform"><input class="ai" placeholder="输入新问题，回车或点确定添加…"><button class="ok">确定</button><button class="ca">取消</button></div>';
        const inp=td.querySelector(".ai");inp.focus();
        const add=()=>{const q=inp.value.trim();if(q){const id="c_"+Date.now();customList().push({id:id,sec:s,q:q});openIds.add(id);save();}render();};
        td.querySelector(".ok").onclick=add;
        td.querySelector(".ca").onclick=()=>render();
        inp.onkeydown=e=>{if(e.key==="Enter")add();if(e.key==="Escape")render();};};
      ar.appendChild(td);tb.appendChild(ar);}
  });
  let base=[];SECTIONS.forEach(s=>base=base.concat(map[s]||[]));
  let done=0;base.forEach(it=>{if(get(it.id).lvl>=2)done++;});
  const tot=base.length,pct=tot?Math.round(done/tot*100):0;
  document.getElementById("pbar").style.width=pct+"%";
  document.getElementById("stat").innerHTML="已掌握(能讲框架+能扛追问)：<b>"+done+"</b> / "+tot+"　("+pct+"%)";
  window.scrollTo(0,_sy);requestAnimationFrame(()=>window.scrollTo(0,_sy));}
const modal=document.getElementById("modal");
document.getElementById("cfgBtn").onclick=()=>{if(cfg){document.getElementById("binId").value=cfg.bin;document.getElementById("binKey").value=cfg.key;}modal.classList.add("show");};
document.getElementById("cfgCancel").onclick=()=>modal.classList.remove("show");
document.getElementById("cfgClear").onclick=()=>{cfg=null;localStorage.removeItem(CFGKEY);setPill("未配置云同步");modal.classList.remove("show");};
document.getElementById("cfgSave").onclick=async()=>{const b=document.getElementById("binId").value.trim(),k=document.getElementById("binKey").value.trim();
  if(!b||!k){alert("请填写 Bin ID 和 Master Key");return;}cfg={bin:b,key:k};localStorage.setItem(CFGKEY,JSON.stringify(cfg));modal.classList.remove("show");await pull();await push();};
document.getElementById("pull").onclick=pull;
document.getElementById("push").onclick=push;
document.getElementById("reset").onclick=()=>{if(confirm("清空本机进度？若已配置云同步，请之后点上传覆盖云端")){state={};save();render();}};
buildFilters();render();
if(cfg){setPill("正在拉取…","busy");pull();}else{setPill("未配置云同步");}
document.addEventListener("visibilitychange",()=>{if(document.visibilityState==="visible")autoSync();});
window.addEventListener("focus",autoSync);
setInterval(autoSync,60000);
</script></body></html>'''
html = html.replace("__ITEMS__", JS).replace("__SEC__", SEC)
pm_css = open("/tmp/tui/node_modules/prosemirror-view/style/prosemirror.css", encoding="utf-8").read()
pm_css += "\n" + open("/tmp/tui/node_modules/prosemirror-gapcursor/style/gapcursor.css", encoding="utf-8").read()
pm_css = pm_css.replace("</style", "<\\/style")
pm_js = open("/tmp/tui/md.bundle.js", encoding="utf-8").read().replace("</script", "<\\/script")
html = html.replace("__PM_CSS__", pm_css).replace("__PM_JS__", pm_js)
with open("秋招必背打卡表-云同步.html","w",encoding="utf-8") as f:
    f.write(html)
print("ok", len(items), "html bytes", len(html))
