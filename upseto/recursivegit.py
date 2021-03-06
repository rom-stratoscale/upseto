from upseto import gitwrapper
from upseto import traversenodouble
import sys


class RecursiveGit:
    def __init__(self, baseDir=".."):
        self._traverse = traversenodouble.TraverseNoDouble(baseDir)

    def run(self, mani, commandLine):
        git = gitwrapper.GitWrapper(".")
        sys.stdout.write('#upseto %s\n' % git.directory())
        sys.stdout.write(git.run(commandLine))
        for dependency in self._traverse.traverse(mani):
            git = gitwrapper.GitWrapper(dependency.projectDir)
            sys.stdout.write('#upseto %s\n' % git.directory())
            sys.stdout.write(git.run(commandLine))
