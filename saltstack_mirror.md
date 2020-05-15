```
# Since Saltstack 3000, rclone is used to mirror repo.
# Below example will mirror all saltstack packages, including archives, for x86_64 RHEL 6, 7 and 8.

RCLONE_CONFIG_S3_TYPE=s3 \
RCLONE_CONFIG_S3_PROVIDER=Other \
RCLONE_CONFIG_S3_ENV_AUTH=false \
RCLONE_CONFIG_S3_ENDPOINT=https://s3.repo.saltstack.com \ 
rclone sync --fast-list --use-server-modtime -v \
       --include="/py3/redhat/[78]/x86_64/3000/**" \
       --include="/yum/redhat/[67]/x86_64/3000/**" \
       --include="/bootstrap/**" \
       s3:s3/ ./saltstack/
```
