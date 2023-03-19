# Automation

## GitLab Runner

### Requirements

- Requires `gitlab_runner/config.toml` to be created. You can build it based off of `gitlab_runner/config.template.toml`

### Notes

- Contains an environment for testing ansible scripts. To use it:
  - go to the directory
    ```shell
    cd gitlab_runner/ansible_env
    ```
  - build the docker image
    ```shell
    ./build.sh
    ```
  - start the docker image (interactive mode)
    ```shell
    ./run.sh
    ```