#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 查找替换执行组
XH = (('样式整理', r'(?<!ctt )class=\"(?:(?!ctt).)*?\"',
       ('保留样式标记', {
           r'([^\"\s]*(?:font-\d{2,}em|font-\d{4,}per|solid|dotted|double|dashed|indent|start-|end-|float|inverse|bg-|display|break|wrap)[^\"\s]*)': r'check-\1',
           r'bold': 'check-bold',
           'line-through': 'check-del',
           'italic': 'check-ita',
           r'em-line[^\"\s]*': 'check-un',
           r'(?:em-sesame|em-dot|em-circle|em-double-cirlce|em-triangle)[^\"\s]*': 'check-dot',
           r'[^\"\s]*align-(?:start|left)': 'check-left',
           r'[^\"\s]*align-center': 'check-center',
           r'[^\"\s]*align-(?:end|right)': 'check-right',
           r'gfont(?!\d)': 'check-int',
           r'gfont([1-9]+)0*': r'check-int check-em1\1',
           r'gfont0([1-9]+)0*': r'check-int check-em0\1',
           r'font-(?:(\d)em(\d+?)0*|(\d{2,}?)0*per)': r'check-em\1\2\3',
           r'font-(\d)em': r'check-em\g<1>0',
           'kogaki': 'check-em08',
           r'color-([A-z\d-]+)': r'check-\1'}),
       ('多余样式清除', {
           r'(?<=[\s\"])(?<!check-)(?:(?!check-)[^\"\s])+?(?=[\s\"])': '',
           r'(?:(?<=\")\s+|\s+(?=\")|\s{2,})': ''})),
      ('标签规范', r'(?s)<page.*?/page>',
       ('代码初始化', {
           r'(?s)<!--(?:(?!-->).)*?-->': '',
           r'(?:^^[\s　]+(?=<)|\s*\n\s*(?=[^<\s])|(?<=>) +(?=<))': ''}),
       ('标签规范化', {
           r'^(<page.*?>)(?:(?!<title>[目導][錄航]</title>)[\s\S])*?<body.*?>': r'\1\n<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"no\"?>\n<!DOCTYPE html>\n<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"zh\" xmlns:epub=\"http://www.idpf.org/2007/ops\" xmlns:xml=\"http://www.w3.org/XML/1998/namespace\">\n<head>\n<title></title>\n<link href=\"../Styles/stylesheet.css\" type=\"text/css\" rel=\"stylesheet\"/>\n<script type=\"text/javascript\" src=\"../Misc/script.js\"></script>\n</head>\n<body>',
           r'(<(p|div|span|a|h\d)[^>\n]*?) */>': r'\1></\2>',
           r'alt=\".*?\"': '',
           r'\s+/>': '/>',
           r'<b>(.*?)</b>': r'<span class=\"check-bold\">\1</span>',
           r'<i>(.*?)</i>': r'<span class=\"check-ita\">\1</span>',
           r'<s>(.*?)</s>': r'<span class=\"check-del\">\1</span>',
           r'<u>(.*?)</u>': r'<span class=\"check-un\">\1</span>',
           r'<strong>(.*?)</strong>': r'<span class=\"check-bolder\">\1</span>'}),
       ('多余标签清除', {
           r'(*)<span[^>\n]*?xmlns=[^>\n]*?>((?:(?!</span>).)*?)</span>': r'\1',
           r'<span(?:(?!id=)[^>\n])*?>[\s　]*</span>': '',
           r'<(p|div)(?:(?!id=)[^>\n])*?>[\s　]*</\1>': '<p><br/></p>',
           r'\s*class=\"[\s　]*\"': '',
           r'<a[^>\n]*?(?:id=\"([^\"\n]*?)\"[^>\n]*?href=\"([^\"\n]*?)\"|href=\"([^\"\n]*?)\"[^>\n]*?id=\"([^\"\n]*?)\")>((?:(?!</a>).)*?)</a>': r'<span id=\"\1\4\"><a href=\"\2\3\">\5</a></span>',
           r'(*)(<[A-z\d]+[^>\n]*?)\s*id=\"([^\"\n]*?)\"([^>\n]*?>[\s\S]*?)<a[^>\n]*?href=\"[^\"\n]*?#\2\s*\"[^>\n]*?>((?:(?!</a>).)*?)</a>': r'\1\3\4',
           r'(*)<div(?:(?!check-|id=)[^>\n])*?>\s*((?:[^<>]*?(?:<(?P<tag>[A-z\d]+)[^>\n]*?>(?:(?!</(?P=tag)>)[\s\S])*</(?P=tag)>|<[^>\n]*?/>))*[^<>]*)</div>\s*': r'\1',
           r'(*)<span(?:[^>\n]*?xmlns[^>\n]*?|(?:(?!check-|id=)[^>\n])*?)>((?:[^<>]*?(?:<(?P<tag>[A-z\d]+)[^>\n]*?>(?:(?!</(?P=tag)>)[\s\S])*</(?P=tag)>|<[^>\n]*?/>))*[^<>]*)</span>': r'\1',
           r'(*)(<a[^>\n]*?>(?:(?!</a>).)*?)<span[^>\n]*?>((?:(?!</span>|</a>).)*?)</span>': r'\1\2',
           r'(?:\s*<rb>(.*?)</rb>\s*|\s*(<rt>.*?</rt>)\s*|\s*<rp[^>\n]*?>.*?</rp>\s*|<hr[^>\n]*?/>|<a id=\"section.*?/a>)': r'\1\2'})),
      ('文本处理', r'(?s)<body.*?/body>',
       ('符号转换', {
           r'\?\?': '？？',
           r'(?:\!\!|‼)': '！！',
           r'(?:\!\?|⁉)': '！？',
           '﹙': '（',
           '﹚': '）',
           r'[︰‥]': '：',
           r'[－─｜]': '—',
           r'(?:\.{3}|⋯)': '…',
           r'[:：]{3}': '……',
           r'[~∼〜]': '～',
           r'[‧・．˙･·]': '•',
           '❤': '♥',
           '╳': '×',
           '︽': '《',
           '︾': '》',
           '﹁': '「',
           '﹂': '」',
           '﹃': '『',
           '﹄': '』',
           r'(?:＜|︿|&lt;)': '〈',
           r'(?:＞|﹀|&gt;)': '〉',
           '&amp;': '＆'}),
       ('标点修正', {
           r'(?:\?？|？\?)': '？？',
           r'(?:\!！|!\!)': '！！',
           r'(?:\?！|？\!)': '？！',
           r'(?:\!？|！\?)': '！？',
           r'(?<=[一-龥あ-ヶー]) *\? *': '？',
           r'(?<=[一-龥あ-ヶー]) *\! *': '！',
           r'(?<=[一-龥あ-ヶー]) *, *': '，',
           r'(?<=[一-龥あ-ヶー]) *: *': '：',
           r'(?<=[一-龥あ-ヶー]) *; *': '；',
           r'(?<=[一-龥あ-ヶー]) *\. *(?=[一-龥あ-ヶー])': '•',
           r'(?<=[A-z]) *　 *(?=[A-z])': ' ',
           r'(?<=\d)(?: *• *(?=\d)|•)': '.',
           r'(?<=[\dA-z]) *— *(?=[\dA-z])': '-',
           r'([△▲▽▼▷▶◁◀☜☚☝☟☞☛↖↑↗←→↙↓↘↕↔ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦㄧㄨㄩㄪㄫㄬㄭㄮㄯ㄰ㄱㆢㄲㆢㄱㆣㄲㆣㄱㆤㄲㆤㄱㆥㄲㆥㄱㆦㄲㆦ˙ˊˇˋ˙˙]+)': r'<span type=\"check\">\1</span>'}),
       ('排版整理', {
           r'([\s　])*<br/>(?(1)[\s　]*|[\s　]+)': '<br/>',
           r'(<[^p][^>\n]*?>[^<\n]*?)<br/>': r'\1\n<p><br/></p>',
           r'\s*<div.*?>(\s*<p><br/></p>)+\s*</div>': r'\1',
           r'<p><br/></p>(\s*<p><br/></p>){2,}': r'<p><br/></p>\n<p><br/></p>',
           r'(?:　 | 　)': '　',
           r'<(p|div)( )*(?(2)class=\"([^\"\n]*?)\")>(　*[^　\n]+?)(　{3,}.*?</\1>)': r'<\1 class=\"check-\2\3\">\4</\1>\n<\1 class=\"check-\2\3\">\5',
           r' {2,}': ' ',
           r'(*)(<a[^>\n]*?>(?:(?!</a>)[\s\S])*?)　{2,}': r'\1　',
           r'(<(?:p|div)[^>\n]*?>)　{1,2}(?!　)': r'\1',
           r'<(p|div)( )*(?(2)class=\"(.*?)\")>　{3,7}(?!　)': r'<\1 class=\"check-center\2\3\">',
           r'<(p|div)( )*(?(2)class=\"(.*?)\")>　{7,}': r'<\1 class=\"check-right\2\3\">',
           r'<p( )*(?(1)class=\"(.*?)\")>(?=.*?[—…]{5,})': r'<p class=\"check-break\1\2\">',
           r'(*)(?:type=\"check\"\s*)?(?:(class=\".*?)check-\s*|style=\".*?\")': r'type=\"check\" \1'}),
       ('行间注处理', {
           r'(*)(<ruby>(?:(?!</ruby>|<rt).)+)<rt[^>\n]*?>((?:(?!</rt>).)+)</rt>((?:(?!</ruby>|<rt).)+)<rt[^>\n]*?>((?:(?!</rt>).)+)': r'\1\3<rt>\2\4',
           r'(?:(?<=</rt>)((?:(?!</ruby>).)+)(</ruby>)|<ruby[^>\n]*?>((?:(?!</ruby>|<rt).)*?)</ruby>)': r'\2<span type=\"check\">\1\3</span>',
           r'<ruby[^>\n]*?>((?:(?!</ruby>|<rt).)+)<rt[^>\n]*?>(?:\s*(?:•|、)+\s*)+</rt></ruby>': r'<span type=\"check\" class=\"dot\">\1</span>'}),
       ('分节处理', {
           r'(?:<p><br/></p>\s*|<div[^>\n]*?>\s*)*<(p|div)((?:(?!cut)[^>\n])*?(?:><span[^>\n]*?)?)>[\s　\[(（【〈《｛{「『-]*([\dA-zΑ-ω-]{1,3}?)[\s　\])）】〉》｝}」』.]*(?:</span>)?</\1>(?(2)(?:\s*<p><br/></p>|\s*</div>)*|(?:\s*<p><br/></p>|\s*</div>)+)': r'<p><br/></p>\n<p type=\"check\" class=\"cut\">- \3 -</p>\n<p><br/></p>',
           r'(?:<p><br/></p>\s*|<div[^>\n]*?>\s*)*<(p|div)((?:(?!cut)[^>\n])*?(?:><span[^>\n]*?)?)>[\s　\[(（【〈《｛{「『-]*([\dA-zΑ-ω-]{1,3}?)[\s　.-]+([^\dA-zΑ-ω-].*?)[\s　\])）】〉》｝}」』]*(?:</span>)?</\1>(?(2)(?:\s*<p><br/></p>|\s*</div>)*|(?:\s*<p><br/></p>|\s*</div>)+)': r'<p><br/></p>\n<p type=\"check\" class=\"cut\">【\3 \4】</p>\n<p><br/></p>',
           r'(?:<p><br/></p>\s*|<div[^>\n]*?>\s*)*<(p|div)(?:(?!cut)[^>\n])*?(?:><span[^>\n]*?)?>[\s　]*([^\n\dA-zΑ-ω一-龥あ-ヶー`~～(){},.\\/;·！…（）—｛｝［］《》〈〉？：“”【】；‘\'，。、『』「」\[\]•-]+)[\s　]*</\1>(?:\s*<p><br/></p>)*': r'<p><br/></p>\n<p type=\"check\" class=\"cut\">\2</p>\n<p><br/></p>',
           r'(?:<p><br/></p>\s*|<div[^>\n]*?>\s*)*<(p|div)((?:(?!cut)[^>\n])*?(?:><span[^>\n]*?)?)>[\s　]*([^\s\dA-z一-龥あ-ヶー`~～(){},.\\/;·！…（）—｛｝［］《》〈〉？：“”【】；‘\'，。、『』「」\[\]•-])[\s　]*([^\dA-zΑ-ω-].*?)[\s　]*(?:</span>)?</\1>(?(2)(?:\s*<p><br/></p>|\s*</div>)*|(?:\s*<p><br/></p>|\s*</div>)+)': r'<p><br/></p>\n<p type=\"check\" class=\"cut\">\3 \4</p>\n<p><br/></p>'}),
       ('样式回复', {
           r'class=\"(\s)*([^\"\n]+?)(?(1)\s*|\s+)\"': r'class=\"\2\"',
           r'\s*class=\"\s*\"': ''})),
      ('章节重构', '',
       ('目录整理', {
           r'<ctt[^>\n]*?>[\s\S]*<a[^>\n]*?>\s*<ch>(?:目录|目錄|目録|目次|CONTENTS|Contents|もくじ|もくろく)(?:页|頁|ページ)?</ch>\s*</a>\s*</ctt>\s*': '',
           r'<ctt[^>\n]*?>[\s\S]*<a[^>\n]*?>\s*<ch>(?:書封|书封|封面|書名|书名|表纸|表紙|ひょうし)(?:页|頁|ページ)?</p>\s*</ch>\s*</ctt>\s*': '',
           r'\s*<ctt[^>\n]*?>\s*<a[^>\n]*?>\s*<ch>(?:版權|版权|奥付|おくづけ)(?:页|頁|ページ)?</ch>\s*</a>[\s\S]*</ctt>': '',
           r'\s*<ctt[^>\n]*?>\s*<a[^>\n]*?>\s*<ch>(?:封底|里表纸|裏表紙|うらびょうし)(?:页|頁|ページ)?</ch>\s*</a>[\s\S]*</ctt>': '',
           r'<ch>([\s　])+(.*?)(?(1)[\s　]*|[\s　]+)</ch>': r'<ch>\2</ch>',
           r'(<ch>\S)[\s　]+(\S(?:[\s　]+.*?)?</ch>)': r'\1\2',
           r'(*)(<ch>(?:(?!</ch>).)*?\S)　{2,}(\S(?:(?!</ch>).)*?</ch>)': r'\1　\2',
           r'(<ch>.*?\S) ([^\n\dA-z].*?</ch>)': r'\1　\2',
           r'(<ch>.*?[一-龥あ-ヶー]) ([A-z\d].*?</ch>)': r'\1　\2',
           r'(<ch>.*?\S)(([-～—])+.+\3+</ch>)': r'\1　\2'}),
       ('标题拉取', {
           r'(<ctt[^>\n]*?>\s*<a[^>\n]*?href=\")(?:[^\"\n]*/)?(([^\"/#\n]*?)#[^\"/\n]*?)(\"[^>\n]*?>[\s\S]*?<ctt[^>\n]*?>\s*<a[^>\n]*?href=\"(?:[^\"\n]*/)?\2\"[^>\n]*?>)': r'\1\3\4',
           r'(<ctt[^>\n]*?>\s*<a[^>\n]*?)href=\"(?:[^\"\n]*/)?([^\"/#\n]*?)\"([^>\n]*?>[\s\S]*?<ctt[^>\n]*?>\s*<a[^>\n]*?href=\"(?:[^\"\n]*/)?\2\"[^>\n]*?>)': r'\1type=\"check\"\3',
           r'(*)^([\s\S]*?<ctt[^>\n]*?>\s*<a[^>\n]*?href=\"(?:[^\"\n]*/)?(.*?)(?:\+part)?\.xhtml)[^>\n]*?>([\s\S]*?<ctt[^>\n]*?>\s*<a[^>\n]*?href=\"(?:[^\"\n]*/)?)\2\.xhtml#([^\"\n]*?)(\"[\s\S]*?<page id=\"(.*?)(?:\+part)?\" href=\"\2(?:\+part)?\.xhtml(?:(?!</page>)[\s\S])*?)^^.*?id=\"\4\".*$$': r'\1\">\3\2+part.xhtml\5</body>\n</html>\n</page>\n<page id=\"\6+part\" href=\"\2+part.xhtml\">\n<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"no\"?>\n<!DOCTYPE html>\n<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"zh\" xmlns:epub=\"http://www.idpf.org/2007/ops\" xmlns:xml=\"http://www.w3.org/XML/1998/namespace\">\n<head>\n<title></title>\n<link href=\"../Styles/stylesheet.css\" type=\"text/css\" rel=\"stylesheet\"/>\n<script type=\"text/javascript\" src=\"../Misc/script.js\"></script>\n</head>\n<body>',
           r'(*)(<ctt[^>\n]*?>\s*<a[^>\n]*?href=\"(?:[^\"\n]*/)?(.*?)\.xhtml[\s\S]*?<ctt[^>\n]*?>\s*<a[^>\n]*?href=\"(?:[^\"\n]*/)?\2)\+part': r'\1_part*',
           r'(*)(<page id=\"(.*?)\" href=\"(.*?)\.xhtml\">[\s\S]*?<page id=\"\2)\+part\" href=\"\3\+part': r'\1_part*\" href=\"\3_part*',
           r'(*)<ctt([^>\n]*?>\s*<a[^>\n]*?href=\"(?:[^\"\n]*/)?(.*?\.xhtml)[^>\n]*?>\s*<ch>([^<>\n]*?)</ch>[\s\S]*?<page.*?href=\"\2\"(?:(?!<body>)[\s\S])*?<title>).*?(</title>(?:(?!<body>)[\s\S])*?<body>)': r'<div\1\3\4\n<h7>\3</h7>',
           r'(</?)ctt([^>\n]*?>)': r'\1div\2',
           r'<title></title>(?:(?!</body>)[^一-龥あ-ヶー])*?\n[^一-龥あ-ヶー\n]*(?:後[^一-龥あ-ヶー\n]*記|后[^一-龥あ-ヶー\n]*记|後書き|あとがき|后书き)[^一-龥あ-ヶー\n]*$$': r'<title>後記</title>\n<link href=\"../Styles/stylesheet.css\" type=\"text/css\" rel=\"stylesheet\"/>\n<script type=\"text/javascript\" src=\"../Misc/script.js\"></script>\n</head>\n<body>\n<h7>後記</h7>',
           r'(*)<title>.+?(</title>(?:(?!<title>)[\s\S])*?)<h7>.+?</h7>\s*((?:(?!<h7>|</p>)[\s\S])*?(?:<title>.+?</title>|<nav))': r'<title>\1\2',
           r'(*)<title>(.+?)(</title>(?:(?!<title>)[\s\S])*?)<h7>\1</h7>\s*((?:(?!<title>)[^一-龥あ-ヶー])*?<title>)(</title>[\s\S]*?<body>)': r'<title>\2\3\1\4\n<h7>\1</h7>',
           r'(*)(<title>(.+?)</title>(?:(?!<title>)[\s\S])*?<h7>\2</h7>(?:(?!<h7>)[\s\S])*?<title>)(</title>[\s\S]*?<title>(.+?)</title>(?:(?!<title>)[\s\S])*?<h7>\4</h7>)': r'\1\2\3',
           r'<ch>(.+?)　+(.*?)</ch>': r'<p>\1</p><p class=\"ctit\">\2</p>',
           r'<ch>(.+?)</ch>': r'<p>\1</p>'}),
       ('标题去重', {
           r'(?<=</h7>)(?:(?!</body>|class=)[^一-龥あ-ヶー])*\n(.+)$$': r'\n<chapter>\1</chapter>\1',
           r'(<h7>(\S+?)(?:[-.•][ 　]+|[ 　]*)(.*?)</h7>\s*<chapter>.*?</chapter>.*$$(?:(?!</body>)[\s\S])*?)^^(.*?\2.*?\3.*)$$': r'\1<chapter>\4</chapter>\4',
           r'(*)(?<=<chapter>)(.*?)(?:<(?:(?!rt)[^>\n])*?>|<rt(?:(?!/rt>).)+/rt>)(.*?)(?=</chapter>)': r'\1\2',
           r'(<h7>(\S+?)(?:[-.•][ 　]+|[ 　]*)(.*?))</h7>(?:(?!</body>)[\s\S])*?<chapter>[^一-龥あ-ヶー\n]*\2[^一-龥あ-ヶー\n]*\3[^一-龥あ-ヶー\n]*</chapter>.*?(<a.*?/a>)?.*$$': r'\1\4</h7>',
           r'(<page id=\"(.*?_part)(\d+)\" href=\"(.*?_part)(\d+)\.xhtml\">((?:(?!<body>)[\s\S])*?<body>)(?:(?!<page)[\s\S])*?)(<page(?:(?!</body>)[\s\S])*?<h7>(\S+?)[ 　]*(.*?)</h7>)\n<chapter>.*?</chapter>((?:(?!</body>)[\s\S])*?)<chapter>[^一-龥あ-ヶー\n]*\8[^一-龥あ-ヶー\n]*\9[^一-龥あ-ヶー\n]*</chapter>.*$$': lambda x: ''.join((x.group(1), '<page id=\"', x.group(2), str(int(x.group(3))+1).zfill(3), '\" href=\"', x.group(4), str(int(x.group(5))+1).zfill(3), '.xhtml\">', x.group(6), '\n', x.group(10), '</body>\n</html>\n</page>', x.group(7))),
           r'(<page id=\"((?:(?!_part).)*?)\" href=\"((?:(?!_part).)*?)\.xhtml\">((?:(?!</body>)[\s\S])*?<body>)(?:(?!<page)[\s\S])*?)(<page(?:(?!</body>)[\s\S])*?<h7>(\S+?)[ 　]*(.*?)</h7>)\n<chapter>.*?</chapter>((?:(?!</body>)[\s\S])*?)<chapter>[^一-龥あ-ヶー\n]*\6[^一-龥あ-ヶー\n]*\7[^一-龥あ-ヶー\n]*</chapter>.*$$': r'\1<page id=\"\2_part001\" href=\"\3_part001.xhtml\">\4\n\8</body>\n</html>\n</page>\5',
           r'<chapter>.*?</chapter>': ''}),
       ('标题样式', {
           r'(<h7>.*</h7>)(?:\s*<p.*?><br/></p>|\s*<([A-z]+)[^>\n]*?>[\s　]*?</\2>|\s*</(?:(?!body)[A-z])+>)+': r'\1',
           r'(<h7>.*</h7>)((?:(?!</body>)[^一-龥あ-ヶー])*?</body>)': r'<div class=\"chapter\">\n\1\n</div>\2',
           r'<h7>(.*?\S)　(\S.*?)</h7>': r'<h4>\1</h4>\n<h5>\2</h5>',
           r'<(h\d)>(.*?)\s*(（[^註注\n]*）)</\1>': r'<\1>\2<span type=\"check\" class=\"em08\">\3</span></\1>',
           r'<h7>(.*)</h7>': r'<h3>\1</h3>'})),
      ('注释生成', '',
       ('行内注释', {
           r'(*)([\s　]*<span[^>\n]*?>)?[\s　]*（([\s　]*<span[^>\n]*?>)?[※﹡*\s　]*[譯译編编]?[註注][\s　]*\d*[\s　：]+((?:[^（）\n]*?（(?:(?!）).)*）)*[^（）\n]+)(?(2)</span>[\s　]*)）[\s　]*(?(1)</span>[\s　]*)(.*(?:\s*<aside>.*?</aside>)*)': r'<sup/>\4\n<aside>\3</aside>',
           r'(*)(</[A-z\d]+>\s*)^^<[A-z\d]+[^>\n]*?>([^一-龥あ-ヶー\n]*<sup/>)[^一-龥あ-ヶー\n]*$$': r'\2\1'}),
       ('页尾注释', {
           r'(*)(?:[\s　]*<(span|sup)[^>\n]*?>)?[\s　]*(?:<a[^>\n]*?href=\"[^\"\n]*?#([^\"\n]*?)\s*\"[^>\n]*?>[\s　]*)?（(?:[\s　]*<a[^>\n]*?href=\"[^\"\n]*?#([^\"\n]*?)\s*\"[^>\n]*?>)?[※﹡*\s　]*[譯译編编]?[註注](?:[\s　]*<a[^>\n]*?href=\"[^\"\n]*?#([^\"\n]*?)\s*\"[^>\n]*?>)?[\s　]*\d*[\s　]*(?:</a>[\s　]*)?）[\s　]*(?:</a>[\s　]*)?(?(1)</\1>[\s　]*)(.*(?:\s*<aside>.*?</aside>)*)([\s\S]*?)^^(.*?<([A-z\d]+)[^>\n]*?id=\"\s*(?:\2|\3|\4)\s*\"[^>\n]*?>(?:[^<>]*?(?:<(?P<tag>[A-z\d]+)[^>\n]*?>(?:(?!</(?P=tag)>)[\s\S])*</(?P=tag)>|<[^>\n]*?/>))*[^<>]*</\8>.*)$$': r'<sup/>\5\n<aside>\7</aside>\6\7',
           r'(?s)(<aside>((?:(?!</aside>).)*?)</aside>.*?)(?<!<aside>)\2(?!</aside>).*?(?=</body>)': r'\1',
           r'(?s)<((?:(?!body)[A-z\d])+)( )*(?(2)[^>\n]*?[^>/\n])>(?:(?!</\1>|</?body).)*(?=</body>)': ''}),
       ('弹注样式', {
           r'^^(.*?<sup/>.*(?:\s*<aside>(?:(?!</aside>)[\s\S])*?</aside>)*)': r'<note>\n\1\n</note>',
           r'(*)(<aside>.*?)<ruby>((?:(?!</ruby>|<rt).)*?)<rt>(.*?)</rt></ruby>': r'\1\2（\3）',
           r'(*)(<aside>(?:(?!</aside>).)*?)\s*(?:<(?:(?!ruby|rt|aside)[^>\n])*?>|\n)+\s*': r'\1',
           r'<aside>[※﹡*\s　]*([譯译編编]?[註注])[\s　]*(\d*)[\s　：]*(.*?</aside>)': r'<aside>\1\2：\3',
           r'<aside>((?:(?!：).)*</aside>)': r'<aside>註：\1'}),
       ('弹注生成', {
           r'(*)^([\s\S]*?)<sup/>([\s\S]*?)<aside>(.*?)(?=</aside>)': r'\1<sup type=\"check\"><a class=\"duokan-footnote\" epub:type=\"noteref\" href=\"#note*\" id=\"note_ref*\"><img alt=\"note\" class=\"zhangyue-footnote\" src=\"../Images/note.png\" zy-footnote=\"\3\"/></a></sup>\2<aside epub:type=\"footnote\" id=\"note*\">\n<a href=\"#note_ref*\">\n<ol class=\"duokan-footnote-content\">\n<li class=\"duokan-footnote-item\" id=\"note*\" value=\"*\">\n<p>\3</p>\n</li>\n</ol>\n</a>\n'})),
      ('图片版式', r'(?s)<page.*?/page>',
       ('SVG处理', {
           r'(?:<p.*?><br/></p>\s*|<div.*?>\s*)*<svg.*?>(?:(?!</svg>)[\s\S])*?<image[^>\n]*?href=\"[^\"\n]*/cover\.(jpe?g|webp)\"/>(?:(?!</svg>)[\s\S])*?</svg>(?:\s*<p.*?><br/></p>|\s*</div>)*': r'<div class=\"cover duokan-image-single\">\n<img alt=\"cover\" src=\"../Images/cover.\1\" zy-enlarge-src=\"self\"/>\n</div>',
           r'(?:<p.*?><br/></p>\s*|<div.*?>\s*)*<svg.*?>(?:(?!</svg>)[\s\S])*?<image[^>\n]*?href=\"[^\"\n]*/([^\"/\n]*?)\.(jpe?g|png|webp)\"[^>\n]*?/>(?:(?!</svg>)[\s\S])*?</svg>(?:\s*<p.*?><br/></p>|\s*</div>)*': r'<div class=\"kuchie duokan-image-single\">\n<img alt=\"\1\" src=\"../Images/\1.\2\" zy-enlarge-src=\"self\"/>\n</div>'}),
       ('IMG处理', {
           r'(?:<p.*?><br/></p>\s*|<div.*?>\s*)*^^[^一-龥あ-ヶー\n]*<img[^>\n]*?src=\"[^\"\n]*/([^\"/\n]*?)\.(jpe?g|webp)\"(?:(?!zy-enlarge-src)[^>\n])*?>[^一-龥あ-ヶー\n]*$$(?:\s*<p.*?><br/></p>|\s*</div>)*': r'<div class=\"illus duokan-image-single\">\n<img alt=\"\1\" src=\"../Images/\1.\2\" zy-enlarge-src=\"self\"/>\n</div>',
           r'(?:<p.*?><br/></p>\s*|<div.*?>\s*)*^^[^一-龥あ-ヶー\n]*<img[^>\n]*?src=\"[^\"\n]*/((?:(?!logo|note)[^\"/\n])*?)\.png\"(?:(?!zy-enlarge-src)[^>\n])*?>[^一-龥あ-ヶー\n]*$$(?:\s*<p.*?><br/></p>|\s*</div>)*': r'<p type=\"check\" class=\"cut\"><img alt=\"\1\" src=\"../Images/\1.png\" zy-enlarge-src=\"none\"/></p>'}),
       ('图片样式修正', {
           r'(?:<p.*?><br/></p>\s*|<div.*?>\s*)*\s*<(?:image|img)[^>\n]*?(?:href|src)=\"[^\"\n]*/((?:(?!logo|note|cover)[^\"/\n])*?)\.([A-z\d]+)\"(?:(?!zy-enlarge-src)[^>\n])*?>\s*(?:\s*<p.*?><br/></p>|\s*</div>)*': r'<img alt=\"\1\" src=\"../Images/\1.\2\"/>',
           r'(?<=<body>)(?:(?!<img)[^一-龥あ-ヶー])*^^(?:(?!cover duokan).)*$$\s*(<img[^>\n]*?src=\"cover.jpe?g\")[^>\n]*?>(?:(?!<img)[^一-龥あ-ヶー])*(?=</body>)': r'\n<div class=\"cover duokan-image-single\">\n\1 zy-enlarge-src=\"self\"/>\n</div>\n',
           r'^((?:(?!cover)[\s\S])*?<page.*?href=\".*?cover(?:(?!</body>)[\s\S])*?<body>)(?:(?!<img|</body>|cover duokan)[^一-龥あ-ヶー])*(<img[^>\n]*?src=\".*?\")[^>\n]*?>(?:(?!<img|</body>|cover duokan)[^一-龥あ-ヶー])*(?=</body>)': r'\1\n<div class=\"cover duokan-image-single\">\n\2 zy-enlarge-src=\"self\"/>\n</div>\n',
           r'(?<=<body>)(?:(?!<img)[^一-龥あ-ヶー])*^^(?:(?!kuchie duokan|cover duokan).)*$$\s*(<img[^>\n]*?src=\".*?\")[^>\n]*?>(?:(?!<img)[^一-龥あ-ヶー])*(?=</body>)': r'\n<div class=\"kuchie duokan-image-single\">\n\1 zy-enlarge-src=\"self\"/>\n</div>\n'})),
      ('页面复查', r'(?s)<page.*?/page>',
       ('TITLE填充', {
           r'<title>.*?(</title>[\s\S]*?<div[^>\n]*?cover duokan)': r'<title>封面\1',
           r'<title>.*?(</title>[\s\S]*?<div[^>\n]*?kuchie duokan)': r'<title>插圖\1'}),
       ('页面检查', {
           r'(?<=<ruby>)(.*?)(<rt>(?:(?!</ruby>|<rt>).)*?</rt>)': r'<rb>\1</rb><rp>（</rp>\2<rp>）</rp>',
           r'(*)(<body>(?:(?!<div)[\s\S])*?)\s*</div>': r'\1',
           r'(*)(<body>(?:(?!<p)[\s\S])*?)\s*</p>': r'\1',
           r'(*)(<body>\s*(<div.*?>)?(?:[^<>]*?(?:<(?P<tag>[A-z\d]+)[^>\n]*?>(?:(?!</(?P=tag)>)[\s\S])*</(?P=tag)>|<[^>\n]*?/>))*[^<>]*)</[A-z\d]+>((?(2)\s*</div>)\s*</body>)': r'\1\3',
           r'(?<=<body>\n)(\s*<p.*?><br/></p>|\s*<([A-z]+)[^>\n]*?>[\s　]*?</\2>|\s)+': '',
           r'(?:\s*<p.*?><br/></p>)*\s*(?=\n</body>)': '',
           r'(?<=<body>)\s*(?=<p)': r'\n<p><br/></p>\n',
           r'(?<=href=\")([^\"\n]+)#[^\"\n]*?(?=\")': r'\1',
           r'(*)(<page.*?href=\"(.*?)\"[\s\S]*?href=\")(?=#)': r'\1\2',
           r'(<[A-z\d]+)((?:(?!type=\"check\")[^>\n])*?>[^\n\dA-zΑ-ω一-龥あ-ヶー`~～\[\](){},.\\/;·！…（）—｛｝［］《》〈〉？：“”【】；‘\'，。、『』「」<>]+)': r'\1 type=\"check\"\2',
           r'(<[A-z\d]+)(((?:(?!type=\"check\")[^>\n])*?>[^<>\n]*?)[1①ⅰⅠiI一壹壱](?:(?!href=)[\s\S])*?\1\3(?:[2②ⅱⅡ二贰貳弐]|[iI]{2}))': r'\1 type=\"check\"\2'})))
