#sublime API: https://www.sublimetext.com/docs/3/api_reference.html

import sublime
import sublime_plugin

class Pref():
        #空函数
        def load(self):
                pass
#保存配置项
s = {}
#加载配置文件
def plugin_loaded():
        global s,Pref
        s = sublime.load_settings('append.sublime-settings')
        s.clear_on_change('reload')
        s.add_on_change('reload',lambda:Pref.load())
        print(s)

#在控制台输入"view.run_command('_append')"即可运行以下代码
class _appendCommand(sublime_plugin.TextCommand):
        def run(self, edit):
                starts = self.view.find_all('^(.)*$',0) #获取内容索引列表，以行为单位
                result = ''
                flag = False
                plugin_loaded()
                linehas = s.get('linehas') #获取linehas配置
                append = s.get('append','') #获取append配置
                if(linehas):
                        for start in starts: #遍历每一行内容
                                include_str = self.view.substr(sublime.Region(start.a,start.b)) #根据索引获取一行内容
                                if(include_str.find(linehas)>-1 and include_str.find(append)==-1):
                                        result+=include_str+append+'\n'
                                        flag = True
                                else:
                                        result+=include_str+'\n'
                #如果有更改，重新写入更改后的内容
                if(flag):
                        self.view.erase(edit,sublime.Region(0,self.view.size()))
                        self.view.insert(edit,0,result)

