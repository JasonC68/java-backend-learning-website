# 秋招后端八股「必背清单」（基于小林coding）

> 目标：抓主干，别贪全。每页只把 **⭐ 必背** 这一档背熟，就能覆盖大部分面试。
> 🔸 次要 = 能讲清思路即可，不用逐字背；⬜ 可跳过 = 冷门/能现推/口水题。
>
> 投递方向：后端 + AI Agent。建议复习优先级：
> **集合 ≈ 并发 ＞ MySQL ≈ JVM ＞ Spring ＞ 网络 ＞ Redis ＞ 扩展(MyBatis/MQ/分布式) ＞ 操作系统 ＞ Java基础**

---

## 一、Java 基础

**⭐ 必背**

- 值传递 vs 引用传递（Java 只有值传递，经典坑题）
- 装箱拆箱 + `Integer` 缓存（-128~127，`==` 陷阱）
- 为什么用 `BigDecimal` 不用 `double`
- 重载 vs 重写
- 抽象类 vs 接口的区别
- `final` / `static` 的作用
- 深拷贝 vs 浅拷贝 + 实现方式
- JVM / JDK / JRE 三者关系
- 八种基本数据类型及字节数
- 封装/继承/多态；多态的体现
- 泛型是什么 + 类型擦除

**🔸 次要**：跨平台原理、编译/解释、类型转换、静态内部类 vs 非静态内部类、接口可定义哪些方法、创建对象的方式

**⬜ 可跳过**：Java 特点/优劣势、和 Python/C 的区别、抽象类能否加 final / 实例化、接口能否有构造函数（理解抽象类与接口后可现推）

---

## 二、集合（Collection）—— ⭐⭐ 重中之重

**⭐ 必背（HashMap 是绝对核心，几乎必问）**

- HashMap 实现原理（数组+链表+红黑树）
- HashMap 的 put / get 过程
- HashMap 扩容机制；为什么容量是 2 的 n 次方；负载因子（0.75）
- 链表转红黑树的阈值（8）；为什么用红黑树而不是平衡二叉树
- 哈希冲突的解决方法
- HashMap 是线程安全的吗？多线程下有什么问题（JDK7 死循环、数据覆盖）
- 重写 equals / hashCode 的注意点
- HashMap 用什么做 Key？为什么 String 适合做 Key
- HashMap vs Hashtable vs ConcurrentHashMap 的区别
- ConcurrentHashMap 怎么实现的（JDK7 分段锁 → JDK8 synchronized + CAS）
- 已经用了 synchronized 为什么还要 CAS
- ArrayList vs LinkedList 区别及应用场景
- ArrayList 扩容机制（1.5 倍）
- ArrayList 为什么线程不安全 / 如何变安全（CopyOnWriteArrayList 原理）
- List vs Set 区别

**🔸 次要**：数组与集合区别、Collection vs Collections、集合遍历方式、ArrayList vs Vector、一边遍历一边修改（fail-fast / ConcurrentModificationException）、List 与数组互转、HashMap key 可否为 null、Set 如何排序/去重、有序 Set（LinkedHashSet/TreeSet）

**⬜ 可跳过**：往 hashmap 存 20 个元素扩容几次、分段锁是否可重入、List 填基本类型报错

---

## 三、并发 / 多线程 —— ⭐⭐ 重中之重

> 注：小林这页偏概念，真实面试更爱深挖 **synchronized、volatile、AQS、ReentrantLock、线程池、CAS/ABA**。下面把这些一并补进必背。

**⭐ 必背**

- JMM（Java 内存模型）+ 可见性/原子性/有序性
  - JMM 是 Java 定义的一套规范，核心解决的是**多线程下共享变量的访问规则**
  - 它的抽象模型是这样的:所有共享变量都存在**主内存**里;每个线程有自己的**工作内存**,线程操作变量时,不是直接改主内存,而是先把变量拷贝到自己的工作内存,改完再写回
  - 问题就出在这里——一个线程改了自己工作内存的值,还没刷回主内存,或者另一个线程没及时从主内存重新读,就会读到旧值,这就是可见性问题的根源。
  - 由此引出并发的**三大问题**:
  
    * **可见性**:一个线程的修改,其他线程不一定能立刻看到。
    * **原子性**:一个操作可能执行到一半被打断,比如 `i++` 其实是读、改、写三步,不是原子的。
    * **有序性**:编译器和 CPU 为了优化会做**指令重排**,单线程下没问题,但多线程下重排可能导致意料之外的结果。
  * JMM 就是通过 **happens-before 规则**,以及 volatile、synchronized、final 这些关键字,来保证在需要的时候满足这三点。比如 happens-before 里很重要的几条:程序顺序规则、锁规则(解锁 happens-before 后续加锁)、volatile 规则(写 happens-before 后续的读)。

