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

# ===== 小林coding 每题精确锚点：我的题目文案 -> 小林页面上对应那道题的锚点（逐板块人工核对）=====
XL_ANCHOR={
 # MySQL（已核对 mysql.html 目录）
 "索引为什么用 B+ 树（vs B树/跳表/哈希）":"mysql为什么用b-树结构-和其他结构比的优点",
 "聚簇索引 vs 非聚簇索引":"mysql聚簇索引和非聚簇索引的区别是什么",
 "联合索引 + 最左匹配原则":"联合索引的实现原理",
 "索引失效的场景":"索引失效有哪些",
 "回表 / 覆盖索引":"什么是覆盖索引",
 "事务的 ACID 及实现":"事务的特性是什么-如何实现的",
 "事务隔离级别 + 默认级别":"事务的隔离级别有哪些",
 "RR 怎么（部分）解决幻读":"mysql-设置了可重读隔离级后-怎么保证不发生幻读",
 "MVCC 实现原理":"介绍mvcc实现原理",
 "redo log / undo log / binlog":"日志文件是分成了哪几种",
 "binlog 两阶段提交":"binlog-两阶段提交过程是怎么样的",
 "一条 SQL 的执行过程":"执行一条sql请求的过程是什么",
 "InnoDB vs MyISAM":"说一下mysql的innodb与myisam的区别",
 "MySQL 有哪些锁":"讲一下mysql里有哪些锁",
 "explain 怎么看":"mysql的explain有什么作用",
 "慢查询怎么优化":"给你张表-发现查询速度很慢-你有那些解决方案",
 # Redis（已核对 redis.html 目录）
 "Redis 为什么快":"redis为什么快",
 "五种数据类型及底层实现":"讲一下redis底层的数据结构",
 "ZSet 底层 / 跳表 / 为什么不用 B+ 树":"redis为什么使用跳表而不是用b-树",
 "RDB vs AOF":"redis有哪2种持久化方式-分别的优缺点是什么",
 "内存淘汰策略":"介绍一下redis-内存淘汰策略",
 "过期删除策略":"介绍一下redis过期删除策略",
 "缓存雪崩 / 击穿 / 穿透":"缓存雪崩、击穿、穿透是什么-怎么解决",
 "布隆过滤器原理":"布隆过滤器原理介绍一下",
 "Redis 和 MySQL 缓存一致性":"如何保证-redis-和-mysql-数据缓存一致性问题",
 "Redis 分布式锁":"redis分布式锁的实现原理-什么场景下用到分布式锁",
 "大 Key / 热 Key 问题":"redis的大key问题是什么",
 "主从复制":"redis主从同步中的增量和完全同步怎么实现",
 "哨兵机制":"哨兵机制原理是什么",
 "怎么保证 Redis 操作原子性":"如何实现redis-原子性",
 # 并发/多线程（已核对 juc.html 目录）
 "JMM（Java 内存模型）+ 三大问题":"java-的内存模型-jmm-介绍一下",
 "线程的创建方式":"线程的创建方式有哪些",
 "线程的六种状态":"java线程的状态有哪些",
 "sleep vs wait":"sleep-和-wait的区别是什么",
 "notify vs notifyAll":"notify-和-notifyall-的区别",
 "怎么保证多线程安全":"怎么保证多线程安全",
 "volatile 作用与原理":"voliatle关键字有什么作用",
 "synchronized 原理 + 锁升级":"synchronized锁升级的过程讲一下",
 "CAS 原理 + ABA 问题":"cas-有什么问题-java是怎么解决的",
 "ReentrantLock vs synchronized + AQS":"synchronized和reentrantlock区别",
 "线程池原理（核心参数/流程/拒绝策略）":"介绍一下线程池的工作原理",
 "BLOCKED vs WAITING / 如何停止线程":"blocked和waiting有啥区别",
 # JVM（已核对 jvm.html 目录）
 "JVM 内存模型（运行时数据区）":"jvm的内存模型介绍一下",
 "堆和栈的区别 / 堆怎么分代":"jvm内存模型里的堆和栈有什么区别",
 "程序计数器为什么线程私有":"程序计数器的作用-为什么是私有的",
 "创建对象的过程":"创建对象的过程",
 "类加载过程":"讲一下类加载过程",
 "双亲委派模型是什么 / 有什么用":"java-中-双亲委派-是什么-有啥用",
 "类加载器有哪些":"类加载器有哪些",
 "判断垃圾的方法":"判断垃圾的方法有哪些",
 "垃圾回收算法":"垃圾回收算法有哪些",
 "垃圾回收器 / CMS vs G1":"垃圾回收器-cms-和-g1的区别",
 "MinorGC / MajorGC / FullGC":"minorgc、majorgc、fullgc的区别-什么场景触发full-gc",
 "四种引用类型":"引用类型有哪些-有什么区别",
 "内存泄漏 vs 内存溢出":"内存泄漏和内存溢出的理解",
 # Spring（已核对 spring.html 目录）
 "IoC / DI 是什么":"spring-ioc和aop-介绍一下",
 "Bean 的生命周期":"bean的生命周期说一下",
 "Bean 的作用域":"spring-bean的作用域有哪些",
 "三级缓存如何解决循环依赖":"spring是如何解决循环依赖的",
 "AOP 原理（JDK 代理 vs CGLIB）":"springaop的原理了解吗",
 "@Transactional 事务原理":"spring的事务什么情况下会失效",
 "事务的传播行为":"spring的事务什么情况下会失效",
 "事务失效的场景":"spring的事务什么情况下会失效",
 "Spring MVC 请求处理流程":"了解springmvc的处理流程吗",
 "Spring Boot 自动装配原理":"springboot自动装配原理是什么",
 "常用注解区别（@Autowired vs @Resource 等）":"spring-常用注解有什么",
 # 集合（已核对 collections.html 目录）
 "HashMap 实现原理":"hashmap实现原理介绍一下",
 "HashMap 的 put / get 过程":"hashmap的put过程介绍一下",
 "HashMap 扩容机制":"hashmap的扩容机制介绍一下",
 "为什么容量是 2 的 n 次方 / 负载因子":"hashmap的大小为什么是2的n次方大小呢",
 "为什么链表转红黑树（而非 AVL）":"为什么hashmap要用红黑树而不是平衡二叉树",
 "哈希冲突的解决方法":"了解的哈希冲突解决方法有哪些",
 "HashMap 线程安全吗 / 多线程下的问题":"列举hashmap在多线程下可能会出现的问题",
 "重写 equals / hashCode 的注意点":"重写hashmap的equal和hashcode方法需要注意什么",
 "HashMap 用什么做 Key / 为什么 String 合适":"hashmap一般用什么做key-为啥string适合做key呢",
 "HashMap vs Hashtable vs ConcurrentHashMap":"说一下hashmap和hashtable、concurrentmap的区别",
 "ConcurrentHashMap 怎么实现的":"concurrenthashmap怎么实现的",
 "用了 synchronized 为什么还要 CAS":"已经用了synchronized-为什么还要用cas呢",
 "ArrayList vs LinkedList":"arraylist和linkedlist的区别-哪个集合是线程安全的",
 "ArrayList 扩容机制":"arraylist的扩容机制说一下",
 "ArrayList 为什么线程不安全 / 怎么变安全":"为什么arraylist不是线程安全的-具体来说是哪里不安全",
 "List vs Set":"java-集合中-list-和-set区别是什么",
 # Java基础（已核对 java.html 目录）
 "值传递 vs 引用传递":"值传递和引用传递的区别",
 "装箱拆箱 + Integer 缓存（-128~127）":"说一下-integer的缓存",
 "为什么用 BigDecimal 不用 double":"为什么用bigdecimal-不用double",
 "重载 vs 重写":"重载与重写有什么区别",
 "抽象类 vs 接口":"java抽象类和接口的区别是什么",
 "final / static 的作用":"java-中-final-作用是什么",
 "深拷贝 vs 浅拷贝 + 实现方式":"深拷贝和浅拷贝的区别",
 "JVM / JDK / JRE 三者关系":"jvm、jdk、jre三者关系",
 "八种基本数据类型及字节数":"八种基本的数据类型",
 "封装/继承/多态，多态的体现":"怎么理解面向对象-简单说说封装继承多态",
 "泛型是什么 + 类型擦除":"什么是泛型",
 # 计算机网络（已核对 network.html 目录）
 "TCP 三次握手 + 为什么三次":"tcp三次握手过程说一下",
 "TCP 四次挥手 + 为什么四次 + 2MSL":"tcp-四次挥手过程说一下",
 "TCP vs UDP":"tcp和udp区别是什么",
 "TCP 为什么可靠":"tcp为什么可靠传输",
 "TCP 拥塞控制":"tcp的拥塞控制介绍一下",
 "GET vs POST":"get和post的使用场景-有哪些区别",
 "HTTP 常用状态码（含 502/504）":"http常用的状态码",
 "HTTP vs HTTPS":"http和https-的区别",
 "HTTPS 握手过程":"https握手过程说一下",
 "HTTP/1.1 vs 2.0":"http1-1和2-0的区别是什么",
 "HTTP 无状态 / Cookie 和 Session":"http到底是不是无状态的",
 "Cookie / Session / Token(JWT)":"token-session-cookie的区别",
 "输入 URL 到页面展示发生了什么":"描述一下打开百度首页后发生的网络过程",
 "DNS 解析流程 / TCP 还是 UDP":"dns-域名解析的工作流程",
 "HTTP 长连接 vs WebSocket":"http长连接与websocket有什么区别",
 # 操作系统（已核对 os.html 目录）
 "进程 vs 线程 vs 协程":"进程-线程-协程的区别是什么",
 "进程的五种状态":"进程的状态-五种状态-如何切换",
 "进程间通信方式（IPC）":"进程间通讯有哪些方式",
 "线程间通信方式":"线程间通讯有什么方式",
 "进程切换 vs 线程切换，为什么线程快":"线程切换为什么比进程切换快-节省了什么资源",
 "用户态 vs 内核态":"用户态和内核态的区别",
 "死锁四条件 + 如何避免":"死锁发生条件是什么",
 "乐观锁 vs 悲观锁 / 自旋锁":"乐观锁和悲观锁有什么区别",
 "虚拟内存 / 地址转换":"虚拟地址是怎么转化到物理地址的",
 "程序的内存布局 / 堆栈区别":"程序的内存布局是怎么样的",
 "页面置换算法":"页面置换有哪些算法",
 "IO 多路复用 / select-poll-epoll":"select、poll、epoll-的区别是什么",
 "epoll 的 LT vs ET":"epoll-的-边缘触发和水平触发有什么区别",
 "零拷贝":"零拷贝是什么",
 # 扩展（已核对 mq.html / cap.html 目录；MyBatis 小林站内无对应页面，保持跳转面试题首页）
 "MQ 的作用（解耦/异步/削峰）":"为什么需要消息队列",
 "MQ 如何保证消息不丢失":"消息丢失怎么解决的",
 "MQ 如何保证不重复消费（幂等）":"消息重复消费怎么解决",
 "MQ 消息积压怎么处理":"如何处理消息队列的消息积压问题",
 "CAP / BASE 理论":"介绍一下cap理论",
 "分布式事务方案（2PC/TCC/本地消息表）":"https://xiaolincoding.com/interview/cap.html#分布式事务的解决方案你知道哪些",
 "分布式 ID 生成方案（雪花算法）":"分布式id有什么方案",
 "限流算法（漏桶/令牌桶等）":"常见的限流算法你知道哪些",
 # MyBatis：小林站内无对应页面，改用 JavaGuide
 "MyBatis #{} 和 ${} 的区别":"https://javaguide.cn/system-design/framework/mybatis/mybatis-interview.html#和-的区别是什么",
 "MyBatis 一级/二级缓存":"https://javaguide.cn/system-design/framework/mybatis/mybatis-interview.html",
 # AI·Agent（xiaolinnote 一题一页，直接用完整 URL）
 "什么是 Agent？与大模型有什么本质不同？":"https://xiaolinnote.com/ai/agent/1_whatisagent.html",
 "Agent 的基本架构由哪些核心组件构成？":"https://xiaolinnote.com/ai/agent/2_components.html",
 "Workflow / Agent / Tools 的概念和区别？":"https://xiaolinnote.com/ai/agent/3_workflow_tools.html",
 "Agent 推理模式有哪些？ReAct 是什么、怎么实现？":"https://xiaolinnote.com/ai/agent/5_react.html",
 "ReAct / Plan-and-Execute / Reflection 的区别与选型？":"https://xiaolinnote.com/ai/agent/6_three_patterns.html",
 "复杂任务怎么做任务拆分？为什么要拆分？":"https://xiaolinnote.com/ai/agent/7_tasksplit.html",
 "Agent 的记忆机制 / 记忆模块怎么设计？":"https://xiaolinnote.com/ai/agent/8_memory.html",
 "长短期记忆怎么存？粒度多大？怎么用？":"https://xiaolinnote.com/ai/agent/9_memory_storage.html",
 "Agent 记忆压缩有哪些方法？":"https://xiaolinnote.com/ai/agent/12_memcompress.html",
 "如何赋予 LLM 规划能力？":"https://xiaolinnote.com/ai/agent/14_planning.html",
 "Agent 的反思机制？为什么用、怎么实现？":"https://xiaolinnote.com/ai/agent/15_reflection.html",
 "什么是 Multi-Agent？Single vs Multi 怎么选？":"https://xiaolinnote.com/ai/agent/11_single_multi.html",
 "多 Agent 的协作、通信与动态路由怎么设计？":"https://xiaolinnote.com/ai/agent/16_collab.html",
 "为什么有时手搓 Agent 而不用框架？":"https://xiaolinnote.com/ai/agent/13_handcode.html",
 # AI·RAG
 "什么是 RAG？完整工作流程是怎样的？":"https://xiaolinnote.com/ai/rag/1_whatisrag.html",
 "RAG 解决了什么问题？RAG vs 微调如何选型？":"https://xiaolinnote.com/ai/rag/3_rag_vs_finetune.html",
 "文档切割（Chunking）策略 / 粒度？":"https://xiaolinnote.com/ai/rag/4_chunking.html",
 "怎么规避语义被切断的问题？":"https://xiaolinnote.com/ai/rag/5_semantic_cuts.html",
 "Embedding 是什么？怎么选和评估？":"https://xiaolinnote.com/ai/rag/6_embedding.html",
 "向量数据库是什么？怎么对比选型？":"https://xiaolinnote.com/ai/rag/8_vectordb.html",
 "向量检索 vs 关键词检索的区别？":"https://xiaolinnote.com/ai/rag/11_retrieval_types.html",
 "Query Rewrite 是什么？目的是什么？":"https://xiaolinnote.com/ai/rag/12_query_rewrite.html",
 "什么是多路召回？怎么做？检索优化策略有哪些？":"https://xiaolinnote.com/ai/rag/13_multi_retrieval.html",
 "进阶 RAG 范式（Self-RAG / Corrective RAG）了解哪些？":"https://xiaolinnote.com/ai/rag/15_advanced_paradigms.html",
 "如何规避 RAG 幻觉？怎么量化 RAG 效果？":"https://xiaolinnote.com/ai/rag/17_hallucination.html",
 "RAG 知识库如何动态与持续更新？":"https://xiaolinnote.com/ai/rag/19_dynamic_update.html",
 # AI·工具调用
 "什么是 Function Calling？原理是什么？":"https://xiaolinnote.com/ai/tools/1_function_calling.html",
 "LLM 如何学会调用工具 / FC 能力怎么训练？":"https://xiaolinnote.com/ai/tools/3_fc_training.html",
 "什么是 MCP？由哪几部分组成？":"https://xiaolinnote.com/ai/tools/5_mcp_components.html",
 "MCP 和 Function Calling 的区别？什么场景用哪个？":"https://xiaolinnote.com/ai/tools/7_fc_vs_mcp_usage.html",
 "Skill 是什么？和 MCP 有什么区别？":"https://xiaolinnote.com/ai/tools/10_mcp_vs_skill.html",
 "Function Calling / Skill / MCP 三者的关系与区别？":"https://xiaolinnote.com/ai/tools/11_fc_skill_mcp.html",
 "什么是 A2A 协议？和 MCP 的区别？":"https://xiaolinnote.com/ai/tools/12_a2a_protocol.html",
 "MCP 通信方式 / SSE vs WebSocket 区别？":"https://xiaolinnote.com/ai/tools/14_sse_vs_websocket.html",
 "LLM 网关解决了什么问题？":"https://xiaolinnote.com/ai/tools/16_llm_gateway.html",
 # AI·大模型基础
 "什么是大语言模型？和传统 NLP 模型有什么区别？":"https://xiaolinnote.com/ai/llm/what_is_llm.html",
 "Transformer 架构基本原理（Encoder/Decoder）？":"https://xiaolinnote.com/ai/llm/transformer_architecture.html",
 "KV Cache 是什么？Prompt Caching 原理（省 token）？":"https://xiaolinnote.com/ai/llm/kv_cache_prompt_caching.html",
 "如何写好 Prompt？Prompt 工程实践经验？":"https://xiaolinnote.com/ai/llm/prompt_engineering.html",
 "什么是 CoT？为什么有效？有什么局限？":"https://xiaolinnote.com/ai/llm/cot.html",
 "大模型为什么会幻觉？怎么缓解？":"https://xiaolinnote.com/ai/llm/hallucination.html",
 "温度值 / Top-P / Top-K 是什么？怎么设置？":"https://xiaolinnote.com/ai/llm/temperature_top_p_top_k.html",
 "项目中如何做模型选型？为什么选这个模型？":"https://xiaolinnote.com/ai/llm/model_selection.html",
}
# ===== JavaGuide 精确跳转（仅 Java 相关板块；找不到对应/相近题目的就不加）=====
_JB1="https://javaguide.cn/java/basis/java-basic-questions-01.html#"
_JB2="https://javaguide.cn/java/basis/java-basic-questions-02.html#"
_JB3="https://javaguide.cn/java/basis/java-basic-questions-03.html#"
_JC1="https://javaguide.cn/java/collection/java-collection-questions-01.html#"
_JC2="https://javaguide.cn/java/collection/java-collection-questions-02.html#"
_JK1="https://javaguide.cn/java/concurrent/java-concurrent-questions-01.html#"
_JK2="https://javaguide.cn/java/concurrent/java-concurrent-questions-02.html#"
_JK3="https://javaguide.cn/java/concurrent/java-concurrent-questions-03.html#"
_JVM_MEM="https://javaguide.cn/java/jvm/memory-area.html#"
_JVM_GC="https://javaguide.cn/java/jvm/jvm-garbage-collection.html#"
_JVM_CLP="https://javaguide.cn/java/jvm/class-loading-process.html#"
_JVM_CL="https://javaguide.cn/java/jvm/classloader.html#"
_JSP="https://javaguide.cn/system-design/framework/spring/spring-knowledge-and-questions-summary.html#"
_JMY="https://javaguide.cn/database/mysql/mysql-questions-01.html#"
_JMYI="https://javaguide.cn/database/mysql/mysql-index.html#"
_JMYV="https://javaguide.cn/database/mysql/innodb-implementation-of-mvcc.html#"
_JMYL="https://javaguide.cn/database/mysql/mysql-logs.html#"
_JRD1="https://javaguide.cn/database/redis/redis-questions-01.html#"
_JRD2="https://javaguide.cn/database/redis/redis-questions-02.html#"
_JNW1="https://javaguide.cn/cs-basics/network/other-network-questions.html#"
_JNW2="https://javaguide.cn/cs-basics/network/other-network-questions2.html#"
_JNWT="https://javaguide.cn/cs-basics/network/tcp-connection-and-disconnection.html#"
_JNWR="https://javaguide.cn/cs-basics/network/tcp-reliability-guarantee.html#"
_JOS1="https://javaguide.cn/cs-basics/operating-system/operating-system-basic-questions-01.html#"
_JOS2="https://javaguide.cn/cs-basics/operating-system/operating-system-basic-questions-02.html#"
_JMQ="https://javaguide.cn/high-performance/message-queue/message-queue.html#"
_JCAP="https://javaguide.cn/distributed-system/protocol/cap-and-base-theorem.html#"
_JDID="https://javaguide.cn/distributed-system/distributed-id.html#"
_JDTX="https://javaguide.cn/distributed-system/distributed-transaction.html#"
_JLIM="https://javaguide.cn/high-availability/limit-request.html#"
_JAG="https://javaguide.cn/ai/agent/agent-basis.html#"
_JAGM="https://javaguide.cn/ai/agent/agent-memory.html#"
_JAGC="https://javaguide.cn/ai/agent/context-engineering.html#"
_JAGP="https://javaguide.cn/ai/agent/prompt-engineering.html#"
_JAGS="https://javaguide.cn/ai/agent/skills.html#"
_JMCP="https://javaguide.cn/ai/agent/mcp.html#"
_JAGW="https://javaguide.cn/ai/agent/workflow-graph-loop.html#"
_JRG="https://javaguide.cn/ai/rag/rag-basis.html#"
_JRGD="https://javaguide.cn/ai/rag/rag-document-processing.html#"
_JRGV="https://javaguide.cn/ai/rag/rag-vector-store.html#"
_JRGU="https://javaguide.cn/ai/rag/rag-knowledge-update.html#"
_JRGO="https://javaguide.cn/ai/rag/rag-optimization.html#"
_JLLM="https://javaguide.cn/ai/llm-basis/llm-operation-mechanism.html#"
_JLLA="https://javaguide.cn/ai/llm-basis/llm-api-engineering.html#"
_JLLF="https://javaguide.cn/ai/llm-basis/structured-output-function-calling.html#"
_JLLE="https://javaguide.cn/ai/llm-basis/llm-evaluation.html#"
_JGW="https://javaguide.cn/ai/system-design/llm-gateway.html#"
JG_ANCHOR={
 # Java基础
 "装箱拆箱 + Integer 缓存（-128~127）":_JB1+"包装类型的缓存机制了解么",
 "为什么用 BigDecimal 不用 double":_JB1+"如何解决浮点数运算的精度丢失问题",
 "重载 vs 重写":_JB1+"⭐️-重载和重写有什么区别",
 "JVM / JDK / JRE 三者关系":_JB1+"⭐️-jvm-vs-jdk-vs-jre",
 "八种基本数据类型及字节数":_JB1+"java-中的几种基本数据类型了解么",
 "抽象类 vs 接口":_JB2+"⭐️-接口和抽象类有什么共同点和区别",
 "深拷贝 vs 浅拷贝 + 实现方式":_JB2+"深拷贝和浅拷贝区别了解吗-什么是引用拷贝",
 "封装/继承/多态，多态的体现":_JB2+"⭐️-面向对象三大特征",
 "泛型是什么 + 类型擦除":_JB3+"什么是泛型-有什么作用",
 # 集合
 "HashMap 实现原理":_JC2+"⭐️-hashmap-的底层实现",
 "为什么容量是 2 的 n 次方 / 负载因子":_JC2+"⭐️-hashmap-的长度为什么是-2-的幂次方",
 "HashMap 线程安全吗 / 多线程下的问题":_JC2+"⭐️-hashmap-为什么线程不安全",
 "HashMap vs Hashtable vs ConcurrentHashMap":_JC2+"⭐️-hashmap-和-hashtable-的区别",
 "ConcurrentHashMap 怎么实现的":_JC2+"⭐️-concurrenthashmap-线程安全的具体实现方式-底层具体实现",
 "重写 equals / hashCode 的注意点":_JB2+"为什么重写-equals-时必须重写-hashcode-方法",
 "ArrayList vs LinkedList":_JC1+"⭐️arraylist-与-linkedlist-区别",
 "ArrayList 扩容机制":_JC1+"⭐️说一说-arraylist-的扩容机制吧",
 "List vs Set":_JC1+"⭐️说说-list-set-queue-map-四者的区别",
 # 并发/多线程
 "线程的创建方式":_JK1+"如何创建线程",
 "线程的六种状态":_JK1+"⭐️-说说线程的生命周期和状态",
 "sleep vs wait":_JK1+"thread-sleep-方法和-object-wait-方法对比",
 "怎么保证多线程安全":_JK1+"如何理解线程安全和不安全",
 "JMM（Java 内存模型）+ 三大问题":_JK2+"⭐️-jmm-java-内存模型",
 "volatile 作用与原理":_JK2+"⭐️-volatile-关键字",
 "synchronized 原理 + 锁升级":_JK2+"jdk1-6-之后的-synchronized-底层做了哪些优化-锁升级原理了解吗",
 "CAS 原理 + ABA 问题":_JK2+"cas-算法",
 "ReentrantLock vs synchronized + AQS":_JK2+"⭐️-synchronized-和-reentrantlock-有什么区别",
 "线程池原理（核心参数/流程/拒绝策略）":_JK3+"⭐️-线程池常见参数有哪些-如何解释",
 # JVM
 "JVM 内存模型（运行时数据区）":_JVM_MEM+"运行时数据区域",
 "创建对象的过程":_JVM_MEM+"对象的创建",
 "堆和栈的区别 / 堆怎么分代":_JVM_GC+"堆空间的基本结构",
 "程序计数器为什么线程私有":_JK1+"程序计数器为什么是私有的",
 "类加载过程":_JVM_CLP+"类加载过程",
 "双亲委派模型是什么 / 有什么用":_JVM_CL+"双亲委派模型",
 "类加载器有哪些":_JVM_CL+"类加载器介绍",
 "判断垃圾的方法":_JVM_GC+"死亡对象判断方法",
 "垃圾回收算法":_JVM_GC+"垃圾收集算法",
 "垃圾回收器 / CMS vs G1":_JVM_GC+"垃圾收集器",
 "MinorGC / MajorGC / FullGC":_JVM_GC+"主要进行-gc-的区域",
 "四种引用类型":_JVM_GC+"引用类型总结",
 # Spring
 "IoC / DI 是什么":_JSP+"⭐️什么是-ioc",
 "Bean 的生命周期":_JSP+"⭐️bean-的生命周期了解么",
 "Bean 的作用域":_JSP+"⭐️bean-的作用域有哪些",
 "三级缓存如何解决循环依赖":_JSP+"spring-循环依赖了解吗-怎么解决",
 "AOP 原理（JDK 代理 vs CGLIB）":_JSP+"⭐️谈谈自己对于-aop-的了解",
 "@Transactional 事务原理":_JSP+"transactional-rollbackfor-exception-class-注解了解吗",
 "事务的传播行为":_JSP+"spring-事务中哪几种事务传播行为",
 "Spring MVC 请求处理流程":_JSP+"⭐️springmvc-工作原理了解吗",
 "常用注解区别（@Autowired vs @Resource 等）":_JSP+"⭐️-autowired-和-resource-的区别是什么",
 # MySQL
 "索引为什么用 B+ 树（vs B树/跳表/哈希）":_JMY+"mysql-索引底层数据结构是什么",
 "聚簇索引 vs 非聚簇索引":_JMYI+"聚簇索引与非聚簇索引",
 "联合索引 + 最左匹配原则":_JMY+"请解释一下-mysql-的联合索引及其最左前缀原则",
 "索引失效的场景":_JMY+"索引失效的原因有哪些",
 "回表 / 覆盖索引":_JMY+"什么是覆盖索引",
 "事务的 ACID 及实现":_JMY+"什么是事务",
 "事务隔离级别 + 默认级别":_JMY+"sql-标准定义了哪些事务隔离级别",
 "RR 怎么（部分）解决幻读":_JMYV+"mvcc➕next-key-lock-防止幻读",
 "MVCC 实现原理":_JMYV+"innodb-对-mvcc-的实现",
 "redo log / undo log / binlog":_JMYL+"redo-log",
 "binlog 两阶段提交":_JMYL+"两阶段提交",
 "InnoDB vs MyISAM":_JMY+"⭐️myisam-和-innodb-有什么区别",
 "MySQL 有哪些锁":_JMY+"表级锁和行级锁了解吗-有什么区别",
 "explain 怎么看":_JMY+"如何分析-sql-的性能",
 "慢查询怎么优化":_JMY+"mysql-性能怎么优化",
 # Redis
 "Redis 为什么快":_JRD1+"⭐️redis-为什么这么快",
 "五种数据类型及底层实现":_JRD1+"redis-常用的数据类型有哪些",
 "ZSet 底层 / 跳表 / 为什么不用 B+ 树":_JRD1+"redis-的有序集合底层为什么要用跳表-而不用平衡树、红黑树或者-b-树",
 "RDB vs AOF":_JRD1+"⭐️redis-持久化机制-重要",
 "内存淘汰策略":_JRD1+"redis-内存淘汰策略了解么",
 "过期删除策略":_JRD1+"redis-过期-key-删除策略了解么",
 "缓存雪崩 / 击穿 / 穿透":_JRD2+"⭐️redis-生产问题-重要",
 "Redis 和 MySQL 缓存一致性":_JRD2+"如何保证缓存和数据库数据的一致性",
 "Redis 分布式锁":_JRD1+"如何基于-redis-实现分布式锁",
 "大 Key / 热 Key 问题":_JRD2+"redis-bigkey-大-key",
 "怎么保证 Redis 操作原子性":_JRD2+"lua-脚本",
 # 计算机网络
 "TCP 三次握手 + 为什么三次":_JNWT+"建立连接-tcp-三次握手",
 "TCP 四次挥手 + 为什么四次 + 2MSL":_JNWT+"断开连接-tcp-四次挥手",
 "TCP vs UDP":_JNW2+"⭐️-tcp-与-udp-的区别-重要",
 "TCP 为什么可靠":_JNWR+"tcp-如何保证传输的可靠性",
 "TCP 拥塞控制":_JNWR+"tcp-的拥塞控制是怎么实现的",
 "GET vs POST":_JNW1+"⭐️-get-和-post-的区别",
 "HTTP 常用状态码（含 502/504）":_JNW1+"⭐️-http-状态码有哪些",
 "HTTP vs HTTPS":_JNW1+"⭐️-http-和-https-有什么区别-重要",
 "HTTPS 握手过程":_JNW1+"https-握手里的-rsa-和-ecdhe-到底差在哪-应用层",
 "HTTP/1.1 vs 2.0":_JNW1+"⭐️-http-1-1-和-http-2-0-有什么区别",
 "HTTP 无状态 / Cookie 和 Session":_JNW1+"⭐️-http-是不保存状态的协议-如何保存用户状态",
 "Cookie / Session / Token(JWT)":_JNW1+"cookie-和-session-有什么区别",
 "输入 URL 到页面展示发生了什么":_JNW1+"⭐️-从输入-url-到页面展示到底发生了什么-非常重要",
 "DNS 解析流程 / TCP 还是 UDP":_JNW1+"⭐️-dns-解析的过程是什么样的",
 "HTTP 长连接 vs WebSocket":_JNW1+"⭐️-websocket-和-http-有什么区别",
 # 操作系统
 "进程 vs 线程 vs 协程":_JOS1+"进程和线程的区别是什么",
 "进程的五种状态":_JOS1+"进程有哪几种状态",
 "进程间通信方式（IPC）":_JOS1+"进程间的通信方式有哪些",
 "线程间通信方式":_JOS1+"线程间的同步的方式有哪些",
 "进程切换 vs 线程切换，为什么线程快":_JOS1+"什么是上下文切换",
 "用户态 vs 内核态":_JOS1+"什么是用户态和内核态",
 "死锁四条件 + 如何避免":_JOS1+"产生死锁的四个必要条件是什么",
 "虚拟内存 / 地址转换":_JOS2+"虚拟地址与物理内存地址是如何映射的",
 "页面置换算法":_JOS2+"常见的页面置换算法有哪些",
 "IO 多路复用 / select-poll-epoll":_JOS2+"select、poll-和-epoll-有什么区别",
 "零拷贝":_JOS2+"什么是零拷贝",
 # 扩展
 "MQ 的作用（解耦/异步/削峰）":_JMQ+"消息队列有什么用",
 "MQ 如何保证消息不丢失":_JMQ+"如何保证消息可靠性",
 "MQ 如何保证不重复消费（幂等）":_JMQ+"如何处理重复消费和幂等",
 "MQ 消息积压怎么处理":_JMQ+"如何处理消息积压",
 "CAP / BASE 理论":_JCAP+"cap-理论",
 "分布式事务方案（2PC/TCC/本地消息表）":_JDTX+"分布式事务解决方案",
 "分布式 ID 生成方案（雪花算法）":_JDID+"snowflake-雪花算法",
 "限流算法（漏桶/令牌桶等）":_JLIM+"常见限流算法有哪些",
 # AI·Agent
 "什么是 Agent？与大模型有什么本质不同？":_JAG+"什么是-ai-agent",
 "Agent 的基本架构由哪些核心组件构成？":_JAG+"做一个-agent-系统-最少要搞定哪三层",
 "Workflow / Agent / Tools 的概念和区别？":_JAG+"ai-工作流和-agent-到底是什么关系",
 "Agent 推理模式有哪些？ReAct 是什么、怎么实现？":_JAG+"react",
 "ReAct / Plan-and-Execute / Reflection 的区别与选型？":_JAG+"各范式怎么选",
 "复杂任务怎么做任务拆分？为什么要拆分？":_JAGP+"任务分解",
 "Agent 的记忆机制 / 记忆模块怎么设计？":_JAGM+"agent-的记忆系统是如何设计的",
 "长短期记忆怎么存？粒度多大？怎么用？":_JAGM+"什么是长期记忆-long-term-memory",
 "Agent 记忆压缩有哪些方法？":_JAGC+"compaction-窗口快满时压缩历史",
 "什么是 Multi-Agent？Single vs Multi 怎么选？":_JAG+"multi-agent",
 "多 Agent 的协作、通信与动态路由怎么设计？":_JAGW+"graph-和-loop-是什么",
 # AI·RAG
 "什么是 RAG？完整工作流程是怎样的？":_JRG+"rag-工作原理了解吗",
 "RAG 解决了什么问题？RAG vs 微调如何选型？":_JRG+"rag-和微调怎么选",
 "文档切割（Chunking）策略 / 粒度？":_JRGD+"如何选择合适的-chunking-策略",
 "怎么规避语义被切断的问题？":_JRGD+"什么是语义丢失-为什么会发生",
 "Embedding 是什么？怎么选和评估？":_JRG+"embedding-是什么",
 "向量数据库是什么？怎么对比选型？":_JRGV+"向量数据库怎么选",
 "向量检索 vs 关键词检索的区别？":_JRGV+"语义检索和关键词检索有什么不同",
 "Query Rewrite 是什么？目的是什么？":_JRGO+"query-rewrite-先把问题变得可检索",
 "什么是多路召回？怎么做？检索优化策略有哪些？":_JRGO+"召回优化-不要只靠向量相似度",
 "进阶 RAG 范式（Self-RAG / Corrective RAG）了解哪些？":_JRG+"rag-有哪些演进阶段",
 "如何规避 RAG 幻觉？怎么量化 RAG 效果？":_JRGO+"评估-不做评估-优化就是玄学",
 "RAG 知识库如何动态与持续更新？":_JRGU+"增量更新和全量重建各适合什么场景",
 # AI·工具调用
 "什么是 Function Calling？原理是什么？":_JLLF+"⭐️-function-calling-到底调用了什么",
 "什么是 MCP？由哪几部分组成？":_JMCP+"mcp-里到底有哪些东西",
 "MCP 和 Function Calling 的区别？什么场景用哪个？":_JMCP+"mcp、function-calling、agent-到底是什么关系",
 "Skill 是什么？和 MCP 有什么区别？":_JAGS+"skill-和-prompt、mcp、function-calling-有什么联系",
 "Function Calling / Skill / MCP 三者的关系与区别？":_JLLF+"function-calling、mcp-tool、http-api、agent-skill-应该怎么分层",
 "什么是 A2A 协议？和 MCP 的区别？":_JAG+"a2a-协议",
 "MCP 通信方式 / SSE vs WebSocket 区别？":_JMCP+"stdio-和-streamable-http-怎么选",
 "LLM 网关解决了什么问题？":_JGW+"为什么需要-llm-gateway",
 # AI·大模型基础
 "KV Cache 是什么？Prompt Caching 原理（省 token）？":_JLLM+"prompt-caching-的省钱逻辑",
 "如何写好 Prompt？Prompt 工程实践经验？":_JAGP+"prompt-应该怎么写",
 "什么是 CoT？为什么有效？有什么局限？":_JAGP+"思维链-chain-of-thought-cot",
 "大模型为什么会幻觉？怎么缓解？":_JAGP+"减少幻觉",
 "温度值 / Top-P / Top-K 是什么？怎么设置？":_JLLM+"⭐️-采样参数如何影响输出稳定性",
 "项目中如何做模型选型？为什么选这个模型？":_JGW+"什么任务适合小模型-什么任务必须上强模型",
}
for rec in items:
    rec["anc"]=XL_ANCHOR.get(rec["q"],"")
    rec["jg"]=JG_ANCHOR.get(rec["q"],"")

