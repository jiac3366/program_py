
public class Logger {
  private FileWriter writer;
  private static final Logger instance = new Logger();

  private Logger() {
    File file = new File("/Users/wangzheng/log.txt");
    writer = new FileWriter(file, true); //true表示追加写入
  }

  public static Logger getInstance() {
    return instance;
  }

  public void log(String message) {
    writer.write(mesasge);
  }
}

// Logger类的应用示例：
public class UserController {
  public void login(String username, String password) {
    // ...省略业务逻辑代码...
    Logger.getInstance().log(username + " logined!");
  }
}

public class OrderController {
  public void create(OrderVo order) {
    // ...省略业务逻辑代码...
    Logger.getInstance().log("Created a order: " + order.toString());
  }
}

// 实现方式
// ===============饿汉式 不支持延迟加载=================

public class IdGenerator {
  private AtomicLong id = new AtomicLong(0);
  private static final IdGenerator instance = new IdGenerator();
  private IdGenerator() {}
  public static IdGenerator getInstance() {
    return instance;
  }
  public long getId() {
    return id.incrementAndGet();
  }
}

// ================懒汉式 有性能问题，不支持高并发======================

public class IdGenerator {
  private AtomicLong id = new AtomicLong(0);
  private static IdGenerator instance;
  private IdGenerator() {}
  public static synchronized IdGenerator getInstance() {
    if (instance == null) {
      instance = new IdGenerator();
    }
    return instance;
  }
  public long getId() {
    return id.incrementAndGet();
  }
}

// =============既支持延迟加载、又支持高并发==================
// 只要 instance 被创建之后，即便再调用 getInstance() 函数也不会再进入到加锁逻辑中了
public class IdGenerator {
  private AtomicLong id = new AtomicLong(0);
  private static IdGenerator instance;
  private IdGenerator() {}
  public static IdGenerator getInstance() {
    if (instance == null) {
      synchronized(IdGenerator.class) { // 此处为类级别的锁
        if (instance == null) {
          instance = new IdGenerator();
        }
      }
    }
    return instance;
  }
  public long getId() {
    return id.incrementAndGet();
  }
}
// 比双重检测更加简单的实现方法，那就是利用 Java 的静态内部类。它有点类似饿汉式，但又能做到了延迟加载

public class IdGenerator {
  private AtomicLong id = new AtomicLong(0);
  private IdGenerator() {}

  private static class SingletonHolder{
    private static final IdGenerator instance = new IdGenerator();
  }
  // SingletonHolder 是一个静态内部类，当外部类 IdGenerator 被加载的时候，并不会创建 SingletonHolder 实例对象。

  // 只有当调用 getInstance() 方法时，SingletonHolder 才会被加载，这个时候才会创建 instance。instance 的唯一性、创建过程的线程安全性，都由 JVM 来保证。
  public static IdGenerator getInstance() {
    return SingletonHolder.instance;
  }

  public long getId() {
    return id.incrementAndGet();
  }
}

// 枚举

public enum IdGenerator {
  INSTANCE;
  private AtomicLong id = new AtomicLong(0);

  public long getId() {
    return id.incrementAndGet();
  }
}