- 线程的创建方式 + 线程的几种状态（生命周期）
  - 通常说有四种，但本质上可以归成两大类。
    - 第一种，**继承 Thread 类**，重写 run() 方法，然后 new 出来调 start()。缺点是 Java 单继承，继承了 Thread 就没法再继承别的类了，不够灵活。
    - 第二种，**实现 Runnable 接口**，实现 run()，再把它传给 Thread 启动。这种比继承好，因为接口可以多实现、不占用继承位，而且把"任务"和"线程"解耦了，更推荐。
    - 第三种，**实现 Callable 接口**，配合 FutureTask 使用。它和 Runnable 的区别是：Callable 的 call() 方法**有返回值，还能抛出受检异常**，可以通过 Future 的 get() 拿到线程执行结果。需要拿返回值的场景用它。
    - 第四种，**用线程池**，通过 ExecutorService 提交 Runnable 或 Callable 任务。这是**生产环境的标准做法**，因为能复用线程、控制并发数、统一管理生命周期，避免手动 new 线程带来的资源失控。
  - 这里有两个常被追问的点我先说清楚：
    - 一是**严格讲，Java 创建线程的方式只有一种**，就是 `new Thread()`，前面这些都是给线程提供任务的不同方式，底层最终都是构造一个 Thread 对象。
    - 二是**必须调 `start()` 而不是 `run()`**：`start()` 才会真正向操作系统申请创建一个新线程、由 JVM 调用 run；直接调 `run()` 只是在当前线程里执行了一个普通方法，根本没有新线程。
  - 状态之间的流转大概是：NEW 调 start 进 RUNNABLE；运行中抢锁失败进 BLOCKED，拿到锁回 RUNNABLE；调 wait/join 进 WAITING，被 notify 唤醒后**先回到 BLOCKED**（因为要重新竞争锁），拿到锁才回 RUNNABLE；调 sleep 进 TIMED_WAITING，超时自动回 RUNNABLE；最后正常或异常结束进 TERMINATED。

- `sleep` vs `wait` 的区别；sleep 是否释放锁/CPU
  - **1. 所属的类不同**: `sleep()` 是 **Thread 类的静态方法**，`wait()` 是 **Object 类的方法**。wait 定义在 Object 上，是因为它要配合对象锁（监视器）来用，每个对象都能作为锁，所以这个方法放在所有对象的基类上。
  - **2. 是否释放锁（最核心的区别）**: `sleep()` **不释放锁**——线程睡着了，但手里攥着的锁不放，别的线程照样进不来。`wait()` **会释放锁**——调用后线程把当前对象的锁让出去，进入这个对象的等待队列，这样其他线程才有机会拿到锁去干活、并在合适的时候唤醒它。
  - **3. 使用的前提不同**: `wait()` **必须在 synchronized 同步块/同步方法里调用**，也就是必须先持有这个对象的锁，否则运行时会抛 `IllegalMonitorStateException`。`sleep()` 没有这个限制，任何地方都能调。
  - **4. 唤醒方式不同**: `sleep(n)` 是**带时间的**，到点自动醒，回到就绪状态。`wait()` 分两种：无参的 `wait()` 会一直等，必须靠别的线程调用同一个对象的 `notify()` 或 `notifyAll()` 来唤醒；带超时的 `wait(n)` 则是要么被唤醒、要么超时自动醒。
  - **5. 设计用途不同**: sleep 是**让线程单纯暂停一段时间**，和协作没关系；wait/notify 是**线程间通信**的机制，专门用来做"等待某个条件满足再继续"这种协作，典型场景就是生产者-消费者。
  - **相同点**也提一下：两者都会让线程暂停、让出 CPU；而且都会响应中断，被 `interrupt()` 时都会抛 InterruptedException。

