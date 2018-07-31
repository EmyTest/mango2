JavaScript 可以通过不同的方式来输出数据：

  1 使用 window.alert() 弹出警告框。
  2 使用 document.write() 方法将内容写到 HTML 文档中。
  3 使用 innerHTML 写入到 HTML 元素。
  4 使用 console.log() 写入到浏览器的控制台。
  
1
  <!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
	
<h1>我的第一个页面</h1>
<p>我的第一个段落。</p>
<script>
window.alert(5 + 6);
</script>
	
</body>
</html>





2
    操作HTML元素
    <!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>
	
<h1>我的第一个 Web 页面</h1>
<p id="demo">我的第一个段落。</p>
<script>
document.getElementById("demo").innerHTML="段落已修改。";
</script>
	
</body>
</html>




3  写到HTML文档

<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>
	
<h1>我的第一个 Web 页面</h1>
<p>我的第一个段落。</p>
<script>
document.write(Date());
</script>
	
</body>
</html>



4 写到控制台

    <!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>
	
<h1>我的第一个 Web 页面</h1>
<p>
浏览器中(Chrome, IE, Firefox) 使用 F12 来启用调试模式， 在调试窗口中点击 "Console" 菜单。
</p>
<script>
a = 5;
b = 6;
c = a + b;
console.log(c);
</script>
	
</body>
</html>




console.log()的用处
主要是方便你调式javascript用的, 你可以看到你在页面中输出的内容。
相比alert他的优点是：
他能看到结构化的东西，如果是alert，弹出一个对象就是[object object],但是console能看到对象的内容。
console不会打断你页面的操作，如果用alert弹出来内容，那么页面就死了，但是console输出内容后你页面还可以正常操作。


document.write是直接写入到页面的内容流，如果在写之前没有调用document.open, 浏览器会自动调用open。每次写完关闭之后重新调用该函数，会导致页面被重写。
innerHTML则是DOM页面元素的一个属性，代表该元素的html内容。你可以精确到某一个具体的元素来进行更改。如果想修改document的内容，则需要修改document.documentElement.innerElement。
innerHTML很多情况下都优于document.write，其原因在于其允许更精确的控制要刷新页面的那一个部分。


DOM 解释
您会经常看到 document.getElementById("id")。
这个方法是 HTML DOM 中定义的。
DOM (Document Object Model)（文档对象模型）是用于访问 HTML 元素的正式 W3C 标准。
格式<script>
那些老旧的实例可能会在 <script> 标签中使用 type="text/javascript"。
现在已经不必这样做了。
JavaScript 是所有现代浏览器以及 HTML5 中的默认脚本语言。
脚本位置
在 <head> 或者 <body> 的JavaScript
外部脚本不能包含 <script> 标签。
输出数据
window.alert() 弹出警告框。
document.write() 方法将内容写到 HTML 文档中。
innerHTML 写入到 HTML 元素。
console.log() 写入到浏览器的控制台。
输出内容
使用 document.write() 向文档输出写内容。
如果在文档已完成加载后执行 document.write，整个 HTML 页面将被覆盖
写到控制台(调试模式)
使用 console.log() 方法在浏览器中显示 JavaScript 值。
F12 启用调试模式， 在调试窗口中点击 "Console" 菜单。



window.alert 的补充:
window.alert(5+6) 与 window.alert("5+6") 输出的值是不一样的。window.alert(5+6) 会输出 11，而window.alert("5+6") 会输出 5+6。这是因为当用引号时会认为引号中是字符串，从而直接将引号中的内容打印出来。
