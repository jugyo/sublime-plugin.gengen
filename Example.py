import sublime, sublime_plugin

class ExampleCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    sublime.message_dialog("foo")