- `notify` vs `notifyAll`
  - 两个都是用来**唤醒在同一个对象上 wait 的线程**的。区别在于唤醒的数量：
    * `notify()` 从这个对象的等待队列里**随机唤醒一个**线程（具体唤醒哪个由 JVM 决定，不保证 FIFO，不可控）。
    * `notifyAll()` 唤醒**等待队列里的所有**线程。
  * 实践中更推荐 notifyAll。因为`notify()` 有"**信号丢失 / 唤醒错线程**"的风险。考虑一个场景：等待队列里既有生产者又有消费者，或者多个线程等待的条件不一样。notify 随机挑一个唤醒，万一唤醒的那个线程发现**条件并不满足**，它会继续 wait 接着睡——而这个 notify 信号就被它"消耗"掉了，真正该被唤醒、条件满足的那个线程反而一直等下去，可能导致整个程序卡死。
  * 用 notifyAll 把所有线程都叫醒，让它们各自重新检查条件，就能避免这个问题。代价是 notifyAll 会有一些**无谓的唤醒和锁竞争开销**（被叫醒但条件不满足的线程又睡回去），但换来的是正确性，绝大多数场景这个开销可以接受。
- 怎么保证多线程安全（synchronized / Lock / 原子类 / volatile）
- volatile 作用与原理（补充，必问）
- synchronized 原理 + 锁升级（偏向→轻量→重量，补充，必问）
- CAS 原理 + ABA 问题（补充，必问）
- ReentrantLock 与 synchronized 的区别 + AQS（补充，必问）
- 线程池原理、核心参数、拒绝策略、工作流程（补充，**超高频**）
- BLOCKED vs WAITING 区别
- 如何停止一个线程（interrupt 机制）

**🔸 次要**：JUC 常用类、常用锁的分类与场景、线程间通信方式、interrupt 如何让线程抛异常、wait 如何恢复 RUNNABLE、Java 线程与 OS 线程的关系

**⬜ 可跳过**：Go 协程 vs Java 线程、notify 选择哪个线程

---

## 四、JVM

**⭐ 必背**

- JVM 内存模型 / 运行时数据区（堆、栈、方法区、程序计数器、本地方法栈）
- 堆和栈的区别；堆分为哪几部分（新生代/老年代，Eden+S0+S1）
- 程序计数器的作用，为什么线程私有
- 创建对象的过程 + 对象在内存的分布
- 类加载过程（加载→验证→准备→解析→初始化）
- 双亲委派模型是什么、有什么用
- 类加载器有哪些
- 判断垃圾的方法（引用计数 vs 可达性分析）
- 垃圾回收算法（标记清除/复制/标记整理）及优缺点
- 垃圾回收器有哪些；CMS 和 G1 的区别
- MinorGC / MajorGC / FullGC 区别，什么场景触发 Full GC
- 四种引用类型（强/软/弱/虚）的区别
- 内存泄漏 vs 内存溢出，及常见场景

**🔸 次要**：String 保存在哪、`String s = new String("abc")` 创建几个对象、Stop The World 阶段、堆/栈溢出排查、什么场景用 CMS / G1、G1 特色、方法区存什么

**⬜ 可跳过**：栈里存指针还是对象、GC 是否只回收堆、大对象放哪个区

---

## 五、MySQL

**⭐ 必背**

- 索引底层为什么用 B+ 树；B+ 树 vs B 树区别；为什么不用跳表/哈希
- 聚簇索引 vs 非聚簇索引
- 联合索引 + 最左匹配原则（含「a=x and c<x 怎么走」「b>x and a=x 是否生效」这类）
- 索引失效的场景
- 回表、覆盖索引是什么
- 事务的 ACID 及如何实现
- 事务隔离级别 + MySQL 默认级别（RR）
- 脏读 / 不可重复读 / 幻读，RR 如何（部分）解决幻读（间隙锁）
- MVCC 实现原理（undo log + ReadView）
- redo log / undo log / binlog 的作用与区别
- binlog 两阶段提交
- 一条 update / 一条 SQL 查询的完整执行过程
- InnoDB vs MyISAM 区别
- MySQL 有哪些锁（表锁/行锁/间隙锁/Next-Key）
- explain 的作用 / 怎么看是否走索引
- 慢查询如何优化

