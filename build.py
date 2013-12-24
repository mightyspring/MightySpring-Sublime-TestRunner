import sublime, sublime_plugin



class RunPythonTestCommand(sublime_plugin.TextCommand):
    def run(self, edit):


        REPO_NAME = '/mightyspring/'
        abs_file = self.view.file_name()
        folders = abs_file.lower().split(REPO_NAME)

        if len(folders) > 1:
            REPO_ROOT = folders[0] + REPO_NAME

            commands = [
                'echo "Running tests, Sir..." ',
                'cd %s' % REPO_ROOT,
                'source venv/bin/activate',
                'python scent.py tests --stop',
                'deactivate',
            ]
            
            self.view.window().run_command(
                'exec',
                {
                    'cmd': [';'.join(commands)],
                    'shell': True,
                    'working_dir': REPO_ROOT,
                }
            )
        else:
            #if the user isn't in the right directory, print a message to the console.
            commands = [
                'echo "Sir, there was an error running Mighty Spring tests."',
                'echo "Please navigate to a file in the MightySpring repositiory and re-run this command."',
            ]
                
            self.view.window().run_command(
                'exec',
                {
                    'cmd': [';'.join(commands)],
                    'shell': True,
                    'working_dir': '',
                }
            )

