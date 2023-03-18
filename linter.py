from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter


class DartAnalyze(Linter):
    cmd = ('dart', 'analyze', '@')
    tempfile_suffix = '-'
    regex = r'^\s*?(?P<error>error|info)?\s*?-.*?:(?P<line>\d+):(?P<col>\d+)\s*?-\s*(?P<message>.*)$'
    multiline = False
    defaults = {
        'selector': 'source.dart'
    }
