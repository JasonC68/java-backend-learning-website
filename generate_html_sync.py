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

# ===== 自动归纳标签：关键词 -> 标签（顺序：越具体越靠前）=====
TAG_RULES=[
  ("ConcurrentHashMap","ConcurrentHashMap"),("Hashtable","Hashtable"),("HashMap","HashMap"),
  ("ArrayList","List"),("LinkedList","List"),("Vector","List"),("List","List"),("Set","Set"),
  ("扩容","扩容"),("红黑树","底层结构"),("AVL","底层结构"),("哈希冲突","哈希"),("负载因子","容量/负载"),("n 次方","容量/负载"),
  ("equals","equals/hashCode"),("hashCode","equals/hashCode"),
  ("ABA","CAS"),("CAS","CAS"),("volatile","volatile"),("锁升级","synchronized"),("synchronized","synchronized"),
  ("JMM","JMM"),("内存模型","JMM"),("AQS","AQS/Lock"),("ReentrantLock","AQS/Lock"),("线程池","线程池"),
  ("sleep","线程基础"),("wait","线程基础"),("notify","线程基础"),("线程的创建","线程基础"),("线程的六种状态","线程基础"),("BLOCKED","线程基础"),("如何停止线程","线程基础"),("多线程安全","线程安全"),
  ("双亲委派","类加载"),("类加载","类加载"),("类加载器","类加载"),
  ("垃圾回收","GC"),("回收器","GC"),("CMS","GC"),("G1","GC"),("MinorGC","GC"),("FullGC","GC"),("判断垃圾","GC"),("回收算法","GC"),
  ("引用类型","引用"),("四种引用","引用"),("创建对象","对象"),("内存泄漏","内存问题"),("内存溢出","内存问题"),
  ("程序计数器","内存区域"),("运行时数据区","内存区域"),("堆和栈","内存区域"),("堆怎么分","内存区域"),
  ("最左匹配","索引"),("联合索引","索引"),("聚簇","索引"),("覆盖索引","索引"),("回表","索引"),("B+","索引"),("索引","索引"),("explain","索引"),
  ("MVCC","事务"),("隔离级别","事务"),("幻读","事务"),("ACID","事务"),("事务","事务"),
  ("redo","日志"),("undo","日志"),("binlog","日志"),
  ("间隙锁","锁"),("InnoDB","存储引擎"),("MyISAM","存储引擎"),("慢查询","优化"),("SQL 的执行","优化"),
  ("跳表","数据结构"),("ZSet","数据结构"),("数据类型","数据结构"),
  ("RDB","持久化"),("AOF","持久化"),("淘汰","内存管理"),("过期","内存管理"),
  ("雪崩","缓存问题"),("击穿","缓存问题"),("穿透","缓存问题"),("布隆","缓存问题"),("一致性","缓存一致性"),
  ("分布式锁","分布式锁"),("大 Key","大Key/热Key"),("热 Key","大Key/热Key"),("主从","高可用"),("哨兵","高可用"),("Redis 为什么快","原理"),("原子","原理"),
  ("三次握手","TCP"),("四次挥手","TCP"),("拥塞","TCP"),("TCP 为什么可靠","TCP"),("TCP","TCP"),("UDP","UDP"),
  ("HTTPS","HTTPS"),("状态码","HTTP"),("GET","HTTP"),("POST","HTTP"),("长连接","HTTP"),("HTTP","HTTP"),
  ("Cookie","会话/认证"),("Session","会话/认证"),("Token","会话/认证"),("JWT","会话/认证"),("无状态","会话/认证"),
  ("DNS","DNS"),("WebSocket","WebSocket"),("URL","综合"),
  ("协程","进程线程"),("进程 vs 线程","进程线程"),("进程的五种状态","进程线程"),("进程间通信","进程通信"),("线程间通信","进程通信"),
  ("用户态","用户/内核态"),("死锁","死锁"),("乐观锁","锁"),("自旋","锁"),
  ("虚拟内存","内存管理"),("页面置换","内存管理"),("内存布局","内存管理"),
  ("epoll","IO"),("多路复用","IO"),("零拷贝","IO"),("进程切换","调度"),
  ("IoC","IoC/DI"),("DI ","IoC/DI"),("循环依赖","循环依赖"),("三级缓存","循环依赖"),("AOP","AOP"),
  ("传播行为","事务"),("事务失效","事务"),("Transactional","事务"),("Bean","Bean"),
  ("Spring MVC","SpringMVC"),("自动装配","SpringBoot"),("注解","注解"),
  ("MyBatis","MyBatis"),("MQ","消息队列"),("消息","消息队列"),("CAP","分布式理论"),("BASE","分布式理论"),
  ("分布式事务","分布式事务"),("分布式 ID","分布式ID"),("限流","限流"),
  ("ReAct","推理范式"),("Plan-and-Execute","推理范式"),("Reflection","推理范式"),("推理模式","推理范式"),("反思","反思"),
  ("记忆","记忆"),("规划","规划"),("任务拆分","规划"),("Multi-Agent","多Agent"),("多 Agent","多Agent"),("手搓","工程"),("Agent","Agent"),
  ("RAG","RAG"),("微调","微调对比"),("Chunking","分块"),("切割","分块"),("切断","分块"),("Embedding","Embedding"),("向量","向量库"),
  ("Query","检索"),("召回","检索"),("检索","检索"),("幻觉","幻觉"),("评测","评估"),("量化 你的 RAG","评估"),
  ("Function Calling","FunctionCalling"),("MCP","MCP"),("Skill","Skill"),("A2A","A2A"),("SSE","通信协议"),("WebRTC","通信协议"),("网关","网关"),
  ("大语言模型","基础"),("Transformer","Transformer"),("KV Cache","推理优化"),("Prompt Caching","推理优化"),("Prompt","Prompt工程"),("CoT","Prompt工程"),("Top-P","采样参数"),("温度","采样参数"),("模型选型","选型"),("MoE","架构"),
]
# 按板块映射到小林 coding 的「小标题」，每题一个标签（规则顺序：越具体越靠前）
SECTION_RULES={
 "集合":([("ArrayList","List"),("LinkedList","List"),("Vector","List"),("List","List"),("Set","Set"),("数组与集合","概念"),("Collection","概念"),("遍历","概念")],"Map"),
 "并发/多线程":([("线程的创建","多线程"),("六种状态","多线程"),("sleep","多线程"),("notify","多线程"),("线程池","多线程"),("BLOCKED","多线程"),("停止线程","多线程"),("JMM","并发安全"),("volatile","并发安全"),("synchronized","并发安全"),("CAS","并发安全"),("AQS","并发安全"),("ReentrantLock","并发安全"),("多线程安全","并发安全")],"多线程"),
 "MySQL":([("最左","索引"),("联合索引","索引"),("聚簇","索引"),("覆盖索引","索引"),("回表","索引"),("B+","索引"),("explain","索引"),("索引","索引"),("MVCC","事务"),("隔离级别","事务"),("幻读","事务"),("ACID","事务"),("事务","事务"),("redo","日志"),("undo","日志"),("binlog","日志"),("InnoDB","存储引擎"),("MyISAM","存储引擎"),("间隙","锁"),("锁","锁"),("慢查询","性能调优"),("优化","性能调优"),("执行过程","架构")],"架构"),
 "JVM":([("双亲委派","类初始化和类加载"),("类加载","类初始化和类加载"),("垃圾","垃圾回收"),("回收","垃圾回收"),("CMS","垃圾回收"),("G1","垃圾回收"),("GC","垃圾回收"),("引用","垃圾回收"),("内存泄漏","垃圾回收"),("内存溢出","垃圾回收"),("内存模型","内存模型"),("运行时数据区","内存模型"),("堆","内存模型"),("栈","内存模型"),("程序计数器","内存模型"),("创建对象","内存模型")],"内存模型"),
 "计算机网络":([("握手","传输层"),("挥手","传输层"),("拥塞","传输层"),("TCP","传输层"),("UDP","传输层"),("HTTPS","应用层"),("HTTP","应用层"),("状态码","应用层"),("GET","应用层"),("POST","应用层"),("Cookie","应用层"),("Session","应用层"),("Token","应用层"),("JWT","应用层"),("DNS","应用层"),("WebSocket","应用层"),("长连接","应用层"),("无状态","应用层"),("URL","网络场景")],"应用层"),
 "Redis":([("跳表","数据结构"),("ZSet","数据结构"),("数据类型","数据结构"),("为什么快","线程模型"),("原子","线程模型"),("RDB","日志"),("AOF","日志"),("淘汰","缓存淘汰和过期删除"),("过期","缓存淘汰和过期删除"),("主从","集群"),("哨兵","集群"),("集群","集群"),("雪崩","场景"),("击穿","场景"),("穿透","场景"),("布隆","场景"),("一致性","场景"),("分布式锁","场景"),("大 Key","场景"),("热 Key","场景")],"场景"),
 "操作系统":([("用户态","用户态和内核态"),("内核态","用户态和内核态"),("虚拟内存","内存管理"),("页面置换","内存管理"),("内存布局","内存管理"),("地址","内存管理"),("epoll","网络i/o"),("多路复用","网络i/o"),("零拷贝","网络i/o"),("乐观锁","锁"),("自旋","锁"),("进程","进程管理"),("线程","进程管理"),("协程","进程管理"),("死锁","进程管理"),("通信","进程管理")],"进程管理"),
 "Spring":([("MVC","SpringMVC"),("DispatcherServlet","SpringMVC"),("请求","SpringMVC"),("自动装配","SpringBoot"),("SpringBoot","SpringBoot"),("starter","SpringBoot")],"Spring"),
 "Java基础":([("值传递","数据类型"),("装箱","数据类型"),("Integer","数据类型"),("BigDecimal","数据类型"),("基本数据类型","数据类型"),("重载","面向对象"),("重写","面向对象"),("抽象类","面向对象"),("接口","面向对象"),("多态","面向对象"),("final","关键字"),("static","关键字"),("深拷贝","深拷贝和浅拷贝"),("浅拷贝","深拷贝和浅拷贝"),("泛型","泛型"),("创建对象","对象")],"概念"),
 "扩展(MyBatis/MQ/分布式)":([("MyBatis","MyBatis"),("MQ","消息队列"),("消息","消息队列"),("分布式事务","分布式"),("分布式 ID","分布式"),("CAP","分布式"),("BASE","分布式"),("限流","分布式")],"分布式"),
 "AI·Agent":([("ReAct","设计范式"),("Plan-and-Execute","设计范式"),("Reflection","设计范式"),("范式","设计范式"),("推理模式","设计范式"),("Multi-Agent","多Agent"),("多 Agent","多Agent"),("记忆","工程实践"),("规划","工程实践"),("任务拆分","工程实践"),("反思","工程实践"),("手搓","工程实践"),("什么是 Agent","概念与架构"),("核心组件","概念与架构"),("Workflow","概念与架构")],"概念与架构"),
 "AI·RAG":([("Chunking","索引构建"),("切割","索引构建"),("切断","索引构建"),("Embedding","索引构建"),("向量","索引构建"),("Query","检索优化"),("召回","检索优化"),("检索","检索优化"),("范式","检索优化"),("幻觉","生产落地"),("评测","生产落地"),("量化","生产落地"),("更新","生产落地"),("微调","基础")],"基础"),
 "AI·工具调用":([("Function Calling","Function Calling"),("MCP","MCP"),("Skill","Skill"),("A2A","协议"),("SSE","协议"),("WebRTC","协议"),("通信","协议"),("网关","网关")],"Function Calling"),
 "AI·大模型基础":([("Transformer","架构原理"),("KV Cache","推理优化"),("Prompt Caching","推理优化"),("Prompt","Prompt工程"),("CoT","Prompt工程"),("幻觉","幻觉"),("Top-P","采样参数"),("温度","采样参数"),("选型","选型")],"基础"),
}
def tags_for(sec,q):
    rules,default=SECTION_RULES.get(sec,([],sec))
    for kw,tag in rules:
        if kw in q: return [tag]
    return [default]
