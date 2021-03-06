import sys
import os

from cliff.app import App
from cliff.commandmanager import CommandManager

from ovmexporter import client


class OVMExporterApp(App):

    def __init__(self):
        super(OVMExporterApp, self).__init__(
            description='OVM exporter CLI',
            version='0.1',
            command_manager=CommandManager('ovmexporter.cli'),
            deferred_help=True)

    def _env(self, var_name, default=None):
        return os.environ.get(var_name, default)

    def build_option_parser(self, description, version, argparse_kwargs=None):
        parser = super(OVMExporterApp, self).build_option_parser(
            description, version, argparse_kwargs)
        
        parser.add_argument(
            '--ovm-endpoint', '-e',
            default=self._env("OVM_EXPORTER_ENDPOINT"),
            help='OVM exporter endpoint.')
        parser.add_argument(
            '--username', '-u',
            default=self._env("OVM_EXPORTER_USERNAME"),
            help='OVM exporter username.')
        parser.add_argument(
            '--password', '-p',
            default=self._env("OVM_EXPORTER_PASSWORD"),
            help='OVM exporter password.')
        parser.add_argument(
            '--insecure', action='store_true',
            help='Skip TLS certificate validation.')
        parser.add_argument(
            '--ca-path',
            default=self._env("OVM_EXPORTER_CAFILE"),
            help='OVM exporter CA certificate file.')
        return parser

    def prepare_to_run_command(self, cmd):
        cmd._cmd_options = self.options


def main(argv=sys.argv[1:]):
    myapp = OVMExporterApp()
    return myapp.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))