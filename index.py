import sublime
import sublime_plugin

class Pref():
        def load(self):
                pass
s = {}
def plugin_loaded():
        global s,Pref
        s = sublime.load_settings('append.sublime-settings')
        s.clear_on_change('reload')
        s.add_on_change('reload',lambda:Pref.load())
        print(s)
#px
#view.run_command(string, <args>)
class _appendCommand(sublime_plugin.TextCommand):
        def run(self, edit):
                starts = self.view.find_all('^(.)*$',0)
                result = ''
                flag = False
                plugin_loaded()
                linehas = s.get('linehas')
                append = s.get('append','')
                if(linehas):
                        for start in starts:
                                include_str = self.view.substr(sublime.Region(start.a,start.b))
                                if(include_str.find(linehas)>-1 and include_str.find(append)==-1):
                                        result+=include_str+append+'\n'
                                        flag = True
                                else:
                                        result+=include_str+'\n'
                if(flag):
                        self.view.erase(edit,sublime.Region(0,self.view.size()))
                        self.view.insert(edit,0,result)

