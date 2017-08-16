import db_interface

back_db = db_interface.DbInterface('host', 'username', 'password', 'forum')
live_db = db_interface.DbInterface('host', 'username', 'password', 'forum')
user_i


def re_insert_post_by_id(db_back, db_live, post_id):

    # Make sure post wasn't added while adding a thread back
    post_check = db_live.get_post_by_id(post_id)

    if post_check:
        return

    # Get original post
    post = db_back.get_post_by_id(post_id)

    # If the position is 0, means it's a thread starter
    if post.position == 0:
        re_insert_thread_by_id(db_back, db_live, post.thread_id)
        return

    # insert post
    db_live.insert_post(post)
    print 'Inserted post '

    # bump thread's reply count
    thread = db_live.get_thread_by_id(post.thread_id)
    thread.bump_reply_count()
    db_live.update_thread(thread)
    print 'Updated thread '

    thread_posts = db_live.get_posts_by_thread_id(post.thread_id)
    for (thread_post) in thread_posts:
        if thread_post.post_date > post.post_date:
            thread_post.bump_position()
            db_live.update_post(thread_post)
            print 'Bumped posts position'

    # handle attachments
    attachments = db_back.get_attachments_for_post_id(post.post_id)
    for (attachment) in attachments:
        db_live.insert_attachment(attachment)
        print 'Inserted attachment'


def re_insert_thread_by_id(db_back, db_live, thread_id):

    # get original thread
    original_thread = db_back.get_thread_by_id(thread_id)
    original_posts = db_back.get_posts_by_thread_id(thread_id)

    # re-insert them
    db_live.insert_thread(original_thread)
    print 'Inserted thread'

    for (post) in original_posts:
        db_live.insert_post(post)
        print 'Inserted post'

        # handle attachments
        attachments = db_back.get_attachments_for_post_id(post.post_id)
        for (attachment) in attachments:
            db_live.insert_attachment(attachment)
            print 'Inserted attachment'

post_ids = back_db.get_post_ids_by_user_id(user_id)

for (post_id) in post_ids:
    post_id = post_id[0]
    print 'Post id: ' + str(post_id)
    re_insert_post_by_id(back_db, live_db, post_id)

back_db.db.close()
live_db.db.close()