JS=json.dumps(items,ensure_ascii=False); SEC=json.dumps(list(data.keys()),ensure_ascii=False)

# ===== 算法刷题：CodeTop 高频前 100（顺序与 codetop.cc 按频度排序一致）=====
ALG_RAW=[("3","无重复字符的最长子串","滑动窗口"),("146","LRU缓存机制","哈希+双向链表"),("206","反转链表","链表"),("215","数组中的第K个最大元素","堆/快选"),("25","K 个一组翻转链表","链表"),("15","三数之和","双指针"),("53","最大子数组和","动态规划"),("补充题4","手撕快速排序","排序"),("5","最长回文子串","动态规划"),("21","合并两个有序链表","链表"),("102","二叉树的层序遍历","BFS"),("200","岛屿数量","DFS"),("33","搜索旋转排序数组","二分"),("1","两数之和","哈希"),("20","有效的括号","栈"),("46","全排列","回溯"),("88","合并两个有序数组","双指针"),("121","买卖股票的最佳时机","动态规划"),("92","反转链表 II","链表"),("103","二叉树的锯齿形层次遍历","BFS"),("300","最长上升子序列","动态规划"),("236","二叉树的最近公共祖先","二叉树"),("23","合并K个排序链表","堆"),("54","螺旋矩阵","模拟"),("143","重排链表","链表"),("141","环形链表","快慢指针"),("415","字符串相加","模拟"),("56","合并区间","排序"),("72","编辑距离","动态规划"),("160","相交链表","双指针"),("42","接雨水","双指针"),("1143","最长公共子序列","动态规划"),("82","删除排序链表中的重复元素 II","链表"),("93","复原IP地址","回溯"),("124","二叉树中的最大路径和","DFS"),("19","删除链表的倒数第N个节点","快慢指针"),("4","寻找两个正序数组的中位数","二分"),("142","环形链表 II","快慢指针"),("165","比较版本号","双指针"),("199","二叉树的右视图","BFS"),("239","滑动窗口最大值","单调队列"),("22","括号生成","回溯"),("704","二分查找","二分"),("32","最长有效括号","栈"),("69","x 的平方根","二分"),("148","排序链表","归并"),("94","二叉树的中序遍历","二叉树"),("232","用栈实现队列","栈"),("31","下一个排列","数组"),("76","最小覆盖子串","滑动窗口"),("2","两数相加","链表"),("322","零钱兑换","动态规划"),("43","字符串相乘","模拟"),("8","字符串转换整数 (atoi)","模拟"),("70","爬楼梯","动态规划"),("105","从前序与中序遍历序列构造二叉树","二叉树"),("41","缺失的第一个正数","原地哈希"),("78","子集","回溯"),("151","翻转字符串里的单词","字符串"),("34","在排序数组中查找元素的第一个和最后一个位置","二分"),("剑指Offer22","链表中倒数第k个节点","快慢指针"),("394","字符串解码","栈"),("129","求根到叶子节点数字之和","DFS"),("155","最小栈","栈"),("101","对称二叉树","二叉树"),("39","组合总和","回溯"),("64","最小路径和","动态规划"),("470","用 Rand7() 实现 Rand10()","数学"),("695","岛屿的最大面积","DFS"),("128","最长连续序列","哈希"),("122","买卖股票的最佳时机 II","贪心"),("104","二叉树的最大深度","二叉树"),("221","最大正方形","动态规划"),("110","平衡二叉树","二叉树"),("234","回文链表","快慢指针"),("152","乘积最大子数组","动态规划"),("14","最长公共前缀","字符串"),("48","旋转图像","模拟"),("240","搜索二维矩阵 II","矩阵"),("98","验证二叉搜索树","二叉树"),("144","二叉树的前序遍历","二叉树"),("179","最大数","贪心"),("662","二叉树最大宽度","BFS"),("543","二叉树的直径","DFS"),("162","寻找峰值","二分"),("62","不同路径","动态规划"),("560","和为K的子数组","前缀和"),("113","路径总和 II","DFS"),("24","两两交换链表中的节点","链表"),("209","长度最小的子数组","滑动窗口"),("198","打家劫舍","动态规划"),("112","路径总和","DFS"),("83","删除排序链表中的重复元素","链表"),("139","单词拆分","动态规划"),("227","基本计算器 II","栈"),("718","最长重复子数组","动态规划"),("226","翻转二叉树","二叉树"),("169","多数元素","摩尔投票"),("207","课程表","拓扑排序"),("283","移动零","双指针")]
# 建议日期：从 2026-07-16 起，第一遍 30 天刷完（每天 3~4 题）；第二遍靠复习＋艾宾浩斯自然落在第二个月
ALG_START=date(2026,7,16)
# 难度（来自 codetop/leetcode）：1=简单 2=中等 3=困难，顺序与 ALG_RAW 一致
ALG_LV=[2,2,1,2,3,2,2,2,2,1,2,2,2,1,1,2,1,1,2,2,
        2,2,3,2,2,1,1,2,3,1,3,2,2,2,3,2,3,2,2,2,
        3,2,1,3,1,2,1,1,2,3,2,2,2,2,1,2,3,2,2,2,
        1,2,2,1,1,2,2,2,2,2,1,1,2,1,1,2,1,2,2,2,
        1,2,2,1,2,2,2,2,2,2,2,1,1,2,2,2,1,1,2,1]
