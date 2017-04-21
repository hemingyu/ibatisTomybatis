# ibatisTomybatis
一定要按照这种顺序：
java文件修改：

将导入的包修改：
org.springframework.orm.ibatis.support.SqlMapClientDaoSupport  --org.mybatis.spring.support.SqlSessionDaoSupport

SqlMapClientDaoSupport   ---   SqlSessionDaoSupport

getSqlMapClientTemplate  ---   getSqlSession

queryForObject    ------   selectOne

queryForList      ---------  selectList

注释了批量操作，因为在myibatis在java里没有批量操作
/fotamgr-5/src/main/java/com/ishengji/download/db/BatchExecute.java(spring里涉及了也要注释)

xml文件修改：
<!DOCTYPE sqlMap PUBLIC "-//ibatis.apache.org//DTD SQL Map 2.0//EN" "http://ibatis.apache.org/dtd/sql-map-2.dtd">  ----
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">

sqlMap  ----- mapper

class --- type

Class --- Type

（
isNull判断property字段是否是null，用isEmpty更方便，包含了null和空字符串
isNotNull对应 test="$2 != null"
isNotEmpty对应 test="$2 != null and $2 != '' " "
传入的map或者类的属性name等于"1"吗，是就附加and和vvvv = '哈哈'
<isEqual property="name" compareValue="1" prepend="and">
vvvv = '哈哈'
< /isEqual>
对应
）

<isNotEmpty.*?prepend=\"(.*?)\".?property=\"(.*?)\"?> -----
<if test="$2 != null and $2 != '' ">\n	$1

<isNotEmpty.*?property=\"(.*?)\".?prepend=\"(.*?)\"?> -----
<if test="$1 != null and $1 != '' ">\n	$2

<isNotEmpty.*?property=\"(.*?)\"  ----   <if test="$1 != null and $1 != '' "

<isNotEmpty  prepend="and" >---  and
注意：如果使用了<if ..> 关闭标签也必须由</isNotEmpty> 更改为</if>,<isNotNull>也这样修改

</isNotEmpty.*?> ---  </if>

<dynamic prepend="WHERE"?> ---  where 1=1修改要小心，要结合上下文修改，与ibatis属性有关系（http://blog.csdn.net/huyanzhiwei/article/details/52186265）

<dynamic>  </dynamic?>  ---- 改为空


<iterate  conjunction ="," >  ----  <foreach  item="item" collection="list" separator ="," >



#value#需要改成:#{value}
#(.*?)#  ------  #{$1}  一定要小心，易出错(#[^{](.*?)#  ------  #{$1})
选择这种实验
#{username} and BINARY u.password=#{password}
= #userid#
$value$需要改成:${value}
\$(.*?)\$  ------  \${$1}

spring.xml修改：
sqlMapClient  ----  sqlSessionFactory

出现的错误：
Caused by: java.lang.IllegalArgumentException: Result Maps collection already contains value for newDown.DeltaByidResult
表示有个mapper里有重复的id为DeltaByidResult的resultMap

返回500,打开F12

将错误复制出来查看
java.lang.NoClassDefFoundError: Could not initialize class com.ishengji.ota.Tools.PropsUtil
	com.ishengji.ota.Action.OperationProjectConfigAction.<init>(OperationProjectConfigAction.java:77)
将PropsUtil.class.getResourceAsStream("/logPath.properties")修改为
PropsUtil.class.getResourceAsStream("/conf/logPath.properties")
（http://personbeta.iteye.com/blog/986241前面有 “   / ” 
“ / ”代表了工程的根目录，例如工程名叫做myproject，“ / ”代表了myproject 
me.class.getResourceAsStream("/com/x/file/myfile.xml"); ）