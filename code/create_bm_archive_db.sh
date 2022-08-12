sqlite-utils create-database test_new_bma.db

sqlite-utils create-table test_new_bma.db images \
    name text \
    content blob \
    md5_hash text \
    created_time text \
    size integer \
    --pk=name 

sqlite-utils create-table test_new_bma.db batch_info \
    id integer \
    year integer \
    name text \
    batch_number integer  \
    --pk=batch_number

sqlite-utils create-table test_new_bma.db archival_steps \
    name text \
    step text \
    step_date text \
    ingest_date text \
    abs_path text \
    rel_path text \
    pash text \
    cropped_from text \
    inverted_from text \
    edited_from text \
    batch_id integer \
    image text

sqlite-utils add-foreign-keys test_new_bma.db \
    archival_steps batch_id batch_info batch_number \
    archival_steps image images name

sqlite-utils index-foreign-keys test_new_bma.db 