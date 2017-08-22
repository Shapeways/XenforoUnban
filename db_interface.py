import MySQLdb
import entities


class DbInterface:
    def __init__(self, host, username, password, db, port):
        if port:
            self.db = MySQLdb.connect(host=host, username=username, password=password, db=db, port=port)
        else:
            self.db = MySQLdb.connect(host=host, username=username, password=password, db=db)

    def insert_post(self, post):
        sql = """INSERT INTO xf_post (
                  post_id,
                  thread_id,
                  user_id,
                  username,
                  post_date,
                  message,
                  ip_id,
                  message_state,
                  attach_count,
                  position,
                  likes,
                  like_users,
                  warning_id,
                  warning_message,
                  last_edit_date,
                  last_edit_user_id,
                  edit_count)
                VALUES (
                  %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
                );"""

        values = (post.post_id, post.thread_id, post.user_id, post.username, post.post_date, post.message,
                  post.ip_id, post.message_state, post.attach_count, post.position, post.likes, post.like_users,
                  post.warning_id, post.warning_message, post.last_edit_date, post.last_edit_user_id, post.edit_count,)

        cursor = self.db.cursor()
        cursor.execute(sql, args=values)
        self.db.commit()
        cursor.close()

    def update_post(self, post):
        sql = """UPDATE xf_post 
                  SET thread_id = %s,
                      user_id = %s,
                      username = %s,
                      post_date = %s,
                      message = %s,
                      ip_id = %s,
                      message_state = %s,
                      attach_count = %s,
                      position = %s,
                      likes = %s,
                      like_users = %s,
                      warning_id = %s,
                      warning_message = %s,
                      last_edit_date = %s,
                      last_edit_user_id = %s,
                      edit_count = %s
                  WHERE post_id = %s
                        ;"""

        values = (post.thread_id, post.user_id, post.username, post.post_date, post.message, post.ip_id,
                  post.message_state, post.attach_count, post.position, post.likes, post.like_users, post.warning_id,
                  post.warning_message, post.last_edit_date, post.last_edit_user_id, post.edit_count, post.post_id)

        cursor = self.db.cursor()
        cursor.execute(sql, args=values)
        self.db.commit()
        cursor.close()

    def get_posts_by_thread_id(self, thread_id):
        sql = """SELECT * FROM xf_post WHERE thread_id = %s;"""

        values = (thread_id,)

        cursor = self.db.cursor()
        cursor.execute(sql, args=values)

        posts = []

        for (post_id, thread_id, user_id, username, post_date, message, ip_id, message_state, attach_count, position,
             likes, like_users, warning_id, warning_message, last_edit_date, last_edit_user_id, edit_count) in cursor:
            posts.append(entities.Post(post_id, thread_id, user_id, username, post_date, message, ip_id, message_state,
                                       attach_count, position,
                                       likes, like_users, warning_id, warning_message, last_edit_date,
                                       last_edit_user_id, edit_count))

        cursor.close()
        return posts

    def get_post_by_id(self, post_id):
        sql = """SELECT * FROM xf_post WHERE post_id = %s;"""

        values = (post_id,)

        cursor = self.db.cursor()
        cursor.execute(sql, args=values)

        post = False

        for (post_id, thread_id, user_id, username, post_date, message, ip_id, message_state, attach_count, position,
             likes, like_users, warning_id, warning_message, last_edit_date, last_edit_user_id, edit_count) in cursor:
            post = entities.Post(post_id, thread_id, user_id, username, post_date, message, ip_id, message_state,
                                       attach_count, position,
                                       likes, like_users, warning_id, warning_message, last_edit_date,
                                       last_edit_user_id, edit_count)

        cursor.close()
        return post

    def update_thread(self, thread):
        sql = """UPDATE xf_thread 
                          SET node_id = %s,
                           title = %s,
                           reply_count = %s,
                           view_count = %s,
                           user_id = %s,
                           username = %s,
                           post_date = %s,
                           sticky = %s,
                           discussion_state = %s,
                           discussion_open = %s,
                           discussion_type = %s,
                           first_post_id = %s,
                           first_post_likes = %s,
                           last_post_date = %s,
                           last_post_id = %s,
                           last_post_user_id = %s,
                           last_post_username = %s,
                           prefix_id = %s,
                           tags = %s
                          WHERE thread_id = %s
                                ;"""

        values = (thread.node_id, thread.title, thread.reply_count, thread.view_count, thread.user_id, thread.username,
                  thread.post_date, thread.sticky, thread.discussion_state, thread.discussion_open,
                  thread.discussion_type, thread.first_post_id, thread.first_post_likes, thread.last_post_date,
                  thread.last_post_id, thread.last_post_user_id, thread.last_post_username, thread.prefix_id,
                  thread.tags, thread.thread_id)

        cursor = self.db.cursor()
        cursor.execute(sql, args=values)
        self.db.commit()
        cursor.close()

    def get_thread_by_id(self, thread_id):
        sql = """SELECT * FROM xf_thread WHERE thread_id = %s;"""

        values = (thread_id,)

        cursor = self.db.cursor()
        cursor.execute(sql, args=values)

        thread = False

        for (thread_id, node_id, title, reply_count, view_count, user_id, username,
             post_date, sticky, discussion_state, discussion_open,
             discussion_type, first_post_id, first_post_likes, last_post_date,
             last_post_id, last_post_user_id, last_post_username, prefix_id,
             tags) in cursor:
            thread = entities.Thread(thread_id, node_id, title, reply_count, view_count, user_id, username,
                                     post_date, sticky, discussion_state, discussion_open,
                                     discussion_type, first_post_id, first_post_likes, last_post_date,
                                     last_post_id, last_post_user_id, last_post_username, prefix_id,
                                     tags)

        cursor.close()
        return thread
    
    def insert_thread(self, thread):
        sql = """INSERT INTO xf_thread (
                            thread_id,
                            node_id,
                            title,
                            reply_count,
                            view_count,
                            user_id,
                            username,
                            post_date,
                            sticky,
                            discussion_state,
                            discussion_open,
                            discussion_type,
                            first_post_id,
                            first_post_likes,
                            last_post_date,
                            last_post_id,
                            last_post_user_id,
                            last_post_username,
                            prefix_id,
                            tags
                        )
                        VALUES (
                          %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
                        );"""

        values = (thread.thread_id, thread.node_id, thread.title, thread.reply_count, thread.view_count, thread.user_id,
                  thread.username, thread.post_date, thread.sticky, thread.discussion_state, thread.discussion_open,
                  thread.discussion_type, thread.first_post_id, thread.first_post_likes, thread.last_post_date,
                  thread.last_post_id, thread.last_post_user_id, thread.last_post_username, thread.prefix_id,
                  thread.tags)

        cursor = self.db.cursor()
        cursor.execute(sql, args=values)
        self.db.commit()
        cursor.close()

    def get_attachment_by_id(self, attachment_id):
        sql = """SELECT * FROM forum.xf_attachment WHERE attachment_id = %s;"""

        values = (attachment_id,)

        cursor = self.db.cursor()
        cursor.execute(sql, args=values)

        attachment = False

        for (attachment_id, data_id, content_type, content_id, attach_date, temp_hash, unassociated,
             view_count) in cursor:
            attachment = entities.Attachment(attachment_id, data_id, content_type, content_id, attach_date, temp_hash,
                                             unassociated, view_count)

        cursor.close()
        return attachment

    def insert_attachment(self, attachment):
        sql = """INSERT INTO forum.xf_attachment (
                            attachment_id,
                            data_id,
                            content_type,
                            content_id,
                            attach_date,
                            temp_hash,
                            unassociated,
                            view_count
                        )
                        VALUES (
                          %s,%s,%s,%s,%s,%s,%s,%s
                        );"""

        values = (attachment.attachment_id, attachment.data_id, attachment.content_type, attachment.content_id,
                  attachment.attach_date, attachment.temp_hash, attachment.unassociated, attachment.view_count)

        cursor = self.db.cursor()
        cursor.execute(sql, args=values)
        self.db.commit()
        cursor.close()

    def get_attachments_for_post_id(self, post_id):
        sql = """SELECT * FROM forum.xf_attachment WHERE content_type = 'post' AND content_id = %s;"""

        values = (post_id,)

        cursor = self.db.cursor()
        cursor.execute(sql, args=values)

        attachments = []

        for (attachment_id, data_id, content_type, content_id, attach_date, temp_hash, unassociated,
             view_count) in cursor:
            attachments.append(entities.Attachment(attachment_id, data_id, content_type, content_id, attach_date,
                                                   temp_hash, unassociated, view_count))

        cursor.close()
        return attachments

    def get_post_ids_by_user_id(self, user_id):
        sql = """SELECT post_id FROM forum.xf_post WHERE user_id = %s AND message_state != 'deleted';"""

        values = (user_id,)

        cursor = self.db.cursor()
        cursor.execute(sql, args=values)

        post_ids = []

        for (post_id) in cursor:
            post_ids.append(post_id)

        cursor.close()
        return post_ids
