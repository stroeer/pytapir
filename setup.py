# This is purely the result of trial and error.

import os
import subprocess
import sys

import stroeer
from setuptools import setup, find_packages, Command

tests_require = []
dev_require = []
install_requires = [
    'setuptools',
    'protobuf>=4.24.3',
    'grpcio>=1.58.0',
]

extras_require = {
    'dev': dev_require,
    'test': tests_require,
}


def long_description():
    with open('README.md', encoding='utf-8') as f:
        return f.read()


def run_bash_command(command):
    try:
        subprocess.check_call([command], shell=True)
    except subprocess.CalledProcessError as error:
        print(f'Command failed with exit code: {error.returncode}')
        sys.exit(error.returncode)


class BuildPackageCommand(Command):
    """Command to generate project *_pb2.py modules from proto files."""
    description = 'run protobuf compiler'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from grpc_tools import protoc
        import pkg_resources

        proto_files = []
        inclusion_root = os.path.abspath('./tapir')
        for root, _, files in os.walk('./tapir'):
            for filename in files:
                if filename.endswith('.proto'):
                    proto_files.append(os.path.abspath(os.path.join(root, filename)))

        well_known_protos_include = pkg_resources.resource_filename('grpc_tools', '_proto')

        for proto_file in proto_files:
            command = [
                          'grpc_tools.protoc',
                          '--proto_path={}'.format(inclusion_root),
                          '--proto_path={}'.format(well_known_protos_include),
                          '--python_out={}'.format('.'),
                          '--grpc_python_out={}'.format('.'),
                      ] + [proto_file]
            if protoc.main(command) != 0:
                raise Exception('error: {} failed'.format(command))

print(f"packages = {find_packages(include=['stroeer', 'stroeer.*'])}")
setup(
    name='pytapir',
    version=stroeer.__version__,
    description=stroeer.__doc__.strip(),
    long_description=long_description(),
    long_description_content_type='text/markdown',
    url='https://pytapir.io/',
    download_url=f'https://github.com/stroeer/pytapir/archive/{stroeer.__version__}.tar.gz',
    author=stroeer.__author__,
    author_email='none@example.com',
    license=stroeer.__licence__,
    packages=find_packages(include=['stroeer', 'stroeer.*']),
    python_requires='>=3.8',
    extras_require=extras_require,
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Environment :: Library',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache 2',
        'Topic :: Api :: Grpc'
    ],
    project_urls={
        'GitHub': 'https://github.com/stroeer/pytapir',
        # 'Documentation': 'https://www.example.com',
        'Online Demo': 'https://www.example.com',
    },
    cmdclass={
        'protoc': BuildPackageCommand
    }
)