**🔸 次要**：三大范式、CHAR vs VARCHAR、自增 ID vs UUID 做主键、性别/status 字段是否适合建索引、前缀索引、redo log 为什么不直接写 B+ 树、主从复制、主从延迟、分库分表、什么字段适合做主键

**⬜ 可跳过**：NoSQL vs SQL、in vs exists、int(1)/int(10)、Text 上限、IP 存储、各种纯 SQL 手写题（按目标公司补）、double write buffer

---

## 六、Redis

**⭐ 必背**

- Redis 为什么快（内存 + 单线程 + IO 多路复用 + 高效数据结构）
- 底层数据结构（String/List/Hash/Set/ZSet）及各自底层实现
- ZSet 底层（跳表 + 哈希表）；跳表怎么实现、为什么不用 B+ 树
- 两种持久化 RDB vs AOF 的优缺点
- 内存淘汰策略（8 种，LRU/LFU）
- 过期删除策略（惰性 + 定期）
- 缓存雪崩 / 击穿 / 穿透是什么、怎么解决
- 布隆过滤器原理
- Redis 和 MySQL 缓存一致性（延迟双删 / 先删缓存再更新库等）
- Redis 分布式锁实现原理（SETNX + 过期 + Lua，Redlock 概念）
- 大 Key / 热 Key 问题及解决
- 主从复制（全量 + 增量同步）
- 哨兵机制原理
- 如何保证 Redis 操作原子性（Lua）

**🔸 次要**：Redis 6 哪里用了多线程、IO 多路复用怎么实现、集群 Cluster 模式与分片路由（CRC16 槽）、本地缓存 vs Redis、应用场景、为什么比 MySQL 快

**⬜ 可跳过**：listpack/压缩列表实现细节、哈希表扩容（渐进式 rehash 可了解）、ZSet 在项目里的具体用法（结合自己项目准备即可）、秒杀场景设计（有项目经验再深挖）

---

## 七、计算机网络

**⭐ 必背**

- TCP 三次握手过程 + 为什么是三次（不是两次/四次）
- TCP 四次挥手过程 + 为什么挥手是四次；为什么要等 2MSL
- TCP 与 UDP 区别
- TCP 为什么可靠（序号/确认/重传/流量控制/拥塞控制）
- TCP 拥塞控制（慢启动、拥塞避免、快重传、快恢复）
- GET vs POST 区别
- HTTP 常用状态码（含 301/302、502/504 区别）
- HTTP vs HTTPS 区别
- HTTPS 握手过程 + 如何防中间人攻击
- HTTP/1.1 vs HTTP/2.0 区别
- HTTP 为什么是无状态的；Cookie / Session 区别
- Cookie / Session / Token（JWT）区别；禁用 cookie 后 session 还能用吗
- 输入一个 URL（打开百度首页）到页面展示发生了什么（综合题，**超高频**）
- DNS 解析流程；DNS 用 TCP 还是 UDP
- HTTP 长连接 vs WebSocket

**🔸 次要**：OSI 与 TCP/IP 分层、HTTP 报文组成、SYN 洪泛、TIME_WAIT 过多的原因、为什么有 HTTP 还要 RPC、JWT 的字段/缺点/泄露处理、Nginx 负载均衡算法及所在层、长连接是什么、断点重传

**⬜ 可跳过**：HTTP/SOCKET/TCP 区别、改 host、localStorage vs Cookie、用 UDP 实现 HTTP、各种握手丢包的细枝末节追问（理解机制后可现推）

**网络攻击（了解即可，能说清概念）**：DDoS、SQL 注入、CSRF、XSS、DNS 劫持

---

## 八、操作系统

**⭐ 必背**

- 进程 vs 线程的区别；进程、线程、协程的区别
- 进程的五种状态及切换
- 进程间通信方式（管道、消息队列、共享内存、信号量、信号、Socket）
- 线程间通信方式
- 进程切换 vs 线程切换；为什么线程切换更快
- 用户态 vs 内核态
- 死锁的四个必要条件 + 如何避免
- 乐观锁 vs 悲观锁；自旋锁是什么、用在哪
- 虚拟内存与物理内存；虚拟地址如何转物理地址（页表）
- 程序的内存布局；堆和栈的区别
- 页面置换算法（FIFO / LRU / LFU）
- IO 多路复用；select / poll / epoll 的区别（**后端高频**）
- epoll 边缘触发 vs 水平触发
- 零拷贝是什么

