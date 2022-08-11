sqlite-utils insert-files test_new_bma.db images ../images/test_workflow_images/*crop* \
    -c name \
    -c content \
    -c md5_hash:md5 \
    -c size \
    -c created_time:ctime_iso