assert len(ALG_LV)==len(ALG_RAW)==100
# 力扣 slug（来自 codetop 接口的 slug_title），顺序与 ALG_RAW 一致；链接 = https://leetcode.cn/problems/<slug>/
ALG_SLUG=["longest-substring-without-repeating-characters","lru-cache","reverse-linked-list","kth-largest-element-in-an-array","reverse-nodes-in-k-group","3sum","maximum-subarray","sort-an-array","longest-palindromic-substring","merge-two-sorted-lists","binary-tree-level-order-traversal","number-of-islands","search-in-rotated-sorted-array","two-sum","valid-parentheses","permutations","merge-sorted-array","best-time-to-buy-and-sell-stock","reverse-linked-list-ii","binary-tree-zigzag-level-order-traversal",
"longest-increasing-subsequence","lowest-common-ancestor-of-a-binary-tree","merge-k-sorted-lists","spiral-matrix","reorder-list","linked-list-cycle","add-strings","merge-intervals","edit-distance","intersection-of-two-linked-lists","trapping-rain-water","longest-common-subsequence","remove-duplicates-from-sorted-list-ii","restore-ip-addresses","binary-tree-maximum-path-sum","remove-nth-node-from-end-of-list","median-of-two-sorted-arrays","linked-list-cycle-ii","compare-version-numbers","binary-tree-right-side-view",
"sliding-window-maximum","generate-parentheses","binary-search","longest-valid-parentheses","sqrtx","sort-list","binary-tree-inorder-traversal","implement-queue-using-stacks","next-permutation","minimum-window-substring","add-two-numbers","coin-change","multiply-strings","string-to-integer-atoi","climbing-stairs","construct-binary-tree-from-preorder-and-inorder-traversal","first-missing-positive","subsets","reverse-words-in-a-string","find-first-and-last-position-of-element-in-sorted-array",
"lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof","decode-string","sum-root-to-leaf-numbers","min-stack","symmetric-tree","combination-sum","minimum-path-sum","implement-rand10-using-rand7","max-area-of-island","longest-consecutive-sequence","best-time-to-buy-and-sell-stock-ii","maximum-depth-of-binary-tree","maximal-square","balanced-binary-tree","palindrome-linked-list","maximum-product-subarray","longest-common-prefix","rotate-image","search-a-2d-matrix-ii","validate-binary-search-tree",
"binary-tree-preorder-traversal","largest-number","maximum-width-of-binary-tree","diameter-of-binary-tree","find-peak-element","unique-paths","subarray-sum-equals-k","path-sum-ii","swap-nodes-in-pairs","minimum-size-subarray-sum","house-robber","path-sum","remove-duplicates-from-sorted-list","word-break","basic-calculator-ii","maximum-length-of-repeated-subarray","invert-binary-tree","majority-element","course-schedule","move-zeroes"]
assert len(ALG_SLUG)==100
alg_items=[{"id":"alg"+str(i),"idx":i+1,"num":n,"q":t,"tag":g,"lv":ALG_LV[i],"slug":ALG_SLUG[i],"iso":(ALG_START+timedelta(days=i*30//100)).isoformat()} for i,(n,t,g) in enumerate(ALG_RAW)]
ALGJS=json.dumps(alg_items,ensure_ascii=False)

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
.bar{position:relative;height:14px;background:#e5e7eb;border-radius:8px;overflow:hidden;margin:8px 0;font-size:0}
.bar>i{display:inline-block;height:100%;vertical-align:top;width:0;transition:width .3s}
#pbar{background:linear-gradient(90deg,#34d399,#059669)}
#pbar2{background:linear-gradient(90deg,#fbbf24,#f59e0b)}
#goalmark{position:absolute;top:0;bottom:0;width:2px;background:#dc2626;z-index:3}
.statline{font-size:13px;margin-bottom:12px}.statline b{color:#059669}
.estrow{display:flex;flex-wrap:wrap;align-items:center;gap:8px 14px;margin:0 0 12px}
.est{font-size:13px;color:#374151;display:flex;flex-wrap:wrap;align-items:center;gap:6px 10px}
.est .estlabel{color:#6b7280}
.est .estseg{background:#f3f4f6;border-radius:8px;padding:3px 10px;white-space:nowrap}
.est .estsub{color:#9ca3af;font-size:12px;margin-left:4px}
.est .esttot{font-weight:600;color:#2563eb;white-space:nowrap}
.est.none{color:#16a34a}
.timer{display:inline-flex;align-items:center;gap:6px;padding:3px 8px;border:1px solid #e5e7eb;border-radius:8px;background:#fff;margin-left:auto}
.timer .tdot{width:6px;height:6px;border-radius:50%;background:#cbd5e1;flex:none}
.timer.run .tdot{background:#16a34a;animation:tblink 1s ease-in-out infinite}
@keyframes tblink{50%{opacity:.3}}
.timer b{font-size:13px;color:#111827;font-variant-numeric:tabular-nums;min-width:58px;display:inline-block;font-weight:600}
.timer button{font-size:12px;line-height:1;border:1px solid #d1d5db;background:#fff;border-radius:6px;width:22px;height:22px;padding:0;cursor:pointer;display:inline-flex;align-items:center;justify-content:center}
.timer #timerToggle{font-size:10px}
.timer button:hover{background:#f3f4f6}
.timer button.on{background:#2563eb;color:#fff;border-color:#2563eb}
body.dark .timer{background:#1f1f1f;border-color:#3a3a3a}
body.dark .timer b{color:#e5e5e5}
body.dark .timer .tdot{background:#4b5563}
body.dark .timer button{background:#262626;border-color:#3a3a3a;color:#d4d4d4}
body.dark .timer button:hover{background:#303030}
@media(max-width:640px){.timer{width:100%;box-sizing:border-box;justify-content:flex-start}}
.focusbar{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:10px 14px;background:#fef2f2;border:1px solid #fecaca;border-radius:12px;padding:10px 14px;margin:0 0 12px}
.focusbar .fp-main{display:flex;align-items:center;gap:8px;flex:1;min-width:220px}
.focusbar .fp-kind{font-size:12px;font-weight:600;padding:2px 9px;border-radius:8px;white-space:nowrap}
.focusbar .fp-kind.new{background:#fee2e2;color:#b91c1c}
.focusbar .fp-kind.review{background:#fecaca;color:#7f1d1d}
.focusbar .fp-q{font-size:14px;color:#111827;font-weight:500;cursor:pointer;text-decoration:underline;text-decoration-color:transparent;text-underline-offset:3px;transition:text-decoration-color .15s}
.focusbar .fp-q:hover{text-decoration-color:currentColor}
.focusbar .fp-side{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.focusbar .fp-time{display:inline-flex;align-items:baseline;gap:6px;margin-right:2px}
.focusbar .fp-time b{font-size:18px;font-variant-numeric:tabular-nums;color:#b91c1c;font-weight:600;min-width:52px;display:inline-block}
.focusbar .fp-time.over b{color:#dc2626}
.focusbar .fp-allot{font-size:12px;color:#6b7280;white-space:nowrap}
#focusBtn{border-color:#dc2626}
#focusBtn:hover{background:#fef2f2}
#focusBtn:disabled{border-color:#e5e7eb;color:#9ca3af;background:#f9fafb;cursor:not-allowed}
#focusBtn:disabled:hover{background:#f9fafb}
body.dark #focusBtn:disabled{border-color:#3a3a3a;color:#6b7280;background:#1c1c1c}
.focusbar .btn.pri,#focusModal .btn.pri,#focusBtn.pri,body.dark .focusbar .btn.pri,body.dark #focusModal .btn.pri,body.dark #focusBtn.pri{background:#dc2626;border-color:#dc2626;color:#fff}
.focusbar .btn.pri:hover,#focusModal .btn.pri:hover,#focusBtn.pri:hover,body.dark .focusbar .btn.pri:hover,body.dark #focusModal .btn.pri:hover,body.dark #focusBtn.pri:hover{background:#b91c1c;border-color:#b91c1c}
body.dark #focusBtn{border-color:#dc2626}
body.dark #focusBtn:hover{background:#2a1416}
body.dark .focusbar{background:#2a1416;border-color:#5f2626}
body.dark .focusbar .fp-q{color:#e5e5e5}
body.dark .focusbar .fp-time b{color:#fca5a5}
body.dark .focusbar .fp-kind.new{background:#5a2323;color:#fca5a5}
body.dark .focusbar .fp-kind.review{background:#491c1c;color:#fda4a4}
@media(max-width:640px){.focusbar .fp-side{width:100%;justify-content:flex-start}}
.toolbar{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px;align-items:center}
.chip{border:1px solid #d1d5db;background:#fff;border-radius:16px;padding:4px 12px;font-size:13px;cursor:pointer;user-select:none}
.chip.active{background:#2563eb;color:#fff;border-color:#2563eb}
.spacer{flex:1}
.btn{border:1px solid #d1d5db;background:#fff;border-radius:6px;padding:5px 10px;font-size:12px;cursor:pointer}
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
td.date{width:120px;min-width:120px;max-width:120px;color:#6b7280;font-size:12px;white-space:nowrap;cursor:pointer;border-radius:6px;overflow:hidden}
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
.cal{position:fixed;z-index:50;background:#fff;border:1px solid #e5e7eb;border-radius:12px;box-shadow:0 8px 24px rgba(0,0,0,.14);padding:10px;width:252px;display:none}
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
.cal-quick{display:flex;gap:4px;margin-top:8px}
.cal-quick button{flex:1;font-size:11px;border:1px solid #93c5fd;background:#eff6ff;color:#2563eb;border-radius:6px;padding:4px 0;cursor:pointer}
.cal-quick button:hover{background:#dbeafe}
body.dark .cal-quick button{background:#1e293b;border-color:#3a3a3a;color:#93c5fd}
.cal-foot{display:flex;justify-content:space-between;gap:4px;margin-top:8px}
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
.preview code{background:#f3f4f6;padding:1px 4px;border-radius:4px;font-size:12px}
.preview pre{background:#f3f4f6;padding:8px;border-radius:6px;overflow:auto}
.preview pre code{background:none;padding:0}
.preview blockquote{border-left:3px solid #d1d5db;margin:5px 0;padding-left:10px;color:#4b5563}
.preview table{border:1px solid #e5e7eb;box-shadow:none;margin:5px 0}.preview th{position:static}
@media(max-width:640px){
  body{padding:10px}
  h1{font-size:18px}
  .hide-sm{display:none}
  /* 筛选行：横向滑动，不再平铺多行 */
  .toolbar{flex-wrap:nowrap;overflow-x:auto;overflow-y:hidden;padding-bottom:3px}
  .toolbar::-webkit-scrollbar{display:none}
  .toolbar{scrollbar-width:none}
  .toolbar>*{flex:0 0 auto}
  .toolbar .spacer{display:none}
  /* 表格改成卡片式 */
  thead{display:none}
  table{display:block;box-shadow:none;border-radius:0;background:transparent}
  tbody{display:block}
  tr.sec-row{display:block}
  tr.sec-row td{display:block;width:auto;border-radius:6px}
  tbody tr:not(.sec-row){display:flex;flex-wrap:wrap;align-items:center;gap:4px 10px;padding:9px 6px}
  tbody tr:not(.sec-row)>td{display:block;border:none;padding:0;height:auto!important;width:auto!important;max-width:none!important;text-align:left}
  tr:not(.sec-row)>td.c:first-child{order:0;color:#9ca3af;font-size:12px;min-width:16px}
  td.q{order:1;flex:1 1 62%;font-size:14px}
  td:nth-child(4){order:2}
  td:nth-child(5){order:3}
  tr.ed-row{display:block}
  tr.ed-row>td{display:block;width:100%!important}
  tr.add-row{display:block}
  tr.add-row>td{display:block;width:100%!important}
  .card{width:94%}
}
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
.memowrap{position:relative}
.memobtn{position:absolute;top:6px;z-index:3;border:none;background:rgba(120,80,0,.10);color:#92700e;border-radius:6px;width:22px;height:22px;font-size:12px;line-height:1;cursor:pointer}
.memofold{right:34px}.memodel{right:8px}
.memobtn:hover{background:rgba(120,80,0,.2)}
.memodel:hover{background:rgba(220,38,38,.18);color:#b91c1c}
.memo-folded{position:relative;border:1px solid #fde68a;background:#fffbeb;border-radius:8px;margin-bottom:8px;padding:10px 64px 10px 14px;font-size:13px;color:#92700e;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;cursor:pointer}
.memo-folded:hover{background:#fef9ec}
.notewrap{position:relative}
.notebtn{position:absolute;top:6px;right:8px;z-index:3;border:none;background:rgba(0,0,0,.06);color:#6b7280;border-radius:6px;width:22px;height:22px;font-size:12px;line-height:1;cursor:pointer}
.notebtn:hover{background:rgba(0,0,0,.12);color:#374151}
.note-folded{position:relative;border:1px solid #e5e7eb;background:#fff;border-radius:8px;padding:10px 40px 10px 14px;font-size:13px;color:#6b7280;cursor:pointer}
.note-folded:hover{background:#f9fafb}
body.dark .notebtn{background:rgba(255,255,255,.08);color:#94a3b8}
body.dark .notebtn:hover{background:rgba(255,255,255,.16);color:#e5e5e5}
body.dark .note-folded{background:#262626;border-color:#3a3a3a;color:#94a3b8}
body.dark .note-folded:hover{background:#2e2e2e}
body.dark .memobtn{background:rgba(255,255,255,.08);color:#fcd34d}
body.dark .memobtn:hover{background:rgba(255,255,255,.16)}
body.dark .memo-folded{background:#2b240a;border-color:#a16207;color:#fcd34d}
body.dark .memo-folded:hover{background:#332a0c}
.codebox{margin-top:6px}
.codewrap{position:relative;border:1px solid #e5e7eb;border-radius:8px;background:#1e1e1e;margin-bottom:8px;overflow:hidden}
.codewrap pre,.codewrap textarea{margin:0;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13px;line-height:1.6;padding:12px 14px;white-space:pre-wrap;word-break:break-word;tab-size:2;box-sizing:border-box}
.codewrap pre{min-height:88px;overflow:hidden}
.codewrap pre code{font:inherit;display:block;min-height:1.6em}
.codewrap textarea{position:absolute;inset:0;width:100%;height:100%;border:none;outline:none;resize:none;background:transparent;color:transparent;caret-color:#fff;overflow:hidden}
.codewrap textarea::placeholder{color:#888}
.codedel,.codefold{position:absolute;top:5px;z-index:3;border:none;background:rgba(255,255,255,.08);color:#aaa;border-radius:6px;width:22px;height:22px;font-size:12px;line-height:1;cursor:pointer}
.codedel{right:7px}.codefold{right:34px}
.codefold:hover{background:rgba(255,255,255,.18);color:#fff}
.codedel:hover{background:rgba(248,113,113,.35);color:#fff}
.codewrap.folded{margin-bottom:6px}
.codewrap.folded pre.foldline{min-height:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;padding:9px 64px 9px 14px}
.codewrap.nodel .codefold{right:7px}
.tag.lc{text-decoration:none;cursor:pointer}
.tag.lc:hover{background:#2563eb;color:#fff;border-color:#2563eb}
body.dark .tag.lc:hover{background:#2563eb;color:#fff;border-color:#2563eb}
.dtag{display:inline-block;font-size:11px;border-radius:10px;padding:0 7px;margin-left:6px;vertical-align:middle;white-space:nowrap}
.dtag.d1{background:#d9ead3;color:#256029;border:1px solid #b7dfa8}
.dtag.d2{background:#fdebc8;color:#b45309;border:1px solid #f3d190}
.dtag.d3{background:#fde2e2;color:#b91c1c;border:1px solid #f8b4b4}
body.dark .dtag.d1{background:#14321c;color:#86efac;border-color:#2f6b3f}
body.dark .dtag.d2{background:#33280a;color:#fcd34d;border-color:#7c5c12}
body.dark .dtag.d3{background:#3a1414;color:#fca5a5;border-color:#7f1d1d}
.hljs{color:#e1e4e8}
.hljs-comment,.hljs-quote{color:#8b949e}
.hljs-keyword,.hljs-selector-tag,.hljs-type,.hljs-literal{color:#ff7b72}
.hljs-string,.hljs-doctag,.hljs-regexp{color:#a5d6ff}
.hljs-number{color:#79c0ff}
.hljs-title,.hljs-section,.hljs-built_in{color:#d2a8ff}
.hljs-attr,.hljs-attribute,.hljs-variable,.hljs-template-variable{color:#ffa657}
.hljs-name,.hljs-tag,.hljs-symbol{color:#7ee787}
.hljs-meta{color:#8b949e}
.note-hidden{font-size:13px;color:#9ca3af;padding:10px 4px}
.bk-item{display:flex;align-items:center;gap:8px;padding:8px 10px;border:1px solid #eee;border-radius:8px;margin-bottom:6px}
.bk-item .meta{flex:1;min-width:0;font-size:13px}
.bk-item .meta .t{color:#6b7280;font-size:12px}
.bk-item button{font-size:12px;border:1px solid #d1d5db;background:#fff;border-radius:6px;padding:3px 10px;cursor:pointer}
.bk-item .rb{color:#2563eb;border-color:#93c5fd}.bk-item .db{color:#b91c1c;border-color:#fca5a5}
.bk-item .cvt{color:#047857;border-color:#6ee7b7}
.bk-item .cvt:hover{background:#ecfdf5}
body.dark .bk-item .cvt{color:#6ee7b7;border-color:#3a3a3a}
body.dark .bk-item{border-color:#3a3a3a}
body.dark .bk-item .meta .t{color:#94a3b8}
body.dark .bk-item button{background:#262626;border-color:#3a3a3a;color:#d4d4d4}
body.dark #bkLabel{background:#121212;border-color:#3a3a3a;color:#e5e5e5}
.theme{display:inline-flex;border:1px solid #d1d5db;border-radius:8px;overflow:hidden}
.theme button{border:none;background:#fff;color:#6b7280;padding:5px 9px;cursor:pointer;display:inline-flex;align-items:center}
.theme button:hover{color:#111827}
.theme button svg{width:15px;height:15px;display:block}
.theme button.on{background:#2563eb;color:#fff}
#cfModal{z-index:200}
#toast{z-index:300;position:fixed;left:50%;bottom:32px;transform:translateX(-50%) translateY(16px);background:#1f2937;color:#fff;padding:9px 18px;border-radius:20px;font-size:13px;box-shadow:0 6px 20px rgba(0,0,0,.25);opacity:0;pointer-events:none;transition:.25s;z-index:100}
#toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
/* ====== 暗色模式 ====== */
body.dark{background:#1a1a1a;color:#e5e5e5}
body.dark .bar{background:#3a3a3a}
body.dark .statline{color:#d4d4d4}
body.dark .est{color:#d4d4d4}
body.dark .est .estseg{background:#262626}
body.dark .est .esttot{color:#60a5fa}
body.dark .est.none{color:#4ade80}
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
body.dark .codewrap{border-color:#3a3a3a}
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
.ProseMirror mark,.preview mark{background:#fef08a;color:inherit;border-radius:4px;padding:0 1px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
body.dark .ProseMirror mark,body.dark .preview mark{background:#854d0e;color:#fef9c3}
.ProseMirror hr{border:none;border-top:1px solid #e5e7eb;margin:12px 0}
</style>
<script>__PM_JS__</script>
<script>__HL_JS__</script>
</head><body>
<div class="row1"><h1>秋招后端 · 打卡表</h1><span class="theme" id="modeSw"><button data-mode="gu">八股</button><button data-mode="alg">算法</button></span><span class="pill" id="syncPill">未配置云同步</span><span class="spacer"></span><span class="theme"><button data-theme="system" title="跟随系统"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="3.5" width="19" height="13" rx="2"/><path d="M8 20.5h8M12 16.5v4"/></svg></button><button data-theme="light" title="亮色"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2.2M12 19.3v2.2M4.6 4.6l1.6 1.6M17.8 17.8l1.6 1.6M2.5 12h2.2M19.3 12h2.2M4.6 19.4l1.6-1.6M17.8 6.2l1.6-1.6"/></svg></button><button data-theme="dark" title="暗色"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A8.5 8.5 0 1 1 11.2 3.2 6.6 6.6 0 0 0 21 12.8z"/></svg></button></span></div>
<div class="sub"><span style="color:#9ca3af">v2.11.4</span></div>
<div class="bar"><i id="pbar"></i><i id="pbar2"></i><span id="goalmark" style="left:60%" title="达到 60% 可开始投递面试"></span></div>
<div class="statline" id="stat"></div>
<div class="estrow">
  <div class="est" id="estLine" title="按单题估时算出的、完成今天剩余任务还需要多久（每完成一题自动减少）"></div>
  <span class="timer" id="timerBox" title="学习计时器：可随时开始 / 暂停 / 重置"><span class="tdot"></span><b id="timerDisp">00:00:00</b><button id="timerToggle" title="开始">▶</button><button id="timerReset" title="重置">↺</button></span>
</div>
<div class="focusbar" id="focusPanel" style="display:none">
  <div class="fp-main"><span class="fp-kind" id="focusKind"></span><span class="fp-q" id="focusQ" title="点击跳到这道题并展开"></span></div>
  <div class="fp-side"><span class="fp-time" id="focusTime"><b id="focusDisp">00:00</b><span class="fp-allot" id="focusAllot"></span></span><button class="btn pri" id="focusDone">✓ 完成本题</button><button class="btn" id="focusPause" title="暂停/继续本题计时">⏸ 暂停</button><button class="btn" id="focusSkip" title="这题先跳过，换下一题">⏭ 跳过</button><button class="btn" id="focusStop">⏹ 结束</button></div>
</div>
<div class="toolbar" id="filters"></div>
<div class="toolbar" id="dateBar">
  <span style="font-size:12px;color:#6b7280">按日期：</span>
  <span class="chip active" data-date="all">全部</span>
  <span class="chip" data-date="todayall" title="今天要打卡的（点 ＋ 算完成）+ 之前没完成顺延的 + 今天到期/逾期要复习的">📌 今天任务</span>
  <button class="btn" id="trimBtn" title="把今天未完成的一部分任务挪到未来" style="margin-left:2px">✂️ 缩减</button>
  <button class="btn" id="focusBtn" title="从今日任务里挑一题、按建议时长开始专注学习/复习">🎯 专注</button>
  <span class="chip" data-date="today">📅 今天打卡</span>
  <span class="chip" data-date="tomorrow">明天</span>
  <span class="chip" data-date="review" title="按艾宾浩斯遗忘曲线，到期/逾期需复习的题">🔁 今日复习</span>
  <span class="pickwrap" style="margin-left:8px"><button class="pickbtn" id="pickBtn">📅 选择日期</button></span>
</div>
<div class="toolbar">
  <span style="font-size:12px;color:#6b7280">按掌握程度：</span>
  <span class="chip active" data-lvl="all">全部</span>
  <span class="chip" data-lvl="0">未开始</span><span class="chip" data-lvl="1">眼熟</span>
  <span class="chip" data-lvl="2">能讲框架</span><span class="chip" data-lvl="3">能扛追问</span>
  <span class="chip" id="starFilter" style="margin-left:8px">⭐ 仅看收藏</span>
</div>
<div class="toolbar" id="diffBar">
  <span style="font-size:12px;color:#6b7280">按难度：</span>
  <span class="chip active" data-diff="all">全部</span>
  <span class="chip" data-diff="1">简单</span>
  <span class="chip" data-diff="2">中等</span>
  <span class="chip" data-diff="3">困难</span>
</div>
<div class="toolbar">
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
<div class="modal" id="cfModal"><div class="card" style="max-width:380px">
  <p id="cfMsg" style="font-size:14px;line-height:1.6;margin-bottom:16px"></p>
  <div class="acts"><button class="btn" id="cfNo">取消</button><button class="btn pri" id="cfYes">确定</button></div>
</div></div>
<div class="modal" id="focusModal"><div class="card" style="max-width:360px">
  <h3 style="font-size:16px;margin-bottom:8px">⏰ 时间到</h3>
  <p id="focusModalMsg" style="font-size:13px;color:#4b5563;margin-bottom:14px;line-height:1.6"></p>
  <div class="acts"><button class="btn" id="focusStopBtn">停止复习</button><button class="btn" id="focusStayBtn">继续本题</button><button class="btn pri" id="focusNextBtn">复习下一题</button></div>
</div></div>
<div id="toast"></div>
<div class="modal" id="trimModal"><div class="card" style="max-width:430px">
  <h3>缩减今日任务</h3>
  <p style="font-size:13px;color:#6b7280;margin-bottom:10px">把今天<b>未完成</b>的一部分任务均匀挪到未来，减轻当天负担。已完成的不动。</p>
  <div style="display:flex;gap:6px;margin-bottom:12px">
    <span class="chip active" data-tt="all">全部</span>
    <span class="chip" data-tt="study">新学习</span>
    <span class="chip" data-tt="review">复习</span>
  </div>
  <div style="display:flex;flex-direction:column;gap:8px">
    <button class="btn" data-trim="0.25">缩减 1/4　·　分散到未来 2 天</button>
    <button class="btn" data-trim="0.5">缩减 1/2　·　分散到未来 4 天</button>
    <button class="btn" data-trim="0.75">缩减 3/4　·　分散到未来 6 天</button>
  </div>
  <div class="acts"><button class="btn" id="trimCancel">取消</button></div>
</div></div>
<div class="modal" id="bkModal"><div class="card" style="max-width:560px">
  <h3>进度备份</h3>
  <p style="font-size:12px;color:#6b7280;margin-bottom:10px">恢复会覆盖当前进度。云端只保留 1 份、跨设备可见；本地可存多份，只在本设备。</p>
  <div style="display:flex;gap:8px;margin-bottom:10px">
    <input id="bkLabel" placeholder="备注" style="flex:1;padding:8px;border:1px solid #d1d5db;border-radius:6px;font-size:13px">
    <button class="btn" id="bkNew">💾 本地备份</button>
    <button class="btn pri" id="bkNewCloud">☁️ 云端备份</button>
  </div>
  <div style="font-size:12px;color:#6b7280;margin:6px 0 4px">☁️ 云端备份</div>
  <div id="bkCloudList" style="max-height:200px;overflow:auto"></div>
  <div style="font-size:12px;color:#6b7280;margin:10px 0 4px">💾 本地备份</div>
  <div id="bkList" style="max-height:200px;overflow:auto"></div>
  <div class="acts">
    <button class="btn" id="bkImportBtn">导入文件</button><input type="file" id="bkImport" accept="application/json" style="display:none">
    <button class="btn" id="bkClose">关闭</button>
  </div>
</div></div>
<div class="modal" id="modal"><div class="card">
  <h3>云同步设置</h3>
  <p>用免费的 <b>Supabase</b> 存进度：建一个项目和 <code>checkin</code> 表，把 <b>Project URL</b> 和 <b>anon key</b> 填到下面。每台设备填一次即可互通。建表 SQL 见配套说明文件。</p>
  <label>Project URL</label><input id="supaUrl" placeholder="https://xxxx.supabase.co">
  <label>anon / publishable key</label><input id="supaKey" placeholder="eyJ... 或 sb_publishable_...">
  <label>图床 API Key（ImgBB，贴图用，可留空）</label><input id="imgKey" placeholder="到 api.imgbb.com 注册免费获取">
  <p style="font-size:12px;color:#6b7280;margin:6px 0 0">填了图床 Key 后，粘贴/拖入的图片会自动上传图床，笔记里只存链接，进度不会再被图片撑爆。</p>
  <div class="acts">
    <button class="btn" id="cfgClear">清除配置</button>
    <button class="btn" id="cfgCancel">取消</button>
    <button class="btn pri" id="cfgSave">保存并同步</button>
  </div>
</div></div>
<script>
const ITEMS=__ITEMS__, SECTIONS=__SEC__, ALG=__ALG__;
const KEY="review_tracker_v2", CFGKEY="sync_cfg_v1";
const LVLS=["未开始","眼熟","能讲框架","能扛追问"];
let state=JSON.parse(localStorage.getItem(KEY)||"{}");
let cfg=JSON.parse(localStorage.getItem(CFGKEY)||"null");
if(cfg&&!cfg.url){cfg=null;localStorage.removeItem(CFGKEY);}   // 旧 JSONBin 配置作废，需重填 Supabase
let imgKey=localStorage.getItem("imgbb_key")||"";
window.IMG_UPLOADER=function(dataUrl){
  if(!imgKey) return Promise.reject(new Error("no imgbb key"));
  const b64=(dataUrl.split(",")[1]||"");
  const fd=new FormData(); fd.append("image",b64);
  return fetch("https://api.imgbb.com/1/upload?key="+encodeURIComponent(imgKey),{method:"POST",body:fd})
    .then(r=>r.json()).then(j=>{if(j&&j.success&&j.data&&(j.data.display_url||j.data.url))return j.data.display_url||j.data.url;throw new Error("upload failed");});
};
let secFilter="all",lvlFilter="all",diffFilter="all",dateFilter="all",pickedDate="",starOnly=false,recycleMode=false,timer=null,openIds=new Set(),editors=[],retryTimer=null,stuckToday=new Set(),stuckDay="",restoring=false;
const DKEY=KEY+"_dirty";
let dirty=localStorage.getItem(DKEY)==="1";
let saveSeq=0;
function setDirty(v){dirty=v;try{v?localStorage.setItem(DKEY,"1"):localStorage.removeItem(DKEY);}catch(e){}}
function touchRev(){state.__rev=Date.now();}
function revOf(o){return (o&&+o.__rev)||0;}
function isDeleted(id){return !!get(id).del;}
function isPurged(id){return !!get(id).purged;}
function isoOf(dt){return dt.getFullYear()+"-"+String(dt.getMonth()+1).padStart(2,"0")+"-"+String(dt.getDate()).padStart(2,"0");}
function todayIso(){return isoOf(new Date());}
function tomorrowIso(){const d=new Date();d.setDate(d.getDate()+1);return isoOf(d);}
const EBB=[1,2,4,7,15,30,60];   // 艾宾浩斯遗忘曲线间隔（天）
function addDays(iso,n){const d=new Date((iso||todayIso())+"T00:00:00");d.setDate(d.getDate()+n);return isoOf(d);}
function schedNext(cnt){const n=EBB[Math.min(Math.max(cnt,1)-1,EBB.length-1)];return addDays(todayIso(),n);}
// 算法题：艾宾浩斯 × 考察频度系数（CodeTop 排名越靠前＝考频越高＝复习越勤）
function freqFactor(idx){return idx<=20?0.7:(idx<=50?0.9:1.1);}
function schedNextAlg(cnt,idx){const n=EBB[Math.min(Math.max(cnt,1)-1,EBB.length-1)];return addDays(todayIso(),Math.max(1,Math.round(n*freqFactor(idx))));}
function loadStuck(){try{const s=JSON.parse(localStorage.getItem("stuck_v1")||"null");if(s&&s.day===todayIso()){stuckDay=s.day;stuckToday=new Set(s.ids);}}catch(e){}}
function saveStuck(){try{localStorage.setItem("stuck_v1",JSON.stringify({day:stuckDay,ids:[...stuckToday]}));}catch(e){}}
function get(id){return state[id]||(state[id]={lvl:0,cnt:0,last:""});}
function qText(it){const o=get(it.id);return (o.q!==undefined&&o.q!=="")?o.q:it.q;}
function esc(s){return (s||"").replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c]));}
function plainFirstLine(html){const d=document.createElement("div");d.innerHTML=html||"";const t=(d.textContent||"").replace(/\\u00a0/g," ").trim();return (t.split("\\n")[0]||"").slice(0,60);}
let cfCb=null;
function confirmDlg(msg,cb){document.getElementById("cfMsg").textContent=msg;cfCb=cb;document.getElementById("cfModal").classList.add("show");}
function toast(msg){const t=document.getElementById("toast");t.textContent=msg;t.classList.add("show");clearTimeout(t._h);t._h=setTimeout(()=>t.classList.remove("show"),2200);}
function md(t){return (window.marked?marked.parse(t||""):"<pre>"+esc(t)+"</pre>");}
function highlightHTML(code){if(window.hljs){try{return hljs.highlightAuto(code||"").value;}catch(e){}}return esc(code);}
function renderCodes(host,o,minOne){
  host.innerHTML="";
  const canDel=!minOne||(o.codes||[]).length>1;   // minOne：至少保留一个代码框，只剩一个时不给删
  (o.codes||[]).forEach((c,idx)=>{
    const box=document.createElement("div");box.className="codewrap"+(c.fold?" folded":"")+(canDel?"":" nodel");
    const btns='<button class="codefold" title="折叠/展开">'+(c.fold?"▸":"▾")+'</button>'+(canDel?'<button class="codedel" title="删除此代码块">✕</button>':'');
    const del=()=>{confirmDlg("删除此代码块？",()=>{o.codes.splice(idx,1);if(!o.codes.length)delete o.codes;save();render();});};
    if(c.fold){
      const first=(c.code||"").split("\\n")[0]||"",more=(c.code||"").indexOf("\\n")>=0;
      box.innerHTML=btns+'<pre class="foldline"><code class="hljs"></code></pre>';
      box.querySelector("code").innerHTML=highlightHTML(first)+(more?' <span style="color:#888">…</span>':"");
      box.style.cursor="pointer";
      box.onclick=e=>{if(e.target.closest(".codedel"))return;c.fold=false;save();render();};
      const db=box.querySelector(".codedel");if(db)db.onclick=e=>{e.stopPropagation();del();};
    }else{
      box.innerHTML=btns+'<pre aria-hidden="true"><code class="hljs"></code></pre><textarea spellcheck="false" placeholder="粘贴代码…"></textarea>';
      const code=box.querySelector("code"),ta=box.querySelector("textarea");
      const paint=()=>{const v=ta.value;code.innerHTML=highlightHTML(v)+(v.slice(-1)==="\\n"?"\\n":"");};
      ta.value=c.code||"";paint();
      ta.oninput=()=>{c.code=ta.value;paint();save();};
      ta.onkeydown=e=>{if(e.key==="Tab"){e.preventDefault();const s=ta.selectionStart,en=ta.selectionEnd;ta.value=ta.value.slice(0,s)+"  "+ta.value.slice(en);ta.selectionStart=ta.selectionEnd=s+2;c.code=ta.value;paint();save();}};
      box.querySelector(".codefold").onclick=()=>{c.fold=true;save();render();};
      const db=box.querySelector(".codedel");if(db)db.onclick=del;
    }
    host.appendChild(box);
  });
}
// ===== 小林coding 跳转：板块 -> 页面，tag -> 页内小标题锚点（锚点对不上时自动停在页顶，退化为板块级）=====
const XLURL={"集合":"https://xiaolincoding.com/interview/collections.html","并发/多线程":"https://xiaolincoding.com/interview/juc.html","MySQL":"https://xiaolincoding.com/interview/mysql.html","JVM":"https://xiaolincoding.com/interview/jvm.html","Spring":"https://xiaolincoding.com/interview/spring.html","计算机网络":"https://xiaolincoding.com/interview/network.html","Redis":"https://xiaolincoding.com/interview/redis.html","操作系统":"https://xiaolincoding.com/interview/os.html","Java基础":"https://xiaolincoding.com/interview/java.html","扩展(MyBatis/MQ/分布式)":"https://xiaolincoding.com/interview/mq.html","AI·Agent":"https://xiaolinnote.com/ai/agent/agent_info.html","AI·RAG":"https://xiaolinnote.com/ai/rag/rag_info.html","AI·工具调用":"https://xiaolinnote.com/ai/tools/tools_info.html","AI·大模型基础":"https://xiaolinnote.com/ai/llm/llm_info.html"};
function xlSlug(s){return (s||"").toLowerCase().replace(/[^a-z0-9\\u4e00-\\u9fa5]+/g,"-").replace(/^-+|-+$/g,"");}
function xlLink(sec,tags,anc){
  if(anc&&/^https?:\/\//.test(anc))return anc;
  let base=XLURL[sec];const t=(tags&&tags[0])||"";
  if(sec==="扩展(MyBatis/MQ/分布式)"){
    if(t==="分布式")base="https://xiaolincoding.com/interview/cap.html";
    else if(t==="MyBatis")return "https://xiaolincoding.com/interview/";
  }
  if(!base)return "";
  if(!/xiaolincoding\\.com\\/interview\\/.+\\.html$/.test(base))return base;
  if(anc)return base+"#"+anc;          // 精确到那一题
  if(t)return base+"#"+xlSlug(t);      // 退回小标题级
  return base;
}
function fmtIso(iso){if(!iso)return"";const d=new Date(iso+"T00:00:00");if(isNaN(d))return iso;const wk=["日","一","二","三","四","五","六"];return (d.getMonth()+1+"").padStart(2,"0")+"-"+(d.getDate()+"").padStart(2,"0")+" 周"+wk[d.getDay()];}
function today(){const d=new Date();return (d.getMonth()+1+"").padStart(2,"0")+"-"+(d.getDate()+"").padStart(2,"0");}
function nowt(){const d=new Date();return (d.getHours()+"").padStart(2,"0")+":"+(d.getMinutes()+"").padStart(2,"0");}
function setPill(t,cls){const p=document.getElementById("syncPill");p.textContent=t;p.className="pill"+(cls?" "+cls:"");}
function api(p){return cfg.url.replace(/\\/$/,"")+"/rest/v1/"+p;}
function H(extra){const h=Object.assign({apikey:cfg.key},extra||{});if(/^eyJ/.test(cfg.key))h.Authorization="Bearer "+cfg.key;return h;}
async function cloudGet(){const r=await fetch(api("checkin?id=eq.main&select=data"),{headers:H()});if(!r.ok)throw 0;const a=await r.json();return a.length?a[0].data:null;}
async function cloudPut(){const r=await fetch(api("checkin?on_conflict=id"),{method:"POST",headers:H({"Content-Type":"application/json","Prefer":"resolution=merge-duplicates,return=minimal"}),body:JSON.stringify([{id:"main",kind:"main",data:state}])});if(!r.ok)throw 0;}
function scheduleRetry(){if(retryTimer)return;retryTimer=setTimeout(()=>{retryTimer=null;autoSync();},10000);}
function clearRetry(){if(retryTimer){clearTimeout(retryTimer);retryTimer=null;}}
function save(){if(state.__backups)delete state.__backups;saveSeq++;touchRev();localStorage.setItem(KEY,JSON.stringify(state));if(cfg){setDirty(true);setPill("待同步…","busy");clearTimeout(timer);timer=setTimeout(push,1200);} }
async function push(){if(!cfg)return;const mySeq=saveSeq;try{setPill("同步中…","busy");await cloudPut();if(saveSeq===mySeq){setDirty(false);clearRetry();setPill("已同步 "+nowt(),"ok");}else{setPill("待同步…","busy");clearTimeout(timer);timer=setTimeout(push,600);}}catch(e){setPill("同步失败，10秒后重试","warn");scheduleRetry();}}
function isEditing(){const a=document.activeElement;return !!(a&&(a.isContentEditable||a.tagName==="INPUT"||a.tagName==="TEXTAREA"));}
function autoSync(){if(!cfg||restoring)return;if(dirty){push();return;}if(isEditing()){scheduleRetry();return;}pull();}
async function pull(force){if(restoring)return;if(!cfg){toast("请先配置云同步");return;}if(!force&&isEditing()){scheduleRetry();return;}try{setPill("拉取中…","busy");const c=await cloudGet();if(c&&typeof c==="object"){
    if(!force&&revOf(c)<revOf(state)){clearRetry();setPill("本机更新，改为上传…","busy");setDirty(true);push();return;}
    state=c;localStorage.setItem(KEY,JSON.stringify(state));setDirty(false);render();}
  clearRetry();setPill("已拉取 "+nowt(),"ok");}catch(e){setPill("拉取失败，10秒后重试","warn");scheduleRetry();}}
function buildFilters(){const f=document.getElementById("filters");f.innerHTML='<span style="font-size:12px;color:#6b7280">板块：</span>';
  const mk=(t,v)=>{const s=document.createElement("span");s.className="chip"+(v===secFilter?" active":"");s.textContent=t;s.onclick=()=>{secFilter=v;buildFilters();render();};return s;};
  f.appendChild(mk("全部","all"));SECTIONS.forEach(s=>f.appendChild(mk(s,s)));}
document.querySelectorAll('[data-lvl]').forEach(c=>c.onclick=()=>{document.querySelectorAll('[data-lvl]').forEach(x=>x.classList.remove("active"));c.classList.add("active");lvlFilter=c.dataset.lvl;render();});
document.querySelectorAll('[data-diff]').forEach(c=>c.onclick=()=>{document.querySelectorAll('[data-diff]').forEach(x=>x.classList.remove("active"));c.classList.add("active");diffFilter=c.dataset.diff;render();});
const pickBtn=document.getElementById("pickBtn"),calBox=document.getElementById("cal");
let calRef=new Date(),calCtx=null;
function updatePickBtn(){pickBtn.textContent=pickedDate?("📅 "+pickedDate.slice(5)):"📅 选择日期";}
function studyDateSet(){const s=new Set();const add=(id,baseIso)=>{const d=realDate(get(id),baseIso);if(d)s.add(d);};if(mode==="alg"){ALG.forEach(it=>add(it.id,it.iso));return s;}ITEMS.forEach(it=>add(it.id,it.iso));customList().forEach(c=>add(c.id,""));return s;}
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
  html+='</div>';
  if(calCtx&&calCtx.quick)html+='<div class="cal-quick">'+calCtx.quick.map(n=>'<button data-q="'+n+'">延后'+n+'天</button>').join('')+'</div>';
  html+='<div class="cal-foot"><button id="calToday">今天</button>'+((calCtx&&calCtx.onNone)?'<button id="calNone">'+(calCtx.noneLabel||"清空日期")+'</button>':'')+((calCtx&&calCtx.onClear)?'<button id="calClear">'+(calCtx.clearLabel||"清除")+'</button>':'<span></span>')+'</div>';
  calBox.innerHTML=html;
  calBox.querySelector("#calPrev").onclick=e=>{e.stopPropagation();calRef=new Date(y,m-1,1);renderCal();};
  calBox.querySelector("#calNext").onclick=e=>{e.stopPropagation();calRef=new Date(y,m+1,1);renderCal();};
  calBox.querySelector("#calToday").onclick=e=>{e.stopPropagation();calRef=new Date();renderCal();};
  const cc=calBox.querySelector("#calClear");if(cc)cc.onclick=e=>{e.stopPropagation();calBox.classList.remove("show");calCtx.onClear();};
  const cn=calBox.querySelector("#calNone");if(cn)cn.onclick=e=>{e.stopPropagation();calBox.classList.remove("show");calCtx.onNone();};
  calBox.querySelectorAll(".cal-quick button").forEach(b=>b.onclick=e=>{e.stopPropagation();calBox.classList.remove("show");calCtx.onQuick(+b.dataset.q);});
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
// ===== 学习计时器（正计时：开始/暂停/重置）=====
let timerElapsed=0,timerStart=0,timerRunning=false,timerTick=null;
function fmtTimer(ms){let s=Math.floor(ms/1000);const h=Math.floor(s/3600);s-=h*3600;const m=Math.floor(s/60);s-=m*60;const p=n=>(n+"").padStart(2,"0");return p(h)+":"+p(m)+":"+p(s);}
function renderTimer(){const d=document.getElementById("timerDisp");if(d)d.textContent=fmtTimer(timerElapsed+(timerRunning?Date.now()-timerStart:0));}
function timerToggle(){const btn=document.getElementById("timerToggle"),box=document.getElementById("timerBox");
  if(timerRunning){timerElapsed+=Date.now()-timerStart;timerRunning=false;if(timerTick){clearInterval(timerTick);timerTick=null;}btn.textContent="▶";btn.title="继续";btn.classList.remove("on");box.classList.remove("run");}
  else{timerStart=Date.now();timerRunning=true;btn.textContent="⏸";btn.title="暂停";btn.classList.add("on");box.classList.add("run");if(timerTick)clearInterval(timerTick);timerTick=setInterval(renderTimer,250);}
  renderTimer();}
function timerReset(){timerElapsed=0;timerRunning=false;if(timerTick){clearInterval(timerTick);timerTick=null;}const btn=document.getElementById("timerToggle");if(btn){btn.textContent="▶";btn.title="开始";btn.classList.remove("on");}const box=document.getElementById("timerBox");if(box)box.classList.remove("run");renderTimer();}
document.getElementById("timerToggle").onclick=timerToggle;
document.getElementById("timerReset").onclick=timerReset;
renderTimer();
// ===== 🎯 专注学习/复习：挑一题 → 本题计时 → 到时提示 → 完成/跳过/结束 =====
let focusOn=false,focusTask=null,focusStartMs=0,focusElapsed=0,focusRunning=false,focusTick=null,focusAlerted=false;
const focusSkipped=new Set();
function focusMs(){return focusElapsed+(focusRunning?Date.now()-focusStartMs:0);}
function fmtMS(ms){let s=Math.floor(ms/1000);const h=Math.floor(s/3600);s-=h*3600;const m=Math.floor(s/60);s-=m*60;const p=n=>(n+"").padStart(2,"0");return (h?h+":":"")+p(m)+":"+p(s);}
function focusMinFor(t){return t.isAlg?(t.kind==="review"?EST_MIN.algRev:EST_MIN.algNew):(t.kind==="review"?EST_MIN.guRev:EST_MIN.guNew);}
function focusQueue(){const ti=todayIso();const rev=[],neu=[];
  const push=(id,baseIso,isAlg,q,sec,idx)=>{const o=get(id);if(o.del||o.purged)return;
    const d=realDate(o,baseIso);const reviewDue=!!o.next&&o.next<=ti;
    if(d&&d>ti){if(reviewDue)rev.push({id:id,kind:"review",isAlg:isAlg,q:q,sec:sec,idx:idx});return;}
    const studyDue=!!d&&d<=ti&&!(o.cnt>0);
    if(studyDue)neu.push({id:id,kind:"new",isAlg:isAlg,q:q,sec:sec,idx:idx});
    else if(reviewDue)rev.push({id:id,kind:"review",isAlg:isAlg,q:q,sec:sec,idx:idx});};
  if(mode==="alg"){ALG.forEach(it=>push(it.id,it.iso,true,qText(it),"算法",it.idx));}
  else{ITEMS.forEach(it=>push(it.id,it.iso,false,qText(it),it.sec));customList().forEach(c=>push(c.id,"",false,qText(c),c.sec));}
  return rev.concat(neu);}   // 复习优先，再新学
function renderFocus(){if(!focusOn||!focusTask)return;const el=document.getElementById("focusDisp");if(!el)return;
  const elapsed=focusMs(),allot=focusMinFor(focusTask)*60000;
  el.textContent=fmtMS(elapsed);
  document.getElementById("focusTime").classList.toggle("over",elapsed>=allot);
  if(!focusAlerted&&elapsed>=allot){focusAlerted=true;showFocusTimeup();}}
function focusSetRun(run){const btn=document.getElementById("focusPause");
  if(run&&!focusRunning){focusStartMs=Date.now();focusRunning=true;if(focusTick)clearInterval(focusTick);focusTick=setInterval(renderFocus,250);if(btn)btn.textContent="⏸ 暂停";}
  else if(!run&&focusRunning){focusElapsed+=Date.now()-focusStartMs;focusRunning=false;if(focusTick){clearInterval(focusTick);focusTick=null;}if(btn)btn.textContent="▶ 继续";}
  renderFocus();}
function focusPause(){if(!focusOn)return;focusSetRun(!focusRunning);}
function loadFocusTask(t){focusTask=t;focusStartMs=Date.now();focusElapsed=0;focusRunning=true;focusAlerted=false;
  const pb=document.getElementById("focusPause");if(pb)pb.textContent="⏸ 暂停";
  const k=document.getElementById("focusKind");k.textContent=t.kind==="review"?"🔁 复习":"🆕 新学";k.className="fp-kind "+t.kind;
  document.getElementById("focusQ").textContent=(t.sec?("["+t.sec+"] "):"")+t.q;
  document.getElementById("focusAllot").textContent="/ 建议 "+fmtMS(focusMinFor(t)*60000);
  if(focusTick)clearInterval(focusTick);focusTick=setInterval(renderFocus,250);renderFocus();}
function focusNext(){const q=focusQueue().filter(t=>!focusSkipped.has(t.id));
  if(!q.length){const skipped=focusSkipped.size;endFocus();toast(skipped?"剩下的都跳过了，专注结束":"🎉 今日任务已全部完成");return;}
  loadFocusTask(q[0]);}
function updateFocusBtn(){const b=document.getElementById("focusBtn");if(!b)return;const none=!focusOn&&focusQueue().length===0;b.disabled=none;b.title=none?"今天没有待办任务，暂时不用专注":"从今日任务里挑一题、按建议时长开始专注学习/复习";}
function startFocus(){focusSkipped.clear();if(!focusQueue().length){toast("🎉 今日任务已全部完成");return;}
  focusOn=true;document.getElementById("focusPanel").style.display="";document.getElementById("focusBtn").classList.add("pri");focusNext();}
function endFocus(){focusOn=false;focusTask=null;focusRunning=false;if(focusTick){clearInterval(focusTick);focusTick=null;}
  const p=document.getElementById("focusPanel");if(p)p.style.display="none";
  const b=document.getElementById("focusBtn");if(b)b.classList.remove("pri");
  document.getElementById("focusModal").classList.remove("show");updateFocusBtn();}
function focusComplete(){if(!focusTask)return;const o=get(focusTask.id);o.cnt=(o.cnt||0)+1;o.last=today();o.next=focusTask.isAlg?schedNextAlg(o.cnt,focusTask.idx):schedNext(o.cnt);save();render();toast("✓ 已完成，下一题");focusNext();}
function focusSkip(){if(!focusTask)return;focusSkipped.add(focusTask.id);focusNext();}
function showFocusTimeup(){focusSetRun(false);const m=document.getElementById("focusModalMsg");if(m&&focusTask)m.textContent="「"+focusTask.q+"」的建议用时 "+focusMinFor(focusTask)+" 分钟已到（计时已暂停）。可以继续复习这一题、进入下一题，或停止。";document.getElementById("focusModal").classList.add("show");}
function resetFiltersForJump(){secFilter="all";lvlFilter="all";diffFilter="all";dateFilter="all";pickedDate="";starOnly=false;
  buildFilters();
  document.querySelectorAll('[data-lvl]').forEach(x=>x.classList.toggle("active",x.dataset.lvl==="all"));
  document.querySelectorAll('[data-diff]').forEach(x=>x.classList.toggle("active",x.dataset.diff==="all"));
  document.querySelectorAll('[data-date]').forEach(x=>x.classList.toggle("active",x.dataset.date==="all"));
  const sf=document.getElementById("starFilter");if(sf)sf.classList.remove("active");updatePickBtn();}
function jumpToFocusItem(){if(!focusOn||!focusTask)return;const id=focusTask.id;openIds.add(id);render();
  let row=document.querySelector('tr[data-id="'+id+'"]');
  if(!row){resetFiltersForJump();openIds.add(id);render();row=document.querySelector('tr[data-id="'+id+'"]');}
  if(row)row.scrollIntoView({behavior:"smooth",block:"center"});}
document.getElementById("focusQ").onclick=jumpToFocusItem;
document.getElementById("focusBtn").onclick=()=>{if(focusOn)endFocus();else startFocus();};
document.getElementById("focusDone").onclick=focusComplete;
document.getElementById("focusPause").onclick=focusPause;
document.getElementById("focusSkip").onclick=focusSkip;
document.getElementById("focusStop").onclick=endFocus;
document.getElementById("focusStopBtn").onclick=endFocus;
document.getElementById("focusStayBtn").onclick=()=>{document.getElementById("focusModal").classList.remove("show");focusSetRun(true);};
document.getElementById("focusNextBtn").onclick=()=>{document.getElementById("focusModal").classList.remove("show");focusComplete();};
function todayCount(){const ti=todayIso();let n=0;const chk=(id,baseIso)=>{const o=get(id);if(o.del||o.purged)return;const d=realDate(o,baseIso);const rd=!!o.next&&o.next<=ti;if(d&&d>ti){if(rd)n++;return;}const sd=!!d&&d<=ti&&!(o.cnt>0);if(sd||rd)n++;};if(mode==="alg"){ALG.forEach(it=>chk(it.id,it.iso));return n;}ITEMS.forEach(it=>chk(it.id,it.iso));customList().forEach(c=>chk(c.id,""));return n;}
// ---- 今日剩余任务估时（八股/算法 · 新学/复习 分类，跨两个模式统计）----
const EST_MIN={guNew:10,guRev:4,algNew:25,algRev:10};   // 单题分钟数
function taskBreakdown(){const ti=todayIso();const b={guNew:0,guRev:0,algNew:0,algRev:0};
  const chk=(id,baseIso,isAlg)=>{const o=get(id);if(o.del||o.purged)return;
    const d=realDate(o,baseIso);const rd=!!o.next&&o.next<=ti;
    if(d&&d>ti){if(rd){if(isAlg)b.algRev++;else b.guRev++;}return;}
    const sd=!!d&&d<=ti&&!(o.cnt>0);
    if(sd){if(isAlg)b.algNew++;else b.guNew++;}
    else if(rd){if(isAlg)b.algRev++;else b.guRev++;}};
  ITEMS.forEach(it=>chk(it.id,it.iso,false));customList().forEach(c=>chk(c.id,"",false));
  ALG.forEach(it=>chk(it.id,it.iso,true));return b;}
function fmtDur(m){m=Math.round(m);if(m<=0)return "0 分钟";const h=Math.floor(m/60),mm=m%60;return (h?h+" 小时":"")+(h&&mm?" ":"")+(mm?mm+" 分钟":"");}
function updateEstimate(){const el=document.getElementById("estLine");if(!el)return;
  const b=taskBreakdown();
  const guMin=b.guNew*EST_MIN.guNew+b.guRev*EST_MIN.guRev;
  const algMin=b.algNew*EST_MIN.algNew+b.algRev*EST_MIN.algRev;
  const total=guMin+algMin;
  if(total<=0){el.className="est none";el.innerHTML="⏱ 今日任务已全部完成，休息一下 🎉";return;}
  el.className="est";
  el.innerHTML="<span class='estlabel'>⏱ 完成今日剩余任务还需：</span>"
    +"<span class='estseg'>八股 "+fmtDur(guMin)+"<span class='estsub'>新学"+b.guNew+"·复习"+b.guRev+"</span></span>"
    +"<span class='estseg'>算法 "+fmtDur(algMin)+"<span class='estsub'>新学"+b.algNew+"·复习"+b.algRev+"</span></span>"
    +"<span class='esttot'>合计 "+fmtDur(total)+"</span>";}
function passDate(it){if(dateFilter==="all")return true;if(dateFilter==="todayall"){const ti=todayIso();const o=get(it.id);const d=itemDate(it);const reviewDue=!!o.next&&o.next<=ti;if(d&&d>ti)return reviewDue;const studyDue=!!d&&d<=ti&&!(o.cnt>0);const doneToday=o.last===today();return studyDue||reviewDue||doneToday;}if(dateFilter==="review"){const nx=get(it.id).next;return !!nx&&nx<=todayIso();}if(dateFilter==="pick"){const d=itemDate(it),nx=get(it.id).next;return d===pickedDate||nx===pickedDate;}const d=itemDate(it);if(!d)return false;return d===(dateFilter==="today"?todayIso():tomorrowIso());}
function customList(){return state.__custom||(state.__custom=[]);}
function sectionMap(){const map={};SECTIONS.forEach(s=>map[s]=[]);
  ITEMS.forEach(it=>{(map[it.sec]||(map[it.sec]=[])).push({id:it.id,sec:it.sec,q:it.q,baseIso:it.iso,tags:it.tags,anc:it.anc,jg:it.jg});});
  customList().forEach(c=>{(map[c.sec]||(map[c.sec]=[])).push({id:c.id,sec:c.sec,q:c.q,baseIso:"",custom:true,tags:[]});});
  Object.keys(map).forEach(s=>map[s].forEach((it,i)=>it.idx=i+1));return map;}
// date==="none" 表示手动清空为「未分配」，不再回落到默认建议日期
function realDate(o,baseIso){if(o.date==="none")return "";return (o.date!==undefined&&o.date!=="")?o.date:(baseIso||"");}
function itemDate(it){return realDate(get(it.id),it.baseIso);}
let mode=localStorage.getItem("mode_v1")||"gu";
function mountEd(host,getv,setv,ph){if(window.MDEditor){editors.push(window.MDEditor(host,getv()||"",(html)=>{setv(html);save();}));}else{host.innerHTML='<textarea class="fa" placeholder="'+(ph||"")+'"></textarea>';const ta=host.querySelector(".fa");ta.value=getv()||"";ta.oninput=()=>{setv(ta.value);save();};}}
function renderAlg(tb){
  const sr=document.createElement("tr");sr.className="sec-row";sr.innerHTML='<td colspan="6">算法 · CodeTop 高频 Top 100</td>';tb.appendChild(sr);
  const DL=["","简单","中等","困难"];
  const list=ALG.map(it=>Object.assign({},it,{baseIso:it.iso})).filter(it=>{const o=get(it.id);if(lvlFilter!=="all"&&o.lvl!=lvlFilter)return false;if(diffFilter!=="all"&&it.lv!=diffFilter)return false;if(starOnly&&!o.star)return false;if(!passDate(it))return false;return true;});
  {const tc=document.querySelector('[data-date="todayall"]');if(tc)tc.textContent="📌 今天任务："+todayCount();}
  updateEstimate();updateFocusBtn();
  list.forEach(it=>{const st=get(it.id);
    const opened=openIds.has(it.id);
    const hasStuff=(st.codes&&st.codes.some(c=>(c.code||c)&&(c.code||c).trim&&(c.code||c).trim()))||(st.memo&&st.memo.trim());
    const tr=document.createElement("tr");tr.dataset.id=it.id;
    tr.innerHTML='<td class="c">'+it.idx+'</td>'+
      '<td class="c hide-sm date">'+(fmtIso(itemDate(it))||'<span style="color:#bbb">＋日期</span>')+'</td>'+
      '<td class="q"><span class="star'+(st.star?' on':'')+'" title="收藏">'+(st.star?'★':'☆')+'</span><span class="qbtn'+(hasStuff?' has':'')+'"><span class="arw">'+(opened?'▾':'▸')+'</span>'+esc(it.q)+'</span><span class="dtag d'+it.lv+'">'+DL[it.lv]+'</span><span class="tag">'+esc(it.tag)+'</span><a class="tag lc" href="https://leetcode.cn/problems/'+it.slug+'/" target="_blank" rel="noopener" title="在力扣打开这道题">LC '+esc(it.num)+' ↗</a></td>'+
      '<td class="c"><button class="lvl l'+st.lvl+'">'+LVLS[st.lvl]+'</button></td>'+
      '<td class="c"><span class="cnt"><button class="minus">−</button><b>'+st.cnt+'</b><button class="plus">＋</button></span></td>'+
      '<td class="c hide-sm last">'+(st.last||"—")+(st.next?' <span class="revdate" title="点击调整/延后复习" style="font-size:11px;cursor:pointer;color:'+(st.next<=todayIso()?"#dc2626":"#9ca3af")+'">↻'+st.next.slice(5)+'</span>':'')+'</td>';
    const dc=tr.querySelector(".date");
    dc.onclick=e=>{e.stopPropagation();openCal(dc,{selected:itemDate(it),dot:true,clearLabel:"恢复默认",noneLabel:"清空日期",
      onPick:iso=>{get(it.id).date=iso;save();render();},
      onNone:()=>{get(it.id).date="none";save();render();},
      onClear:()=>{delete get(it.id).date;save();render();}});};
    tr.querySelector(".star").onclick=e=>{e.stopPropagation();st.star=!st.star;save();render();};
    tr.querySelector(".qbtn").onclick=()=>{opened?openIds.delete(it.id):openIds.add(it.id);render();};
    tr.querySelector(".lvl").onclick=()=>{st.lvl=(st.lvl+1)%4;save();render();};
    tr.querySelector(".plus").onclick=()=>{st.cnt++;st.last=today();st.next=schedNextAlg(st.cnt,it.idx);save();render();if(focusOn&&focusTask&&focusTask.id===it.id){toast("✓ 已完成，下一题");focusNext();}};
    tr.querySelector(".minus").onclick=()=>{if(st.cnt>0){st.cnt--;if(st.cnt>0)st.next=schedNextAlg(st.cnt,it.idx);else delete st.next;}save();render();};
    const rv=tr.querySelector(".revdate");
    if(rv)rv.onclick=e=>{e.stopPropagation();openCal(rv,{selected:st.next,dot:false,clearLabel:"移出复习",quick:[3,7,14],
      onPick:iso=>{st.next=iso;save();render();},
      onClear:()=>{delete st.next;save();render();},
      onQuick:n=>{st.next=addDays(st.next||todayIso(),n);save();render();}});};
    tb.appendChild(tr);
    if(opened){
      const er=document.createElement("tr");er.className="ed-row";
      const td=document.createElement("td");td.colSpan=6;const o=st;
      if(o.codes)o.codes=o.codes.map(c=>typeof c==="string"?{code:c}:c);
      if(!o.codes||!o.codes.length)o.codes=[{code:""}];
      let bar='<div class="ehint">';
      bar+=(!o.memoOn)?'<button class="ebtn addmemo">＋ 助记</button>':'';
      bar+='<button class="ebtn addcode">＋ 代码</button>';
      bar+='</div>';
      let body='';
      if(o.memoOn){
        if(o.memoHide){const mf=plainFirstLine(o.memo);body+='<div class="memo-folded"><button class="memofold memobtn">▸</button><button class="memodel memobtn">✕</button>💡 助记'+(mf?'：'+esc(mf):'')+'</div>';}
        else body+='<div class="memo-label">💡 助记</div><div class="memowrap"><button class="memofold memobtn" title="隐藏助记">▾</button><button class="memodel memobtn" title="删除助记">✕</button><div class="tui-memo"></div></div>';
      }
      body+='<div class="codebox"></div>';
      td.innerHTML=bar+body;
      const addb=td.querySelector(".addmemo");if(addb)addb.onclick=()=>{o.memoOn=true;o.memoHide=false;save();render();};
      const delMemo=()=>confirmDlg("删除助记？",()=>{o.memoOn=false;delete o.memo;o.memoHide=false;save();render();});
      const mw=td.querySelector(".memowrap");
      if(mw){mw.querySelector(".memofold").onclick=e=>{e.stopPropagation();o.memoHide=true;save();render();};mw.querySelector(".memodel").onclick=e=>{e.stopPropagation();delMemo();};}
      const mfold=td.querySelector(".memo-folded");
      if(mfold){mfold.querySelector(".memodel").onclick=e=>{e.stopPropagation();delMemo();};mfold.onclick=e=>{if(e.target.closest(".memodel"))return;o.memoHide=false;save();render();};}
      td.querySelector(".addcode").onclick=()=>{o.codes=o.codes||[];o.codes.push({code:""});save();render();};
      er.appendChild(td);tb.appendChild(er);
      if(o.memoOn&&!o.memoHide)mountEd(td.querySelector(".tui-memo"),()=>o.memo,v=>o.memo=v,"写思路/口诀…");
      renderCodes(td.querySelector(".codebox"),o,true);
    }
  });
  let done=0,fam=0;ALG.forEach(it=>{const l=get(it.id).lvl;if(l>=2)done++;else if(l==1)fam++;});
  const tot=ALG.length,pct=tot?Math.round(done/tot*100):0,fpct=tot?Math.round(fam/tot*100):0;
  document.getElementById("pbar").style.width=pct+"%";
  document.getElementById("pbar2").style.width=fpct+"%";
  document.getElementById("stat").innerHTML="已掌握(能讲框架+能扛追问)：<b>"+done+"</b> / "+tot+"　("+pct+"%)　·　<span style='color:#d97706'>眼熟 "+fam+"</span>";
}
function render(){const tb=document.getElementById("tb");
  const _sy=window.scrollY;
  editors.forEach(e=>{try{e.destroy();}catch(_){}});editors=[];
  tb.innerHTML="";
  if(mode==="alg"){renderAlg(tb);window.scrollTo(0,_sy);requestAnimationFrame(()=>window.scrollTo(0,_sy));return;}
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
        tr.querySelector(".purge").onclick=()=>{confirmDlg("永久删除这道题？不可恢复",()=>{if(it.custom){state.__custom=customList().filter(c=>c.id!==it.id);delete state[it.id];}else{const o=get(it.id);delete o.del;o.purged=true;}save();render();});};
        tb.appendChild(tr);});
      return;
    }
    list.forEach(it=>{const st=get(it.id);
      const opened=openIds.has(it.id), hasNote=st.note&&st.note.trim();
      const tr=document.createElement("tr");tr.dataset.id=it.id;
      tr.innerHTML='<td class="c">'+it.idx+'</td>'+
        '<td class="c hide-sm date">'+(fmtIso(itemDate(it))||'<span style="color:#bbb">＋日期</span>')+'</td>'+
        '<td class="q"><span class="star'+(st.star?' on':'')+'" title="收藏">'+(st.star?'★':'☆')+'</span><span class="qbtn'+(hasNote?' has':'')+'"><span class="arw">'+(opened?'▾':'▸')+'</span>'+esc(qText(it))+(it.custom?' <span style="color:#9333ea;font-size:11px">·自建</span>':'')+'</span>'+((it.tags||[]).map(t=>'<span class="tag">'+esc(t)+'</span>').join(''))+(function(u){if(!u)return '';const jg=/javaguide\.cn/.test(u);return '<a class="tag lc" href="'+u+'" target="_blank" rel="noopener" title="'+(jg?'在 JavaGuide 打开这一题':'在小林coding打开这一题')+'">'+(jg?'JavaGuide':'小林')+' ↗</a>';})(xlLink(it.sec,it.tags,it.anc))+(it.jg?'<a class="tag lc" href="'+it.jg+'" target="_blank" rel="noopener" title="在 JavaGuide 打开这一题">JavaGuide ↗</a>':'')+'<span class="qedit" title="编辑题目">✎</span></td>'+
        '<td class="c"><button class="lvl l'+st.lvl+'">'+LVLS[st.lvl]+'</button></td>'+
        '<td class="c"><span class="cnt"><button class="minus">−</button><b>'+st.cnt+'</b><button class="plus">＋</button></span></td>'+
        '<td class="c hide-sm last">'+(st.last||"—")+(st.next?' <span class="revdate" title="点击调整/延后复习" style="font-size:11px;cursor:pointer;color:'+(st.next<=todayIso()?"#dc2626":"#9ca3af")+'">↻'+st.next.slice(5)+'</span>':'')+'</td>';
      const dc=tr.querySelector(".date");
      dc.onclick=e=>{e.stopPropagation();openCal(dc,{selected:itemDate(it),dot:true,clearLabel:"恢复默认",noneLabel:"清空日期",
        onPick:iso=>{get(it.id).date=iso;save();render();},
        onNone:()=>{get(it.id).date="none";save();render();},
        onClear:()=>{delete get(it.id).date;save();render();}});};
      const rv=tr.querySelector(".revdate");
      if(rv)rv.onclick=e=>{e.stopPropagation();openCal(rv,{selected:st.next,dot:false,clearLabel:"移出复习",quick:[3,7,14],
        onPick:iso=>{st.next=iso;save();render();},
        onClear:()=>{delete st.next;save();render();},
        onQuick:n=>{st.next=addDays(st.next||todayIso(),n);save();render();}});};
      tr.querySelector(".star").onclick=e=>{e.stopPropagation();st.star=!st.star;save();render();};
      tr.querySelector(".qedit").onclick=e=>{e.stopPropagation();const cell=tr.querySelector(".q");cell.innerHTML='<input class="qin">';const inp=cell.querySelector(".qin");inp.value=qText(it);inp.focus();const commit=()=>{const v=inp.value.trim();if(v)get(it.id).q=v;save();render();};inp.onkeydown=ev=>{if(ev.key==="Enter")commit();else if(ev.key==="Escape")render();};inp.onblur=commit;};
      tr.querySelector(".qbtn").onclick=()=>{opened?openIds.delete(it.id):openIds.add(it.id);render();};
      tr.querySelector(".lvl").onclick=()=>{st.lvl=(st.lvl+1)%4;save();render();};
      tr.querySelector(".plus").onclick=()=>{st.cnt++;st.last=today();st.next=schedNext(st.cnt);save();render();if(focusOn&&focusTask&&focusTask.id===it.id){toast("✓ 已完成，下一题");focusNext();}};
      tr.querySelector(".minus").onclick=()=>{if(st.cnt>0){st.cnt--;if(st.cnt>0)st.next=schedNext(st.cnt);else delete st.next;}save();render();};
      tb.appendChild(tr);
      if(opened){
        const er=document.createElement("tr");er.className="ed-row";
        const td=document.createElement("td");td.colSpan=6;const o=st;
        if(o.code!==undefined&&!o.codes){o.codes=o.code?[{code:o.code}]:[];delete o.code;delete o.codeOn;delete o.codeHide;}
        if(o.codes)o.codes=o.codes.map(c=>typeof c==="string"?{code:c}:c);
        let bar='<div class="ehint">';
        bar+=(!o.memoOn)?'<button class="ebtn addmemo">＋ 助记</button>':'';
        bar+='<button class="ebtn addcode">＋ 代码</button>';
        bar+='<button class="del">🗑 删除</button></div>';
        let body='';
        if(o.memoOn){
          if(o.memoHide){const mf=plainFirstLine(o.memo);body+='<div class="memo-folded"><button class="memofold memobtn">▸</button><button class="memodel memobtn">✕</button>💡 助记'+(mf?'：'+esc(mf):'')+'</div>';}
          else body+='<div class="memo-label">💡 助记</div><div class="memowrap"><button class="memofold memobtn" title="隐藏助记">▾</button><button class="memodel memobtn" title="删除助记">✕</button><div class="tui-memo"></div></div>';
        }
        if(o.noteHide)body+='<div class="note-folded"><button class="notefold notebtn" title="显示答案">▸</button>📝 答案已隐藏</div>';
        else body+='<div class="notewrap"><button class="notefold notebtn" title="隐藏答案">▾</button><div class="tui"></div></div>';
        if(o.codes&&o.codes.length)body+='<div class="codebox"></div>';
        td.innerHTML=bar+body;
        const addb=td.querySelector(".addmemo");if(addb)addb.onclick=()=>{o.memoOn=true;o.memoHide=false;save();render();};
        const delMemo=()=>confirmDlg("删除助记？",()=>{o.memoOn=false;delete o.memo;o.memoHide=false;save();render();});
        const mw=td.querySelector(".memowrap");
        if(mw){mw.querySelector(".memofold").onclick=e=>{e.stopPropagation();o.memoHide=true;save();render();};mw.querySelector(".memodel").onclick=e=>{e.stopPropagation();delMemo();};}
        const mfold=td.querySelector(".memo-folded");
        if(mfold){mfold.querySelector(".memodel").onclick=e=>{e.stopPropagation();delMemo();};mfold.onclick=e=>{if(e.target.closest(".memodel"))return;o.memoHide=false;save();render();};}
        td.querySelector(".addcode").onclick=()=>{o.codes=o.codes||[];o.codes.push({code:""});save();render();};
        const nw=td.querySelector(".notewrap");if(nw)nw.querySelector(".notefold").onclick=e=>{e.stopPropagation();o.noteHide=true;save();render();};
        const nfold=td.querySelector(".note-folded");if(nfold)nfold.onclick=()=>{o.noteHide=false;save();render();};
        td.querySelector(".del").onclick=()=>{get(it.id).del=true;openIds.delete(it.id);save();render();};
        er.appendChild(td);tb.appendChild(er);
        const mount=(host,getv,setv,ph)=>{if(window.MDEditor){editors.push(window.MDEditor(host,getv()||"",(html)=>{setv(html);save();}));}else{host.innerHTML='<textarea class="fa" placeholder="'+(ph||"")+'"></textarea>';const ta=host.querySelector(".fa");ta.value=getv()||"";ta.oninput=()=>{setv(ta.value);save();};}};
        if(o.memoOn&&!o.memoHide)mount(td.querySelector(".tui-memo"),()=>o.memo,v=>o.memo=v,"写助记/口诀…");
        if(!o.noteHide)mount(td.querySelector(".tui"),()=>st.note,v=>st.note=v,"# 在这里写你总结的答案…");
        if(o.codes&&o.codes.length)renderCodes(td.querySelector(".codebox"),o);
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
  let done=0,fam=0;base.forEach(it=>{const l=get(it.id).lvl;if(l>=2)done++;else if(l==1)fam++;});
  const tot=base.length,pct=tot?Math.round(done/tot*100):0,fpct=tot?Math.round(fam/tot*100):0;
  document.getElementById("pbar").style.width=pct+"%";
  document.getElementById("pbar2").style.width=fpct+"%";
  const GOAL=60;
  document.getElementById("stat").innerHTML="已掌握(能讲框架+能扛追问)：<b>"+done+"</b> / "+tot+"　("+pct+"%)　·　<span style='color:#d97706'>眼熟 "+fam+"</span>　·　"+(pct>=GOAL?"<span style='color:#16a34a'>✅ 已过可投递线，可以开始投面试</span>":"<span style='color:#dc2626'>距可投递线(60%)还差 "+(GOAL-pct)+"%</span>");
  if(dateFilter==="todayall")saveStuck();
  {const tc=document.querySelector('[data-date="todayall"]');if(tc)tc.textContent="📌 今天任务："+todayCount();}
  updateEstimate();updateFocusBtn();
  window.scrollTo(0,_sy);requestAnimationFrame(()=>window.scrollTo(0,_sy));}
const modal=document.getElementById("modal");
document.getElementById("cfgBtn").onclick=()=>{if(cfg){document.getElementById("supaUrl").value=cfg.url;document.getElementById("supaKey").value=cfg.key;}document.getElementById("imgKey").value=imgKey;modal.classList.add("show");};
document.getElementById("cfgCancel").onclick=()=>modal.classList.remove("show");
document.getElementById("cfgClear").onclick=()=>{cfg=null;localStorage.removeItem(CFGKEY);setPill("未配置云同步");modal.classList.remove("show");};
document.getElementById("cfgSave").onclick=async()=>{const b=document.getElementById("supaUrl").value.trim().replace(/\\/$/,""),k=document.getElementById("supaKey").value.trim(),ik=document.getElementById("imgKey").value.trim();
  imgKey=ik;if(ik)localStorage.setItem("imgbb_key",ik);else localStorage.removeItem("imgbb_key");
  if(b&&k){cfg={url:b,key:k};localStorage.setItem(CFGKEY,JSON.stringify(cfg));modal.classList.remove("show");await pull();await push();return;}
  if(b||k){toast("Project URL 和 anon key 需要一起填写");return;}
  modal.classList.remove("show");};
document.getElementById("pull").onclick=async()=>{if(!cfg){toast("请先配置云同步");return;}
  if(dirty){confirmDlg("本机还有未同步的改动，拉取会用云端内容覆盖它们，确定吗？",()=>pull(true));return;}
  try{const c=await cloudGet();if(c&&revOf(c)<revOf(state)){confirmDlg("云端的内容比本机旧，拉取会覆盖本机较新的进度，确定吗？",()=>pull(true));return;}}catch(e){}
  pull(true);};
document.getElementById("push").onclick=push;
document.getElementById("reset").onclick=()=>{confirmDlg("清空本机进度？若已配置云同步，请之后点上传覆盖云端",()=>{state={};save();render();});};
// ===== 进度备份（本设备）=====
const BKEY="backups_v1";
function loadBackups(){try{return JSON.parse(localStorage.getItem(BKEY)||"[]");}catch(e){return [];}}
function saveBackups(a){try{localStorage.setItem(BKEY,JSON.stringify(a));}catch(e){toast("备份存储已满，请删除旧备份或导出后删除");}}
function fmtTs(ts){const d=new Date(ts),p=n=>(n+"").padStart(2,"0");return (d.getMonth()+1)+"-"+d.getDate()+" "+p(d.getHours())+":"+p(d.getMinutes());}
function progCount(s){try{return Object.keys(JSON.parse(s)).filter(k=>!k.startsWith("__")).length;}catch(e){return 0;}}
function renderBackups(){const a=loadBackups(),box=document.getElementById("bkList");
  if(!a.length){box.innerHTML='<div style="color:#9ca3af;font-size:13px;padding:8px">还没有备份，点上面「新建备份」</div>';return;}
  box.innerHTML=a.map((b,i)=>'<div class="bk-item"><div class="meta"><div>'+(esc(b.label)||"备份")+'</div><div class="t">'+fmtTs(b.ts)+' · '+progCount(b.data)+' 题有记录</div></div><button class="rb" data-i="'+i+'">恢复</button><button class="xb" data-i="'+i+'">导出</button><button class="db" data-i="'+i+'">删除</button></div>').join("");
  box.querySelectorAll(".rb").forEach(b=>b.onclick=()=>{const i=+b.dataset.i;confirmDlg("恢复到这个备份？当前进度会被覆盖",async()=>{const a=loadBackups();restoring=true;try{const keep=bkIndex();const snap=JSON.parse(a[i].data);snap.__bkIndex=keep;state=snap;touchRev();localStorage.setItem(KEY,JSON.stringify(state));render();bkModal.classList.remove("show");clearTimeout(timer);if(cfg){await cloudPut();setDirty(false);setPill("已恢复 "+nowt(),"ok");}}catch(e){toast("备份损坏");}restoring=false;});});
  box.querySelectorAll(".db").forEach(b=>b.onclick=()=>{const i=+b.dataset.i,a=loadBackups();a.splice(i,1);saveBackups(a);renderBackups();});
  box.querySelectorAll(".xb").forEach(b=>b.onclick=()=>{const i=+b.dataset.i,a=loadBackups();const blob=new Blob([a[i].data],{type:"application/json"});const x=document.createElement("a");x.href=URL.createObjectURL(blob);x.download="打卡备份-"+a[i].ts+".json";x.click();});
}
// ---- 缩减今日任务：把未完成的一部分挪到未来 ----
function todayTaskItems(){const ti=todayIso();const res=[];
  const chk=(id,baseIso)=>{const o=get(id);if(o.del||o.purged)return;const d=realDate(o,baseIso);if(d&&d>ti)return;const reviewDue=!!o.next&&o.next<=ti;const studyDue=!!d&&d<=ti&&!(o.cnt>0);if(studyDue||reviewDue)res.push({id:id,reviewDue:reviewDue});};
  if(mode==="alg"){ALG.forEach(it=>chk(it.id,it.iso));return res;}
  ITEMS.forEach(it=>chk(it.id,it.iso));customList().forEach(c=>chk(c.id,""));return res;}
const trimModal=document.getElementById("trimModal");
let trimType="all";
const TT_LABEL={all:"全部",study:"新学习",review:"复习"};
function trimListBy(t){let l=todayTaskItems();if(t==="study")l=l.filter(x=>!x.reviewDue);else if(t==="review")l=l.filter(x=>x.reviewDue);return l;}
function trimRefreshChips(){document.querySelectorAll("#trimModal [data-tt]").forEach(ch=>{ch.classList.toggle("active",ch.dataset.tt===trimType);ch.textContent=TT_LABEL[ch.dataset.tt]+" "+trimListBy(ch.dataset.tt).length;});}
document.getElementById("trimBtn").onclick=()=>{trimRefreshChips();trimModal.classList.add("show");};
document.getElementById("trimCancel").onclick=()=>trimModal.classList.remove("show");
document.querySelectorAll("#trimModal [data-tt]").forEach(ch=>ch.onclick=()=>{trimType=ch.dataset.tt;trimRefreshChips();});
document.querySelectorAll("#trimModal [data-trim]").forEach(btn=>btn.onclick=()=>{
  const frac=parseFloat(btn.dataset.trim),N={"0.25":2,"0.5":4,"0.75":6}[btn.dataset.trim]||2;
  const list=trimListBy(trimType),total=list.length,toMove=Math.round(total*frac);
  if(toMove<=0){toast("没有可缩减的"+(trimType==="all"?"":TT_LABEL[trimType])+"任务");return;}
  const moving=[];for(let j=0;j<toMove;j++)moving.push(list[Math.floor((j+0.5)*total/toMove)]);  // 等距采样均匀缩减
  moving.forEach((m,k)=>{const off=(k%N)+1,o=get(m.id);if(m.reviewDue)o.next=addDays(todayIso(),off);else o.date=addDays(todayIso(),off);});
  save();render();trimModal.classList.remove("show");
});
const bkModal=document.getElementById("bkModal");
// ---- 云端备份：每个备份单独一个小仓库，主进度只存索引（不会撑爆主仓库）----
function bkIndex(){return state.__bkIndex||(state.__bkIndex=[]);}
function renderCloud(){const box=document.getElementById("bkCloudList");
  if(!cfg){box.innerHTML='<div style="color:#9ca3af;font-size:13px;padding:8px">配置「☁️ 云同步」后可用</div>';return;}
  const a=bkIndex();
  if(!a.length){box.innerHTML='<div style="color:#9ca3af;font-size:13px;padding:8px">还没有云端备份，点上方「☁️ 云端备份」创建</div>';return;}
  box.innerHTML=a.map((b,i)=>'<div class="bk-item"><div class="meta"><div>'+(esc(b.label)||"备份")+'</div><div class="t">'+fmtTs(b.ts)+'</div></div><button class="rb" data-i="'+i+'">恢复</button><button class="cvt" data-i="'+i+'" title="转为本地备份，云端这份会删除">转为本地</button><button class="db" data-i="'+i+'">删除</button></div>').join("");
  box.querySelectorAll(".cvt").forEach(btn=>btn.onclick=async()=>{const i=+btn.dataset.i,b=bkIndex()[i];
    btn.disabled=true;btn.textContent="转换中…";
    try{
      const r=await fetch(api("checkin?id=eq."+encodeURIComponent(b.bin)+"&select=data"),{headers:H()});if(!r.ok)throw 0;
      const arr=await r.json();if(!arr.length)throw 0;
      const la=loadBackups();la.unshift({ts:b.ts,label:b.label,data:JSON.stringify(arr[0].data)});if(la.length>30)la.length=30;
      saveBackups(la);
      if(!loadBackups().some(x=>x.ts===b.ts)){toast("本地空间不足，转换失败");btn.disabled=false;btn.textContent="转为本地";return;}
      bkIndex().splice(i,1);save();
      try{await fetch(api("checkin?id=eq."+encodeURIComponent(b.bin)),{method:"DELETE",headers:H()});}catch(e){}
      renderBackups();renderCloud();toast("已转为本地备份");
    }catch(e){toast("转换失败，检查网络");btn.disabled=false;btn.textContent="转为本地";}
  });
  box.querySelectorAll(".rb").forEach(btn=>btn.onclick=()=>{const i=+btn.dataset.i,b=bkIndex()[i];confirmDlg("恢复到这个云端备份？当前进度会被覆盖",async()=>{restoring=true;try{const r=await fetch(api("checkin?id=eq."+encodeURIComponent(b.bin)+"&select=data"),{headers:H()});if(!r.ok)throw 0;const a=await r.json();if(!a.length)throw 0;const snap=a[0].data;snap.__bkIndex=bkIndex();state=snap;touchRev();localStorage.setItem(KEY,JSON.stringify(state));render();bkModal.classList.remove("show");clearTimeout(timer);if(cfg){await cloudPut();setDirty(false);setPill("已恢复 "+nowt(),"ok");}}catch(e){toast("恢复失败，检查网络");}restoring=false;});});
  box.querySelectorAll(".db").forEach(btn=>btn.onclick=async()=>{const i=+btn.dataset.i,b=bkIndex()[i];bkIndex().splice(i,1);save();renderCloud();try{await fetch(api("checkin?id=eq."+encodeURIComponent(b.bin)),{method:"DELETE",headers:H()});}catch(e){}});
}
document.getElementById("backupBtn").onclick=()=>{renderBackups();renderCloud();bkModal.classList.add("show");};
document.getElementById("bkClose").onclick=()=>bkModal.classList.remove("show");
document.getElementById("bkImportBtn").onclick=()=>document.getElementById("bkImport").click();
document.getElementById("bkNew").onclick=()=>{const a=loadBackups();a.unshift({ts:Date.now(),label:document.getElementById("bkLabel").value.trim(),data:JSON.stringify(state)});if(a.length>30)a.length=30;saveBackups(a);document.getElementById("bkLabel").value="";renderBackups();};
async function doCloudBackup(old){const btn=document.getElementById("bkNewCloud");btn.disabled=true;btn.textContent="备份中…";
  try{const snap=Object.assign({},state);delete snap.__bkIndex;delete snap.__backups;
    const lbl=document.getElementById("bkLabel").value.trim();
    const rid="bk_"+Date.now();
    const r=await fetch(api("checkin"),{method:"POST",headers:H({"Content-Type":"application/json","Prefer":"return=minimal"}),body:JSON.stringify([{id:rid,kind:"backup",label:lbl,data:snap}])});if(!r.ok)throw 0;
    if(old&&old.bin!==rid){try{await fetch(api("checkin?id=eq."+encodeURIComponent(old.bin)),{method:"DELETE",headers:H()});}catch(e){}}
    state.__bkIndex=[{ts:Date.now(),label:lbl,bin:rid}];
    document.getElementById("bkLabel").value="";save();renderCloud();toast(old?"已覆盖云端备份":"云端备份完成");}
  catch(e){toast("云端备份失败，检查网络/配置");}
  btn.disabled=false;btn.textContent="☁️ 云端备份";}
document.getElementById("bkNewCloud").onclick=()=>{if(!cfg){toast("请先配置「☁️ 云同步」");return;}
  const old=bkIndex()[0];
  if(old)confirmDlg("云端只保留 1 份备份。新建会覆盖现有的（"+fmtTs(old.ts)+"），确定吗？",()=>doCloudBackup(old));
  else doCloudBackup(null);};
document.getElementById("bkImport").onchange=function(){const f=this.files[0];if(!f)return;const r=new FileReader();r.onload=()=>{try{JSON.parse(r.result);const a=loadBackups();a.unshift({ts:Date.now(),label:"导入 "+f.name,data:r.result});saveBackups(a);renderBackups();}catch(e){toast("文件格式不对");}};r.readAsText(f);this.value="";};
function applyTheme(){const m=localStorage.getItem("theme")||"system";const dark=m==="dark"||(m==="system"&&window.matchMedia&&matchMedia("(prefers-color-scheme: dark)").matches);document.body.classList.toggle("dark",dark);document.querySelectorAll(".theme button").forEach(b=>b.classList.toggle("on",b.dataset.theme===m));}
document.querySelectorAll(".theme button").forEach(b=>b.onclick=()=>{localStorage.setItem("theme",b.dataset.theme);applyTheme();});
if(window.matchMedia)try{matchMedia("(prefers-color-scheme: dark)").addEventListener("change",()=>{if((localStorage.getItem("theme")||"system")==="system")applyTheme();});}catch(e){}
applyTheme();
document.getElementById("cfYes").onclick=()=>{document.getElementById("cfModal").classList.remove("show");const f=cfCb;cfCb=null;if(f)f();};
document.getElementById("cfNo").onclick=()=>{document.getElementById("cfModal").classList.remove("show");cfCb=null;};
function applyMode(){document.querySelectorAll("#modeSw button").forEach(b=>b.classList.toggle("on",b.dataset.mode===mode));document.getElementById("filters").style.display=mode==="alg"?"none":"";document.getElementById("diffBar").style.display=mode==="alg"?"":"none";render();}
document.querySelectorAll("#modeSw button").forEach(b=>b.onclick=()=>{if(focusOn)endFocus();mode=b.dataset.mode;localStorage.setItem("mode_v1",mode);applyMode();});
loadStuck();buildFilters();applyMode();
if(cfg){if(dirty){setPill("有未同步的改动，正在上传…","busy");push();}else{setPill("正在拉取…","busy");pull();}}else{setPill("未配置云同步");}
document.addEventListener("visibilitychange",()=>{if(document.visibilityState==="visible")autoSync();});
window.addEventListener("focus",autoSync);
setInterval(autoSync,60000);
</script></body></html>'''
html = html.replace("__ITEMS__", JS).replace("__SEC__", SEC).replace("__ALG__", ALGJS)
pm_css = open("/tmp/tui/node_modules/prosemirror-view/style/prosemirror.css", encoding="utf-8").read()
pm_css += "\n" + open("/tmp/tui/node_modules/prosemirror-gapcursor/style/gapcursor.css", encoding="utf-8").read()
pm_css = pm_css.replace("</style", "<\\/style")
pm_js = open("/tmp/tui/md.bundle.js", encoding="utf-8").read().replace("</script", "<\\/script")
hl_js = open("/tmp/tui/hl.bundle.js", encoding="utf-8").read().replace("</script", "<\\/script")
html = html.replace("__PM_CSS__", pm_css).replace("__PM_JS__", pm_js).replace("__HL_JS__", hl_js)
with open("秋招必背打卡表-云同步.html","w",encoding="utf-8") as f:
    f.write(html)
print("ok", len(items), "html bytes", len(html))
