# STERAePub++标准化模板<br/>
<b>～ePub自动化快速精排 for ver1.2.x～</b>
<br/><br/>

## 使用条件
- <b>适用工具：</b>Sigil 1.8.0+
- <b>适用对象：</b>以[《台灣 EPUB 3 製作指引》](https://github.com/dpublishing/epub3guide)为标准的ePub电子书源
- <b>目标类型：</b>横排中文（GBK）ePub电子书
- <b>靶向适配：</b>WebKit内核浏览器/多看阅读/Starrea/iBooks/Kindle
- <b>执行标准：</b>EPUB 3.0.1/XHTML 1.1/CSS 3.0/ECMAScript 5
<br/>

## 使用方法
*（带"\*"条目请参[注意事项](#tips)）*

>### 前期准备
>- 将`插件`内的*zip*在Sigil插件管理中直接安装，无需解压
>- 将`自动化`内的*ini*导入Sigil搜索模板，将<b>「书源处理」</b>组剪切至搜索模板根目录
>- 将`自动化`内的*txt*复制至`C:\Users\用户名\AppData\Local\sigil-ebook\sigil`
>- 在Sigil首选项中勾选<b>「EPUB可以使用JavaScript」</b>选项
><br/>
>
>### 预处理
>- 打开`书源.epub`
>- 检查`OEBPS/Images`，寻找可能是行内图的字符图、标题图等，多为*png*
>- 检查*xhtml*，用相应字符替换字符图，统一标题图格式以便后续替换
>- 检查`目录.xhtml`，确保目录链接至每个章节的第一个主文本*xhtml*
><br/>
>
>### 自动化执行\#1
>- 删除`OEBPS/Styles`中的所有文件
>- 规范化重命名`OEBPS/Images`内的图片文件并删除多余图片
>- 选中`OEBPS/Text`的最后一个文件，通过<b>「添加现有文件」</b>将`素材`内的文件导入
>- 打开`OEBPS/Text/insert.xhtml`，并按照如下格式填写`<body>`子节点：
>	<pre><code>&lt;mark class="rit-name"&gt;[书籍标题]&lt;mark&gt;
>	&lt;mark class="rit-number"\&gt;[书籍卷号]&lt;/mark\&gt;
>	&lt;mark class="rit-subname"\&gt;[书籍副标题]&lt;/mark\&gt;
>	&lt;mark class="rit-author"\&gt;[作者名字]&lt;/mark\&gt;
>	&lt;mark class="rit-aut-illu"\&gt;[画师名字]&lt;/mark\&gt;
>	&lt;mark class="rit-intro"\&gt;&lt;/mark\&gt;
>	[简介文本]</code></pre>
>- 保存*epub*
>- 打开*nav*后关闭其他标签页，运行<b>「自动执行列表1」</b>，等待运行完毕
><br/>
> 
>### 自动化执行#2
>- 选中`OEBPS/Text`中除*nav*外的所有文件，合并文件
>- 打开*nav*后关闭其他标签页，运行<b>「自动执行列表2」</b>，等待运行完毕
>- 关闭*epub*且不保存
><br/>
>
>### 自动化执行#3
>- 在`桌面`找到文件名含有`"epub2"`的*epub*
>- 规范化重命名*xhtml*，调整前后顺序并删除空白/多余的*xhtml*
<br/>

<h2 id="tips">注意事项</h2>