for rec in items:
    rec["tags"]=tags_for(rec["sec"],rec["q"])

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
table{width:100%;table-layout:fixed;border-collapse:collapse;background:#fff;border-radius:10px;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,.08)}
th:nth-child(1),td:nth-child(1){width:56px}
th:nth-child(4),td.lvlcol{width:100px}
th:nth-child(5){width:104px}
th:nth-child(6){width:132px}
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
.restore,.purge{border:1px solid #d1d5db;background:#fff;border-radius:6px;padding:3px 12px;font-size:12px;cursor:pointer}
.restore{color:#2563eb;border-color:#93c5fd}.restore:hover{background:#eff6ff}
.purge{color:#b91c1c;border-color:#fca5a5}.purge:hover{background:#fef2f2}
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
.qedit{cursor:pointer;color:#d4d4d4;margin-left:8px;font-size:13px}
.qedit:hover{color:#2563eb}
.qin{width:92%;height:24px;line-height:22px;padding:0 8px;border:1px solid #93c5fd;border-radius:6px;font-size:13px;box-sizing:border-box;vertical-align:middle}
.tag{display:inline-block;font-size:11px;color:#3730a3;background:#eef2ff;border:1px solid #e0e7ff;border-radius:10px;padding:0 7px;margin-left:6px;vertical-align:middle;white-space:nowrap}
tbody tr:not(.sec-row):not(.ed-row):not(.add-row)>td{height:24px}
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
.ebtn{border:1px solid #d1d5db;background:#fff;border-radius:6px;padding:2px 10px;font-size:12px;cursor:pointer;margin-right:6px}
.ebtn:hover{background:#f3f4f6}
.tui-memo{border:1px solid #fde68a;border-radius:8px;background:#fffbeb;margin-bottom:8px;overflow:hidden}
.tui-memo .ProseMirror{outline:none;min-height:70px;padding:10px 14px;font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;font-size:14px;line-height:1.7;color:#1f2937;overflow-wrap:break-word;word-break:break-word}
.memo-label{font-size:12px;color:#b45309;margin:0 0 4px;font-weight:600}
.note-hidden{font-size:13px;color:#9ca3af;padding:10px 4px}
.bk-item{display:flex;align-items:center;gap:8px;padding:8px 10px;border:1px solid #eee;border-radius:8px;margin-bottom:6px}
.bk-item .meta{flex:1;min-width:0;font-size:13px}
.bk-item .meta .t{color:#6b7280;font-size:12px}
.bk-item button{font-size:12px;border:1px solid #d1d5db;background:#fff;border-radius:6px;padding:3px 10px;cursor:pointer}
.bk-item .rb{color:#2563eb;border-color:#93c5fd}.bk-item .db{color:#b91c1c;border-color:#fca5a5}
body.dark .bk-item{border-color:#3a3a3a}
body.dark .bk-item .meta .t{color:#94a3b8}
body.dark .bk-item button{background:#262626;border-color:#3a3a3a;color:#d4d4d4}
body.dark #bkLabel{background:#121212;border-color:#3a3a3a;color:#e5e5e5}
.theme{display:inline-flex;border:1px solid #d1d5db;border-radius:8px;overflow:hidden}
.theme button{border:none;background:#fff;color:#6b7280;padding:5px 9px;cursor:pointer;display:inline-flex;align-items:center}
.theme button:hover{color:#111827}
.theme button svg{width:15px;height:15px;display:block}
.theme button.on{background:#2563eb;color:#fff}
/* ====== 暗色模式 ====== */
body.dark{background:#1a1a1a;color:#e5e5e5}
body.dark .bar{background:#3a3a3a}
body.dark .statline{color:#d4d4d4}
body.dark .pill{background:#3a3a3a;color:#d4d4d4}
body.dark .chip{background:#262626;border-color:#3a3a3a;color:#d4d4d4}
body.dark .chip.active{background:#2563eb;color:#fff;border-color:#2563eb}
body.dark .btn{background:#262626;border-color:#3a3a3a;color:#d4d4d4}
body.dark .btn:hover{background:#303030}
body.dark .btn.pri{background:#2563eb;color:#fff;border-color:#2563eb}
body.dark .pickbtn{background:#262626;border-color:#3a3a3a;color:#d4d4d4}
body.dark table{background:#262626;box-shadow:none}
body.dark th,body.dark td{border-color:#3a3a3a}
body.dark tr.sec-row td{background:#2e2e2e;color:#c7d2fe}
body.dark td.date{color:#94a3b8}
body.dark td.date:hover{background:#303030}
body.dark .last{color:#94a3b8}
body.dark .cnt button{background:#262626;border-color:#3a3a3a;color:#e5e5e5}
body.dark .cnt button:hover{background:#303030}
body.dark .qedit{color:#475569}
body.dark .tag{background:#262626;color:#a5b4fc;border-color:#3a3a3a}
body.dark .tui{background:#121212;border-color:#3a3a3a}
body.dark .ProseMirror{color:#e5e5e5}
body.dark .tui-memo{background:#2a2410;border-color:#a16207}
body.dark .ProseMirror code{background:#3a3a3a;color:#fca5a5}
body.dark .ProseMirror pre{background:#121212}
body.dark .ProseMirror pre code{color:#e5e5e5}
body.dark .ProseMirror blockquote{background:#262626;border-left-color:#4a4a4a;color:#d4d4d4}
body.dark .ProseMirror strong{color:#f1f5f9}
body.dark .ProseMirror li::marker{color:#94a3b8}
body.dark .ProseMirror a{color:#60a5fa}
body.dark .tui-memo{background:#2b240a;border-color:#a16207}
body.dark .memo-label{color:#fcd34d}
body.dark .note-hidden{color:#64748b}
body.dark .ebtn{background:#262626;border-color:#3a3a3a;color:#d4d4d4}
body.dark .ebtn:hover{background:#303030}
body.dark .qin,body.dark .fa,body.dark .addform .ai{background:#121212;border-color:#3a3a3a;color:#e5e5e5}
body.dark .addq{background:#2a2a2a;border-color:#2563eb;color:#93c5fd}
body.dark .add-row td{background:#262626}
body.dark .ed-row td{background:#242424}
body.dark .del{background:#262626;border-color:#7f1d1d;color:#f87171}
body.dark .del:hover{background:#3a1f1f}
body.dark .restore{background:#262626;color:#93c5fd;border-color:#3a3a3a}
body.dark .purge{background:#262626;color:#f87171;border-color:#7f1d1d}
body.dark .cal{background:#262626;border-color:#3a3a3a;color:#e5e5e5}
body.dark .cal-head button{background:#3a3a3a;color:#e5e5e5}
body.dark .cal-day:hover{background:#303030}
body.dark .cal-foot button{background:#262626;border-color:#3a3a3a;color:#d4d4d4}
body.dark .modal .card{background:#262626;color:#e5e5e5}
body.dark .card p{color:#94a3b8}
body.dark .card input{background:#121212;border-color:#3a3a3a;color:#e5e5e5}
body.dark .theme{border-color:#3a3a3a}
body.dark .theme button{background:#262626;color:#d4d4d4}
body.dark .theme button:hover{color:#fff}
body.dark .theme button.on{background:#2563eb;color:#fff}
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
<div class="row1"><h1>秋招后端必背 · 打卡表</h1><span class="pill" id="syncPill">未配置云同步</span><span class="spacer"></span><span class="theme"><button data-theme="system" title="跟随系统"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="3.5" width="19" height="13" rx="2"/><path d="M8 20.5h8M12 16.5v4"/></svg></button><button data-theme="light" title="亮色"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2.2M12 19.3v2.2M4.6 4.6l1.6 1.6M17.8 17.8l1.6 1.6M2.5 12h2.2M19.3 12h2.2M4.6 19.4l1.6-1.6M17.8 6.2l1.6-1.6"/></svg></button><button data-theme="dark" title="暗色"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A8.5 8.5 0 1 1 11.2 3.2 6.6 6.6 0 0 0 21 12.8z"/></svg></button></span></div>
<div class="sub"><span style="color:#9ca3af">v2.6.5</span></div>
<div class="bar"><i id="pbar"></i></div>
<div class="statline" id="stat"></div>
<div class="toolbar" id="filters"></div>
<div class="toolbar">
  <span style="font-size:12px;color:#6b7280">按日期：</span>
  <span class="chip active" data-date="all">全部</span>
  <span class="chip" data-date="todayall" title="今天要打卡的（点 ＋ 算完成）+ 之前没完成顺延的 + 今天到期/逾期要复习的">📌 今天任务</span>
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
  <button class="btn" id="backupBtn">💾 备份</button>
  <button class="btn" id="recycleBtn">🗑 回收站</button>
  <button class="btn" id="reset">清空</button>
</div>
<table><thead><tr>
<th class="c">序号</th><th class="c hide-sm">建议日期</th><th>面试问题</th>
<th class="c">掌握程度</th><th class="c">复习次数</th><th class="c hide-sm">上次复习</th>
</tr></thead><tbody id="tb"></tbody></table>

<div class="cal" id="cal"></div>
<div class="modal" id="bkModal"><div class="card" style="max-width:560px">
  <h3>进度备份</h3>
  <p style="font-size:12px;color:#6b7280;margin-bottom:10px">恢复会覆盖当前进度（建议先新建一个备份）。云端备份跨设备可见；本地备份只在本设备。</p>
  <div style="display:flex;gap:8px;margin-bottom:10px">
    <input id="bkLabel" placeholder="备注（可选）" style="flex:1;padding:8px;border:1px solid #d1d5db;border-radius:6px;font-size:13px">
    <button class="btn" id="bkNew">💾 本地备份</button>
    <button class="btn pri" id="bkNewCloud">☁️ 云端备份</button>
  </div>
  <div style="font-size:12px;color:#6b7280;margin:6px 0 4px">☁️ 云端备份（跨设备）</div>
  <div id="bkCloudList" style="max-height:200px;overflow:auto"></div>
  <div style="font-size:12px;color:#6b7280;margin:10px 0 4px">💾 本地备份（本设备）</div>
  <div id="bkList" style="max-height:200px;overflow:auto"></div>
  <div class="acts">
    <label class="btn" style="cursor:pointer">导入文件<input type="file" id="bkImport" accept="application/json" style="display:none"></label>
    <button class="btn" id="bkClose">关闭</button>
  </div>
</div></div>
<div class="modal" id="modal"><div class="card">
  <h3>云同步设置</h3>
  <p>用免费的 <b>JSONBin.io</b> 存进度：注册后新建一个 Bin（内容填 <code>{}</code>），把 <b>Bin ID</b> 和 <b>Master Key</b> 填到下面。每台设备填一次即可互通。详见配套说明文件。</p>
  <label>Bin ID</label><input id="binId" placeholder="例如 6650a1b2ac...">
  <label>Master Key（$2a$10$... 开头）</label><input id="binKey" placeholder="X-Master-Key">
  <label>图床 API Key（ImgBB，贴图用，可留空）</label><input id="imgKey" placeholder="到 api.imgbb.com 注册免费获取">
  <p style="font-size:12px;color:#6b7280;margin:6px 0 0">填了图床 Key 后，粘贴/拖入的图片会自动上传图床，笔记里只存链接，进度不会再被图片撑爆。</p>
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
let imgKey=localStorage.getItem("imgbb_key")||"";
window.IMG_UPLOADER=function(dataUrl){
  if(!imgKey) return Promise.reject(new Error("no imgbb key"));
  const b64=(dataUrl.split(",")[1]||"");
  const fd=new FormData(); fd.append("image",b64);
  return fetch("https://api.imgbb.com/1/upload?key="+encodeURIComponent(imgKey),{method:"POST",body:fd})
    .then(r=>r.json()).then(j=>{if(j&&j.success&&j.data&&(j.data.display_url||j.data.url))return j.data.display_url||j.data.url;throw new Error("upload failed");});
};
let secFilter="all",lvlFilter="all",dateFilter="all",pickedDate="",starOnly=false,recycleMode=false,timer=null,openIds=new Set(),editors=[],dirty=false,retryTimer=null,stuckToday=new Set(),stuckDay="",restoring=false;
function isDeleted(id){return !!get(id).del;}
function isPurged(id){return !!get(id).purged;}
function isoOf(dt){return dt.getFullYear()+"-"+String(dt.getMonth()+1).padStart(2,"0")+"-"+String(dt.getDate()).padStart(2,"0");}
function todayIso(){return isoOf(new Date());}
function tomorrowIso(){const d=new Date();d.setDate(d.getDate()+1);return isoOf(d);}
const EBB=[1,2,4,7,15,30,60];   // 艾宾浩斯遗忘曲线间隔（天）
function addDays(iso,n){const d=new Date((iso||todayIso())+"T00:00:00");d.setDate(d.getDate()+n);return isoOf(d);}
function schedNext(cnt){const n=EBB[Math.min(Math.max(cnt,1)-1,EBB.length-1)];return addDays(todayIso(),n);}
function loadStuck(){try{const s=JSON.parse(localStorage.getItem("stuck_v1")||"null");if(s&&s.day===todayIso()){stuckDay=s.day;stuckToday=new Set(s.ids);}}catch(e){}}
function saveStuck(){try{localStorage.setItem("stuck_v1",JSON.stringify({day:stuckDay,ids:[...stuckToday]}));}catch(e){}}
function get(id){return state[id]||(state[id]={lvl:0,cnt:0,last:""});}
function qText(it){const o=get(it.id);return (o.q!==undefined&&o.q!=="")?o.q:it.q;}
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
function save(){if(state.__backups)delete state.__backups;localStorage.setItem(KEY,JSON.stringify(state));if(cfg){dirty=true;setPill("待同步…","busy");clearTimeout(timer);timer=setTimeout(push,1200);} }
async function push(){if(!cfg)return;try{setPill("同步中…","busy");await cloudPut();dirty=false;clearRetry();setPill("已同步 "+nowt(),"ok");}catch(e){setPill("同步失败，10秒后重试","warn");scheduleRetry();}}
function isEditing(){const a=document.activeElement;return !!(a&&(a.isContentEditable||a.tagName==="INPUT"||a.tagName==="TEXTAREA"));}
function autoSync(){if(!cfg||restoring)return;if(dirty){push();return;}if(isEditing()){scheduleRetry();return;}pull();}
async function pull(){if(restoring)return;if(!cfg){alert("请先配置云同步");return;}if(isEditing()){scheduleRetry();return;}try{setPill("拉取中…","busy");const c=await cloudGet();if(c&&typeof c==="object"){state=c;localStorage.setItem(KEY,JSON.stringify(state));render();}clearRetry();setPill("已拉取 "+nowt(),"ok");}catch(e){setPill("拉取失败，10秒后重试","warn");scheduleRetry();}}
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
document.getElementById("recycleBtn").onclick=function(){recycleMode=!recycleMode;this.classList.toggle("pri",recycleMode);render();};
function todayCount(){const ti=todayIso();let n=0;const chk=(id,baseIso)=>{const o=get(id);if(o.del||o.purged)return;const d=(o.date&&o.date!=="")?o.date:baseIso;const rd=!!o.next&&o.next<=ti;if(d&&d>ti){if(rd)n++;return;}const sd=!!d&&d<=ti&&!(o.cnt>0);const dt=o.last===today();if(sd||rd||dt)n++;};ITEMS.forEach(it=>chk(it.id,it.iso));customList().forEach(c=>chk(c.id,""));return n;}
function passDate(it){if(dateFilter==="all")return true;if(dateFilter==="todayall"){const ti=todayIso();const o=get(it.id);const d=itemDate(it);const reviewDue=!!o.next&&o.next<=ti;if(d&&d>ti)return reviewDue;const studyDue=!!d&&d<=ti&&!(o.cnt>0);const doneToday=o.last===today();return studyDue||reviewDue||doneToday;}if(dateFilter==="review"){const nx=get(it.id).next;return !!nx&&nx<=todayIso();}if(dateFilter==="pick"){const d=itemDate(it),nx=get(it.id).next;return d===pickedDate||nx===pickedDate;}const d=itemDate(it);if(!d)return false;return d===(dateFilter==="today"?todayIso():tomorrowIso());}
function customList(){return state.__custom||(state.__custom=[]);}
function sectionMap(){const map={};SECTIONS.forEach(s=>map[s]=[]);
  ITEMS.forEach(it=>{(map[it.sec]||(map[it.sec]=[])).push({id:it.id,sec:it.sec,q:it.q,baseIso:it.iso,tags:it.tags});});
  customList().forEach(c=>{(map[c.sec]||(map[c.sec]=[])).push({id:c.id,sec:c.sec,q:c.q,baseIso:"",custom:true,tags:[]});});
  Object.keys(map).forEach(s=>map[s].forEach((it,i)=>it.idx=i+1));return map;}
function itemDate(it){const o=get(it.id);return (o.date!==undefined&&o.date!=="")?o.date:(it.baseIso||"");}
function render(){const tb=document.getElementById("tb");
  const _sy=window.scrollY;
  editors.forEach(e=>{try{e.destroy();}catch(_){}});editors=[];
  tb.innerHTML="";
  const map=sectionMap();
  const secs=Object.keys(map).filter(s=>secFilter==="all"||s===secFilter);
  secs.forEach(s=>{
    let list;
    if(recycleMode){ list=map[s].filter(it=>isDeleted(it.id)&&!isPurged(it.id)); if(list.length===0)return; }
    else { list=map[s].filter(it=>!isDeleted(it.id)&&!isPurged(it.id)&&(lvlFilter==="all"||get(it.id).lvl==lvlFilter)&&passDate(it)&&(!starOnly||get(it.id).star));
           if(list.length===0&&(lvlFilter!=="all"||dateFilter!=="all"||starOnly))return; }
    const sr=document.createElement("tr");sr.className="sec-row";sr.innerHTML='<td colspan="6">'+esc(s)+'</td>';tb.appendChild(sr);
    if(recycleMode){
      list.forEach(it=>{const tr=document.createElement("tr");
        tr.innerHTML='<td class="c">'+it.idx+'</td><td class="c hide-sm date"></td><td class="q">'+esc(qText(it))+(it.custom?' <span style="color:#9333ea;font-size:11px">·自建</span>':'')+'</td>'+
          '<td class="c" colspan="3"><button class="restore">↩ 恢复</button> <button class="purge">🗑 永久删除</button></td>';
        tr.querySelector(".restore").onclick=()=>{delete get(it.id).del;save();render();};
        tr.querySelector(".purge").onclick=()=>{if(confirm("永久删除这道题？不可恢复")){if(it.custom){state.__custom=customList().filter(c=>c.id!==it.id);delete state[it.id];}else{const o=get(it.id);delete o.del;o.purged=true;}save();render();}};
        tb.appendChild(tr);});
      return;
    }
    list.forEach(it=>{const st=get(it.id);
      const opened=openIds.has(it.id), hasNote=st.note&&st.note.trim();
      const tr=document.createElement("tr");
      tr.innerHTML='<td class="c">'+it.idx+'</td>'+
        '<td class="c hide-sm date">'+(fmtIso(itemDate(it))||'<span style="color:#bbb">＋日期</span>')+'</td>'+
        '<td class="q"><span class="star'+(st.star?' on':'')+'" title="收藏">'+(st.star?'★':'☆')+'</span><span class="qbtn'+(hasNote?' has':'')+'"><span class="arw">'+(opened?'▾':'▸')+'</span>'+esc(qText(it))+(it.custom?' <span style="color:#9333ea;font-size:11px">·自建</span>':'')+'</span>'+((it.tags||[]).map(t=>'<span class="tag">'+esc(t)+'</span>').join(''))+'<span class="qedit" title="编辑题目">✎</span></td>'+
        '<td class="c"><button class="lvl l'+st.lvl+'">'+LVLS[st.lvl]+'</button></td>'+
        '<td class="c"><span class="cnt"><button class="minus">−</button><b>'+st.cnt+'</b><button class="plus">＋</button></span></td>'+
        '<td class="c hide-sm last">'+(st.last||"—")+(st.next?' <span style="font-size:11px;color:'+(st.next<=todayIso()?"#dc2626":"#9ca3af")+'">↻'+st.next.slice(5)+'</span>':'')+'</td>';
      const dc=tr.querySelector(".date");
      dc.onclick=e=>{e.stopPropagation();openCal(dc,{selected:itemDate(it),dot:true,clearLabel:"恢复默认",
        onPick:iso=>{get(it.id).date=iso;save();render();},
        onClear:()=>{delete get(it.id).date;save();render();}});};
      tr.querySelector(".star").onclick=e=>{e.stopPropagation();st.star=!st.star;save();render();};
      tr.querySelector(".qedit").onclick=e=>{e.stopPropagation();const cell=tr.querySelector(".q");cell.innerHTML='<input class="qin">';const inp=cell.querySelector(".qin");inp.value=qText(it);inp.focus();const commit=()=>{const v=inp.value.trim();if(v)get(it.id).q=v;save();render();};inp.onkeydown=ev=>{if(ev.key==="Enter")commit();else if(ev.key==="Escape")render();};inp.onblur=commit;};
      tr.querySelector(".qbtn").onclick=()=>{opened?openIds.delete(it.id):openIds.add(it.id);render();};
      tr.querySelector(".lvl").onclick=()=>{st.lvl=(st.lvl+1)%4;save();render();};
      tr.querySelector(".plus").onclick=()=>{st.cnt++;st.last=today();st.next=schedNext(st.cnt);save();render();};
      tr.querySelector(".minus").onclick=()=>{if(st.cnt>0){st.cnt--;if(st.cnt>0)st.next=schedNext(st.cnt);else delete st.next;}save();render();};
      tb.appendChild(tr);
      if(opened){
        const er=document.createElement("tr");er.className="ed-row";
        const td=document.createElement("td");td.colSpan=6;const o=st;
        let bar='<div class="ehint">';
        bar+=(!o.memoOn)?'<button class="ebtn addmemo">＋ 助记</button>':'<button class="ebtn tgmemo">'+(o.memoHide?'显示助记':'隐藏助记')+'</button><button class="ebtn delmemo">删除助记</button>';
        bar+='<button class="ebtn tgnote">'+(o.noteHide?'显示答案':'隐藏答案')+'</button>';
        bar+='<button class="del">🗑 删除</button></div>';
        let body='';
        if(o.memoOn&&!o.memoHide)body+='<div class="memo-label">💡 助记</div><div class="tui-memo"></div>';
        body+=o.noteHide?'<div class="note-hidden">（答案已隐藏，点"显示答案"查看）</div>':'<div class="tui"></div>';
        td.innerHTML=bar+body;
        const addb=td.querySelector(".addmemo");if(addb)addb.onclick=()=>{o.memoOn=true;o.memoHide=false;save();render();};
        const tgm=td.querySelector(".tgmemo");if(tgm)tgm.onclick=()=>{o.memoHide=!o.memoHide;save();render();};
        const dm=td.querySelector(".delmemo");if(dm)dm.onclick=()=>{if(confirm("删除助记？")){o.memoOn=false;delete o.memo;o.memoHide=false;save();render();}};
        td.querySelector(".tgnote").onclick=()=>{o.noteHide=!o.noteHide;save();render();};
        td.querySelector(".del").onclick=()=>{get(it.id).del=true;openIds.delete(it.id);save();render();};
        er.appendChild(td);tb.appendChild(er);
        const mount=(host,getv,setv,ph)=>{if(window.MDEditor){editors.push(window.MDEditor(host,getv()||"",(html)=>{setv(html);save();}));}else{host.innerHTML='<textarea class="fa" placeholder="'+(ph||"")+'"></textarea>';const ta=host.querySelector(".fa");ta.value=getv()||"";ta.oninput=()=>{setv(ta.value);save();};}};
        if(o.memoOn&&!o.memoHide)mount(td.querySelector(".tui-memo"),()=>o.memo,v=>o.memo=v,"写助记/口诀…");
        if(!o.noteHide)mount(td.querySelector(".tui"),()=>st.note,v=>st.note=v,"# 在这里写你总结的答案…");
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
  let base=[];SECTIONS.forEach(s=>base=base.concat((map[s]||[]).filter(it=>!isDeleted(it.id)&&!isPurged(it.id))));
  let done=0;base.forEach(it=>{if(get(it.id).lvl>=2)done++;});
  const tot=base.length,pct=tot?Math.round(done/tot*100):0;
  document.getElementById("pbar").style.width=pct+"%";
  document.getElementById("stat").innerHTML="已掌握(能讲框架+能扛追问)：<b>"+done+"</b> / "+tot+"　("+pct+"%)";
  if(dateFilter==="todayall")saveStuck();
  {const tc=document.querySelector('[data-date="todayall"]');if(tc)tc.textContent="📌 今天任务："+todayCount();}
  window.scrollTo(0,_sy);requestAnimationFrame(()=>window.scrollTo(0,_sy));}
const modal=document.getElementById("modal");
document.getElementById("cfgBtn").onclick=()=>{if(cfg){document.getElementById("binId").value=cfg.bin;document.getElementById("binKey").value=cfg.key;}document.getElementById("imgKey").value=imgKey;modal.classList.add("show");};
document.getElementById("cfgCancel").onclick=()=>modal.classList.remove("show");
document.getElementById("cfgClear").onclick=()=>{cfg=null;localStorage.removeItem(CFGKEY);setPill("未配置云同步");modal.classList.remove("show");};
document.getElementById("cfgSave").onclick=async()=>{const b=document.getElementById("binId").value.trim(),k=document.getElementById("binKey").value.trim(),ik=document.getElementById("imgKey").value.trim();
  imgKey=ik;if(ik)localStorage.setItem("imgbb_key",ik);else localStorage.removeItem("imgbb_key");
  if(b&&k){cfg={bin:b,key:k};localStorage.setItem(CFGKEY,JSON.stringify(cfg));modal.classList.remove("show");await pull();await push();return;}
  if(b||k){alert("Bin ID 和 Master Key 需要一起填写");return;}
  modal.classList.remove("show");};
document.getElementById("pull").onclick=pull;
document.getElementById("push").onclick=push;
document.getElementById("reset").onclick=()=>{if(confirm("清空本机进度？若已配置云同步，请之后点上传覆盖云端")){state={};save();render();}};
// ===== 进度备份（本设备）=====
const BKEY="backups_v1";
function loadBackups(){try{return JSON.parse(localStorage.getItem(BKEY)||"[]");}catch(e){return [];}}
function saveBackups(a){try{localStorage.setItem(BKEY,JSON.stringify(a));}catch(e){alert("备份存储已满，请删除旧备份或导出后删除");}}
function fmtTs(ts){const d=new Date(ts),p=n=>(n+"").padStart(2,"0");return (d.getMonth()+1)+"-"+d.getDate()+" "+p(d.getHours())+":"+p(d.getMinutes());}
function progCount(s){try{return Object.keys(JSON.parse(s)).filter(k=>!k.startsWith("__")).length;}catch(e){return 0;}}
function renderBackups(){const a=loadBackups(),box=document.getElementById("bkList");
  if(!a.length){box.innerHTML='<div style="color:#9ca3af;font-size:13px;padding:8px">还没有备份，点上面「新建备份」</div>';return;}
  box.innerHTML=a.map((b,i)=>'<div class="bk-item"><div class="meta"><div>'+(esc(b.label)||"备份")+'</div><div class="t">'+fmtTs(b.ts)+' · '+progCount(b.data)+' 题有记录</div></div><button class="rb" data-i="'+i+'">恢复</button><button class="xb" data-i="'+i+'">导出</button><button class="db" data-i="'+i+'">删除</button></div>').join("");
  box.querySelectorAll(".rb").forEach(b=>b.onclick=async()=>{const i=+b.dataset.i,a=loadBackups();if(!confirm("恢复到这个备份？当前进度会被覆盖"))return;restoring=true;try{state=JSON.parse(a[i].data);localStorage.setItem(KEY,JSON.stringify(state));render();bkModal.classList.remove("show");clearTimeout(timer);if(cfg){await cloudPut();dirty=false;setPill("已恢复 "+nowt(),"ok");}}catch(e){alert("备份损坏");}restoring=false;});
  box.querySelectorAll(".db").forEach(b=>b.onclick=()=>{const i=+b.dataset.i,a=loadBackups();a.splice(i,1);saveBackups(a);renderBackups();});
  box.querySelectorAll(".xb").forEach(b=>b.onclick=()=>{const i=+b.dataset.i,a=loadBackups();const blob=new Blob([a[i].data],{type:"application/json"});const x=document.createElement("a");x.href=URL.createObjectURL(blob);x.download="打卡备份-"+a[i].ts+".json";x.click();});
}
const bkModal=document.getElementById("bkModal");
// ---- 云端备份：每个备份单独一个小仓库，主进度只存索引（不会撑爆主仓库）----
function bkIndex(){return state.__bkIndex||(state.__bkIndex=[]);}
function renderCloud(){const box=document.getElementById("bkCloudList");
  if(!cfg){box.innerHTML='<div style="color:#9ca3af;font-size:13px;padding:8px">配置「☁️ 云同步」后可用</div>';return;}
  const a=bkIndex();
  if(!a.length){box.innerHTML='<div style="color:#9ca3af;font-size:13px;padding:8px">还没有云端备份，点上方「☁️ 云端备份」创建</div>';return;}
  box.innerHTML=a.map((b,i)=>'<div class="bk-item"><div class="meta"><div>'+(esc(b.label)||"备份")+'</div><div class="t">'+fmtTs(b.ts)+'</div></div><button class="rb" data-i="'+i+'">恢复</button><button class="db" data-i="'+i+'">删除</button></div>').join("");
  box.querySelectorAll(".rb").forEach(btn=>btn.onclick=async()=>{const i=+btn.dataset.i,b=bkIndex()[i];if(!confirm("恢复到这个云端备份？当前进度会被覆盖"))return;restoring=true;try{const r=await fetch("https://api.jsonbin.io/v3/b/"+b.bin+"/latest",{headers:{"X-Master-Key":cfg.key}});if(!r.ok)throw 0;const j=await r.json();const snap=j.record;snap.__bkIndex=bkIndex();state=snap;localStorage.setItem(KEY,JSON.stringify(state));render();bkModal.classList.remove("show");clearTimeout(timer);if(cfg){await cloudPut();dirty=false;setPill("已恢复 "+nowt(),"ok");}}catch(e){alert("恢复失败，检查网络");}restoring=false;});
  box.querySelectorAll(".db").forEach(btn=>btn.onclick=async()=>{const i=+btn.dataset.i,b=bkIndex()[i];bkIndex().splice(i,1);save();renderCloud();try{await fetch("https://api.jsonbin.io/v3/b/"+b.bin,{method:"DELETE",headers:{"X-Master-Key":cfg.key}});}catch(e){}});
}
document.getElementById("backupBtn").onclick=()=>{renderBackups();renderCloud();bkModal.classList.add("show");};
document.getElementById("bkClose").onclick=()=>bkModal.classList.remove("show");
document.getElementById("bkNew").onclick=()=>{const a=loadBackups();a.unshift({ts:Date.now(),label:document.getElementById("bkLabel").value.trim(),data:JSON.stringify(state)});if(a.length>30)a.length=30;saveBackups(a);document.getElementById("bkLabel").value="";renderBackups();};
document.getElementById("bkNewCloud").onclick=async()=>{if(!cfg){alert("请先配置「☁️ 云同步」");return;}const btn=document.getElementById("bkNewCloud");btn.disabled=true;btn.textContent="备份中…";
  try{const snap=Object.assign({},state);delete snap.__bkIndex;delete snap.__backups;
    const r=await fetch("https://api.jsonbin.io/v3/b",{method:"POST",headers:{"Content-Type":"application/json","X-Master-Key":cfg.key},body:JSON.stringify(snap)});if(!r.ok)throw 0;const j=await r.json();
    const a=bkIndex();a.unshift({ts:Date.now(),label:document.getElementById("bkLabel").value.trim(),bin:j.metadata.id});if(a.length>15)a.length=15;
    document.getElementById("bkLabel").value="";save();renderCloud();}
  catch(e){alert("云端备份失败，检查网络/配置");}
  btn.disabled=false;btn.textContent="☁️ 云端备份";};
document.getElementById("bkImport").onchange=function(){const f=this.files[0];if(!f)return;const r=new FileReader();r.onload=()=>{try{JSON.parse(r.result);const a=loadBackups();a.unshift({ts:Date.now(),label:"导入 "+f.name,data:r.result});saveBackups(a);renderBackups();}catch(e){alert("文件格式不对");}};r.readAsText(f);this.value="";};
function applyTheme(){const m=localStorage.getItem("theme")||"system";const dark=m==="dark"||(m==="system"&&window.matchMedia&&matchMedia("(prefers-color-scheme: dark)").matches);document.body.classList.toggle("dark",dark);document.querySelectorAll(".theme button").forEach(b=>b.classList.toggle("on",b.dataset.theme===m));}
document.querySelectorAll(".theme button").forEach(b=>b.onclick=()=>{localStorage.setItem("theme",b.dataset.theme);applyTheme();});
if(window.matchMedia)try{matchMedia("(prefers-color-scheme: dark)").addEventListener("change",()=>{if((localStorage.getItem("theme")||"system")==="system")applyTheme();});}catch(e){}
applyTheme();
loadStuck();buildFilters();render();
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
