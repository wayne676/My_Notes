## hashCode & equals
Java中, Set要求元素不重复. 如何判断重复?  Object.equals 方法<br>
如果集合中已经有1000元素了, 第1001个元素加入集合就要调用1000次 equals 方法<br>
hasdCode 得到一个对象存储的物理地址(实际可能并不是)<br>
新元素进来时候先 调用 hashCode 物理地址是不是被占用了 如果没有 放入 如果有 调用 equals

所以，Java对于eqauls方法和hashCode方法是这样规定的：

如果两个对象相同，那么它们的hashCode值一定要相同。

如果两个对象的hashCode相同，它们并不一定相同。

为什么重写eqauls一定要重写hashcode:<br>
hashCode本来就是为了提高程序少使用equals才存在的, 只重写 equals 会出现 不同类型对象的特征相同和判定是相同对象 实际上并不是
