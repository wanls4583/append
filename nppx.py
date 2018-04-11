import sublime
import sublime_plugin
#px
class NopxCommand(sublime_plugin.TextCommand):
        def run(self, edit):
                starts = self.view.find_all('^(.)*$',0)
                result = '';
                flag = False
                for start in starts:
                        include_str = self.view.substr(sublime.Region(start.a,start.b))
                        if(include_str.find('px')>-1 and include_str.find('/*px*/')==-1):
                                result+=include_str+'/*px*/\n'
                                flag = True
                        else:
                                result+=include_str+'\n'
                if(flag):
                        self.view.erase(edit,sublime.Region(0,self.view.size()))
                        self.view.insert(edit,0,result)