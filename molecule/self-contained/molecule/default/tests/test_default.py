import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package_is_runnable(host):
    host.run_test("/usr/share/self-contained-app/self-contained-app")


def test_package_symlink_is_runnable(host):
    host.run_test("/usr/local/bin/self-contained-app")


def test_readme_is_deployed(host):
    assert host.file("/etc/dotnet-packaging/README.md").exists


def test_hidden_file_is_ignored(host):
    assert \
        not host.file("/usr/share/self-contained-app/.gitignore").exists


def test_empty_file_is_ignored(host):
    assert \
        not host.file("/usr/share/self-contained-app/empty").exists
