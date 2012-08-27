import sublime, sublime_plugin

class {{{name}}}Command(sublime_plugin.TextCommand):
  def run(self, edit):
    sublime.message_dialog("foo")
