import compileall
import os
import shutil
import fire
import python_minifier


class CompileMinify(object):
    """Minify, compile and remove python files"""

    def __init__(self, directory=os.getcwd()):
        print(directory)
        self.directory = directory

    def run(self, remove_tests: bool = False, remove_py: bool = False):
        self._apply_to_python_files(self._minify_and_compile, remove_tests, remove_py)
        print("Python files minified and compiled")

    def _apply_to_python_files(self, function, *args, **kwargs):
        level = 0
        for r, d, f in os.walk(self.directory):
            if r.endswith("tests") and kwargs["remove_tests"]:
                shutil.rmtree(r)
            elif level > 0:
                for file in f:
                    if file.endswith(".py"):
                        file = os.path.join(r, file)
                        function(file)
                        if kwargs["remove_py"]:
                            os.remove(file)
            level += 1

    @staticmethod
    def _minify_and_compile(file):
        with open(file) as f:
            buff = f.read()
        with open(file, "w") as f:
            mnf = python_minifier.minify(buff)
            f.write(mnf)
        compileall.compile_file(file, force=True, quiet=True, legacy=True)


def entrypoint():
    fire.Fire(CompileMinify)