**🔸 次要**：协程优势、进程为何崩溃不影响其他进程、进程调度算法、信号 vs 信号量、共享内存实现、写时复制（CoW）、fork 复制了什么、brk/mmap、malloc 1KB vs 1MB、内存不足会发生什么、Redis/Nginx/Netty 为何高性能、中断流程与类型、银行家算法

**⬜ 可跳过**：线程切换上下文存哪、进程上下文有哪些、多线程是否越多越好（理解切换成本后可现推）

---

## 九、Spring / Spring Boot —— ⭐ 框架轮主战场

> 八股基础轮过了之后，框架/项目轮基本就是 Spring 的天下，必背。

**⭐ 必背**

- IoC / DI 是什么（控制反转、依赖注入）
- Bean 的生命周期（实例化→属性填充→初始化→使用→销毁，及各扩展点）
- Bean 的作用域（singleton / prototype / request / session）
- 三级缓存如何解决循环依赖（为什么是三级、能不能两级）
- AOP 是什么、原理（JDK 动态代理 vs CGLIB 的区别与选择）
- `@Transactional` 事务原理（基于 AOP 代理）
- 事务的传播行为（REQUIRED / REQUIRES_NEW 等常见 7 种）
- **事务失效的场景**（自调用、方法非 public、异常被 catch、异常类型不匹配、未被 Spring 管理）—— 超高频
- Spring MVC 一次请求的处理流程（DispatcherServlet 调度链）
- Spring Boot 自动装配原理（`@SpringBootApplication` / `@EnableAutoConfiguration` / SPI / spring.factories）
- 常用注解区别（`@Autowired` vs `@Resource`、`@Component` vs `@Bean`）

**🔸 次要**：BeanFactory vs ApplicationContext、常见扩展点（BeanPostProcessor、InitializingBean、Aware）、starter 机制、Spring 用到的设计模式、`@Configuration` 的代理增强、循环依赖为什么解决不了构造器注入/prototype

**⬜ 可跳过**：Spring 各模块组成、Environment/Profile 细节、SpringBoot 内嵌容器实现细节

---

## 十、扩展：MyBatis / 消息队列 / 分布式 —— ⭐ 按简历技术栈取用

> 简历里写了哪个就重点准备哪个。没用过的可只看 ⭐ 概念题。

**⭐ 必背**

MyBatis：

- `#{}` 和 `${}` 的区别（预编译防注入 vs 直接拼接）
- 一级缓存 / 二级缓存

消息队列（MQ）：

- MQ 的作用（解耦、异步、削峰填谷）
- 如何保证消息不丢失（生产端 / broker / 消费端三段）
- 如何保证消息不重复消费（消费幂等）
- 消息积压怎么处理

分布式：

- CAP 理论 / BASE 理论
- 分布式事务方案（2PC、TCC、本地消息表、最大努力通知）
- 分布式 ID 生成方案（雪花算法 Snowflake 等）
- 常见限流算法（计数器、滑动窗口、漏桶、令牌桶）

**🔸 次要**：MyBatis 工作原理 / `$` 动态 SQL、RabbitMQ vs Kafka vs RocketMQ 区别、消息顺序性、分布式锁的几种实现对比、一致性哈希、幂等的几种实现方式

**⬜ 可跳过**：各 MQ 的具体配置参数、各注册中心（Nacos/Eureka/ZK）的细节对比（用到再看）

---

## 复习建议

1. **先横扫所有 ⭐**，形成主干；二刷再补 🔸。⬜ 不背，留作面前扫一眼。
2. **HashMap、线程池、B+ 树/索引、MVCC、缓存三兄弟**是后端面试的「常驻嘉宾」，务必能手画/手推、能讲透原理。
3. **AI Agent 方向**：八股仍以上述后端为主；额外准备好你简历里的 Agent 项目（框架选型、Function Calling、RAG、上下文管理、并发与限流），面试官更爱深挖项目。
4. 每个 ⭐ 问题练成「30 秒讲清 + 能被追问两层」的程度，比背 100 个浅问题更有用。
