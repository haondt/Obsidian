docker run -it --rm \
    --name ansible_env \
    --group-add 1006 \
    -l com.obsidian.host="docker-automation" \
    -l com.obsidian.service="ansible-env" \
    -e COM_OBSIDIAN_KVS_HOST="http://docker-selfhosted:8188" \
    -v $(pwd)/../ansible:/ansible \
    -w /ansible \
    ansible_env
