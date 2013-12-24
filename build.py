import sublime, sublime_plugin



class RunPythonTestCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        abs_file = self.view.file_name()
        self.test_root = abs_file.split('mightyspring')[0] + 'mightyspring/'

        commands = [
            'cd %s' % self.test_root,
            'source venv/bin/activate',
            'python scent.py tests --stop',
            'deactivate',
        ]


        self.view.window().run_command(
            'exec',
            {
                'cmd': [';'.join(commands)],
                'shell': True,
                'working_dir': self.test_root,
            }
        )


        '''
        v = self.view.window().get_output_panel('exec')
        edit = v.begin_edit()
        v.insert(edit, v.size(), 'Running Tests...\n')
        v.end_edit(edit)
        v.show(v.size())
        '''
